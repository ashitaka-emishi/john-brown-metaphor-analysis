# Goal 00 - Establish the John Brown Research Foundation

## Objective

Define the question, scope, source hierarchy, proposed corpus, codebook draft,
and disconfirming tests without acquiring sources or approving interpretations.

## Required Inputs

- `AGENTS.md`
- `research/dossier/research-dossier.md`
- `research/notes/question-and-scope.md`
- `research/notes/method.md`
- `research/notes/source-acquisition-plan.md`
- `research/notes/codebook-draft.md`

## Required Artifacts

- Revised dossier if needed
- Proposed source register rows, still unverified
- Question-and-scope note
- Method note
- Source-acquisition plan
- Dossier claim inventory
- Codebook draft

## Completion Criteria

- The primary research question is explicit.
- Source types and tiers are defined.
- Chronological corpus periods are documented.
- Disconfirming tests are documented.
- No source is marked verified.
- `python -m john_brown_research validate` and `pytest` pass.

## Stop Conditions

Stop at the corpus-approval human gate. Present the question, scope, corpus
periods, proposed corpus, source hierarchy, codebook draft, acquisition plan,
risks, and exact approval requested.
