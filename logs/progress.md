# Progress Log

## Current state

Repository migrated to the John Brown metaphor-analysis mission. No John Brown
corpus source has yet been acquired under this project.

## Next checkpoint

Continue Goal 10 acquisition from the approved source queue. Prioritize the
strongest-provenance public sources while preserving stop conditions for
derivative, reported, inaccessible, or attribution-uncertain sources. Do not
populate evidence rows, form a thesis, or publish findings until acquisition
and verification criteria are met.

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
