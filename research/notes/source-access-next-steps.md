# Source Access Next Steps

Status: active follow-up after Goal 10 acquisition completion.

## AUC John Brown Collection

Next step completed: inspected a high-priority public digital-object page for
`Correspondence and Map, John Brown to Seth Thompson, January 4, 1836`
(`digital_objects/6800`).

Result:

- The public digital-object metadata page was preserved locally as
  `research/corpus/primary/raw/SRC-AUC-CAND-6800-digital-object.html`.
- The linked handle URL `http://hdl.handle.net/20.500.12322/auc.028:0053`
  returned HTTP 403 during direct acquisition.
- The collection-level rights statement remains controlling: underlying
  materials may be protected by copyright and/or repository or copyright-holder
  property.
- After the scholar manually handled the AUC CAPTCHA and supplied the permitted
  PDF, citation, and item-level metadata, `auc.028.0053` was registered as
  `SRC-0019`. The supplied item metadata states `NO COPYRIGHT - UNITED STATES`
  with rights statement `http://rightsstatements.org/vocab/NoC-US/1.0/`.
- Codex moved the scholar-supplied PDF into the raw corpus and generated a
  manifest hash. Because the item-level metadata supplied by the scholar states
  `NO COPYRIGHT - UNITED STATES`, this specific raw PDF and its raw manifest
  may be tracked in the public repository. The attempted text extraction
  produced only form-feed characters, so the normalized file is a placeholder
  rather than a usable OCR or transcription. No password, cookie, browser
  profile, or private account state was captured.
- A later local OCR pass rendered the PDF at 300 DPI and ran Tesseract 5.5.2,
  producing
  `research/corpus/primary/normalized/SRC-0019-auc-028-0053-correspondence-map-brown-thompson-1836-ocr.txt`.
  The result is noisy discovery OCR, not verified transcription.

Human feedback gate:

The gate is cleared only for `auc.028.0053` / `SRC-0019` because the scholar
provided item-level rights metadata and the file. Public raw-file tracking is
also limited to this item. Other AUC digital objects remain gated: decide
whether to authorize repository-contact workflow or repeat the human-mediated
inspection/download protocol for each item.

Prepared follow-up:

- Created `research/notes/auc-contact-draft.md` with a repository-contact
  email draft and a human-in-browser inspection protocol.
- No email has been sent.
- No login, CAPTCHA, browser-cookie capture, or restricted download has been
  attempted.
- Browser control was unavailable in the Codex session, so the current AUC
  path is manual scholar inspection of the page and terms.
- The manual protocol succeeded for `auc.028.0053`; carry it forward for any
  additional AUC objects unless AUC supplies broader written guidance.

## Contemporary Trial Witnesses

Next step completed: looked beyond modern derivative pages for stronger public
trial-address witnesses.

Result:

- Added `SRC-0013`, the Internet Archive / New York Times issue from
  1859-11-03, after OCR search found the opening of Brown's courtroom speech.
- Added `SRC-0015`, the Avalon Project hosted transcription of `Life, Trial and
  Execution of Captain John Brown; 1859`, as discovery/comparison text.
- Added `SRC-0016`, the Internet Archive page-image scan of the 1859 De Witt
  pamphlet that corresponds to the Avalon text, as the preferred source witness
  over the hosted transcription.
- Follow-up web search confirmed the Richmond Dispatch witness as a known
  comparison target, but no public scan was acquired in this pass.
- Added `SRC-0017`, the Internet Archive / Milwaukee Daily Sentinel issue from
  1859-11-03, as a second contemporary newspaper witness candidate. The IA
  DjVuTXT derivative returned HTTP 500, so normalized working text was extracted
  locally from the public PDF.

Carry-forward:

In Goal 20, compare `SRC-0010`, `SRC-0013`, `SRC-0015`, `SRC-0016`, and any
additional contemporary newspaper witnesses before finalizing courtroom-address
wording.

## Digital Commonwealth / Boston Public Library

Next step completed: used Digital Commonwealth public search, JSON, and IIIF
routes to locate and preserve one additional high-value Brown-authored item.

Result:

- Added `SRC-0014`, John Brown autograph letter signed to Thomas Wentworth
  Higginson, Charlestown, Jefferson County, Virginia, 1859-11-22.
- Added `SRC-0018`, John Brown autograph letter signed to "Dear Wife and
  Children All," Chambersburg, Pennsylvania, 1859-10-01.
- Preserved repository metadata, IIIF manifest, page images, raw manifest, and
  noisy local OCR for targeted autograph-letter acquisitions.
- Repository metadata and IIIF manifest state no known copyright restrictions
  and no known restrictions on use.

Carry-forward:

Continue targeted Digital Commonwealth acquisition only where an item advances
coverage or verification. Avoid collection-wide bulk acquisition.
