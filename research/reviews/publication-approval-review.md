# Publication Approval Review

Date: 2026-07-16

Package reviewed: `outputs/`

Source commit audited before publication approval:
`9a4ba49f077d2b9ec60533e953868791ed980f46`

## Result

Recommendation: approve only as a transparent public working-paper package, not
as a journal-final or quotation-final publication.

The package is coherent and source-audited for human review. It should not be
published without the scholar's explicit approval because the project
instructions reserve publication decisions to the human scholar.

## Package Artifacts Checked

- `outputs/paper.html`
- `outputs/paper.pdf`
- `outputs/publication-readme.md`
- `outputs/reproducibility-report.md`
- `outputs/publication-audit.md`
- `outputs/evidence-appendix.csv`

All six artifacts exist locally and contain content.

## Approval Criteria

### Source and quotation status

Decision: conditionally acceptable for a working-paper release.

The package discloses the remaining quotation-finality limits:

- `SRC-0005` Bliss Copy human transcription should receive a second
  manuscript-image check before quotation-final use.
- `SRC-0006` Everett pamphlet text is OCR-derived and should be checked against
  page images before final quotation use.
- `SRC-0011` is a Dickinson derivative transcription pending original newspaper
  image review.
- `SRC-0041` is noisy OCR and is used only for limited reception framing.

These limits are not hidden. They do, however, make the package inappropriate
to present as final scholarly publication without qualification.

### Claims and scope

Decision: acceptable.

The Goal 50 narrowed claims are reflected in the manuscript: public rhetoric,
this Civil War rather than war in general, and Lincoln's public presentation
rather than private belief. The paper also preserves Everett, Second Inaugural,
reception, and bodily-violence counterpressure.

### Public-output boundary

Decision: acceptable.

The output package does not include raw corpus files, browser profiles, cookies,
secrets, paywalled works, or restricted source files. It includes rendered
manuscript outputs, audit files, and an evidence appendix.

### Reproducibility

Decision: acceptable after metadata correction.

The package records the commands, versions, render warning, evidence counts,
claim counts, and citation audit. The stale commit hash in
`outputs/publication-readme.md` and `outputs/reproducibility-report.md` was
updated during this review to match the current audited commit.

## Recommendation to Scholar

If the intended release is a transparent public working paper with disclosed
source limitations, approval is reasonable.

If the intended release is journal submission, archival publication, or a
quotation-final version, defer approval until page-image checks for `SRC-0005`,
`SRC-0006`, `SRC-0011`, and relevant newspaper quotations are completed.

## Human Gate

Publication approval was granted by the scholar on 2026-07-16 for release as a
public working-paper package with the disclosed limitations.

This approval does not cover journal-final, quotation-final, or
limitation-free publication.
