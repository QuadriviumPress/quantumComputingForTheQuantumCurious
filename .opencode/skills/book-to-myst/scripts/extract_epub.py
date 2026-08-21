#!/usr/bin/env python3
"""Extract an EPUB and build a structured manifest for book conversion.

Usage:
    python extract_epub.py <book.epub> --out work/epub

Extracts the EPUB zip to <out>/extract/ and writes <out>/manifest.json with:
  - chapters in spine order (file, title, parsed chapter number, section tree)
  - per-chapter counts: paragraphs, figures, display/inline equation images,
    tables, citations
  - per-chapter image lists split into: figures (keep) vs equation images (never keep)
  - frontmatter/backmatter files
"""
import argparse
import json
import os
import re
import sys
import zipfile

from bs4 import BeautifulSoup

# Equation-image naming varies slightly across Springer EPUBs:
# display: *_TeX_Equ21.png / *_Equ210_HTML.png
# inline:  *_TeX_IEq217.png / *_IEq5_HTML.gif
DISPLAY_EQ_RE = re.compile(r"(_TeX_Equ\d+|_Equ\d+_HTML)")
INLINE_EQ_RE = re.compile(r"(_TeX_IEq\d+|_IEq\d+_HTML)")


def img_kind(src):
    base = os.path.basename(src)
    if DISPLAY_EQ_RE.search(base):
        return "display_eq"
    if INLINE_EQ_RE.search(base):
        return "inline_eq"
    return "figure"


def clean_latex(alt):
    """Convert an EPUB math-image alt string to plain LaTeX."""
    if not alt:
        return None
    lat = alt.strip()
    for wrapper in ("$$", "$"):
        if lat.startswith(wrapper) and lat.endswith(wrapper) and len(lat) > 2:
            lat = lat[len(wrapper):-len(wrapper)].strip()
            break
    return lat or None


def parse_chapter(soup):
    h1 = soup.find("h1", class_="ChapterTitle")
    title = h1.get_text(" ", strip=True) if h1 else None
    num = None
    if title:
        m = re.match(r"^(\d+)\.?\s+(.*)$", title)
        if m:
            num = int(m.group(1))
            title = m.group(2)
    sections = []
    for h in soup.find_all(["h2", "h3", "h4"]):
        cls = h.get("class") or []
        level = None
        for c in cls:
            m = re.match(r"Section(\d)", c)
            if m:
                level = int(m.group(1))
                break
        text = h.get_text(" ", strip=True)
        m = re.match(r"^(\d+(?:\.\d+)*)\s+(.*)$", text)
        secnum = m.group(1) if m else None
        sectitle = m.group(2) if m else text
        if text:
            sections.append({"level": level, "number": secnum, "title": sectitle})
    counts = {"para": 0, "figure": 0, "display_eq": 0, "inline_eq": 0,
              "table": 0, "citation": 0, "exercise_like": 0}
    images = {"figure": [], "display_eq": [], "inline_eq": []}

    # Ordered equation harvest: every math image has alt="$$ <latex> $$"
    equations = []
    # Figure harvest with book caption numbers (e.g. "Fig. 1.4")
    figures = []
    for img in soup.find_all("img"):
        src = img.get("src", "")
        base = os.path.basename(src)
        kind = img_kind(src)
        counts[kind] += 1
        images[kind].append(base)
        latex = clean_latex(img.get("alt", ""))
        fig_el = img.find_parent("figure")
        if kind in ("display_eq", "inline_eq"):
            eq = {"kind": kind, "file": base, "latex": latex}
            holder = img.find_parent(attrs={"id": re.compile(r"^Equ\d+$")})
            if holder:
                eq["id"] = holder.get("id")
            equations.append(eq)
        elif fig_el:
            entry = {"file": base, "id": fig_el.get("id")}
            num_el = fig_el.find("span", class_="CaptionNumber")
            if num_el:
                entry["number"] = num_el.get_text(" ", strip=True)
            cap_el = fig_el.find("figcaption")
            if cap_el:
                entry["caption"] = cap_el.get_text(" ", strip=True)
            figures.append(entry)
    counts["table"] = len(soup.find_all("table"))
    counts["para"] = len(soup.find_all("p"))
    citations = soup.find_all("p", class_="Citation") or soup.find_all(
        class_=re.compile(r"Citation"))
    counts["citation"] = len(citations)
    counts["exercise_like"] = len(soup.find_all(string=re.compile(
        r"^\s*(Example|Problem|Exercise)\s+\d+", re.IGNORECASE)))
    missing_alt = [e for e in equations if not e.get("latex")]
    return {"title": title, "number": num, "sections": sections,
            "counts": counts, "images": images,
            "equations": {"total": len(equations),
                          "missing_alt": len(missing_alt),
                          "list": equations},
            "figures_detailed": figures}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("epub")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    extract_dir = os.path.join(args.out, "extract")
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(args.epub) as z:
        z.extractall(extract_dir)

    # locate package.opf
    opf_path = None
    with zipfile.ZipFile(args.epub) as z:
        container = z.read("META-INF/container.xml").decode("utf-8")
        m = re.search(r'full-path="([^"]+)"', container)
        if m:
            opf_path = m.group(1)
    if not opf_path:
        print(json.dumps({"error": "no package.opf found"}))
        sys.exit(1)

    opf_file = os.path.join(extract_dir, opf_path)
    soup = BeautifulSoup(open(opf_file, encoding="utf-8").read(), "xml")
    opf_dir = os.path.dirname(opf_path)

    manifest = {}
    for item in soup.find_all("item"):
        iid = item.get("id")
        href = item.get("href")
        manifest[iid] = {"href": href,
                         "media": item.get("media-type", ""),
                         "path": os.path.normpath(os.path.join(opf_dir, href))}

    spine = []
    for itemref in soup.find_all("itemref"):
        iid = itemref.get("idref")
        if iid in manifest and manifest[iid]["media"] in (
                "application/xhtml+xml", "text/html"):
            spine.append(manifest[iid]["path"])

    chapters, other = [], []
    for path in spine:
        full = os.path.join(extract_dir, path)
        if not os.path.exists(full):
            continue
        csoup = BeautifulSoup(open(full, encoding="utf-8").read(), "lxml")
        body = csoup.find("body") or csoup
        is_chapter = (body.get("epub:type") == "chapter"
                      or csoup.find("h1", class_="ChapterTitle") is not None)
        entry = {"file": path, "abs_path": os.path.abspath(full)}
        if is_chapter:
            parsed = parse_chapter(csoup)
            entry.update(parsed)
            # per-chapter sidecars for conversion subagents
            num = entry.get("number") or (len(chapters) + 1)
            with open(os.path.join(args.out, f"math_ch{num:02d}.json"),
                      "w", encoding="utf-8") as f:
                json.dump(parsed["equations"], f, indent=1)
            with open(os.path.join(args.out, f"figures_ch{num:02d}.json"),
                      "w", encoding="utf-8") as f:
                json.dump(parsed["figures_detailed"], f, indent=1)
            entry["math_sidecar"] = os.path.abspath(
                os.path.join(args.out, f"math_ch{num:02d}.json"))
            entry["figures_sidecar"] = os.path.abspath(
                os.path.join(args.out, f"figures_ch{num:02d}.json"))
            chapters.append(entry)
        else:
            entry["title"] = (csoup.find("title").get_text(strip=True)
                              if csoup.find("title") else None)
            other.append(entry)

    out = {"epub": os.path.abspath(args.epub),
           "extract_dir": os.path.abspath(extract_dir),
           "chapters": chapters,
           "other": other}
    out_path = os.path.join(args.out, "manifest.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({"manifest": os.path.abspath(out_path),
                      "chapters": len(chapters),
                      "chapter_titles": [c.get("title") for c in chapters]}))


if __name__ == "__main__":
    main()
