# Migration Inventory

Date: 2026-07-21

Goal: migrate this copied repository from the Lincoln/Gettysburg project to
`john-brown-metaphor-analysis` while preserving the generic governed scholarly
build-system architecture.

## Repository Protection

- Working directory: `/Users/andrewhammer/codegarden/john-brown-metaphor-analysis`.
- The directory name and migration file identify this as a migration copy, not
  the authoritative Lincoln project.
- Previous remote before protection: `origin`
  `https://github.com/ashitaka-emishi/lincoln-war-research-project.git`.
- Protection action: removed the old `origin` remote before destructive local
  migration work.
- Current branch: `master`.
- Ignored local state includes `.env`, `.venv/`, `.quarto/`, `.pytest_cache/`,
  and `.ruff_cache/`; these must not be exposed during migration.
- Pre-migration baseline:
  - `.venv/bin/python -m lincoln_research validate` passed.
  - `.venv/bin/pytest` passed: 10 tests passed.

## Preserve Unchanged

These files are generic or infrastructure-only unless later checkpoints reveal
specific stale content:

- `.gitignore`
- `.vscode/extensions.json`
- `.vscode/settings.json`
- `.vscode/tasks.json`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `styles.css`
- `config/schemas/intervention-log.fields`
- `config/schemas/process-events.fields`
- `scripts/fetch_source.py`
- `scripts/normalize_text.py`
- `scripts/new_evidence_id.py`
- `tests/test_util.py`

## Preserve and Generalize

These files contain reusable governance, methodology, validation, or site
architecture but need names, examples, commands, or case references generalized:

- `README.md`
- `AGENTS.md`
- `pyproject.toml`
- `_quarto.yml`
- `.github/workflows/publish.yml`
- `.env.example`
- `config/project.yml`
- `config/schemas/source-register.fields`
- `config/schemas/evidence-matrix.fields`
- `config/schemas/claims.fields`
- `methodology/artifact-model.md`
- `methodology/governance-model.md`
- `methodology/human-ai-boundary.md`
- `methodology/methodology.md`
- `methodology/evaluation-plan.md`
- `methodology/limitations.md`
- `methodology/decisions/README.md`
- `methodology-paper/methodology-paper.qmd`
- `methodology-paper/references.bib`
- `src/lincoln_research/schemas.py`
- `src/lincoln_research/util.py`
- `src/lincoln_research/validate.py`
- `tests/test_validate.py`
- `scripts/acquire_chronicling_page.py`
- `scripts/extract_chronicling_text.py`
- `src/lincoln_research/loc_chronicling.py`
- `tests/test_loc_chronicling.py`

## Rewrite for John Brown

These active project documents should be rewritten so they express the John
Brown metaphor-analysis mission and contain no active Lincoln findings:

- `research/dossier/research-dossier.md`
- `research/notes/question-and-scope.md`
- `research/notes/method.md`
- `research/notes/source-acquisition-plan.md`
- `research/notes/dossier-claim-inventory.md`
- `paper/paper.qmd`
- `paper/references.bib`
- `index.qmd`
- `working-paper.qmd`
- `workflow.qmd`
- `evidence.qmd`
- `publication-audit.qmd`
- `reproducibility-report.qmd`
- `reviews/index.qmd`
- `goals/00-research-foundation.md`
- `goals/10-corpus-acquisition.md`
- `goals/20-evidence-coding.md`
- `goals/30-analysis-and-thesis.md`
- `goals/40-draft-paper.md`
- `goals/50-adversarial-review.md`
- `goals/60-final-publication.md`
- `goals/99-master-goal.md`
- `goals/methodology/M00-methodology-foundation.md`
- `goals/methodology/M10-instrument-current-workflow.md`
- `goals/methodology/M20-evaluate-case-study.md`
- `goals/methodology/M30-draft-methodology-paper.md`
- `goals/methodology/M40-review-methodology.md`

## Reset to Schema/Header Only

These files preserve data architecture but must not retain Lincoln records as
current John Brown evidence, claims, approvals, events, or interventions:

- `research/data/source-register.csv`
- `research/data/evidence-matrix.csv`
- `research/data/claims.csv`
- `case-study/process-events.csv`
- `case-study/intervention-log.csv`

## Archive Temporarily

These files are useful only as migration evidence or prior-case context. They
must not function as active John Brown findings:

- `MIGRATE-TO-JOHN-BROWN-METAPHOR-ANALYSIS.md`
- `REPO-METHODOLOGY-PATCH.md`
- `case-study/retrospective/goal-00-retrospective.md`
- `case-study/retrospective/goal-10-to-date.md`
- `case-study/human-decisions.md`
- `case-study/thesis-history.md`
- `methodology/case-study-findings.md`
- `methodology/methodology-publication-readiness.md`
- `methodology/methodology-review.md`
- `methodology/research-question.md`

## Delete as Lincoln-Specific Output

These generated or completed-state files should be removed from active paths:

- `_site/`
- `outputs/paper.html`
- `outputs/paper.pdf`
- `outputs/paper_files/`
- `outputs/evidence-appendix.csv`
- `outputs/publication-audit.md`
- `outputs/publication-readme.md`
- `outputs/reproducibility-report.md`
- `methodology-paper/methodology-paper.html`
- `methodology-paper/methodology-paper_files/`
- `research/reviews/*.md`
- `reviews/*.qmd` except a clean `reviews/index.qmd` scaffold
- Lincoln corpus files under `research/corpus/primary/raw/`
- Lincoln normalized files under `research/corpus/primary/normalized/`
- `src/lincoln_war_research.egg-info/`

## Regenerate After Migration

These artifacts should be regenerated from the clean John Brown scaffolds:

- `_site/`
- `outputs/`
- Quarto caches under `.quarto/` and `paper/.quarto/`
- `src/john_brown_research.egg-info/`
- rendered paper, review, publication-audit, and reproducibility outputs

## Lincoln-Specific Path Inventory

Paths containing `Lincoln`, `lincoln`, `Gettysburg`, or `gettysburg` include:

- `src/lincoln_research/`
- `src/lincoln_war_research.egg-info/`
- `.venv/bin/lincoln-research` and related installed package metadata
  (ignored local environment)
- `research/corpus/primary/raw/SRC-0001-gettysburg-address-nicolay-copy.pdf`
- `research/corpus/primary/raw/SRC-0002-gettysburg-address-hay-copy.pdf`
- `research/corpus/primary/raw/SRC-0003-gettysburg-address-everett-copy.html`
- `research/corpus/primary/raw/SRC-0004-gettysburg-address-bancroft-copy.html`
- `research/corpus/primary/raw/SRC-0005-gettysburg-address-bliss-copy-smithsonian-transcript.pdf`
- `research/corpus/primary/raw/SRC-0006-everett-gettysburg-oration-ceremony-pamphlet.pdf`
- `research/corpus/primary/raw/SRC-0040-coverage-of-gettysburg-address-dickinson.html`
- `research/corpus/primary/normalized/SRC-0001-gettysburg-address-nicolay-copy.txt`
- `research/corpus/primary/normalized/SRC-0002-gettysburg-address-hay-copy.txt`
- `research/corpus/primary/normalized/SRC-0003-gettysburg-address-everett-copy.txt`
- `research/corpus/primary/normalized/SRC-0004-gettysburg-address-bancroft-copy.txt`
- `research/corpus/primary/normalized/SRC-0005-gettysburg-address-bliss-copy-smithsonian-transcript.txt`
- `research/corpus/primary/normalized/SRC-0006-everett-gettysburg-oration-ceremony-pamphlet.txt`
- `research/corpus/primary/normalized/SRC-0040-coverage-of-gettysburg-address-dickinson.txt`

Content-level matches occur throughout active research, paper, site, goals,
methodology case-study, output, and log files. These are classified above for
rewrite, reset, temporary archive, deletion, or intentional methodological
history.

## Former Research Question Embeddings

The former question appears in:

- `AGENTS.md`
- `README.md`
- `config/project.yml`
- `research/dossier/research-dossier.md`
- `REPO-METHODOLOGY-PATCH.md`
- `logs/progress.md`

All active occurrences must be replaced or reclassified as prior-case history.

## Generated or Published Output

Generated/publication artifacts are present in `_site/`, `outputs/`, and
`methodology-paper/methodology-paper.html` with support files. They represent
completed Lincoln publication state and must be deleted or regenerated as clean
John Brown scaffolds.

## Source, Evidence, Claim, Review, Approval, and Case-Study Records

- Sources: `research/data/source-register.csv` contains 42 Lincoln-era rows and
  `research/corpus/primary/` contains Lincoln raw and normalized files.
- Evidence: `research/data/evidence-matrix.csv` contains 32 Lincoln evidence
  records.
- Claims: `research/data/claims.csv` contains 9 Lincoln claim records.
- Reviews: `research/reviews/*.md` and `reviews/*.qmd` contain Lincoln review
  state and rendered wrappers.
- Approvals: `research/notes/corpus-approval.md`,
  `research/notes/thesis-approval.md`, and
  `research/reviews/publication-approval-review.md` are Lincoln-specific and
  cannot transfer to the John Brown project.
- Case study: `case-study/process-events.csv`,
  `case-study/intervention-log.csv`, retrospective notes, thesis history, and
  methodology findings describe the Lincoln case and must be reset or clearly
  marked as prior-case context.

## Checkpoint 0 Status

Completion criteria met:

- Migration inventory exists.
- Lincoln-specific paths and active state have been classified.
- No Lincoln research files have been deleted during checkpoint 0.
- Pre-migration validation and tests were run once and passed.

