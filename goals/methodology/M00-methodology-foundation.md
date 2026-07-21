# Methodology Goal M00 - Establish the Case 2 Methodology Track

## Objective

Preserve the generic scholarly build-system methodology and define how the John
Brown project will be evaluated as a prospective second case.

## Required Inputs

- `methodology/*.md`
- `case-study/*.csv`
- `logs/progress.md`

## Required Artifacts

- Baseline methodology document
- Case 2 evaluation plan
- Case 2 findings scaffold
- Empty or migration-only process/intervention logs

## Completion Criteria

- Generic methodology is preserved.
- Prior-case findings are not represented as current results.
- Evaluation questions and limits are explicit.
- `python -m john_brown_research validate` and `pytest` pass.

## Stop Conditions

Stop if methodology findings are being asserted before the methodology-findings
approval gate.
