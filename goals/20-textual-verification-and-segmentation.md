# Goal 20 - Textual Verification and Segmentation

## Objective

Verify source text, preserve variants, and segment the approved corpus into
locatable passages suitable for coding.

## Required Inputs

- Approved acquired corpus
- Source register
- Raw and normalized source files

## Required Artifacts

- Segmentation notes
- Textual-variant notes
- Passage locator conventions
- Updated source register verification statuses

## Completion Criteria

- Material quotations have stable locators.
- Variants and conflicting witnesses are preserved.
- Reported statements are marked by witness and transmission status.
- No uncertain wording is used as settled source text.
- `python -m john_brown_research validate` and `pytest` pass.

## Stop Conditions

Stop if a material quotation cannot be verified, provenance is uncertain,
source transcription conflicts materially across witnesses, or authorship is
uncertain for thesis-bearing material.
