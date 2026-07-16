# Progress Log

## Current state

Scaffold initialized. No research source is yet verified.

## Next checkpoint

Run Goal 00 and stop at corpus approval.

## 2026-07-16 - Goal 00 research foundation

- Checkpoint scope: convert the dossier into a controlled research plan without treating its claims as verified evidence.
- Read `AGENTS.md`, the `$scholarly-research` skill, `goals/00-research-foundation.md`, and `research/dossier/research-dossier.md`.
- Expanded `research/data/source-register.csv` to inventory the dossier's proposed Gettysburg manuscripts, ceremony/context sources, Lincoln comparative corpus, reception sources, secondary works, and online source guides.
- All source-register rows remain `unverified`; unresolved source identities, provenance gaps, rights issues, and copyrighted secondary works are marked rather than silently resolved.
- Completed `research/notes/question-and-scope.md` with research question, unit of analysis, temporal boundaries, public/private distinction, Civil War/all-war distinction, and an operational definition of sacrifice.
- Completed `research/notes/method.md` with source hierarchy, acquisition/preservation rules, textual-variant method, coding method, claim control, comparative method, reception method, adversarial review, and human gates.
- Completed `research/notes/source-acquisition-plan.md` with authoritative-repository priorities, phased acquisition plan, risks, exclusions, and proposed corpus for approval.
- Created `research/notes/dossier-claim-inventory.md` to separate provisional dossier claims from verified evidence and identify disconfirming tests.
- Mechanical CSV check passed: 40 source rows, 16 schema columns, no malformed rows.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 3 tests passed.
- Stop condition reached: corpus approval human gate.

## 2026-07-16 - Goal 10 corpus acquisition

- Checkpoint scope: verify prerequisites before acquiring or normalizing any corpus material.
- Read `AGENTS.md`, the `$scholarly-research` skill, `goals/10-corpus-acquisition.md`, and `research/dossier/research-dossier.md`.
- Stop condition reached: Goal 10 precondition is not satisfied because `research/notes/corpus-approval.md` is not present.
- No sources were acquired, normalized, hashed, or marked verified during this checkpoint.
- Continuation recheck confirmed the approval file is still absent; acquisition remains paused at the same gate.
- Scholar directed creation of `research/notes/corpus-approval.md`; Goal 10 precondition is now satisfied.
- Created the approval record with lawful-access, provenance, raw/normalized separation, variant-preservation, and stop-condition limits.
- Acquired LOC PDFs for `SRC-0001` Nicolay Copy and `SRC-0002` Hay Copy using `scripts/fetch_source.py`; normalized separate text with `pdftotext` and `scripts/normalize_text.py`.
- Updated `research/data/source-register.csv` for `SRC-0001` and `SRC-0002` with local paths, retrieval date, hashes, rights status, acquisition method, and verified status.
- Added local `.env` configuration for `LINCOLN_RESEARCH_USER_AGENT`; `.env` remains ignored by Git.
- Chrome-assisted discovery setup was requested for CAPTCHA/search-gated sources. Chrome is installed and running, and the native host manifest is correct, but the Codex Chrome Extension is installed/enabled in Chrome `Profile 2` while the selected profile is `Default`, where the extension is not installed. Browser-assisted scraping is paused until the selected Chrome profile has the extension enabled or the profile selection is corrected.
- Chrome DevTools MCP was noted as installed in VS Code, but no `chrome-devtools` MCP namespace is exposed to this Codex session; exact tool discovery surfaced only the bundled Chrome extension route and Node browser runtime.
- Acquired authoritative representations for Gettysburg manuscript witnesses `SRC-0003` Everett Copy from ALPLM, `SRC-0004` Bancroft/Cornell Copy from Cornell University Library, and raw `SRC-0005` Bliss/White House Copy manuscript imagery from Smithsonian/NMAH.
- Acquired `SRC-0006` Everett/ceremony pamphlet from Internet Archive and `SRC-0007` Wills invitation from LOC; identified the same 1864 pamphlet as the source for `SRC-0008` ceremony order/program and `SRC-0009` prayers/hymns/dirge/benediction.
- Verification checkpoint: source identity checks used file type, PDF metadata, repository metadata, and known phrase searches. Everett and Bancroft normalized text passed identity-level checks; OCR for the Smithsonian Bliss manuscript failed badly and was not retained.
- Stop condition reached: `SRC-0005` has verified raw provenance and hash, but normalized text requires human transcription from the manuscript image before it can be marked verified. The scholar offered to transcribe handwriting if needed.
- Continuation recheck confirmed the same stop condition remains active: `SRC-0005` still lacks reliable normalized text. Added `research/notes/bliss-copy-transcription-needed.md` to identify the raw source, expected normalized-text path, and post-transcription verification checks.
- Blocked-audit recheck confirmed the same stop condition remains active for a third consecutive Goal 10 turn: `SRC-0005` still lacks reliable normalized text. Goal 10 cannot proceed without human transcription or another legally preservable authoritative transcript.
- Created `research/corpus/primary/normalized/SRC-0005-gettysburg-address-bliss-copy-smithsonian-transcript.txt` as the human transcription target with page markers. Opened the target file in VS Code and the raw Smithsonian PDF in Chrome; automated horizontal window arrangement was blocked by macOS assistive-access permissions.
- Scholar completed and approved the `SRC-0005` human transcription. Updated the source register with the normalized path and raw/normalized hashes; replaced the old transcription-needed note with `research/notes/bliss-copy-transcription.md`. The Gettysburg manuscript-witness stop condition is cleared for acquisition purposes, with quotation-level page-image verification still required.
- Encoded repeatable LOC Chronicling America support in `src/lincoln_research/loc_chronicling.py`, `scripts/acquire_chronicling_page.py`, and `scripts/extract_chronicling_text.py`; added focused tests for URL construction and full-text extraction.
- Acquired and normalized `SRC-0040` Dickinson House Divided reception guide as a discovery source only.
- Acquired and normalized two public issue-level reception examples from LOC Chronicling America: `SRC-0041` New-York Daily Tribune, 1863-11-20, and `SRC-0042` Union County Star and Lewisburg Chronicle, 1863-11-27.
- Updated `SRC-0010` as a partially verified reception sampling frame and marked `SRC-0011` Harrisburg Patriot/Patriot and Union criticism blocked because issue-level access was not legally/reliably available in this environment; retrospective summaries were not treated as primary evidence.
- Produced `research/notes/corpus-report.md` documenting acquired corpus, repeatable commands, OCR limits, and reception blocks.
- Scholar approved using the Dickinson House Divided transcription of `SRC-0011` pending the original newspaper image. Downloaded the Dickinson record, extracted a normalized derivative transcription, and updated `SRC-0011` to `verified-derivative-transcription` with page-image verification still pending for final quotation use.

## 2026-07-15 — Public repository and project website

- Publication approval received through the scholar's explicit instruction to create and push a public GitHub repository.
- Checkpoint scope: initialize Git on `master`, add a status-conscious Quarto project website, configure GitHub Pages deployment, validate, and publish.
- The website will distinguish the unverified dossier from completed scholarship; no research claims are being approved or advanced at this checkpoint.
- Local checks use a `.venv` created from the scholar-selected installed Python 3.9.6. The editable install required `--ignore-requires-python` because project metadata specifies Python 3.11+; compatible pytest 8.3.5 and iniconfig 2.1.0 were selected for this local environment.
- Validation passed, all 3 tests passed, the public website rendered to `_site/`, and `quarto render paper/paper.qmd` produced the manuscript HTML and PDF outputs.
- The scholar subsequently approved upgrading to Python 3.11. Homebrew Python 3.11.15 was installed, `.venv` was recreated, and the project installed normally with its declared development dependencies. Validation and all 3 tests pass without compatibility overrides.
- Public repository created at <https://github.com/ashitaka-emishi/lincoln-war-research-project> with `master` as the default branch, public visibility, and a mission-specific description.
- GitHub Pages configured for Actions and the Quarto landing page verified live at <https://ashitaka-emishi.github.io/lincoln-war-research-project/>. The deployed site contains the status-conscious landing page only; the provisional dossier is not rendered as a site page.

## 2026-07-16 - Methodology-track integration

- Added a parallel methodology-paper track around the active Lincoln historical project.
- Preserved the existing corpus, goals, source register, research method, and paper structure.
- Added a general methodology specification, human-AI boundary, artifact model, governance model, evaluation plan, and limitations.
- Added retrospective case-study records for completed Goal 00 and Goal 10 work to date.
- Added prospective process-event and human-intervention instrumentation.
- Added methodology-specific goals and a Quarto methodology-paper scaffold.
- Updated repository instructions and README without changing historical research scope.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 10 tests passed.

## 2026-07-16 - Goal 20 evidence coding

- Checkpoint scope: begin evidence-matrix coding from the acquired Goal 10
  corpus while prospectively logging material methodology events.
- Read `AGENTS.md`, the `$scholarly-research` skill,
  `goals/20-evidence-coding.md`, and `research/dossier/research-dossier.md`.
- Populated the coded evidence matrix in
  `research/data/evidence-matrix.csv` with stable `OBS-` identifiers.
- Added working `CLM-` claim records in `research/data/claims.csv` so
  thesis-bearing claims map to supporting and counter evidence.
- Coded Gettysburg Address close-reading rows, manuscript-variant rows,
  Wills/ceremonial context, Everett comparison rows, comparative Lincoln rows
  from Lyceum through the Last Public Address, and limited
  reception/counterevidence rows.
- Produced `research/notes/coding-memo.md` with codebook use, initial
  findings, variant comparison, and open limits.
- Produced `research/reviews/coding-review.md` with source/interpretation
  separation checks, alternative-reading checks, and residual risks.
- Current evidence limits: Bliss Copy quotation use still needs manuscript-image
  second pass; OCR-derived pamphlet/newspaper rows need page-image checks;
  `SRC-0011` remains derivative pending original newspaper image.
- Consistency audit: 32 evidence rows, 9 claims, no missing claim-evidence
  references, all evidence rows include alternative readings, and
  disconfirming rows remain visible.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 10 tests passed.
- `git diff --check` passed.

## 2026-07-16 - Goal 30 analysis and thesis

- Checkpoint scope: analyze the coded evidence matrix, test the working thesis
  against disconfirmation, and stop at the thesis approval gate.
- Read `AGENTS.md`, the `$scholarly-research` skill,
  `goals/30-analysis-and-thesis.md`, `research/dossier/research-dossier.md`,
  `research/data/evidence-matrix.csv`, `research/data/claims.csv`,
  `research/notes/coding-memo.md`, and
  `research/reviews/coding-review.md`.
- Updated `research/data/claims.csv` so each claim points to the Goal 30
  analysis/provisional-thesis artifacts and has `provisional-thesis` status.
- Created `research/notes/argument-map.md` with thesis clauses, support,
  counterevidence, confidence levels, and distinctions between direct
  Gettysburg evidence and comparative evidence.
- Created `research/reviews/disconfirmation-review.md` with six falsification
  tests and six steelmanned competing interpretations.
- Created `research/notes/provisional-thesis.md` with the proposed thesis,
  clause-by-clause evidence map, limits, and proposed revisions from the dossier
  thesis.
- Created `research/notes/findings.md` with high-, medium-, and low-confidence
  findings.
- Consistency audit: 9 claims, no missing claim-evidence references, and all
  four Goal 30 deliverables are present.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 10 tests passed.
- `git diff --check` passed.
- Stop condition reached: thesis approval human gate. The thesis, strongest
  counterargument, unresolved evidence, and proposed revisions must be presented
  to the scholar before proceeding to drafting.
- Scholar approved the qualified thesis. Updated `research/notes/provisional-thesis.md`,
  `research/notes/findings.md`, and `research/data/claims.csv` to record
  thesis approval while preserving the stated limits.
- Final completion audit: 9 claims, all in `approved-thesis` status; no missing
  claim-evidence references; all four Goal 30 deliverables are present.
- `.venv/bin/python -m lincoln_research validate` passed after approval.
- `.venv/bin/pytest` passed after approval: 10 tests passed.
- `git diff --check` passed after approval.
- Created `research/notes/thesis-approval.md` from the scholar's approval so
  Goal 40's drafting precondition is explicit.

## 2026-07-16 - Goal 40 scholarly paper draft

- Checkpoint scope: draft a 7,000-9,000 word scholarly paper from approved
  claims and evidence, cite through `paper/references.bib`, and audit source
  use.
- Read `AGENTS.md`, the `$scholarly-research` skill,
  `goals/40-draft-paper.md`, `research/dossier/research-dossier.md`,
  `research/notes/thesis-approval.md`,
  `research/notes/provisional-thesis.md`,
  `research/notes/argument-map.md`, and
  `research/reviews/disconfirmation-review.md`.
- Replaced the placeholder manuscript in `paper/paper.qmd` with a 7,137-word
  draft organized around the nine required Goal 40 sections.
- Expanded `paper/references.bib` so every citation key used in the draft
  resolves to a project-preserved source.
- Created `research/reviews/draft-source-audit.md`; it reports no unresolved
  critical failures and preserves quotation-finality caveats for later review.
- Added `paper/.gitignore` to keep Quarto scratch files under `paper/.quarto/`
  out of Git.
- `quarto render paper/paper.qmd` passed and produced ignored local outputs
  `outputs/paper.html` and `outputs/paper.pdf`; Quarto emitted a noncritical
  path warning about `outputs/paper_files/libs`.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 10 tests passed.
- `git diff --check` passed.

## 2026-07-16 - Goal 50 adversarial scholarly review

- Checkpoint scope: attempt to disprove, narrow, or materially improve the
  Goal 40 draft before publication preparation.
- Read `AGENTS.md`, the `$scholarly-research` skill,
  `goals/50-adversarial-review.md`, the Goal 40 draft, the claim map, and the
  existing draft source audit.
- Created the six required adversarial review reports:
  `research/reviews/historical-review.md`,
  `research/reviews/rhetorical-review.md`,
  `research/reviews/theological-language-review.md`,
  `research/reviews/source-and-citation-review.md`,
  `research/reviews/critical-countervoice-review.md`, and
  `research/reviews/anachronism-review.md`.
- Accepted or partially accepted critiques where the draft risked overclaiming:
  generalizing the Civil War into war as such, implying private belief,
  understating Everett/convention, understating soldier agency, implying
  intentional suppression, and using "refound" or "political theology" too
  broadly.
- Rejected with caution the claim that sacrifice was merely imposed: the draft
  defines sacrifice restrictively and demonstrates it through giving,
  consecration, obligation, unfinished work, and new birth rather than treating
  death alone as sacrifice.
- Revised `paper/paper.qmd` to replace summary-level "refound" language with
  "new birth of freedom," remove the "political theology" keyword, preserve
  soldier agency, avoid intentional-sounding "suppresses" language, and narrow
  the conclusion to Lincoln's public presentation of this Civil War in this
  ceremonial setting.
- Updated `research/data/claims.csv` so affected claims record Goal 50 review
  status and links to the adversarial reports.
- No critical citation failures were found. Remaining source caveats are
  publication-final checks for `SRC-0005`, `SRC-0006`, `SRC-0011`, and
  `SRC-0041`.
- `quarto render paper/paper.qmd` passed and updated ignored local render
  outputs in `outputs/`; Quarto emitted the same noncritical path warning
  about `outputs/paper_files/libs`.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 10 tests passed.
- `git diff --check` passed.

## 2026-07-16 - Goal 60 final publication package

- Checkpoint scope: create a reproducible, source-audited publication-review
  package and stop at the publication approval human gate.
- Read `AGENTS.md`, the `$scholarly-research` skill,
  `goals/60-final-publication.md`, the research dossier, the current draft,
  source register, claim map, evidence matrix, and prior Goal 40/50 reviews.
- Confirmed current paper and bibliography are already finalized for package
  preparation after Goal 50 narrowing; no additional thesis-expanding edits
  were made.
- Ran citation and claim audits: 25 citation keys used, 25 bibliography
  entries, no missing keys, no unused keys, 32 evidence rows, 9 claims, and no
  broken claim-to-evidence references.
- Exported `outputs/evidence-appendix.csv` from
  `research/data/evidence-matrix.csv` with 32 evidence rows.
- Created `outputs/publication-readme.md`,
  `outputs/reproducibility-report.md`, and `outputs/publication-audit.md`.
- Publication package excludes raw corpus files, browser data, secrets,
  cookies, and paywalled or restricted source files.
- Known limitations remain recorded for publication review: `SRC-0005` Bliss
  Copy manuscript-image second pass, `SRC-0006` OCR-derived Everett pamphlet
  quote checks, `SRC-0011` derivative Dickinson transcription pending original
  newspaper image, and `SRC-0041` noisy OCR used only for limited reception
  framing.
- `outputs/paper.html`, `outputs/paper.pdf`,
  `outputs/publication-readme.md`, `outputs/reproducibility-report.md`,
  `outputs/publication-audit.md`, and `outputs/evidence-appendix.csv` all
  exist after the final render/package check.
- `quarto render paper/paper.qmd` passed and produced HTML/PDF outputs;
  Quarto emitted the same noncritical path warning about
  `outputs/paper_files/libs`.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 10 tests passed.
- `git diff --check` passed.
- Stop condition reached: publication approval human gate. Do not publish,
  upload, push externally, or otherwise distribute the package without
  explicit scholar approval.

## 2026-07-16 - Publication approval review

- Checkpoint scope: review the Goal 60 package in `outputs/` and determine
  whether it is ready for scholar publication approval.
- Read `AGENTS.md`, the `$scholarly-research` skill, Goal 60 package files,
  and the current repository state.
- Corrected stale package metadata in `outputs/publication-readme.md` and
  `outputs/reproducibility-report.md` so the audited commit is
  `9a4ba49f077d2b9ec60533e953868791ed980f46`.
- Created `research/reviews/publication-approval-review.md`.
- Recommendation: approve only as a transparent public working-paper package
  with disclosed limitations. Do not treat as journal-final or
  quotation-final until page-image checks are completed for `SRC-0005`,
  `SRC-0006`, `SRC-0011`, and relevant newspaper quotations.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 10 tests passed.
- `git diff --check` passed.
- Publication approval remains a human decision under `AGENTS.md`. Stop at the
  human gate until the scholar explicitly approves publication of the package
  and the intended release type.
- Scholar approved publication of the Goal 60 package as a public working-paper
  package with the disclosed limitations, including committing, pushing, and
  publishing only the approved outputs.
- Updated `outputs/publication-readme.md`, `outputs/publication-audit.md`, and
  `research/reviews/publication-approval-review.md` to record the approved
  release type and to clarify that this approval does not cover journal-final,
  quotation-final, or limitation-free publication.
- Confirmed `outputs/paper.html` references `outputs/paper_files/`; those
  Quarto support assets are approved output dependencies and must be committed
  with the HTML manuscript.
- `.venv/bin/python -m lincoln_research validate` passed after approval.
- `.venv/bin/pytest` passed after approval: 10 tests passed.
- `quarto render paper/paper.qmd` passed after approval and refreshed
  `outputs/paper.html`, `outputs/paper.pdf`, and `outputs/paper_files/`;
  Quarto emitted the same noncritical path warning about
  `outputs/paper_files/libs`.
- `git diff --check` passed after approval.

## 2026-07-16 - Public landing page update

- Checkpoint scope: update the GitHub Pages landing page to reflect the
  approved public working-paper package.
- Verified the live page still described the project as a scaffold with source
  acquisition incomplete and the paper as an outline.
- Updated `index.qmd` to describe the current public working-paper status,
  link to the approved outputs, and preserve disclosed limitations.
- Updated `_quarto.yml` so Quarto copies `outputs/**` into `_site`, allowing
  the GitHub Pages deployment to serve `outputs/paper.html`,
  `outputs/paper.pdf`, audit files, reproducibility report, and evidence
  appendix from the site.
- `quarto render .` passed and copied the approved output package into
  `_site/outputs/`.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 10 tests passed.
- `git diff --check -- . ':(exclude)_site/**'` passed.
- Committed and pushed landing-page update as `278a439`.
- GitHub Pages workflow `29486048963` completed successfully for commit
  `278a4399bd5bc45f93a6036e7f71a4caa5c589c8`.
- Verified the live site with a cache-busting request: the landing page shows
  the working-paper status and links to `outputs/paper.html` and
  `outputs/paper.pdf`.
- Verified `https://ashitaka-emishi.github.io/lincoln-war-research-project/outputs/paper.html`
  returns HTTP 200.
