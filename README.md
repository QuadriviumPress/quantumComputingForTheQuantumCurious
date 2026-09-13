# Quantum Computing for the Quantum Curious

This repository contains a MyST Markdown edition of *Quantum Computing for
the Quantum Curious* by Ciaran Hughes, Joshua Isaacson, Anastasia Perry,
Ranbel F. Sun, and Jessica Turner. The MyST book is the primary edition
maintained here: its configuration, chapters, and figure assets all live at
the repository root.

The original book was published by Springer in 2021 and is available as an
open-access work at
[doi:10.1007/978-3-030-61601-4](https://doi.org/10.1007/978-3-030-61601-4).
This rendition preserves the book's prose, equations, figures, worksheets,
and chapter structure in an accessible web-native format.

## Read and edit the MyST edition

The main entry points are:

- [`myst.yml`](myst.yml) — project metadata and table of contents
- [`index.md`](index.md) — book landing page
- [`chapters/`](chapters/) — the ten converted chapters
- [`images/`](images/) — EPUB-derived chapter figures

## Build

```bash
npm install
npm run start          # preview
npm run verify         # structural and conversion checks
npm run build          # static site in _build/html/
npm run check          # verify and build
```

CI runs on pull requests (`.github/workflows/ci.yml`); pushes to `main`
deploy via [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

## Live site

https://quadriviumpress.com/QuantumComputingForTheQuantumCurious/

## License

© The Author(s) 2021. The original book and this MyST edition are licensed
under the [Creative Commons Attribution 4.0 International License
(CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
