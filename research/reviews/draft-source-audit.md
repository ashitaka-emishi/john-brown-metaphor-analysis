# Draft Source Audit

Date: 2026-07-16

Artifact audited: `paper/paper.qmd`

## Result

No unresolved critical failures for the Goal 40 draft.

The draft is suitable as a source-grounded working manuscript. It is not yet a
publication-final text. Several quotation-finality cautions remain for later
review goals.

Draft length: 7,137 words, within the Goal 40 range of 7,000-9,000 words.

## Scope Check

The draft follows the approved thesis in `research/notes/thesis-approval.md`
and `research/notes/provisional-thesis.md`.

The draft stays within the approved scope:

- public Gettysburg rhetoric, not private belief;
- Lincoln's construction of this Civil War, not war in general;
- sacrificial obligation as a rhetorical transformation, not an assertion that
  every soldier death is inherently sacrifice;
- plural Lincoln war frames rather than a single sacrificial doctrine.

## Required Sections

All Goal 40 required sections are present in `paper/paper.qmd`:

1. Introduction and methodological limits.
2. Historical and ceremonial context.
3. War as the test of an embodied proposition.
4. Soldier death and national life.
5. Consecration and interpretive authority.
6. The dead as a claim upon the living.
7. New birth, emancipation, and transformation.
8. Providence, judgment, and counterevidence.
9. Conclusion.

## Citation Check

The draft cites through `paper/references.bib`.

All citation keys used in `paper/paper.qmd` resolve in `paper/references.bib`.

Material historical and textual claims cite project-preserved sources:

- Gettysburg manuscript witnesses: `SRC-0001` through `SRC-0005`.
- Wills invitation and cemetery ceremony: `SRC-0006`, `SRC-0007`.
- Everett comparison: `SRC-0006`.
- Comparative Lincoln texts: `SRC-0013` through `SRC-0028`.
- Reception examples: `SRC-0011`, `SRC-0041`.

## Quotation Check

Material quotations were checked against locally preserved normalized text in
`research/corpus/primary/normalized/` and mapped to approved evidence rows in
`research/data/evidence-matrix.csv`.

No quotation in the draft is taken from the provisional dossier alone.

## Known Noncritical Caveats

- `SRC-0005` Bliss Copy is a human transcription from manuscript images. It was
  approved for acquisition and draft use, but publication-final quotation should
  receive a second manuscript-image check.
- `SRC-0006` ceremony pamphlet text is OCR-derived. Quotations used in final
  publication should be checked against page images.
- `SRC-0011` is a derivative Dickinson transcription pending original newspaper
  image acquisition. The draft explicitly states this limitation and does not
  use it as final broad reception proof.
- `SRC-0041` newspaper text is noisy OCR. The draft uses it only for limited
  reception framing and explicitly notes the OCR limitation.

## Alternative Reading Check

The draft includes the strongest alternative reading: the Gettysburg Address may
be conventional cemetery rhetoric and wartime mobilization rather than a
distinctive Lincoln theory of war.

The draft answers that alternative by narrowing the thesis: Lincoln's
distinctiveness lies in compression and sequence, not in inventing sacrifice or
consecration language.

## Critical Failures

None.

## Render Check

`quarto render paper/paper.qmd` completed and created ignored local render
outputs in `outputs/paper.html` and `outputs/paper.pdf`.

Quarto emitted a noncritical warning about refusing to remove
`outputs/paper_files/libs` because of the project path configuration. The render
still completed successfully.

## Recommended Next Checks

For Goal 50 or publication preparation:

- page-image verification for Bliss, Everett pamphlet, and newspaper
  quotations;
- deeper secondary-source engagement;
- Chicago citation polishing;
- render review for Quarto output.
