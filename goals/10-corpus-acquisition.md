# Goal 10 — Acquire and Normalize the Corpus

## Objective

Build a provenance-preserving local corpus of legally accessible primary texts and source metadata.


## Operating contract

Read `AGENTS.md`, the `$scholarly-research` skill, and the files named below.
Work in checkpoints. Update `logs/progress.md`.
Do not proceed past a human gate.
Run `python -m lincoln_research validate` and `pytest` before completion.


## Preconditions

Human approval is recorded in `research/notes/corpus-approval.md`.

## Required work

1. Use the source register as the queue.
2. Prefer documented downloads or APIs over scraping.
3. For authorized HTML, use `scripts/fetch_source.py` or a tested source adapter.
4. Preserve raw content and normalized text separately.
5. Calculate SHA-256 hashes.
6. Record retrieval metadata and rights status.
7. Acquire the Gettysburg manuscript witnesses or authoritative representations.
8. Acquire comparative Lincoln texts, Everett, ceremony materials where available, and a balanced reception sample.
9. Produce `research/notes/corpus-report.md`.

## Completion criteria

- Every acquired source has provenance and hash.
- Raw and normalized content are separate.
- No access control was bypassed.
- Required corpus is complete or explicitly blocked.
- Validation and tests pass.

## Stop conditions

Stop if a required source cannot be legally or reliably acquired, provenance is uncertain, or variants remain unresolved.
