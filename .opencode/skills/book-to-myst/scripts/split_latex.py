#!/usr/bin/env python3
"""Split a monolithic OCR LaTeX extraction into per-chapter slice files.

Usage:
    python split_latex.py principlesOfMechanics.tex --out work/tex

Writes one .tex slice per \\section*{...} (or \\chapter/\\section) heading plus
slices.json with per-slice stats: line range, example/problem counts,
includegraphics (incl. broken image-not-found refs), dollar-sign parity,
and equation environments. Non-chapter slices (front matter, Solutions,
Problems headings inside chapters) are kept as separate slices; the outline
phase decides how to stitch them back onto chapters.
"""
import argparse
import json
import os
import re

SPLIT_RE = re.compile(r"^\\(?:chapter|\*?section)\*?\{", re.MULTILINE)
TITLE_RE = re.compile(r"^\\(?:chapter|\*?section)\*?\{(.*)\}", re.MULTILINE)


def slug(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s[:60] or "untitled"


def stats(chunk):
    examples = re.findall(r"Example\s+(\d+\.\d+)", chunk)
    problems = re.findall(r"^Problem\s+(\d+\.\d+)", chunk, re.MULTILINE)
    includegraphics = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}",
                                 chunk)
    dollars = chunk.count("$") - chunk.count(r"\$")
    envs = re.findall(r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}",
                      chunk)
    return {
        "examples": sorted(set(examples)),
        "n_examples": len(examples),
        "n_problems": len(problems),
        "includegraphics": includegraphics,
        "n_image_not_found": sum(1 for g in includegraphics
                                 if "not-found" in g or not g.strip()),
        "dollar_parity": "even" if dollars % 2 == 0 else "ODD (unbalanced!)",
        "equation_envs": envs,
        "n_mathrm_tilde": chunk.count(r"\mathrm{~}"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    src = open(args.tex, encoding="utf-8").read()
    lines = src.splitlines(keepends=True)

    starts = [m.start() for m in SPLIT_RE.finditer(src)]
    if not starts:
        starts = [0]
    elif starts[0] != 0:
        starts.insert(0, 0)

    slices = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(src)
        chunk = src[start:end]
        m = TITLE_RE.match(chunk)
        title = m.group(1).strip() if m else "(preamble)"
        fname = f"slice_{i:03d}_{slug(title)}.tex"
        path = os.path.join(args.out, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(chunk)
        slices.append({
            "index": i,
            "title": title,
            "file": os.path.abspath(path),
            "line_start": src[:start].count("\n") + 1,
            "line_end": src[:end].count("\n") + 1,
            "stats": stats(chunk),
        })

    out = os.path.join(args.out, "slices.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"source": os.path.abspath(args.tex),
                   "preamble_lines": slices[0]["line_end"] if slices else 0,
                   "slices": slices}, f, indent=2)
    print(json.dumps({"slices_json": os.path.abspath(out),
                      "n_slices": len(slices),
                      "titles": [s["title"] for s in slices]}))


if __name__ == "__main__":
    main()
