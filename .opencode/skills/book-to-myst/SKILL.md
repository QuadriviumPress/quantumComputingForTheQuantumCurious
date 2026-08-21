---
name: book-to-myst
description: Convert a full textbook (PDF + EPUB + legacy LaTeX attempt) into a
  MyST Markdown book project (mystmd.org) with faithful math, figures,
  worked examples, and numbering. Use when the user wants to convert
  "Principles of Mechanics" (or any Springer-style PDF/EPUB book) to MyST,
  rebuild the book as a website, or produce myst.yml + chapter .md files.
---

# Book → MyST Book Conversion Skill

Convert a complete textbook — PDF + EPUB + a partial LaTeX extraction — into a
MyST Markdown book project: one `.md` file per chapter, real LaTeX math
(KaTeX-rendered), book figures, worked examples as `prf:example` directives,
end-of-chapter problems as `exercise` directives, and a `myst.yml` with a
faithful table of contents. The output builds with the standard `myst` CLI
into a website (and optionally PDF).

**Scripts are in:** `{SKILL_DIR}/scripts/`

The running example throughout is *Principles of Mechanics* (Salma Alrasheed,
Springer 2019, CC-BY-4.0, DOI 10.1007/978-3-030-15195-9) in
`/home/QuadriviumPress/PrinciplesOfMechanics`, but every step generalizes to any
book with the same three source types.

## Environment

WSL2 (Ubuntu). Installing packages with apt/pip is allowed.

```bash
# Python helpers (pip on this box needs --break-system-packages)
pip install --user --break-system-packages pymupdf pillow beautifulsoup4 lxml
# MyST CLI (installed via nvm node v24 as of 2026-08; verify first)
myst -v            # if missing: npm install -g mystmd   (node >= 20 required)
```

## Source Authority Rules (read first!)

The three sources have different reliability per content type. Follow this
priority:

| Content | Authority | Notes |
|---|---|---|
| Structure, section tree, prose | **EPUB XHTML** | Springer semantic HTML, clean text, exact section numbers |
| Math LaTeX | **EPUB `alt` attributes** | Every equation image carries `alt="$$ <latex> $$"` — verified 100% coverage in this book. Use the `math_chNN.json` sidecars. |
| Figure images | **EPUB PNGs** (`*_FigN_HTML.png`) | Vector-quality renders; caption numbers in `<span class="CaptionNumber">` |
| Math cross-check / ambiguity resolution | LaTeX `.tex` slices | OCR extraction — has errors, but sometimes preserves structure |
| Visual ground truth / figure recovery | **PDF page renders** | DPI 120 PNGs; also used for final spot-check QA |

**Never do:**
- Never copy `TeX_Equ*/TeX_IEq*` equation images into the book — math must
  become real LaTeX text.
- Never trust the `.tex` file for chapter boundaries (this book's tex is
  **missing `\section*` headings for chapters 3, 6, 10**; "Solutions" and
  "Problems" appear as sibling sections; front-matter junk slices exist).
- Never paraphrase prose. Faithful conversion, typo fixes only where the PDF
  confirms the tex/EPUB is wrong.

## Output Directory Convention

All scratch work goes under `work/` (git-ignored). The MyST edition is the
repository's primary deliverable and lives at the repository root. The legacy
LaTeX rendition and its images live under `latex/`:

```
./
├── myst.yml
├── index.md               ← title page + license/attribution + {toc}
├── references.bib
├── chapters/
│   ├── ch-01-units-and-vectors.md
│   ├── ...
│   └── ch-10-oscillatory-motion.md
└── images/
    └── ch-01/…ch-10/      ← figure PNGs copied from EPUB extract
latex/
├── principlesOfMechanics.tex
└── images/                 ← legacy PDF-extraction images
work/                      ← git-ignored scratch
├── epub/                  ← extract_epub.py output (manifest + sidecars)
├── pages/                 ← PDF page renders (page_001.png …)
└── tex/                   ← split_latex.py output (slices + slices.json)
outline.json               ← book plan (BookPlan schema, Phase 2)
```

---

## Workflow

### Phase 0 — Verify environment

```bash
myst -v && python3 -c "import pymupdf, bs4, PIL, lxml; print('deps OK')"
```

Install anything missing (see Environment). Create `work/` dirs.

### Phase 1 — Extract all sources

```bash
python3 {SKILL_DIR}/scripts/extract_epub.py tmp/PrinciplesOfMechanics.epub --out work/epub
python3 {SKILL_DIR}/scripts/pdf_to_images.py tmp/PrinciplesOfMechanics.pdf --dpi 120 --out work/pages
python3 {SKILL_DIR}/scripts/split_latex.py latex/principlesOfMechanics.tex --out work/tex
```

Outputs:
- `work/epub/manifest.json` — 10 chapters in spine order: titles, section
  trees, counts, `figures_sidecar` / `math_sidecar` paths.
- `work/epub/math_chNN.json` — ordered equation list:
  `{"kind": "inline|display", "id": "EquN", "file": "…", "latex": "…"}`.
- `work/epub/figures_chNN.json` — ordered figures:
  `{"file": "…FigN_HTML.png", "number": "Fig. 1.1", "caption": "…"}`.
- `work/pages/` — `page_001.png` … `page_179.png` (JSON page map on stdout).
- `work/tex/slices.json` — 50+ slices with stats (examples found, broken
  `image-not-found` refs, dollar parity, `\mathrm{~}` counts).

Map tex slices onto EPUB chapters by title (e.g. slice "Units and Vectors" →
ch 1). Slices titled "Solution X.Y", "Problems", "Scalar Triple Product" etc.
belong to the preceding chapter. Chapters 3, 6, 10 have **no** tex slice —
their math comes entirely from EPUB alt text.

### Phase 2 — Read & plan (`outline.json`)

Read each chapter's manifest entry, section tree, and sidecars. Spot-view 3–5
PDF page renders per chapter to calibrate (figures are dense; page ranges in
the PDF roughly track chapter order). Then write `outline.json`:

```json
{
  "book": {
    "title": "Principles of Mechanics",
    "subtitle": "Fundamental University Physics",
    "authors": ["Salma Alrasheed"],
    "date": 2019,
    "doi": "10.1007/978-3-030-15195-9",
    "license": "CC-BY-4.0",
    "source_url": "https://link.springer.com/book/10.1007/978-3-030-15195-9"
  },
  "chapters": [
    {
      "number": 1,
      "title": "Units and Vectors",
      "slug": "ch-01-units-and-vectors",
      "sources": {
        "xhtml": "work/epub/extract/OEBPS/html/459974_1_En_1_Chapter.xhtml",
        "tex_slice": "work/tex/slice_008_units-and-vectors.tex",
        "math": "work/epub/math_ch01.json",
        "figures": "work/epub/figures_ch01.json"
      },
      "source_counts": {"figures": 29, "display_eq": 124, "inline_eq": 378, "examples": 16},
      "notes": ["two 'Problems' sections in tex — EPUB has one", "…"]
    }
  ],
  "references": {"source": "backmatter XHTML", "count": 0}
}
```

`source_counts` come from the manifest; `verify_book.py` compares them
against the converted files later.

### Phase 3 — Scaffold the repository-root MyST project

1. `myst.yml`:

```yaml
version: 1
project:
  title: Principles of Mechanics
  subtitle: Fundamental University Physics
  short_title: Principles of Mechanics
  authors:
    - name: Salma Alrasheed
      corresponding: true
      affiliations:
        - institution: King Abdullah University of Science and Technology
          city: Thuwal
          country: Saudi Arabia
  date: 2019
  doi: 10.1007/978-3-030-15195-9
  license: CC-BY-4.0
  open_access: true
  bibliography: references.bib
  github: <repo owner>/PrinciplesOfMechanics
  toc:
    - file: index.md
    - file: chapters/ch-01-units-and-vectors.md
    - file: chapters/ch-02-kinematics.md
    # … all ten chapters in order …
    - file: chapters/ch-10-oscillatory-motion.md
site:
  template: book-theme
  title: Principles of Mechanics
  options:
    favicon: images/favicon.png   # optional
  actions:
    - title: Springer Open Access Book
      url: https://link.springer.com/book/10.1007/978-3-030-15195-9
  nav: []
```

   Chapter = page ⇒ MyST numbers figures/equations per page, which matches
   the book's per-chapter numbering naturally. Custom numbering (e.g.
   `Figure %s` templates) lives under `project.numbering` — see
   https://mystmd.org/guide/cross-references#numbering — only touch it if
   built-in numbering disagrees with the book.

2. `index.md` — title-page content, brief description, attribution
   (© The Author(s) 2019, CC-BY-4.0 link, source URL), then
   `:::{toc}\n:context: project\n:::`.

3. Copy figure images (figures ONLY — never `TeX_Equ*/TeX_IEq*`):

```bash
for N in 01 02 03 04 05 06 07 08 09 10; do
  mkdir -p images/ch-$N
  cp work/epub/extract/OEBPS/images/459974_1_En_${N#0}_Chapter/*_Fig*_HTML.png images/ch-$N/ 2>/dev/null || true
done
```

   (Chapter image dirs are `459974_1_En_<N>_Chapter` with unpadded N. Verify
   counts against `figures_chNN.json`.)

4. `references.bib` — this book has no formal bibliography; if a book does,
   convert backmatter `p.Citation` entries to BibTeX with keys `ref-1…ref-N`
   and map in-text `[N]` to `{cite}`ref-N``.

5. Add `work/` and `_build/` to `.gitignore`.

### Phase 4 — Convert chapters (subagents)

**Delegate each chapter to a fresh subagent** (Task tool). By now the
orchestrator context is long; a clean per-chapter context produces far better
math and figure fidelity. Launch chapters sequentially or 2–3 in parallel.

Subagent prompt template (fill placeholders):

````
You are converting Chapter {N} ("{TITLE}") of a physics textbook to MyST
Markdown. Produce exactly one file: chapters/{SLUG}.md

## Sources
1. XHTML (structure + prose authority): {XHTML_PATH}
2. Math sidecar (ordered equations with LaTeX from alt text): {MATH_JSON}
3. Figures sidecar (files + book caption numbers): {FIGURES_JSON}
   Figure images already copied to: images/ch-{NN}/
4. LaTeX slice (math cross-check only, contains OCR errors): {TEX_SLICE}
5. PDF page renders for visual verification: {PAGES_DIR} (view when unsure)

## Chapter frontmatter (first thing in the file)
---
title: {N}. {TITLE}
short_title: "Ch. {N} — {SHORT}"        # <= 40 chars
label: ch-{N}
doi: 10.1007/978-3-030-15195-9_{N}
---

## Conversion rules
- Structure: `Section1/Heading` -> `##`, `Section2` -> `###`, `Section3` ->
  `####`. KEEP the printed section numbers in the heading text (e.g.
  `## 1.1 Introduction`). Skip Springer boilerplate (ContextInformation,
  copyright, DOI banner, author contact blocks).
- Prose: one `<p class="Para">` = one paragraph. `Emphasis`/`Italic` spans ->
  `*…*`; `Bold` -> `**…**`; subscripts/superscripts -> `~…~` / `^…^`.
  Lists -> `- ` / `1. `. Do NOT paraphrase.
- Math: replace every equation <img> with LaTeX from the math sidecar
  (matched in document order: display -> ```{math} blocks, inline -> $…$).
  NEVER reference or copy the equation PNGs. Label display equations that the
  book refers back to as `:label: eq-{N}-{seq}`.
- Figures: for each entry in the figures sidecar, insert at its position in
  the flow:

  ```{figure} ../images/ch-{NN}/{file}
  :name: fig-{N}-{M}

  {caption text verbatim from the sidecar, minus the "Fig. N.M" prefix}
  ```

  where M comes from the sidecar's caption number. Subfigures (Fig a/b files)
  may share one figure block using {image} or a grid — keep it simple.
- Worked examples ("Example {N}.{k} … Solution {N}.{k} …"):

  ```{prf:example}
  :label: example-{N}-{k}
  :enumerator: {N}.{k}

  Statement…

  :::{admonition} Solution {N}.{k}
  :class: dropdown

  Worked solution…
  :::
  ```

- End-of-chapter "Problems": each numbered problem becomes

  ```{exercise}
  :label: prob-{N}-{k}
  :enumerator: {N}.{k}

  Problem text…
  ```

- Cross-references in prose: "Fig. 1.28" -> [](#fig-1-28); "Example 2.3" ->
  [](#example-2-3); "Sect. 6.3" -> [](#sec-6-3) (label sections with
  `(sec-N-M)=` anchors when referenced); "Chap. 5" -> [](#ch-5).
- Tables: markdown pipe tables, values verbatim from the XHTML/PDF.
- LaTeX cleanup when borrowing math from the .tex slice:
  `\mathrm{~}` -> `\,`; `~` inside units -> `\,`; strip OCR garbage
  (`$22-8714$`, stray "ERE"); vectors -> `\mathbf{…}` (book convention),
  units -> `\mathrm{…}`; restore list punctuation mangled to `, \cdot(`.
- When the tex and the EPUB alt LaTeX disagree, the EPUB wins; if both look
  wrong, view the PDF page render and transcribe.

## Method
Read the XHTML top to bottom, consuming the sidecars in order. Write the file
incrementally (Write then Edit-append section by section) — chapters are
500–1500 lines. Verify visually ambiguous passages against the PDF renders.

## Report back
- lines written; counts: figures, {prf:example}, {exercise}, display math
- any equations where you distrusted both sources (list them)
- any figure whose image is missing from images/ch-{NN}/
- any unresolved cross-references (no matching target in this chapter)
````

### Phase 5 — Missing figure recovery (grounding crops)

For every figure reported missing (or broken, e.g. the tex's
`image-not-found`): delegate a **fresh grounding subagent** per source page,
exactly like the reference skill:

```
Locate the figure "{visual description / caption}" on page image {PAGE_PATH}
and crop it:

1. Read the page image; find the target.
2. Bounding box in normalized 0-999 coords [X1, Y1, X2, Y2]
   (thousandths of width/height, tight fit +10-20 units margin).
3. python3 {SKILL_DIR}/scripts/crop.py --path {PAGE_PATH} \
       --box X1 Y1 X2 Y2 --name fig_{N}_{M} --out-dir images/ch-{NN}
4. Read the output PNG to verify; adjust and re-run if wrong.
Report: file path + final box.
```

Copy verified crops into `images/ch-NN/` and reference them like any
other figure.

### Phase 6 — Build & verify loop

```bash
myst build          # static site build; read ALL warnings
myst start          # interactive preview at :3000 for visual check
python3 {SKILL_DIR}/scripts/verify_book.py . --outline outline.json
```

Fix until clean:
- **Errors** (exit 1): unbalanced `$`, duplicate labels, missing image files,
  OCR residue (`\mathrm{~}`, `image-not-found`, `TeX_IEq`, `·(`, `ERE`,
  `22-8714`, raw `\section`/`\includegraphics`, `$$` blocks).
- **myst warnings**: unknown labels/links, unreferenced figures, numbering
  complaints.
- **Count mismatches** vs `outline.json` (`source_counts`) — investigate each:
  a missing figure usually means a subfigure merge or a grounding crop is
  needed; a missing example usually means an OCR-mangled heading in the EPUB
  (check the PDF).

Then visual spot-check: for each chapter, open 3 random PDF page renders and
compare against the built site (math rendering, figure placement, caption
numbers).

### Phase 7 — Final checklist

- [ ] `myst build` zero warnings; `verify_book.py` exit 0
- [ ] 10 chapter files, TOC order matches the book
- [ ] Figure counts per chapter match `source_counts` (or documented reason)
- [ ] Example/problem enumerators match the book's N.M numbering
- [ ] No equation images anywhere; all math is LaTeX (KaTeX renders)
- [ ] All in-text "Fig./Example/Sect./Chap." references resolve as links
- [ ] index.md carries © The Author(s) 2019 + CC-BY-4.0 + Springer source URL
- [ ] `work/` and `_build/` git-ignored
- [ ] Optional PDF export: add a `project.exports` entry (format `pdf`,
      template `book`, `articles:` = all chapter files) then `myst build`
- [ ] Commit only when the user asks

## Known OCR Hazards (this book's .tex)

| Symptom | Fix |
|---|---|
| `\mathrm{~}` (thin-space OCR) | `\,` |
| `$22-8714$`, stray `ERE` | delete |
| Lists flattened to `, \cdot(\mathrm{b})` inline | restore `(a)/(b)/(c)` list structure |
| Chapters 3/6/10 missing headings | EPUB is the structure authority |
| `image-not-found` includegraphics | Phase 5 grounding crop |
| Duplicate figure files `…-080(1).jpg` in legacy `images/` | prefer EPUB PNGs; legacy `images/` only as fallback |
| `\section*{Solution X.Y}` / `{Problems}` slices | merge into their chapter during conversion |
| xeCJK/polyglossia preamble | irrelevant — discard |

## Language

English book → English MyST project. No mixing.
