# Corpus Report

Status: Goal 10 acquisition in progress. No source is yet cleared for
interpretive or thesis-bearing use.

## SRC-0002 - Provisional Constitution and Ordinances

Checkpoint date: 2026-07-21

Acquisition status: acquired as raw page images and repository metadata;
normalized as working OCR only.

Source: DocsTeach / National Archives page for `Provisional Constitution and
Ordinances for the People of the United States Written by John Brown`, National
Archives Identifier 3819337.

Raw preservation:

- `research/corpus/primary/raw/SRC-0002-provisional-constitution-docsteach.html`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-docsteach-image.jpg`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-docsteach-media.json`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-page-01.webp`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-page-02.webp`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-page-03.webp`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-page-04.webp`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-page-05.webp`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-page-06.webp`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-page-07.webp`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-page-08.webp`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-page-09.webp`
- `research/corpus/primary/raw/SRC-0002-provisional-constitution-manifest.sha256`

Normalized derivative:

- `research/corpus/primary/normalized/SRC-0002-provisional-constitution-ocr.txt`
- `research/corpus/primary/normalized/SRC-0002-ocr-pages/`

Provenance and rights:

- DocsTeach identifies the record as from Records of the Adjutant General's
  Office, Record Group 94, National Archives Identifier 3819337.
- The preserved DocsTeach page states Public Domain, Free of Known Copyright
  Restrictions.
- The acquisition used public DocsTeach page and media URLs with conservative
  request delay and a descriptive research user agent.

Verification caveats:

- The normalized OCR is noisy and must not be used as quotation-final text.
- Page 09 produced no OCR text; verify whether it contains only non-textual or
  low-contrast content before any segmentation claim.
- The DocsTeach media endpoint lists duplicate page-image uploads. This
  checkpoint preserved one consistent nine-page image set from the same upload
  path and recorded the full media JSON for audit.
- National Archives Catalog API follow-up returned application HTML rather than
  parseable record JSON during this checkpoint; the preserved DocsTeach page is
  the current metadata witness.

Permitted next use:

Use `SRC-0002` in Goal 20 textual verification and segmentation. Do not quote
or code interpretively from the OCR until text is checked against the raw page
images.
