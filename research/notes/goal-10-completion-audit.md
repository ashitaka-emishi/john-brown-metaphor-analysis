# Goal 10 Completion Audit

Audit date: 2026-07-21

Goal: build a lawful, provenance-preserving corpus of John Brown sources after
corpus approval.

## Requirement Check

- Approved Goal 00 corpus package: satisfied by the 2026-07-21 human approval
  recorded in `research/notes/corpus-approval.md`,
  `research/notes/codebook-approval.md`, and
  `case-study/intervention-log.csv`.
- Raw source files: satisfied locally for acquired sources by raw manifests
  recorded in `research/data/source-register.csv`.
- Normalized text files: satisfied locally for acquired sources by normalized
  paths recorded in `research/data/source-register.csv`.
- Updated source register with hashes and rights status: satisfied for all
  acquired sources; unacquired collection/finding targets remain marked as
  unverified or blocked.
- Corpus report: satisfied by `research/notes/corpus-report.md`.
- Source-substitution approval records where derivative or reported texts are
  needed: satisfied by `research/notes/source-substitution-log.md`, which
  records that no thesis-bearing source substitution has been approved.
- Every acquired source has provenance, hash, rights status, and verification
  status: satisfied by `research/data/source-register.csv`.
- Raw and normalized files remain separate: satisfied by storage under
  `research/corpus/primary/raw/` and `research/corpus/primary/normalized/`.
- No access control was bypassed: satisfied by the acquisition log and source
  notes. Public APIs, documented IIIF endpoints, direct public files, and public
  web pages were used. AUC underlying materials were not downloaded because
  rights and access terms require caution.
- Validation commands: satisfied. `.venv/bin/python -m john_brown_research
  validate` passed and `.venv/bin/pytest` passed with 11 tests on
  2026-07-21 after this file was added.

## Corpus Period Status

- Formation and baseline: acquired at discovery/verification-ready level via
  `SRC-0003` and `SRC-0008`; AUC collection-level possibilities remain blocked
  or future-contact only.
- Kansas and armed resistance: acquired at verification-ready level via Tier 1
  autograph letters `SRC-0011` and `SRC-0012`.
- Preparation for Harpers Ferry: acquired at verification-ready level via
  `SRC-0002`.
- Capture, trial, imprisonment, and execution: acquired at
  verification-ready/discovery level via `SRC-0004`, `SRC-0005`, `SRC-0009`,
  and `SRC-0010`; modern derivative pages remain discovery-only, and reported
  statements require comparison in Goal 20.

## Carry-Forward Limits

Goal 10 acquisition does not approve interpretation, thesis, evidence coding,
publication, or quotation-final use.

All OCR and repository transcriptions remain unverified until Goal 20. Any
quotation, segmentation, or coding must be checked against preserved page
images, PDF scans, or stronger witnesses.
