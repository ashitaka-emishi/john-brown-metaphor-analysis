# Goal 60 — Produce the Final Publication Package

## Objective

Create a reproducible, source-audited package for human publication review.


## Operating contract

Read `AGENTS.md`, the `$scholarly-research` skill, and the files named below.
Work in checkpoints. Update `logs/progress.md`.
Do not proceed past a human gate.
Run `python -m lincoln_research validate` and `pytest` before completion.


## Required work

1. Finalize `paper/paper.qmd` and bibliography.
2. Run citation, quotation, source, and claim audits.
3. Render HTML and PDF with Quarto.
4. Write `outputs/publication-readme.md`.
5. Write `outputs/reproducibility-report.md`.
6. Export an evidence appendix.
7. Exclude restricted source files from public outputs.
8. Record known limitations.

## Completion criteria

- HTML and PDF exist in `outputs/`.
- Validation and tests pass.
- Reproducibility report records commands and software versions.
- No critical review issue remains.

## Stop condition

Stop at the **publication approval human gate**. Do not publish, upload, or push externally without explicit instruction.
