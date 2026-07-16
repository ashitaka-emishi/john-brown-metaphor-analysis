# Reproducibility Report

Date prepared: 2026-07-16

Source commit audited before publication approval:
`9a4ba49f077d2b9ec60533e953868791ed980f46`

## Environment

- Python: `Python 3.11.15` via `.venv/bin/python`
- Pytest: invoked through `.venv/bin/pytest`
- Quarto: `1.9.37`
- TeX/PDF engine: Quarto successfully invoked LuaHBTeX during render. The
  `lualatex` executable was not directly available on the shell PATH during
  this audit.

## Commands Run

```bash
.venv/bin/python -m lincoln_research validate
.venv/bin/pytest
quarto render paper/paper.qmd
git diff --check
```

## Results

- Project validation: passed.
- Tests: passed, 10 tests.
- Quarto render: passed, producing `outputs/paper.html` and
  `outputs/paper.pdf`.
- Diff whitespace check: passed.

## Render Notes

Quarto emitted a noncritical warning:

```text
Refusing to remove directory .../outputs/paper_files/libs since it is not a
subdirectory of the main project directory.
```

The render still completed and produced the HTML and PDF outputs.

## Data and Evidence Counts

- Evidence rows exported: 32.
- Claims audited: 9.
- Citation keys used in `paper/paper.qmd`: 25.
- Bibliography entries in `paper/references.bib`: 25.
- Missing bibliography keys: none.
- Unused bibliography keys: none.
- Missing claim-to-evidence references: none.

## Reproduction Steps

1. From the repository root, create or activate the project environment.
2. Run `.venv/bin/python -m lincoln_research validate`.
3. Run `.venv/bin/pytest`.
4. Run `quarto render paper/paper.qmd`.
5. Review generated files in `outputs/`.
6. Confirm that source caveats in `publication-readme.md` and
   `publication-audit.md` remain acceptable for the intended publication venue.

## Package Boundary

The output package intentionally excludes raw and normalized corpus files. Those
remain in the repository research structure and are not copied into `outputs/`.
