# Migration Goal: John Brown Metaphor Analysis

## Purpose

Migrate an existing copy of the `lincoln-war-research-project` repository into a new, independent scholarly research project named:

```text
john-brown-metaphor-analysis
```

The migrated repository must preserve the governed scholarly build-system methodology while removing or resetting Lincoln-specific research content, identifiers, claims, evidence, publication artifacts, and project status.

This document is intended to be placed in the repository root and executed as a Codex goal, for example:

```text
/goal Execute MIGRATE-TO-JOHN-BROWN-METAPHOR-ANALYSIS.md checkpoint by checkpoint. Preserve the generic methodology and validation architecture, remove or reset Lincoln-specific research state, update logs/progress.md after each checkpoint, and stop at every human gate or documented stop condition.
```

---

## Primary Research Question

> **How did John Brown use metaphor, biblical allusion, and religious typology in his surviving writings and authenticated statements to understand his antislavery mission, his use of violence, the failure at Harpers Ferry, and his approaching death?**

## Compact Research Question

> **How did John Brown’s symbolic language construct his understanding of his actions and death in the struggle against slavery?**

The primary question is authoritative. The compact question may be used for navigation, summaries, and public-facing descriptions.

---

## Working Project Identity

### Repository name

```text
john-brown-metaphor-analysis
```

### Scholarly working title

```text
Blood, Bonds, and the Cause:
John Brown’s Metaphorical Understanding of Violence and Death
```

### Neutral alternate title

```text
John Brown’s Symbolic Self-Understanding:
Metaphor, Providence, Violence, and Death in His Surviving Writings
```

### Python package name

Rename the project package from:

```text
lincoln_research
```

to:

```text
john_brown_research
```

The public CLI validation command must become:

```bash
python -m john_brown_research validate
```

Do not retain Lincoln-specific package names, imports, command examples, or module references.

---

## Governing Interpretation Rule

The project must not claim direct access to John Brown’s private mind.

The project may analyze:

- how Brown represented his actions;
- how Brown framed his obligations;
- how Brown described slavery, violence, failure, providence, suffering, and death;
- how his symbolic vocabulary changed over time;
- and what role he publicly or privately assigned himself in the antislavery struggle.

Use formulations such as:

```text
Brown represented...
Brown framed...
Brown’s surviving writings suggest...
Brown’s authenticated statements construct...
Brown’s language permits the interpretation...
```

Avoid unsupported formulations such as:

```text
Brown secretly believed...
Brown’s true psychological motive was...
Brown unconsciously intended...
Brown knew with certainty...
```

Claims about private belief require explicit evidence and human approval.

---

## Core Analytical Distinctions

The migrated project must distinguish at least the following categories:

1. **Source text** — what Brown or a reliable contemporary witness actually wrote or recorded.
2. **Observation** — a directly supportable description of the wording, structure, or recurrence.
3. **Metaphor** — language in which one conceptual domain structures another.
4. **Biblical quotation** — direct or near-direct scriptural wording.
5. **Biblical allusion** — scriptural language or narrative invoked without explicit quotation.
6. **Religious typology** — a person, event, or action interpreted through a recurring biblical pattern.
7. **Providential claim** — language assigning divine direction, judgment, timing, preservation, or purpose.
8. **Moral analogy** — a comparison used to make antislavery action intelligible as ordinary duty.
9. **Role construction** — Brown’s representation of himself as servant, father, captain, witness, instrument, prisoner, martyr, or another role.
10. **Interpretation** — an analytical account of what the symbolic language does.
11. **Broader claim** — a bounded proposition about Brown’s public or epistolary self-understanding.

Do not collapse all religious language into metaphor.

---

## Initial Metaphor and Symbolic-Language Families

Treat these as provisional discovery categories, not predetermined conclusions:

- bondage and liberation;
- captivity, chains, bonds, deliverance, and rescue;
- divine cause and human instrument;
- law, higher law, justice, guilt, sentence, and judgment;
- family, brotherhood, children, and the despised poor;
- war, command, defense, resistance, and invasion;
- blood, sacrifice, suffering, offering, and martyrdom;
- seed, harvest, fruition, and future victory;
- providential time, testing, discipline, and vindication;
- body versus cause;
- death versus continued moral action;
- failure transformed into testimony;
- slavery as sin, crime, oppression, disease, or captivity;
- nation, government, constitution, and moral order.

The research process must allow categories to be revised, split, merged, or rejected after corpus review.

---

## Proposed Chronological Corpus Structure

The corpus design should permit diachronic comparison.

### Period 1 — Formation and baseline

Approximate scope:

```text
early correspondence through the beginning of the Kansas conflict
```

Research purpose:

- establish Brown’s ordinary religious and moral vocabulary;
- identify recurring providential language before armed antislavery action;
- distinguish stable lifelong patterns from post-capture intensification.

### Period 2 — Kansas and armed resistance

Research purpose:

- examine how Brown framed violence, defense, punishment, rescue, and command;
- identify changes in his representation of slavery and moral duty;
- test whether he already understood himself through sacrificial or providential roles.

### Period 3 — Preparation for Harpers Ferry

Research purpose:

- examine planning correspondence and organizational documents;
- analyze military, governmental, liberation, and biblical language;
- determine how Brown represented the anticipated relationship among action, violence, law, and death.

### Period 4 — Capture, trial, imprisonment, and execution

Research purpose:

- analyze Brown’s explanation of the raid;
- examine how he framed tactical failure;
- identify changes in the use of blood, sacrifice, providence, witness, justice, and death;
- test whether Brown consciously represented execution as politically or morally productive.

No period may be treated as complete until its proposed source set is reviewed and approved by the scholar.

---

## Source Hierarchy

### Tier 1 — strongest evidence

- surviving John Brown manuscript;
- authenticated facsimile;
- signed letter or document;
- archival transcription linked to a preserved manuscript;
- court statement with strong textual provenance;
- contemporaneous document whose authorship can be established.

### Tier 2 — usable with qualification

- contemporary newspaper transcription;
- courtroom or stenographic report;
- immediately published interview;
- duplicate or copy whose relationship to an original can be documented;
- family copy or recipient transcription with known provenance.

### Tier 3 — contextual or discovery evidence

- later recollection;
- memoir written substantially after the event;
- partisan paraphrase;
- unattributed quotation;
- quotation whose manuscript or contemporary witness cannot be identified;
- secondary quotation without accessible source verification.

Tier 3 material must not support a thesis-bearing quotation without human approval and an explicit limitation.

---

## Required Methodological Continuity

Preserve the generic principles of the existing repository:

- human scholarly authority;
- source-grounded analysis;
- separation of source, observation, interpretation, and conclusion;
- immutable raw files and separate normalized text;
- stable identifiers;
- explicit verification status;
- alternative readings;
- confidence levels;
- contradictory and disconfirming evidence;
- adversarial review;
- human corpus, thesis, findings, and publication gates;
- reproducible validation and rendering;
- public disclosure of source and methodological limitations;
- AI as a subordinate research and engineering assistant;
- research integrity over goal completion.

The migrated repository remains a governed scholarly build system.

---

## Methodology Case Relationship

The Lincoln project was the first completed case used to develop and evaluate the methodology.

This repository is a second, prospective application.

The new repository must not import Lincoln case findings as evidence about John Brown. It may preserve generic methodology documents, but the new case-study logs and findings must begin empty.

The second case should deliberately improve the evaluation design by recording:

- accepted AI recommendations;
- materially revised AI recommendations;
- rejected AI recommendations;
- deferred recommendations;
- human overrides;
- source substitutions;
- definition changes;
- category changes;
- time or burden estimates where practical;
- and explicit evaluation cutoffs tied to commit SHAs.

# Migration Plan

## Checkpoint 0 — Inspect and protect the copied repository

### Objective

Confirm that the working directory is a copy intended for migration and identify all Lincoln-specific content before making destructive changes.

### Required actions

1. Read:
   - `README.md`
   - `AGENTS.md`
   - `pyproject.toml`
   - `_quarto.yml`
   - all files under `goals/`
   - all files under `methodology/`
   - all schemas under `config/schemas/`
   - all Python modules and tests;
   - `logs/progress.md`.

2. Inventory:
   - every path containing `Lincoln`, `lincoln`, `Gettysburg`, or `gettysburg`;
   - every file that embeds the former research question;
   - every generated or published output;
   - every source, evidence, claim, review, approval, and case-study record.

3. Confirm:
   - the repository is not the authoritative Lincoln repository;
   - no secrets, ignored corpus files, or local-only data will be unintentionally exposed;
   - the Git remote points to the intended new repository or is removed before publication.

4. Create:

```text
migration/inventory.md
```

The inventory must classify files as:

- preserve unchanged;
- preserve and generalize;
- rewrite for John Brown;
- reset to schema/header only;
- archive temporarily;
- delete as Lincoln-specific output;
- regenerate after migration.

### Stop condition

Stop if the repository appears to be the authoritative Lincoln project rather than a copy.

Stop if destructive changes would affect a remote or branch not explicitly intended for migration.

### Completion criteria

- migration inventory exists;
- all Lincoln-specific paths are classified;
- no files have yet been deleted;
- current validation and tests have been run once to establish the pre-migration baseline.

---

## Checkpoint 1 — Establish new project identity

### Objective

Replace repository-level Lincoln identity with John Brown project identity.

### Required changes

Update:

- `README.md`
- `AGENTS.md`
- `pyproject.toml`
- package metadata;
- repository description text;
- `_quarto.yml`;
- site title and navigation;
- any CI workflow names;
- any badge, URL, or Pages path;
- all command examples;
- all title metadata in QMD files;
- all root-level project descriptions.

### Required project description

Use or adapt:

```text
A governed AI-assisted scholarly research project examining how John Brown used metaphor, biblical allusion, and religious typology to understand his antislavery mission, violence, the failure at Harpers Ferry, and his approaching death.
```

### Required AGENTS.md mission

`AGENTS.md` must include the primary research question and these John Brown-specific epistemic rules:

- do not infer private belief from public rhetoric without explicit evidence;
- distinguish Brown’s own words from contemporary reports and later recollections;
- distinguish metaphor, biblical quotation, allusion, typology, providential claim, and later martyr construction;
- preserve textual variants;
- do not treat later martyr memory as evidence of Brown’s original wording;
- do not equate death with sacrifice unless Brown’s language or a clearly identified interpretive warrant supports the classification;
- distinguish tactical failure from Brown’s own interpretation of failure;
- distinguish Brown’s self-construction from later Northern or Southern reception;
- record contested authorship and uncertain attribution;
- never invent quotations, dates, archival identifiers, metadata, or locators.

### Completion criteria

- no public-facing project metadata identifies the project as a Lincoln study;
- the primary research question appears in `README.md` and `AGENTS.md`;
- the project title is consistent across repository and Quarto configuration.

---

## Checkpoint 2 — Rename the Python package and validation interface

### Objective

Rename the code layer from `lincoln_research` to `john_brown_research`.

### Required actions

1. Rename:

```text
src/lincoln_research/
```

to:

```text
src/john_brown_research/
```

2. Update:
   - imports;
   - module execution entry points;
   - tests;
   - scripts;
   - `pyproject.toml`;
   - README commands;
   - workflow files;
   - goal documents;
   - validation documentation.

3. Ensure this command works:

```bash
python -m john_brown_research validate
```

4. Remove obsolete Lincoln package references.

### Validation

Run:

```bash
python -m john_brown_research validate
pytest
```

### Completion criteria

- package imports resolve;
- tests run against the renamed package;
- no active code path imports `lincoln_research`;
- validation command succeeds or documented migration failures are resolved before continuing.

---

## Checkpoint 3 — Reset historical research state

### Objective

Remove Lincoln evidence and approvals while preserving reusable schemas and directory architecture.

### Reset to header/schema only

Reset:

```text
research/data/source-register.csv
research/data/evidence-matrix.csv
research/data/claims.csv
case-study/process-events.csv
case-study/intervention-log.csv
```

Preserve exact schemas unless a documented John Brown requirement justifies an additive schema change.

### Delete or replace Lincoln-specific research artifacts

Remove or rewrite, as appropriate:

- Lincoln dossier;
- Lincoln question-and-scope notes;
- Lincoln corpus approval;
- Lincoln acquisition plan;
- Lincoln corpus report;
- Lincoln transcription notes;
- Lincoln coding memo;
- Lincoln argument map;
- Lincoln provisional thesis;
- Lincoln findings;
- Lincoln thesis approval;
- Lincoln review reports;
- Lincoln publication approval;
- Lincoln evidence appendix;
- Lincoln working paper;
- Lincoln bibliography;
- Lincoln rendered outputs;
- Lincoln site evidence pages;
- Lincoln site review pages;
- Lincoln case-study findings;
- Lincoln-specific methodology evaluation results;
- any generated files describing completed Lincoln work.

Do not retain completed Lincoln approvals as approvals for the new project.

### Raw and normalized corpus

Delete Lincoln corpus files from the copy unless the scholar explicitly requests an archive.

Do not commit copyrighted or restricted source material merely because it existed in the copied working directory.

### Progress log

Replace the stale top-level state in `logs/progress.md` with:

```markdown
# Progress Log

## Current state

Repository migrated to the John Brown metaphor-analysis mission. No John Brown corpus has yet been approved or acquired under this project.

## Next checkpoint

Execute Goal 00 to define the question, scope, coding framework, proposed corpus, and disconfirming tests. Stop at the corpus-approval human gate.
```

Preserve a concise migration record below the current-state section.

### Completion criteria

- research tables contain headers only;
- no Lincoln claim or evidence IDs remain active;
- no Lincoln human approval is represented as current;
- no generated Lincoln publication artifact remains in the active publication path;
- project status accurately states that John Brown research has not yet begun.

---

## Checkpoint 4 — Rebuild the research dossier and foundation documents

### Objective

Create a provisional John Brown research specification without treating hypotheses as verified evidence.

### Required files

Create or rewrite:

```text
research/dossier/research-dossier.md
research/notes/question-and-scope.md
research/notes/method.md
research/notes/source-acquisition-plan.md
research/notes/dossier-claim-inventory.md
research/notes/codebook-draft.md
```

### Dossier requirements

The dossier must contain:

1. primary research question;
2. compact question;
3. significance;
4. unit of analysis;
5. chronological boundaries;
6. distinction between private letters, public statements, reported statements, and later recollections;
7. initial corpus periods;
8. source hierarchy;
9. initial symbolic-language categories;
10. tentative hypotheses;
11. explicit disconfirming possibilities;
12. expected source-access and copyright risks;
13. limitations on claims about Brown’s inner psychology;
14. relationship to later public reception, clearly marked as outside the primary question;
15. proposed paper structure;
16. human decisions still required.

### Required disconfirming possibilities

At minimum, test whether:

- Brown’s prison language differs substantially from earlier correspondence;
- sacrificial language intensified only after conviction;
- Brown remained primarily a practical military actor rather than a martyr-oriented actor;
- later editors imposed a stronger Christological or prophetic frame than Brown used himself;
- Brown used multiple inconsistent symbolic frames;
- biblical language reflected ordinary nineteenth-century Protestant idiom rather than a distinctive self-construction;
- metaphor frequency does not correspond to interpretive importance;
- the surviving corpus is distorted by preservation and publication bias;
- reported trial statements differ materially across witnesses.

### Completion criteria

- all foundation files exist;
- every substantive claim in the dossier is marked provisional;
- the source hierarchy and interpretive boundary are explicit;
- disconfirming tests are present;
- no source is marked verified before acquisition and provenance review.

---

## Checkpoint 5 — Adapt the data model and codebook

### Objective

Ensure the evidence system can represent metaphor, biblical allusion, typology, provenance, and diachronic change.

### Required review

Inspect the current schemas for:

- source register;
- evidence matrix;
- claims;
- reviews;
- process events;
- interventions.

Prefer additive schema evolution.

### Evidence matrix requirements

Each evidence record should support:

- stable observation ID;
- source ID;
- date;
- corpus period;
- document type;
- audience or recipient;
- public/private/report status;
- source tier;
- locator;
- verbatim text or faithful transcription;
- textual-variant status;
- symbolic-language category;
- source-domain and target-domain fields for metaphor where applicable;
- biblical citation or likely allusion;
- typological pattern;
- Brown role construction;
- relationship to violence;
- relationship to failure;
- relationship to death;
- observation;
- interpretation;
- alternative reading;
- disconfirming status;
- confidence;
- review status;
- provenance or attribution caveat.

Not every field must be populated for every row. Empty fields must mean “not applicable” or “not yet coded,” never silent uncertainty.

### Codebook requirements

`research/notes/codebook-draft.md` must define:

- metaphor identification rules;
- biblical quotation criteria;
- biblical allusion criteria;
- religious typology criteria;
- providential-claim criteria;
- role-construction criteria;
- sacrificial-frame criteria;
- distinction between Brown’s wording and analyst interpretation;
- diachronic comparison rules;
- confidence scale;
- alternative-reading requirement;
- disconfirming-evidence rule;
- attribution and textual-variant handling.

### Completion criteria

- schemas validate empty project state;
- codebook definitions are operational enough for two coders to apply;
- no category presupposes the final thesis;
- tests cover any schema additions.

---

## Checkpoint 6 — Rewrite the goal sequence

### Objective

Preserve the staged workflow while adapting it to John Brown metaphor analysis.

### Historical-research goal sequence

Rewrite the existing goal files so they implement:

1. `00-research-foundation.md`
2. `10-corpus-acquisition.md`
3. `20-textual-verification-and-segmentation.md`
4. `30-metaphor-and-symbolic-language-coding.md`
5. `40-diachronic-analysis-and-thesis.md`
6. `50-draft-paper.md`
7. `60-adversarial-review.md`
8. `70-final-publication.md`

The repository may retain the previous numbering if renumbering would cause unnecessary breakage, but the logical stages above must exist.

### Required human gates

- corpus approval;
- source-substitution approval for derivative or reported texts;
- codebook approval;
- thesis approval;
- methodology-findings approval;
- publication approval.

### Required stop conditions

Stop when:

- authorship or attribution is uncertain;
- a material quotation cannot be verified;
- a source transcription conflicts materially across witnesses;
- access or rights rules prohibit acquisition;
- a required period lacks adequate evidence;
- a metaphor classification depends only on analyst intuition;
- biblical allusion is uncertain and thesis-bearing;
- evidence materially contradicts the working thesis;
- the project begins conflating Brown’s self-representation with later martyr reception;
- validation fails;
- a human gate is reached.

### Completion criteria

- every goal has objective, required inputs, required artifacts, completion criteria, and stop conditions;
- no goal contains Lincoln-specific sources, claims, or outputs;
- the goal sequence stops before corpus acquisition until human approval.

---

## Checkpoint 7 — Reset and instrument the methodology case study

### Objective

Begin a prospective second-case evaluation of the scholarly build system.

### Preserve as baseline

Preserve and generalize as needed:

```text
methodology/methodology.md
methodology/governance-model.md
methodology/human-ai-boundary.md
methodology/artifact-model.md
methodology/evaluation-plan.md
methodology/limitations.md
```

### Replace case-specific findings

Remove active Lincoln case-study findings from the new case.

Create:

```text
methodology/baseline-methodology.md
methodology/case-2-evaluation-plan.md
methodology/case-2-findings.md
```

`case-2-findings.md` must begin as an unapproved scaffold.

### Case 2 evaluation additions

Track where practical:

- event timestamp;
- capture mode;
- proposal source;
- accepted/revised/rejected/deferred status;
- human rationale;
- evidence reviewed;
- artifact changed;
- epistemic effect;
- rework caused;
- time or effort estimate;
- AI/tool cost where available;
- commit SHA;
- evaluation cutoff.

### Completion criteria

- new logs contain headers plus migration events only;
- Lincoln event counts are not reported as current;
- Case 2 evaluation questions are defined before substantive research begins;
- the evaluation plan acknowledges that this is a second case, not independent universal validation.

---

## Checkpoint 8 — Rebuild paper and website scaffolds

### Objective

Create clean public-facing and manuscript scaffolds without presenting provisional claims as findings.

### Required files

Rewrite:

```text
paper/paper.qmd
paper/references.bib
index.qmd
working-paper.qmd
workflow.qmd
evidence.qmd
reviews/index.qmd
publication-audit.qmd
reproducibility-report.qmd
```

Delete obsolete rendered Lincoln pages and review wrappers.

### Paper scaffold sections

The initial paper scaffold should include:

1. Introduction
2. Research Question and Scope
3. Corpus and Source Problems
4. Method for Metaphor, Allusion, and Typology
5. Brown’s Baseline Symbolic Vocabulary
6. Kansas and Armed Resistance
7. Harpers Ferry Planning
8. Capture, Trial, and Imprisonment
9. Failure, Providence, Blood, and Death
10. Diachronic Findings
11. Counterevidence and Alternative Interpretations
12. Limitations
13. Conclusion

Do not populate findings before evidence coding and thesis approval.

### Website status

The site must state:

- this is an active research project;
- the corpus is not yet approved or complete;
- the dossier is provisional;
- no final findings or working paper are yet available;
- methodology and evidence artifacts will be published only after approval.

### Completion criteria

- Quarto renders the clean scaffold;
- no public page claims the Lincoln paper or methodology results belong to this project;
- all broken Lincoln links are removed;
- no placeholder is presented as completed scholarship.

---

## Checkpoint 9 — Validation and migration audit

### Objective

Prove that the repository is internally consistent as a John Brown project before corpus approval.

### Required searches

Search the active repository for:

```text
Lincoln
lincoln
Gettysburg
gettysburg
lincoln_research
Lincoln, Gettysburg, and the Nature of War
```

Classify any remaining occurrence as:

- intentionally retained methodological history;
- citation to the prior case;
- obsolete migration residue.

Remove obsolete residue.

### Required commands

Run:

```bash
python -m john_brown_research validate
pytest
quarto render .
git diff --check
```

If the repository uses targeted Quarto rendering, also render the paper scaffold directly.

### Required migration report

Create:

```text
migration/migration-report.md
```

The report must include:

- source repository identity;
- migration date;
- files preserved;
- files generalized;
- files reset;
- files deleted;
- package rename;
- schema changes;
- tests run;
- render status;
- remaining limitations;
- remaining intentional references to the Lincoln case;
- next human gate.

### Final stop condition

Stop at the corpus-approval human gate.

Do not acquire sources, mark sources verified, populate evidence rows, form a thesis, or publish findings until the scholar reviews and approves:

- the question;
- scope;
- chronological periods;
- proposed corpus;
- source hierarchy;
- codebook draft;
- and acquisition plan.

# Acceptance Criteria

The migration is complete only when all of the following are true:

- [ ] Repository identity is `john-brown-metaphor-analysis`.
- [ ] The primary research question is authoritative and visible.
- [ ] No active package or command uses `lincoln_research`.
- [ ] `python -m john_brown_research validate` succeeds.
- [ ] Tests pass.
- [ ] Quarto renders the clean project scaffold.
- [ ] Lincoln source, evidence, claim, review, approval, and publication state is removed from the active project.
- [ ] Generic methodology and governance controls remain.
- [ ] John Brown-specific epistemic requirements are present.
- [ ] Source, observation, metaphor, allusion, typology, interpretation, and conclusion are distinguished.
- [ ] The chronological corpus structure is documented.
- [ ] The source hierarchy is documented.
- [ ] The codebook remains provisional pending human approval.
- [ ] Research tables are empty except for headers.
- [ ] New process and intervention logs contain only migration-era records.
- [ ] Project status accurately states that the John Brown corpus is not yet approved.
- [ ] No public page presents provisional claims as findings.
- [ ] The migration audit contains no unexplained Lincoln residue.
- [ ] The repository stops at the corpus-approval human gate.

---

# Human Review Package

At the migration-completion gate, present the scholar with:

1. the primary and compact research questions;
2. the proposed title;
3. the chronological corpus periods;
4. the proposed source hierarchy;
5. the draft symbolic-language categories;
6. the disconfirming tests;
7. any proposed schema changes;
8. the codebook draft;
9. the acquisition plan;
10. the migration report;
11. unresolved source-access or copyright risks;
12. the exact approval requested.

The approval request should be:

> Approve, revise, or reject the proposed John Brown research scope, corpus design, source hierarchy, and draft codebook. Approval authorizes Goal 10 corpus acquisition only; it does not approve any interpretation, thesis, or publication.

---

# Non-Goals

This migration does not:

- prove that Brown understood himself as a martyr;
- prove that Brown’s death caused the Civil War;
- analyze Northern or Southern reception as the primary question;
- treat later songs, memorials, biographies, or political uses as evidence of Brown’s original self-understanding;
- authorize publication of findings;
- authorize use of unverifiable attributed quotations;
- authorize bypassing paywalls, authentication, access controls, or copyright restrictions;
- preserve Lincoln conclusions as evidence for the John Brown case;
- establish universal validity of the methodology.

---

# Initial Working Hypotheses

These are provisional and must be treated as testable, revisable, and rejectable:

1. Brown framed slavery principally through bondage, injustice, and moral obligation.
2. Brown represented himself as subordinate to a divine or moral cause rather than as an autonomous originator.
3. Military and rescue metaphors coexisted in tension.
4. His post-capture writings increasingly transformed tactical failure into testimony or providential efficacy.
5. Blood and death became more prominent symbolic resources as execution approached.
6. Brown’s later language may have enabled, but must not be conflated with, the martyr construction produced by supporters.
7. Brown’s symbolic system may be coherent across decades, or it may contain discontinuities produced by changing audiences and circumstances.

No hypothesis may be promoted to a claim without source-grounded evidence, alternative readings, and human review.
