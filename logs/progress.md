# Progress Log

## Current state

Repository migrated to the John Brown metaphor-analysis mission. Goal 10 corpus
acquisition is complete at the acquisition level. Acquired sources have been
preserved locally with raw manifests, normalized working text or transcription
derivatives, hashes, rights notes, and verification-status caveats. No acquired
source is quotation-final, evidence coded, thesis-bearing, or
publication-approved.
Goal 10 completion audit is complete: acquisition-level coverage exists for
all approved corpus periods, with AUC underlying manuscript acquisition blocked
by rights/access terms and modern derivative trial pages limited to discovery.

## Next checkpoint

Begin Goal 20 textual verification and segmentation. Do not populate evidence
rows, form a thesis, or publish findings until quotations and segments are
checked against preserved source witnesses.

### 2026-07-21 - Goal 10 SRC-0002 acquisition

- Checkpoint scope: acquire and preserve `SRC-0002`, the DocsTeach / National
  Archives page images and metadata for `Provisional Constitution and
  Ordinances for the People of the United States Written by John Brown`.
- Preserved the DocsTeach HTML page, thumbnail image, WordPress media metadata,
  and a nine-page full-resolution image set under
  `research/corpus/primary/raw/`.
- Created a raw-file SHA-256 manifest at
  `research/corpus/primary/raw/SRC-0002-provisional-constitution-manifest.sha256`.
- Generated page-level OCR and a combined normalized working OCR file at
  `research/corpus/primary/normalized/SRC-0002-provisional-constitution-ocr.txt`.
- Updated `research/data/source-register.csv` with local paths, retrieval
  timestamp, manifest hash, rights statement, acquisition method, and
  `acquired-ocr-unverified` status.
- Created `research/notes/corpus-report.md` with provenance, rights, and
  verification caveats for the source.
- The OCR is noisy and is not quotation-final. Any quotation, segmentation, or
  evidence coding must be verified against the preserved page images in Goal 20.
- DocsTeach media metadata included duplicate page-image uploads; this
  checkpoint preserved one consistent nine-page set and retained the media JSON
  for audit.
- The skill-referenced `references/source-acquisition.md` file is absent in
  this migrated repository, so acquisition followed `AGENTS.md`,
  `goals/10-corpus-acquisition.md`, and
  `research/notes/source-acquisition-plan.md`.

### 2026-07-21 - Goal 10 SRC-0003 acquisition

- Checkpoint scope: acquire and preserve `SRC-0003`, the Internet Archive /
  Boston Public Library item `[Extracts from letters by John Brown]
  [manuscript]`.
- Preserved Internet Archive metadata JSON, Text PDF, DjVu OCR text, and DjVu
  XML under `research/corpus/primary/raw/`.
- Created a raw-file SHA-256 manifest at
  `research/corpus/primary/raw/SRC-0003-extractsfromlett00mays-manifest.sha256`.
- Generated a normalized working OCR file at
  `research/corpus/primary/normalized/SRC-0003-extractsfromlett00mays-ocr.txt`.
- Updated `research/data/source-register.csv` with local paths, retrieval
  timestamp, manifest hash, rights note, acquisition method, and
  `acquired-ocr-unverified` status.
- Updated `research/notes/corpus-report.md` with provenance and verification
  caveats.
- Item metadata describes the witness as copies in Samuel May's hand of Brown's
  original correspondence, with a cataloger-supplied title; it is not an
  autograph Brown manuscript.
- The OCR is extremely noisy and may be used only for discovery until manually
  checked against the scan witness.
- Initial guessed Internet Archive derivative filenames returned 404; the
  acquisition used filenames advertised in the preserved item metadata.

### 2026-07-21 - Goal 10 SRC-0008 item-level acquisition

- Checkpoint scope: acquire one item-level correspondence witness from the
  approved `SRC-0001` Digital Commonwealth / Boston Public Library collection.
- Added `SRC-0008`, `Copies of correspondence to and from John Brown`, to
  `research/data/source-register.csv`.
- Preserved Digital Commonwealth item JSON, IIIF manifest, four IIIF page
  images, transcription-object JSON, and the advertised plain-text derivative
  under `research/corpus/primary/raw/`.
- Created a raw-file SHA-256 manifest at
  `research/corpus/primary/raw/SRC-0008-digitalcommonwealth-dv143964q-manifest.sha256`.
- Generated a normalized transcription derivative at
  `research/corpus/primary/normalized/SRC-0008-digitalcommonwealth-dv143964q-transcription.txt`.
- Updated `research/notes/corpus-report.md` with provenance, rights, and
  verification caveats.
- Digital Commonwealth metadata lists no known copyright restrictions and no
  known restrictions on use, and identifies the item as Boston Public Library
  Anti-Slavery Collection material with local call number `MS B.1.6 v.1, p.49`.
- The source remains `acquired-transcription-unverified`: it consists of
  copies/transcriptions, not necessarily Brown autograph documents, and the
  repository transcription must be checked against the page images before
  quotation or coding.
- The human-facing page returned browser verification in one web view; the
  documented `.json` and IIIF endpoints remained available and were used.

### 2026-07-21 - Goal 10 derivative-source gate

- Stop condition reached before acquiring derivative or reported trial-text
  targets as anything more than discovery sources.
- Remaining queue items include derivative or reported courtroom-statement
  pages (`SRC-0004`, `SRC-0005`), federal-record finding-aid material
  (`SRC-0006`), and repository finding-aid or item-level acquisition work
  (`SRC-0001`, `SRC-0007`).
- The next human decision should choose whether to authorize discovery-only
  acquisition of derivative trial pages, require stronger contemporary
  witnesses first, or continue acquiring collection/finding-aid materials.
- No interpretation, thesis, evidence coding, source substitution, or
  publication decision is approved by the current acquisition checkpoint.

### 2026-07-21 - Goal 10 SRC-0006, SRC-0007, and SRC-0009 acquisition

- Checkpoint scope: continue Goal 10 after the user's instruction to complete
  the goal by acquiring non-derivative public finding-aid and government-report
  targets before derivative trial pages.
- Preserved the National Archives Senate guide page for `SRC-0006` and
  normalized it as finding-aid/discovery text.
- Preserved AUC John Brown collection overview, inventory, and digitized
  material listing pages for `SRC-0007` and normalized them as finding-aid
  discovery text.
- AUC underlying item-level acquisition is blocked at this checkpoint because
  the finding-aid rights statement says materials are protected by copyright
  and/or repository or copyright-holder property; no image download or
  quotation use is authorized without clearer terms or repository-contact
  workflow approval.
- Added and acquired `SRC-0009`, the United States Senate public PDF
  `Harpers Ferry Investigation, 1860`, as a stronger government-record witness
  for the capture/trial period.
- Extracted normalized working text from the Senate PDF. The extraction is
  imperfect and must be checked against the PDF before quotation or evidence
  coding.
- Updated `research/data/source-register.csv` and
  `research/notes/corpus-report.md` with paths, hashes, rights notes,
  provenance, and verification caveats.

### 2026-07-21 - Goal 10 trial and Kansas branch acquisition

- Checkpoint scope: acquire stronger trial-address and Kansas-period witnesses
  while keeping derivative pages in discovery-only status.
- Added and acquired `SRC-0010`, the 1860 American Anti-Slavery Society
  pamphlet `Testimonies of Capt. John Brown, at Harper's Ferry: with his
  address to the court`, from Internet Archive.
- Acquired `SRC-0004` and `SRC-0005` public web pages as discovery-only modern
  derivative sources. They are not approved source substitutions and are not
  quotation-final.
- Located and acquired two Digital Commonwealth / Boston Public Library
  Kansas-period autograph letters:
  `SRC-0011`, Brown to "Dear Friend and Other Friends", Osawatomie, Kansas,
  10 and 13 September 1858, and `SRC-0012`, Brown to Franklin Benjamin
  Sanborn, Missouri Line, 20 and 30 July and 6 August 1858.
- Preserved metadata, IIIF manifests, page images, and raw/OCR derivatives as
  available; generated noisy local manuscript OCR for `SRC-0011` and
  `SRC-0012` because no repository transcription was advertised.
- Updated `research/data/source-register.csv` and
  `research/notes/corpus-report.md` with paths, hashes, rights notes,
  provenance, and verification caveats.
- No source was marked quotation-final or evidence-coded.

### 2026-07-21 - Goal 10 completion audit

- Created `research/notes/source-substitution-log.md`.
- Created `research/notes/goal-10-completion-audit.md`.
- Source-substitution status: no thesis-bearing source substitution is
  approved. `SRC-0004` and `SRC-0005` are discovery-only; `SRC-0010` is a
  stronger public pamphlet witness but remains posthumous and
  quotation-unverified.
- Corpus period status at acquisition level:
  formation/baseline acquired with remaining AUC possibilities blocked;
  Kansas/armed resistance acquired through Tier 1 autograph letters;
  preparation acquired through `SRC-0002`; capture/trial/imprisonment/execution
  acquired through government, pamphlet, and discovery witnesses.
- Carry-forward limit: Goal 10 does not approve interpretation, thesis,
  evidence coding, publication, or quotation-final use.
- `.venv/bin/python -m john_brown_research validate` passed.
- `.venv/bin/pytest` passed with 11 tests.
- `git diff --check` passed.

### 2026-07-21 - Post-Goal 10 source-access next steps

- Checkpoint scope: work the next step for each of the three unresolved source
  access tracks and stop for human feedback where required.
- AUC track: preserved the public digital-object page for
  `Correspondence and Map, John Brown to Seth Thompson, January 4, 1836`
  (`digital_objects/6800`). Direct acquisition of the linked handle URL
  returned HTTP 403, and the collection rights statement remains restrictive.
  Human feedback is required before repository-contact or human-in-browser
  access work.
- Trial-witness track: added `SRC-0013`, the 1859-11-03 New York Times issue
  from Internet Archive, after OCR showed the opening of Brown's courtroom
  speech. Added `SRC-0015`, the Avalon Project hosted De Witt transcription,
  and `SRC-0016`, the Internet Archive De Witt pamphlet scan.
- Digital Commonwealth/BPL track: added `SRC-0014`, Brown's 1859-11-22
  autograph letter to Thomas Wentworth Higginson, with metadata, IIIF manifest,
  page images, raw manifest, and local OCR.
- No source is quotation-final, evidence-coded, thesis-bearing, or
  publication-approved.

### 2026-07-21 - Source-access follow-up pass 2

- Checkpoint scope: continue the three source-access tracks and preserve the
  human feedback gate where required.
- AUC track: created `research/notes/auc-contact-draft.md`, containing a
  repository-contact email draft and a human-in-browser inspection protocol.
  No email was sent, no login or CAPTCHA was attempted, and no restricted file
  was downloaded.
- Trial-witness track: incorporated the Avalon Project as `SRC-0015` and
  acquired the corresponding Internet Archive De Witt pamphlet scan as
  `SRC-0016`. A follow-up web search confirmed the Richmond Dispatch witness as
  a target, but no public scan was acquired during this pass.
- Digital Commonwealth/BPL track: retained the newly acquired `SRC-0014`
  Higginson prison-period autograph letter as the latest targeted BPL
  acquisition; no bulk collection scrape was attempted.
- Human feedback remains required before AUC repository-contact or
  human-in-browser restricted-access work proceeds.

### 2026-07-21 - Corpus and codebook approval gate

- Scholar approved the proposed John Brown research scope, corpus design,
  source hierarchy, and draft codebook.
- Created `research/notes/corpus-approval.md`.
- Created `research/notes/codebook-approval.md`.
- Recorded the approval in `case-study/process-events.csv` and
  `case-study/intervention-log.csv`.
- Approval authorizes Goal 10 corpus acquisition only; it does not approve any
  interpretation, thesis, finding, or publication.
- Stop condition remains before actual acquisition: `research/data/source-register.csv`
  is currently header-only, so there is no concrete approved source queue to
  acquire from without adding and reviewing proposed source rows.

### 2026-07-21 - Goal 10 source queue setup

- Checkpoint scope: begin Goal 10 by creating a concrete source-register queue
  from the approved corpus design before downloading source files.
- Added seven unverified acquisition targets to
  `research/data/source-register.csv` across the approved corpus periods and
  source hierarchy.
- Updated `research/notes/source-acquisition-plan.md` with the initial source
  queue.
- Candidate repositories include Digital Commonwealth / Boston Public Library,
  National Archives / DocsTeach, Internet Archive / Boston Public Library,
  House Divided / Dickinson College, Famous Trials, National Archives Senate
  records guides, and Atlanta University Center.
- Several entries are collection guides, derivative transcriptions, or
  reported statements; they require item-level review, stronger provenance, or
  source-substitution approval before thesis-bearing use.
- No source was downloaded, normalized, hashed, or marked verified during this
  checkpoint.

## Migration Record

### 2026-07-21 - Checkpoint 0 inventory

- Created `migration/inventory.md`.
- Confirmed this working directory is a migration copy at
  `/Users/andrewhammer/codegarden/john-brown-metaphor-analysis`.
- Removed the old Git remote that pointed to the prior project repository.
- Ran the pre-migration baseline:
  `.venv/bin/python -m lincoln_research validate` passed and
  `.venv/bin/pytest` passed with 10 tests.

### 2026-07-21 - Checkpoint 1 project identity

- Updated repository metadata, active public pages, configuration, and
  instructions for the John Brown metaphor-analysis mission.
- Added the primary John Brown research question and project-specific
  epistemic rules to `README.md` and `AGENTS.md`.
- Replaced active completed-paper pages with no-findings scaffolds.

### 2026-07-21 - Checkpoint 2 package rename

- Renamed the Python package to `john_brown_research`.
- Updated scripts, tests, command examples, environment variables, and package
  metadata.
- Regenerated editable package metadata.
- `.venv/bin/python -m john_brown_research validate` passed.
- `.venv/bin/pytest` passed with 10 tests.

### 2026-07-21 - Checkpoint 3 research-state reset

- Reset `research/data/source-register.csv`,
  `research/data/evidence-matrix.csv`, `research/data/claims.csv`,
  `case-study/process-events.csv`, and `case-study/intervention-log.csv` to
  headers only.
- Deleted prior-project corpus files from active raw and normalized corpus
  directories while preserving `.gitkeep` placeholders.
- Deleted generated publication/site outputs from active output paths.
- Deleted prior-project review reports and active review wrappers.
- Deleted prior-project approval, transcription, thesis, findings, coding, and
  corpus-report notes.
- Replaced foundation-note files with provisional John Brown migration
  scaffolds.

### 2026-07-21 - Checkpoint 4 foundation documents

- Rebuilt `research/dossier/research-dossier.md` as a provisional John Brown
  research specification.
- Rewrote `research/notes/question-and-scope.md`,
  `research/notes/method.md`, `research/notes/source-acquisition-plan.md`, and
  `research/notes/dossier-claim-inventory.md`.
- Created `research/notes/codebook-draft.md` with operational definitions for
  metaphor, biblical quotation, biblical allusion, religious typology,
  providential claim, role construction, sacrificial frame, diachronic
  comparison, confidence, alternatives, disconfirming evidence, attribution,
  and variants.
- Included the required disconfirming possibilities in the dossier.
- No source is marked verified, no corpus is approved, and no hypothesis is
  promoted to a claim.
- `.venv/bin/python -m john_brown_research validate` passed.
- `.venv/bin/pytest` passed with 10 tests.

### 2026-07-21 - Checkpoint 5 data model and codebook

- Reviewed source-register, evidence-matrix, claims, process-events, and
  intervention schemas; no separate review schema exists in the current
  architecture.
- Expanded `config/schemas/source-register.fields` and
  `research/data/source-register.csv` additively with `corpus_period`,
  `source_tier`, `authorship_status`, and `attribution_caveat`.
- Expanded `config/schemas/evidence-matrix.fields` and
  `research/data/evidence-matrix.csv` for corpus period, document type,
  audience, public/private/report status, source tier, textual variants,
  symbolic-language category, metaphor domains, biblical citation/allusion,
  typology, Brown role construction, relationships to violence/failure/death,
  disconfirming status, and provenance or attribution caveat.
- Added a focused schema test requiring the Brown-specific evidence fields.
- The codebook remains provisional and does not presuppose the final thesis.
- `.venv/bin/python -m john_brown_research validate` passed.
- `.venv/bin/pytest` passed with 11 tests.

### 2026-07-21 - Checkpoint 6 goal sequence

- Rewrote the historical goal sequence as:
  `00-research-foundation.md`, `10-corpus-acquisition.md`,
  `20-textual-verification-and-segmentation.md`,
  `30-metaphor-and-symbolic-language-coding.md`,
  `40-diachronic-analysis-and-thesis.md`, `50-draft-paper.md`,
  `60-adversarial-review.md`, and `70-final-publication.md`.
- Rewrote `goals/99-master-goal.md` for the John Brown workflow.
- Rewrote methodology goals M00 through M40 for the prospective second-case
  methodology track.
- Added required human gates and stop conditions across the goal sequence,
  including corpus approval, source-substitution approval, codebook approval,
  thesis approval, methodology-findings approval, and publication approval.
- Targeted goal search found no Lincoln, Gettysburg, old package, or old
  command residue.
- `.venv/bin/python -m john_brown_research validate` passed.
- `.venv/bin/pytest` passed with 11 tests.

### 2026-07-21 - Checkpoint 7 methodology case study

- Replaced active case-study files with a prospective second-case setup for
  the John Brown project.
- Repopulated `case-study/process-events.csv` with migration-era records only.
- Left `case-study/intervention-log.csv` header-only because no John Brown
  human intervention beyond the initiating migration goal has yet been
  separately logged.
- Rewrote `case-study/README.md`, `case-study/human-decisions.md`, and
  `case-study/thesis-history.md`.
- Removed old retrospective case-study notes from active paths.
- Replaced active prior-case findings with a pointer to the new unapproved
  `methodology/case-2-findings.md` scaffold.
- Created `methodology/baseline-methodology.md`,
  `methodology/case-2-evaluation-plan.md`, and
  `methodology/case-2-findings.md`.
- Rewrote `methodology/research-question.md` and
  `methodology/methodology-review.md` for the second-case status.
- `.venv/bin/python -m john_brown_research validate` passed.
- `.venv/bin/pytest` passed with 11 tests.

### 2026-07-21 - Checkpoint 8 paper and website scaffolds

- Confirmed required scaffolds exist: `paper/paper.qmd`,
  `paper/references.bib`, `index.qmd`, `working-paper.qmd`, `workflow.qmd`,
  `evidence.qmd`, `reviews/index.qmd`, `publication-audit.qmd`, and
  `reproducibility-report.qmd`.
- Removed stale Quarto repository-action metadata because the old remote was
  removed and no new repository URL is configured yet.
- Rendered the clean scaffold with `quarto render .`; output was created at
  `_site/index.html`.
- The site states that the project is active, the corpus is not approved or
  complete, the dossier is provisional, and no findings or working paper are
  available yet.
- `.venv/bin/python -m john_brown_research validate` passed.
- `.venv/bin/pytest` passed with 11 tests.

### 2026-07-21 - Checkpoint 9 validation and migration audit

- Ran the required residue search for `Lincoln`, `lincoln`, `Gettysburg`,
  `gettysburg`, `lincoln_research`, and
  `Lincoln, Gettysburg, and the Nature of War`.
- Removed obsolete active residue from the methodology paper scaffold, test
  fixture, and old repository patch file.
- Classified remaining prior-case terms as intentional migration history in
  the migration spec, inventory, report, progress log, and migration-era
  process event.
- Created `migration/migration-report.md`.
- `.venv/bin/python -m john_brown_research validate` passed.
- `.venv/bin/pytest` passed with 11 tests.
- `quarto render .` passed.
- `quarto render paper/paper.qmd` passed and regenerated scaffold HTML/PDF;
  Quarto emitted a noncritical warning about the nested paper output support
  directory.
- `git diff --check` passed.
- Final stop condition reached: corpus-approval human gate.
