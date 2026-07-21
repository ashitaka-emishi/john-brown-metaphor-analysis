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

## SRC-0019 - Brown to Seth Thompson, 1836-01-04

Checkpoint date: 2026-07-21

Acquisition status: acquired through human-mediated AUC RADAR access after the
scholar completed the CAPTCHA flow and supplied the PDF, citation, metadata,
and rights statement. The raw PDF is tracked in the repository because the
scholar supplied item-level `NO COPYRIGHT - UNITED STATES` metadata. Initial
embedded-text extraction produced only form-feed characters; a later Tesseract
OCR pass created noisy discovery text.

Source: `Correspondence and Map, John Brown to Seth Thompson, January 4, 1836`,
Robert W. Woodruff Library of the Atlanta University Center, Inc.,
`http://hdl.handle.net/20.500.12322/auc.028:0053`.

Raw preservation:

- `research/corpus/primary/raw/SRC-0019-auc-028-0053-correspondence-map-brown-thompson-1836.pdf`
- `research/corpus/primary/raw/SRC-0019-auc-028-0053-correspondence-map-brown-thompson-1836-manifest.sha256`

Normalized derivative:

- `research/corpus/primary/normalized/SRC-0019-auc-028-0053-correspondence-map-brown-thompson-1836.txt`
- `research/corpus/primary/normalized/SRC-0019-auc-028-0053-correspondence-map-brown-thompson-1836-ocr.txt`
- `research/corpus/primary/normalized/SRC-0019-auc-028-0053-correspondence-map-brown-thompson-1836-ocr.sha256`

The original normalized derivative is a placeholder created by `pdftotext`; it
is not a usable transcription. The `-ocr.txt` file was generated with
Tesseract 5.5.2 from 300 DPI `pdftoppm` page renders. It is machine OCR only,
not a verified transcription.

Provenance and rights:

- AUC metadata supplied by the scholar identifies Brown as correspondent and
  Seth Thompson as addressee.
- Local identifier: `auc.028.0053`.
- Extent: 5 pages.
- Series: `John Brown Collection, Correspondence: Seth Thompson, 1814-1831
  Series`.
- Rights statement supplied from the AUC metadata: `NO COPYRIGHT - UNITED
  STATES`, `http://rightsstatements.org/vocab/NoC-US/1.0/`.
- Public repository tracking is limited to this item-level raw PDF and its raw
  manifest and does not apply to other AUC objects.

Verification caveats:

- Codex did not access AUC through stored credentials or captured browser
  state; the scholar performed the CAPTCHA-gated step and supplied the file.
- The OCR is noisy on handwritten pages and more legible on the typed dealer
  notes on pages 4 and 5.
- A manual transcription or corrected OCR must be verified against the PDF page
  images before any quotation, passage segmentation, or coding.
- This acquisition clears access only for `auc.028.0053`; it does not establish
  permission or rights status for other AUC objects.

Permitted next use:

Use this as a Tier 1 formation/baseline witness for Goal 20 transcription
correction, verification, and segmentation. The OCR may support discovery and
navigation only; do not quote or code it until page-image verification is
complete.

## SRC-0010 - Testimonies of Capt. John Brown

Checkpoint date: 2026-07-21

Acquisition status: acquired as Internet Archive metadata, PDF, DjVu OCR, and
DjVu XML; normalized as working OCR.

Source: `Testimonies of Capt. John Brown, at Harper's Ferry: with his address
to the court`, published by the American Anti-Slavery Society in 1860.

Verification caveats:

- This is a posthumous published pamphlet witness, not a stenographic court
  original.
- The publisher's framing belongs to the American Anti-Slavery Society and must
  be separated from Brown-attributed text.
- Compare any courtroom-address quotation against contemporary newspaper or
  government witnesses before final use.

Permitted next use:

Use `SRC-0010` in Goal 20 as a stronger public witness than modern web
derivative pages for the courtroom-address branch, with posthumous publication
and editorial-framing caveats.

## SRC-0013 - The New York Times, 1859-11-03

Checkpoint date: 2026-07-21

Acquisition status: acquired as Internet Archive metadata, full issue PDF,
DjVu OCR text, and DjVu XML; normalized as working OCR.

Source: `The New York Times 1859-11-03: Vol. 9, Iss. 2534`.

Verification caveats:

- This is a contemporary newspaper report, not a Brown-authored manuscript.
- OCR contains the opening of Brown's courtroom speech, but exact wording,
  page, and column must be verified against the PDF scan.
- Reuse rights are not explicit in Internet Archive item metadata.

Permitted next use:

Use `SRC-0013` in Goal 20 as a contemporary newspaper witness candidate for
Brown's courtroom-address wording.

## SRC-0017 - Milwaukee Daily Sentinel, 1859-11-03

Checkpoint date: 2026-07-21

Acquisition status: acquired as Internet Archive metadata, full issue PDF, and
DjVu XML; normalized as working text extracted locally from the PDF.

Source: `Milwaukee Daily Sentinel (1859-11-03)`.

Verification caveats:

- This is a contemporary newspaper report, not a Brown-authored manuscript.
- OCR/text extraction contains the opening of Brown's courtroom speech, but
  exact wording, page, and column must be verified against the PDF scan.
- The advertised Internet Archive DjVuTXT derivative returned HTTP 500 during
  acquisition; this failure is recorded in the source register.
- Reuse rights are not explicit in Internet Archive item metadata.

Permitted next use:

Use `SRC-0017` in Goal 20 as a second contemporary newspaper witness candidate
for Brown's courtroom-address wording.

## SRC-0015 - Avalon Project Hosted De Witt Text

Checkpoint date: 2026-07-21

Acquisition status: acquired as a hosted web transcription and normalized text.

Source: Avalon Project at Yale Law School, `Life, Trial and Execution of
Captain John Brown; 1859`.

Verification caveats:

- Avalon is a hosted transcription, not the preferred page-image witness.
- Use it for navigation and comparison against `SRC-0016`, not as
  quotation-final evidence.

Permitted next use:

Use `SRC-0015` as discovery/comparison text in Goal 20, subordinate to the
Internet Archive De Witt scan.

## SRC-0016 - De Witt Life, Trial, and Execution Pamphlet

Checkpoint date: 2026-07-21

Acquisition status: acquired as Internet Archive metadata, PDF, DjVu OCR text,
and DjVu XML; normalized as working OCR.

Source: 1859 Robert M. De Witt pamphlet, `The life, trial, and execution of
Captain John Brown`.

Verification caveats:

- The pamphlet is a published compilation, not Brown-authored as a whole.
- Brown-attributed statements require locator-level verification against the
  scan and comparison with newspaper/government witnesses.
- Internet Archive metadata does not expose an explicit rights or license
  field.

Permitted next use:

Use `SRC-0016` in Goal 20 as the page-image/OCR witness corresponding to the
Avalon-hosted De Witt text.

## SRC-0004 and SRC-0005 - Modern Trial-Statement Discovery Pages

Checkpoint date: 2026-07-21

Acquisition status: acquired as public web pages and normalized discovery text
only.

Sources:

- `SRC-0004`: House Divided / Dickinson College, `John Brown's Statement
  (1859)`.
- `SRC-0005`: Famous Trials, `John Brown's Speech to the Court at his Trial`.

Stop condition:

These are not approved source substitutions and are not quotation-final. Use
them only to identify wording, source trails, and comparison targets. Do not
let either page anchor evidence coding unless the scholar explicitly approves
source substitution after stronger-witness comparison.

## SRC-0011 and SRC-0012 - Kansas-Period Autograph Letters

Checkpoint date: 2026-07-21

Acquisition status: acquired as Digital Commonwealth / Boston Public Library
item metadata, IIIF manifests, and page images; normalized as local working OCR
only.

Sources:

- `SRC-0011`: `John Brown autograph letter to "Dear Friend and Other Friends",
  Osawatomie, Kansas, 10 & 13 September 1858`.
- `SRC-0012`: `John Brown autograph letter signed to Franklin Benjamin
  Sanborn, Missouri Line, 20 & 30 July, 6 August 1858`.

Provenance and rights:

- Digital Commonwealth metadata identifies both as Brown autograph letters.
- Repository metadata and IIIF manifests state no known copyright restrictions
  and no known restrictions on use.
- Repository metadata says the letters were printed in F. B. Sanborn's `The
  Life and Letters of John Brown`.

Verification caveats:

- No repository transcription was advertised for either item.
- Local manuscript OCR is noisy and discovery-only.
- Quote, segmentation, and coding work must be done from page-image
  verification in Goal 20.

Permitted next use:

Use these as Tier 1 Kansas-period witnesses for Goal 20 transcription
verification and segmentation.

## SRC-0014 - Brown to Thomas Wentworth Higginson, 1859-11-22

Checkpoint date: 2026-07-21

Acquisition status: acquired as Digital Commonwealth / Boston Public Library
item metadata, IIIF manifest, and page images; normalized as local working OCR
only.

Source: `John Brown autograph letter signed to Thomas Wentworth Higginson,
Charlestown, Jefferson Co., Va., 22 November 1859`.

Provenance and rights:

- Digital Commonwealth metadata identifies Brown as author and Higginson as
  addressee.
- Repository metadata lists local call number `MS E.5.1, pt. 2, p. 117`.
- Repository metadata and IIIF manifest state no known copyright restrictions
  and no known restrictions on use.

Verification caveats:

- No repository transcription was advertised.
- Local manuscript OCR is noisy and discovery-only.
- Quote, segmentation, and coding work must be done from page-image
  verification in Goal 20.

Permitted next use:

Use this as a Tier 1 prison-period Brown-authored witness for Goal 20
transcription verification and segmentation.

## SRC-0018 - Brown to Wife and Children, 1859-10-01

Checkpoint date: 2026-07-21

Acquisition status: acquired as Digital Commonwealth / Boston Public Library
item metadata, IIIF manifest, and page images; normalized as local working OCR
only.

Source: `John Brown autograph letter signed to "Dear Wife and Children All",
Chambersburg, PA, 1 October 1859`.

Provenance and rights:

- Digital Commonwealth metadata identifies Brown as author and Mary Ann Day
  Brown as addressee.
- Repository metadata lists local call number `MS E.5.1, pt. 1, p. 40`.
- Repository metadata and IIIF manifest state no known copyright restrictions
  and no known restrictions on use.

Verification caveats:

- No repository transcription was advertised.
- Local manuscript OCR is noisy and discovery-only.
- Metadata notes verso epitaphs; quotation, segmentation, and coding require
  page-image verification in Goal 20.

Permitted next use:

Use this as a Tier 1 pre-raid/family-correspondence witness for Goal 20
transcription verification and segmentation.
