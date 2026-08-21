#!/usr/bin/env python3
"""QA verification for a converted MyST book project.

Usage:
    python verify_book.py book/ [--outline work/outline.json]

Checks per chapter file (book/chapters/*.md):
  - image references in {figure} directives resolve to existing files
  - labels (:label: ...) are unique across the whole book
  - unescaped $ count is even (unbalanced inline math heuristic)
  - OCR/LaTeX residue artifacts are absent
  - directive counts (figures, math, examples, exercises, tables)
Optionally compares per-chapter figure/example counts against outline.json.
Exit code 1 on any ERROR (warnings do not fail).
"""
import argparse
import glob
import json
import os
import re
import sys

ARTIFACTS = {
    "image-not-found": r"image-not-found",
    "mathrm-tilde": r"\\mathrm\{~\}",
    "epub-eq-image-ref": r"(?:TeX_)?(?:I?Equ|IEq)\d+[^\s$]*\.(?:gif|png)",
    "ocr-artifact-ERE": r"\bERE\b",
    "ocr-issn-garbage": r"22-8714",
    "ocr-dot-paren": r"·\(",
    "double-dollar-math": r"^\$\$",
    "raw-includegraphics": r"\\includegraphics",
    "raw-section-command": r"\\section",
    "unsupported-varvec": r"\\varvec",
}

LABEL_RE = re.compile(r"^:label:\s*(\S+)", re.MULTILINE)
FIGURE_RE = re.compile(r"^```\{figure\}\s*(\S+)", re.MULTILINE)
MATH_RE = re.compile(r"^```\{math\}", re.MULTILINE)
EXAMPLE_RE = re.compile(r"^`{3,}\{prf:example\}", re.MULTILINE)
EXERCISE_RE = re.compile(r"^```\{exercise\}", re.MULTILINE)
ENUMERATOR_RE = re.compile(r"^:enumerator:\s*(.+)$", re.MULTILINE)
TABLE_RE = re.compile(r"^\s*\|?[\s:|-]{5,}\|?\s*$", re.MULTILINE)


def unescaped_dollars(text):
    return len(re.findall(r"(?<!\\)\$", text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book_dir")
    ap.add_argument("--outline")
    args = ap.parse_args()

    book = args.book_dir
    files = sorted(glob.glob(os.path.join(book, "chapters", "*.md")))
    if not files:
        files = sorted(glob.glob(os.path.join(book, "*.md")))
    errors, warnings, report = [], [], []
    all_labels = {}

    for f in files:
        rel = os.path.relpath(f, book)
        text = open(f, encoding="utf-8").read()
        entry = {"file": rel}

        for m in LABEL_RE.finditer(text):
            lab = m.group(1)
            if lab in all_labels:
                errors.append(f"{rel}: duplicate label '{lab}' "
                              f"(also in {all_labels[lab]})")
            all_labels[lab] = rel
        entry["labels"] = len(LABEL_RE.findall(text))

        for m in FIGURE_RE.finditer(text):
            img = m.group(1)
            img_path = os.path.normpath(
                os.path.join(os.path.dirname(f), img))
            if not os.path.exists(img_path):
                errors.append(f"{rel}: figure image not found: {img}")
        entry["figures"] = len(FIGURE_RE.findall(text))

        if unescaped_dollars(text) % 2 != 0:
            errors.append(f"{rel}: odd number of unescaped '$' "
                          f"({unescaped_dollars(text)}) - unbalanced math")
        for name, pat in ARTIFACTS.items():
            hits = re.findall(pat, text, re.MULTILINE)
            if hits:
                errors.append(f"{rel}: artifact '{name}' x{len(hits)}")

        entry["math_blocks"] = len(MATH_RE.findall(text))
        entry["examples"] = len(EXAMPLE_RE.findall(text))
        entry["exercises"] = len(EXERCISE_RE.findall(text))
        entry["enumerators"] = ENUMERATOR_RE.findall(text)
        entry["tables"] = len(TABLE_RE.findall(text))
        if unescaped_dollars(text) > 4000:
            warnings.append(f"{rel}: very large inline-math count, "
                            f"consider checking")
        report.append(entry)

    if args.outline and os.path.exists(args.outline):
        outline = json.load(open(args.outline, encoding="utf-8"))
        by_num = {c.get("number"): c for c in outline.get("chapters", [])}
        for entry in report:
            m = re.search(r"ch-(\d+)", entry["file"])
            if not m:
                continue
            num = int(m.group(1))
            ch = by_num.get(num)
            if not ch:
                continue
            src_figs = ch.get("source_counts", {}).get("figures")
            if src_figs is not None and entry["figures"] != src_figs:
                warnings.append(
                    f"{entry['file']}: {entry['figures']} figures converted, "
                    f"source had {src_figs}")
            src_ex = ch.get("source_counts", {}).get("examples")
            if src_ex is not None and entry["examples"] != src_ex:
                warnings.append(
                    f"{entry['file']}: {entry['examples']} examples converted, "
                    f"source had {src_ex}")

    print(json.dumps({"errors": errors, "warnings": warnings,
                      "chapters": report}, indent=2))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
