# Goal 10 - Acquire and Preserve the Corpus

## Objective

Build a lawful, provenance-preserving corpus of Brown sources only after corpus
approval.

## Required Inputs

- Approved Goal 00 corpus package
- `research/data/source-register.csv`
- `research/notes/source-acquisition-plan.md`
- `research/notes/codebook-draft.md`

## Required Artifacts

- Raw source files
- Normalized text files
- Updated source register with hashes and rights status
- Corpus report
- Source-substitution approval records where derivative or reported texts are
  needed

## Completion Criteria

- Every acquired source has provenance, hash, rights status, and verification
  status.
- Raw and normalized files remain separate.
- Each corpus period is complete or explicitly blocked.
- No access control was bypassed.
- `python -m john_brown_research validate` and `pytest` pass.

## Stop Conditions

Stop if authorship or attribution is uncertain, a material quotation cannot be
verified, transcriptions conflict materially, access or rights rules prohibit
acquisition, a required period lacks adequate evidence, or a source
substitution requires human approval.
