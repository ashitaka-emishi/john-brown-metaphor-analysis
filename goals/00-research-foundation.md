# Goal 00 — Establish the Research Foundation

## Objective

Convert the dossier into a controlled research plan without treating its preliminary claims as verified facts.


## Operating contract

Read `AGENTS.md`, the `$scholarly-research` skill, and the files named below.
Work in checkpoints. Update `logs/progress.md`.
Do not proceed past a human gate.
Run `python -m lincoln_research validate` and `pytest` before completion.


## Required work

1. Read `research/dossier/research-dossier.md`.
2. Inventory every proposed primary and secondary source.
3. Create or revise `research/data/source-register.csv`.
4. Complete `research/notes/question-and-scope.md`, defining:
   - research question;
   - unit of analysis;
   - temporal scope;
   - public-rhetoric/private-belief distinction;
   - Civil-War/all-war distinction;
   - operational definition of sacrifice.
5. Complete `research/notes/method.md`.
6. Complete `research/notes/source-acquisition-plan.md`.
7. Identify copyright, access, and provenance risks.
8. Create `research/notes/dossier-claim-inventory.md`.

## Completion criteria

- All named dossier sources have source-register rows.
- No source is marked verified unless inspected.
- Scope and terms are operationally defined.
- Acquisition prioritizes authoritative repositories.
- Validation and tests pass.

## Stop condition

Stop at the **corpus approval human gate** and present proposed corpus, exclusions, risks, and unresolved identities.
