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

## SRC-0003 - Extracts From Letters by John Brown

Checkpoint date: 2026-07-21

Acquisition status: acquired as Internet Archive / Boston Public Library
metadata and scan derivatives; normalized as working OCR only.

Source: Internet Archive item `extractsfromlett00mays`, cataloged as
`[Extracts from letters by John Brown] [manuscript]`.

Raw preservation:

- `research/corpus/primary/raw/SRC-0003-extractsfromlett00mays-metadata.json`
- `research/corpus/primary/raw/SRC-0003-extractsfromlett00mays.pdf`
- `research/corpus/primary/raw/SRC-0003-extractsfromlett00mays-djvu.txt`
- `research/corpus/primary/raw/SRC-0003-extractsfromlett00mays-djvu.xml`
- `research/corpus/primary/raw/SRC-0003-extractsfromlett00mays-manifest.sha256`

Normalized derivative:

- `research/corpus/primary/normalized/SRC-0003-extractsfromlett00mays-ocr.txt`

Provenance and rights:

- Internet Archive metadata identifies the item contributor as Boston Public
  Library.
- The metadata describes the source as a holograph and states that the extracts
  are copies in Samuel May's hand of Brown's original correspondence.
- The metadata does not expose an explicit rights or license field in the
  preserved JSON.

Verification caveats:

- This is not an autograph Brown manuscript. It is a copied extract witness and
  must carry that attribution caveat in any later use.
- The OCR is extremely noisy because the source is manuscript handwriting.
- Initial guessed IA derivative filenames returned 404; advertised filenames
  from the item metadata were then used.

Permitted next use:

Use `SRC-0003` for Goal 20 manuscript-copy verification and segmentation only.
Do not quote, code, or infer from the OCR until the relevant passages are
checked against the PDF or image-derived source witness.

## SRC-0008 - Copies of Correspondence to and From John Brown

Checkpoint date: 2026-07-21

Acquisition status: acquired as Digital Commonwealth / Boston Public Library
item metadata, IIIF manifest, page images, transcription metadata, and
repository text derivative; normalized as transcription text pending
image-level verification.

Source: Digital Commonwealth item `commonwealth:dv143964q`, discovered from
the approved `SRC-0001` collection.

Raw preservation:

- `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-dv143964q-metadata.json`
- `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-dv143964q-manifest.json`
- `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-8p58s2051-transcription.json`
- `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-8p58s2051-text-plain.txt`
- `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-dv1439650.jpg`
- `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-dv1439668.jpg`
- `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-dv143967j.jpg`
- `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-dv143968t.jpg`
- `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-dv143964q-manifest.sha256`

Normalized derivative:

- `research/corpus/primary/normalized/SRC-0008-digitalcommonwealth-dv143964q-transcription.txt`

Provenance and rights:

- Digital Commonwealth metadata lists the item under the Boston Public Library
  Anti-Slavery Collection, with local call number `MS B.1.6 v.1, p.49`.
- The IIIF manifest and metadata state no known copyright restrictions and no
  known restrictions on use.
- The acquisition used Digital Commonwealth's documented JSON and IIIF access
  routes and the advertised transcription derivative key.

Verification caveats:

- The item consists of copies/transcriptions, not necessarily Brown autograph
  documents.
- Metadata says the transcriptions and annotations are not in the same hand and
  identifies May as annotator.
- The normalized text is a repository transcription derivative and must be
  checked against the preserved page images before quotation or coding.
- The human-facing item page returned browser verification in one web view;
  documented JSON and IIIF endpoints remained available and were used.

Permitted next use:

Use `SRC-0008` in Goal 20 for item-level verification and segmentation within
the correspondence-copy tier. Do not treat repository transcription wording as
final without page-image comparison.

## SRC-0006 - NARA Senate Records Guide

Checkpoint date: 2026-07-21

Acquisition status: acquired as a National Archives public finding-aid page and
normalized discovery text.

Raw preservation:

- `research/corpus/primary/raw/SRC-0006-nara-senate-guide.html`
- `research/corpus/primary/raw/SRC-0006-nara-senate-guide-manifest.sha256`

Normalized derivative:

- `research/corpus/primary/normalized/SRC-0006-nara-senate-guide.txt`

Provenance and rights:

- The guide identifies the Senate Select Committee to Inquire into the Facts
  Attending the Invasion and Seizure of the United States Armory at Harpers
  Ferry and National Archives Microfilm Publication `M1196`.
- This source is a guide to federal records, not Brown-authored evidence.

Permitted next use:

Use `SRC-0006` as a provenance and discovery source for locating government
records. Do not code it as Brown language or as a witness to Brown's rhetoric.

## SRC-0007 - AUC John Brown Collection Finding Aid

Checkpoint date: 2026-07-21

Acquisition status: acquired as public finding-aid overview, inventory, and
digitized-materials listing pages. Underlying item acquisition is blocked until
rights and access terms are resolved.

Raw preservation:

- `research/corpus/primary/raw/SRC-0007-auc-john-brown-collection.html`
- `research/corpus/primary/raw/SRC-0007-auc-john-brown-collection-inventory.html`
- `research/corpus/primary/raw/SRC-0007-auc-john-brown-collection-digitized.html`
- `research/corpus/primary/raw/SRC-0007-auc-john-brown-collection-manifest.sha256`

Normalized derivative:

- `research/corpus/primary/normalized/SRC-0007-auc-john-brown-collection-finding-aid.txt`

Provenance and rights:

- The finding aid identifies the collection as correspondence and papers of
  John Brown, relatives, and associates, with majority dates 1826-1859.
- The public digitized-materials listing identifies many digital records,
  including early Seth Thompson correspondence and Harpers Ferry-related
  letters.
- The rights statement says collection materials are protected by copyright
  and/or are property of the Robert W. Woodruff Library at Atlanta University
  Center and/or the copyright holder.

Stop condition:

Do not acquire underlying AUC manuscript images or quote from them until public
download/use terms are established or the scholar authorizes a repository
contact workflow.

## SRC-0009 - Harpers Ferry Investigation, 1860

Checkpoint date: 2026-07-21

Acquisition status: acquired as a United States Senate public PDF and extracted
working text.

Raw preservation:

- `research/corpus/primary/raw/SRC-0009-senate-harpers-ferry-investigation-1860.pdf`
- `research/corpus/primary/raw/SRC-0009-senate-harpers-ferry-investigation-1860-manifest.sha256`

Normalized derivative:

- `research/corpus/primary/normalized/SRC-0009-senate-harpers-ferry-investigation-1860.txt`

Provenance and rights:

- The PDF is a public United States Senate scan of the 1860 Harpers Ferry
  investigation report.
- The source is a government report and testimony compilation, not a
  Brown-authored source.

Verification caveats:

- The extracted text is OCR-like and imperfect. Verify any use against the PDF
  image.
- Brown statements in this report are reported/government-record witnesses and
  require attribution caveats.

Permitted next use:

Use `SRC-0009` for Goal 20 government-record segmentation and to identify
reported statements or testimony that require locator-level verification.
