# Goal 30 - Metaphor and Symbolic-Language Coding

## Objective

Code passages for metaphor, biblical quotation, biblical allusion, typology,
providential claim, role construction, violence, failure, death, alternatives,
and disconfirming evidence.

## Required Inputs

- Verified segmented corpus
- Approved codebook
- `research/data/evidence-matrix.csv`

## Required Artifacts

- Populated evidence matrix
- Coding memo
- Coding review

## Completion Criteria

- Every thesis-bearing row separates source text, observation, classification,
  interpretation, alternative reading, and confidence.
- Metaphor classifications identify source and target domains where applicable.
- Biblical allusions and typology are marked as certain or uncertain.
- Disconfirming evidence remains visible.
- `python -m john_brown_research validate` and `pytest` pass.

## Stop Conditions

Stop at the codebook-approval gate before thesis-bearing coding. Stop later if
a metaphor classification depends only on analyst intuition, a biblical
allusion is uncertain and thesis-bearing, or evidence begins conflating Brown's
self-representation with later martyr reception.
