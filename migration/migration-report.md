# Migration Report

Date: 2026-07-21

## Source Repository Identity

This working directory was migrated from a copied state of the prior
`lincoln-war-research-project`. The old `origin` remote pointed to
`https://github.com/ashitaka-emishi/lincoln-war-research-project.git` and was
removed before destructive migration work.

Current repository identity: `john-brown-metaphor-analysis`.

Current base commit before migration edits: `fe2c765`.

## Preserved

- Generic validation architecture in `src/john_brown_research/`.
- CSV schema validation.
- Raw/normalized corpus directory architecture with `.gitkeep` placeholders.
- Goals-based workflow architecture.
- Generic methodology principles: human authority, source traceability,
  alternative readings, disconfirming evidence, review, and publication gates.
- Quarto site and paper scaffold architecture.

## Generalized

- `README.md`, `AGENTS.md`, `_quarto.yml`, `config/project.yml`,
  `.env.example`, and workflow metadata.
- Methodology goals and case-study scaffolds for a prospective second case.
- Source-acquisition scripts and Chronicling America helper defaults.
- Tests and command examples for `john_brown_research`.

## Reset

- `research/data/source-register.csv` to header only.
- `research/data/evidence-matrix.csv` to header only.
- `research/data/claims.csv` to header only.
- `case-study/process-events.csv` to migration-era records only.
- `case-study/intervention-log.csv` to header only.
- Active research notes, approvals, findings, reviews, and thesis files.
- Active methodology findings and review state.

## Deleted

- Prior-project corpus files from active raw and normalized corpus paths.
- Prior-project research review reports.
- Prior-project active review QMD wrappers.
- Prior-project generated publication outputs and site pages.
- Prior-project methodology-paper rendered HTML and support files.
- Obsolete `REPO-METHODOLOGY-PATCH.md`.
- Obsolete `src/lincoln_war_research.egg-info/` generated metadata.

## Package Rename

Renamed:

```text
src/lincoln_research/
```

to:

```text
src/john_brown_research/
```

The public validation command is now:

```bash
python -m john_brown_research validate
```

The console script is now:

```bash
john-brown-research
```

## Schema Changes

`source-register` gained:

- `corpus_period`
- `source_tier`
- `authorship_status`
- `attribution_caveat`

`evidence-matrix` gained fields for:

- date, corpus period, document type, audience or recipient;
- public/private/report status;
- source tier;
- textual variants;
- symbolic-language category;
- metaphor source and target domains;
- biblical citation or allusion;
- typological pattern;
- Brown role construction;
- relationship to violence, failure, and death;
- disconfirming status;
- provenance or attribution caveat.

## Tests Run

- Pre-migration baseline:
  - `.venv/bin/python -m lincoln_research validate` passed.
  - `.venv/bin/pytest` passed with 10 tests.
- After package rename and later checkpoints:
  - `.venv/bin/python -m john_brown_research validate` passed.
  - `.venv/bin/pytest` passed with 11 tests.
- Final audit command set:
  - `.venv/bin/python -m john_brown_research validate` passed.
  - `.venv/bin/pytest` passed with 11 tests.
  - `quarto render .` passed.
  - `quarto render paper/paper.qmd` passed and produced scaffold HTML/PDF.
  - `git diff --check` passed.

## Render Status

The clean Quarto site scaffold renders to `_site/index.html`.

The paper scaffold renders to `outputs/paper.html` and `outputs/paper.pdf`.
Quarto emitted a noncritical warning during direct paper render about refusing
to remove `outputs/paper_files/libs` because of the nested paper project output
path. The render completed successfully.

## Remaining Limitations

- No new Git remote is configured yet.
- No John Brown corpus has been approved, acquired, or verified.
- No source register rows, evidence rows, claim rows, thesis, findings, or
  publication approval exist for the John Brown project.
- The codebook is provisional and awaits human approval.
- Source-access and copyright risks remain unresolved until corpus approval and
  acquisition planning.

## Remaining Intentional Prior-Case References

Remaining occurrences of old-case terms are intentionally confined to:

- `MIGRATE-TO-JOHN-BROWN-METAPHOR-ANALYSIS.md`, the governing migration spec;
- `migration/inventory.md`, the checkpoint-0 inventory;
- `migration/migration-report.md`, this audit report;
- `logs/progress.md`, the concise migration record;
- `case-study/process-events.csv`, migration-era records explaining reset of
  prior-case state.

These are migration history, not active John Brown evidence, claims, findings,
approvals, package names, or publication state.

## Next Human Gate

Corpus approval.

Approval requested:

> Approve, revise, or reject the proposed John Brown research scope, corpus
> design, source hierarchy, and draft codebook. Approval authorizes Goal 10
> corpus acquisition only; it does not approve any interpretation, thesis, or
> publication.

