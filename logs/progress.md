# Progress Log

## Current state

Scaffold initialized. No research source is yet verified.

## Next checkpoint

Run Goal 00 and stop at corpus approval.

## 2026-07-16 - Goal 00 research foundation

- Checkpoint scope: convert the dossier into a controlled research plan without treating its claims as verified evidence.
- Read `AGENTS.md`, the `$scholarly-research` skill, `goals/00-research-foundation.md`, and `research/dossier/research-dossier.md`.
- Expanded `research/data/source-register.csv` to inventory the dossier's proposed Gettysburg manuscripts, ceremony/context sources, Lincoln comparative corpus, reception sources, secondary works, and online source guides.
- All source-register rows remain `unverified`; unresolved source identities, provenance gaps, rights issues, and copyrighted secondary works are marked rather than silently resolved.
- Completed `research/notes/question-and-scope.md` with research question, unit of analysis, temporal boundaries, public/private distinction, Civil War/all-war distinction, and an operational definition of sacrifice.
- Completed `research/notes/method.md` with source hierarchy, acquisition/preservation rules, textual-variant method, coding method, claim control, comparative method, reception method, adversarial review, and human gates.
- Completed `research/notes/source-acquisition-plan.md` with authoritative-repository priorities, phased acquisition plan, risks, exclusions, and proposed corpus for approval.
- Created `research/notes/dossier-claim-inventory.md` to separate provisional dossier claims from verified evidence and identify disconfirming tests.
- Mechanical CSV check passed: 40 source rows, 16 schema columns, no malformed rows.
- `.venv/bin/python -m lincoln_research validate` passed.
- `.venv/bin/pytest` passed: 3 tests passed.
- Stop condition reached: corpus approval human gate.

## 2026-07-15 — Public repository and project website

- Publication approval received through the scholar's explicit instruction to create and push a public GitHub repository.
- Checkpoint scope: initialize Git on `master`, add a status-conscious Quarto project website, configure GitHub Pages deployment, validate, and publish.
- The website will distinguish the unverified dossier from completed scholarship; no research claims are being approved or advanced at this checkpoint.
- Local checks use a `.venv` created from the scholar-selected installed Python 3.9.6. The editable install required `--ignore-requires-python` because project metadata specifies Python 3.11+; compatible pytest 8.3.5 and iniconfig 2.1.0 were selected for this local environment.
- Validation passed, all 3 tests passed, the public website rendered to `_site/`, and `quarto render paper/paper.qmd` produced the manuscript HTML and PDF outputs.
- The scholar subsequently approved upgrading to Python 3.11. Homebrew Python 3.11.15 was installed, `.venv` was recreated, and the project installed normally with its declared development dependencies. Validation and all 3 tests pass without compatibility overrides.
- Public repository created at <https://github.com/ashitaka-emishi/lincoln-war-research-project> with `master` as the default branch, public visibility, and a mission-specific description.
- GitHub Pages configured for Actions and the Quarto landing page verified live at <https://ashitaka-emishi.github.io/lincoln-war-research-project/>. The deployed site contains the status-conscious landing page only; the provisional dossier is not rendered as a site page.
