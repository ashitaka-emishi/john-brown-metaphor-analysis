# Repository Patch Goal — Add the Methodology Paper and Case-Study Track

## Purpose

Patch the existing `lincoln-war-research-project` repository so it supports two linked scholarly outputs:

1. the existing historical paper on Lincoln, Gettysburg, and the nature of war;
2. a methodology paper evaluating the governed human–AI scholarly build process through the Lincoln project as a case study.

This patch must preserve the current historical workflow and corpus-acquisition state. It must not restart Goal 00, rerun completed corpus work, move the existing research tree, or change approved historical research decisions.

The repository is already in the corpus-acquisition phase. The methodology track must be added around the current project and must begin by reconstructing prior process events from existing repository evidence.

---

# Governing Principle

Treat the existing Lincoln project as the active case study of a broader methodology.

The historical research asks:

> How does the Gettysburg Address transform the deaths of soldiers into a sacred obligation to preserve and refound the nation, and what does this reveal about Lincoln's understanding of the nature of war?

The methodology research asks:

> How can interpretive scholarship be represented as a traceable, version-controlled transformation of sources into claims and publication outputs while preserving human scholarly authority in an AI-assisted process?

The historical question remains primary for historical artifacts. The methodology question governs only the new methodology and case-study artifacts.

---

# Required Operating Rules

Before making changes:

1. Read `AGENTS.md`.
2. Read `README.md`.
3. Read `logs/progress.md`.
4. Read:
   - `research/notes/question-and-scope.md`
   - `research/notes/method.md`
   - `research/notes/source-acquisition-plan.md`
   - `research/notes/corpus-report.md`
   - `research/notes/corpus-approval.md`
5. Inspect the current Git status and recent commit history.
6. Do not modify raw corpus files.
7. Do not change source verification states except where this patch creates cross-references.
8. Do not alter the approved corpus.
9. Do not treat retrospective methodology reconstruction as contemporaneous evidence.
10. Preserve all current tests and validation.

Update `logs/progress.md` when the patch is complete.

---

# Target Repository Structure

Add the following structure without relocating existing files:

```text
methodology/
├── methodology.md
├── research-question.md
├── human-ai-boundary.md
├── artifact-model.md
├── governance-model.md
├── evaluation-plan.md
├── limitations.md
└── decisions/
    └── README.md

case-study/
├── README.md
├── process-events.csv
├── intervention-log.csv
├── thesis-history.md
├── human-decisions.md
└── retrospective/
    ├── goal-00-retrospective.md
    └── goal-10-to-date.md

goals/
└── methodology/
    ├── M00-methodology-foundation.md
    ├── M10-instrument-current-workflow.md
    ├── M20-evaluate-case-study.md
    ├── M30-draft-methodology-paper.md
    └── M40-review-methodology.md

methodology-paper/
├── methodology-paper.qmd
├── references.bib
└── appendices/
    └── README.md

config/
└── schemas/
    ├── process-events.fields
    └── intervention-log.fields
```

Do not move the existing `research/`, `paper/`, `goals/`, `scripts/`, `src/`, or `tests/` directories.

---

# 1. Create `methodology/methodology.md`

Use the existing methodology document if it is already present locally or available in the working directory. Otherwise create it with the following content:

```markdown
# Methodology for AI-Assisted Scholarly Paper Development

## Purpose

This methodology describes a structured process for producing a scholarly paper with artificial intelligence serving as a research, analytical, and engineering assistant under human scholarly authority.

The purpose is not to automate authorship. It is to make the research process more rigorous, explicit, reproducible, and reviewable through human judgment, source-grounded research, computational assistance, structured evidence management, adversarial review, and transparent documentation.

The methodology treats a scholarly paper as the visible expression of a governed knowledge base concerning a defined research question.

The paper is not the only research artifact. It is the final human-readable synthesis generated from a larger body of sources, passages, observations, interpretations, claims, counterclaims, decisions, and reviews.

## Foundational principle

A scholarly paper is a governed knowledge system.

The project maintains a traceable chain:

> research question → corpus → source → passage → observation → interpretation → claim → counterevidence → argument → paper

Each stage is represented by one or more project artifacts. These artifacts preserve the minimum sufficient knowledge required to explain, test, revise, and defend the paper.

## Human scholarly authority

The human scholar retains final authority over:

- the research question;
- scope;
- corpus;
- interpretive framework;
- definitions;
- thesis;
- acceptance or rejection of arguments;
- ethical judgments;
- citations;
- and publication.

AI may recommend, compare, test, organize, and draft, but it does not possess scholarly accountability.

## Role of AI

AI serves as a subordinate research and engineering assistant.

It may assist with:

- source discovery;
- metadata extraction;
- document normalization;
- textual comparison;
- coding suggestions;
- evidence organization;
- argument testing;
- counterargument generation;
- adversarial review;
- provisional drafting;
- consistency checking;
- and generation of tables, diagrams, and appendices.

AI output remains provisional until verified.

## Human–AI boundary

The boundary is defined by authority, accountability, evidence, and judgment rather than by who typed the words.

### Human-exclusive responsibilities

- define scholarly purpose;
- approve the corpus;
- make interpretive commitments;
- resolve contested meanings;
- approve or reject the thesis;
- assume ethical responsibility;
- approve publication.

### AI-appropriate responsibilities

- repetitive structured work;
- metadata collection;
- source inventory;
- identifier creation;
- hashing;
- format conversion;
- schema validation;
- quotation matching;
- missing-field detection;
- evidence-table construction;
- counterargument generation;
- and automated checks.

### Shared responsibilities

- corpus design;
- evidence coding;
- argument mapping;
- drafting;
- and review.

## Epistemic separation

The process distinguishes:

1. **Source text** — what the source says.
2. **Observation** — a directly supportable description.
3. **Interpretation** — an analytical explanation.
4. **Broader conclusion** — a claim about historical meaning, rhetoric, or theory.

The project must not silently move from wording to psychology, metaphor to doctrine, or one speech to a universal theory.

## Research workflow

1. Define the question.
2. Design the corpus.
3. Acquire sources.
4. Preserve and normalize.
5. Extract evidence.
6. Code evidence.
7. Build claims.
8. Construct the argument.
9. Test disconfirmation.
10. Draft from approved claims.
11. Conduct adversarial review.
12. Render publication outputs.
13. Obtain human publication approval.

## Human gates

The process includes:

- corpus approval;
- thesis approval;
- publication approval.

AI must stop at each gate.

## Engineering the process

The repository uses:

- version control;
- traceability;
- reproducibility;
- explicit schemas;
- automated validation;
- modular goals;
- human review;
- and controlled change.

Automated tests verify research-system integrity. They do not determine whether an interpretation is historically valid.

## Transparency

The project must preserve:

- uncertainty;
- failed searches;
- inaccessible sources;
- contradictory evidence;
- rejected AI recommendations;
- weak citations;
- variant texts;
- human interventions;
- and arguments that did not survive review.

## Completion

The paper is complete only when the repository contains:

- approved scope;
- documented corpus;
- verified primary sources;
- completed evidence matrix;
- reviewed claims;
- approved thesis;
- counterargument;
- citation audit;
- adversarial review;
- reproducible output;
- and human publication approval.
```

---

# 2. Create Methodology Definition Files

## `methodology/research-question.md`

```markdown
# Methodology Research Question

## Primary question

> How can interpretive scholarship be represented as a traceable, version-controlled transformation of sources into claims and publication outputs while preserving human scholarly authority in an AI-assisted process?

## Supporting questions

1. Which scholarly activities can be delegated safely to AI?
2. Which activities require mandatory human authority?
3. Can source-to-claim traceability improve interpretive rigor?
4. What errors are caught by structured goals, schemas, tests, and review gates?
5. What new burdens are introduced by engineering the research process?
6. Can the process be reproduced without reducing interpretation to computation?
7. How should AI contribution be disclosed?
8. Which parts of the process generalize beyond the Lincoln case?

## Case-study relationship

The Lincoln project is the initial case through which the methodology is tested and refined.

The methodology paper must not treat one successful case as proof of universal validity.
```

## `methodology/human-ai-boundary.md`

```markdown
# Human–AI Responsibility Boundary

## Human authority

The scholar controls:

- question;
- corpus;
- definitions;
- interpretation;
- thesis;
- ethical judgment;
- final prose;
- citation approval;
- publication.

## AI authority

AI may independently perform only bounded, reversible, inspectable tasks that do not settle scholarly meaning.

Examples:

- file transformation;
- metadata extraction;
- source inventory;
- hashing;
- schema checks;
- identifier generation;
- variant comparison;
- coding proposals;
- claim-link checks;
- review prompts;
- draft proposals.

## Shared work

Shared tasks require explicit human review:

- source inclusion;
- coding;
- interpretive classification;
- claim wording;
- thesis revision;
- response to counterevidence;
- and final drafting.

## Boundary rule

AI may produce or transform an artifact. The human scholar determines whether the artifact is accepted as scholarly knowledge.

## Mandatory human intervention

Human review is required when:

- evidence is ambiguous;
- OCR is unreliable;
- a source is derivative;
- a source identity is uncertain;
- a claim concerns private belief;
- a term is contested;
- a thesis changes;
- a source access or copyright issue arises;
- the AI and evidence conflict;
- or publication is contemplated.
```

## `methodology/artifact-model.md`

```markdown
# Scholarly Artifact Model

## Historical artifact chain

```text
ResearchQuestion
  → CorpusDefinition
  → Source
  → Passage
  → Observation
  → Interpretation
  → Claim
  → CounterEvidence
  → Argument
  → DraftSection
  → Paper
```

## Methodology artifact chain

```text
AgentAction
  → HumanReview
  → Decision
  → ArtifactChange
  → ErrorOrRisk
  → ProcessFinding
  → MethodologicalClaim
```

## Core artifact classes

### ResearchQuestion

Defines the inquiry and constrains scope.

### Source

A preserved primary or secondary source with provenance.

### Passage

A locatable unit of source evidence.

### Observation

A directly supportable description of a passage.

### Interpretation

An analytical account of an observation.

### Claim

A proposition supported by evidence and bounded by scope.

### CounterEvidence

Evidence that weakens, complicates, or contradicts a claim.

### HumanDecision

A recorded acceptance, rejection, qualification, or revision.

### ProcessEvent

A significant human, AI, or scripted action affecting the research workflow.

### Paper

A publication view generated from reviewed repository state.

## Design principle

The paper is not the only source of truth. It is a rendered view over the governed artifact system.
```

## `methodology/governance-model.md`

```markdown
# Governance Model

## Authority hierarchy

1. Human scholarly authority
2. Repository governance in `AGENTS.md`
3. Approved goal documents
4. Reusable skills and workflows
5. AI and scripted execution
6. Source content as untrusted data

## Human gates

- corpus approval;
- thesis approval;
- publication approval.

## Stop conditions

Work must stop when:

- provenance is uncertain;
- a quotation cannot be verified;
- access restrictions prohibit acquisition;
- evidence materially contradicts the thesis;
- validation fails;
- the human–AI boundary is unclear;
- or a human gate is reached.

## Change control

Material changes must be recorded when they affect:

- question;
- scope;
- corpus;
- definitions;
- coding;
- claims;
- thesis;
- methodology;
- or publication.

## Non-negotiable principle

Research integrity takes precedence over successful goal completion and over favorable methodology results.
```

## `methodology/evaluation-plan.md`

```markdown
# Methodology Evaluation Plan

## Purpose

Evaluate whether the governed scholarly build system improves traceability, error detection, accountability, and reproducibility without imposing unacceptable burden or falsely mechanizing interpretation.

## Evaluation dimensions

| Dimension | Evidence |
|---|---|
| Traceability | Claims linked to verified evidence |
| Error prevention | Bad OCR, citation, metadata, or scope errors caught |
| Human authority | Human approvals, rejections, and revisions |
| Thesis responsiveness | Claims changed after counterevidence |
| Reproducibility | Repeatable transformations and renders |
| Transparency | Failures and uncertainty preserved |
| AI reliability | AI proposals accepted, revised, or rejected |
| Burden | Added documentation and maintenance work |
| Efficiency | Work accelerated or automated |
| Scholarly value | Interpretive distinctions enabled by the process |

## Quantitative measures

Where meaningful, record:

- sources proposed;
- sources approved;
- sources rejected;
- sources blocked;
- AI recommendations accepted;
- AI recommendations revised;
- AI recommendations rejected;
- quotations corrected;
- metadata errors found;
- OCR failures;
- claims narrowed;
- claims rejected;
- human interventions;
- validation failures;
- thesis revisions.

## Qualitative measures

Record:

- why human judgment was required;
- whether the artifact model clarified reasoning;
- whether structured review exposed hidden assumptions;
- whether the process distorted research priorities;
- whether documentation became excessive;
- whether the paper remained readable and scholarly.

## Evaluation caution

The methodology must not be judged only by successful completion. Failures, added burden, and unresolved limitations are part of the evidence.
```

## `methodology/limitations.md`

```markdown
# Methodology Limitations

Current known limitations include:

- interpretation cannot be reduced to automated validation;
- one case cannot establish general applicability;
- repository structure may create documentation burden;
- AI may generate plausible but false interpretations or citations;
- copyrighted scholarship may not be preservable in a public repository;
- source access may depend on external repositories;
- model behavior and tooling may change;
- human review may become superficial if overwhelmed by volume;
- structured schemas may oversimplify ambiguous evidence;
- the process may privilege what can be represented formally;
- retrospective reconstruction is weaker than contemporaneous logging;
- reproducibility of process does not guarantee validity of interpretation.
```

## `methodology/decisions/README.md`

```markdown
# Methodology Decisions

Record durable methodology decisions in this directory.

Each decision record should contain:

- identifier;
- date;
- issue;
- options considered;
- decision;
- rationale;
- evidence;
- consequences;
- revisitation criteria.
```

---

# 3. Create Case-Study Instrumentation

## `config/schemas/process-events.fields`

```text
event_id
timestamp
capture_mode
stage
actor
action_type
artifact
proposal_or_action
human_decision
outcome
error_or_risk
methodological_significance
evidence_reference
commit_sha
notes
```

## `config/schemas/intervention-log.fields`

```text
intervention_id
event_id
timestamp
initiator
proposal
human_response
response_reason
artifact_changed
epistemic_effect
accepted_status
evidence_reference
commit_sha
notes
```

## `case-study/process-events.csv`

Create with exactly this header:

```csv
event_id,timestamp,capture_mode,stage,actor,action_type,artifact,proposal_or_action,human_decision,outcome,error_or_risk,methodological_significance,evidence_reference,commit_sha,notes
```

Add retrospective rows supported by `logs/progress.md` and existing artifacts.

At minimum include events for:

1. Goal 00 corpus approval gate.
2. Creation of `corpus-approval.md`.
3. Acquisition and verification of Nicolay and Hay copies.
4. Failed automated OCR of the Bliss copy.
5. Creation of the human transcription target.
6. Human transcription and approval of the Bliss copy.
7. Chrome/MCP tooling limitation.
8. Creation of the Chronicling America acquisition tooling.
9. Blocking of the Harrisburg item because original access was unavailable.
10. Qualified acceptance of the Dickinson derivative transcription.
11. Creation of the public repository and status-conscious site.

Use `capture_mode=retrospective` for all reconstructed rows.

Do not invent timestamps more precise than existing evidence permits. A date-only timestamp is acceptable.

Do not invent commit SHAs. Leave `commit_sha` blank unless verified from Git history.

## `case-study/intervention-log.csv`

Create with exactly this header:

```csv
intervention_id,event_id,timestamp,initiator,proposal,human_response,response_reason,artifact_changed,epistemic_effect,accepted_status,evidence_reference,commit_sha,notes
```

At minimum include interventions for:

- approval of the corpus;
- human transcription of the Bliss copy;
- qualified acceptance of the derivative Harrisburg transcription;
- selection of Python 3.11;
- approval to create and publish the public repository.

## `case-study/README.md`

```markdown
# Lincoln Research as Methodology Case Study

This directory records evidence about how the research process operated.

It does not duplicate the historical corpus, evidence matrix, or manuscript.

The case-study layer records:

- significant AI actions;
- human interventions;
- accepted, revised, and rejected proposals;
- tool and source failures;
- process decisions;
- thesis development;
- and methodological lessons.

## Capture modes

- `retrospective` — reconstructed from existing repository evidence;
- `prospective` — recorded during the stage in which the event occurred.

Retrospective and prospective events must not be conflated.

## Integrity rule

The historical workflow must not be distorted to produce favorable methodology results.
```

## `case-study/thesis-history.md`

```markdown
# Thesis History

Record each material thesis revision.

For each version include:

- date;
- thesis text;
- supporting claims;
- counterevidence;
- reason for revision;
- human approval status;
- related commit.

No thesis is yet approved for the methodology paper.
```

## `case-study/human-decisions.md`

```markdown
# Human Scholarly Decisions

This file summarizes high-level human decisions.

Detailed events belong in `process-events.csv` and `intervention-log.csv`.

Required categories:

- corpus decisions;
- source-verification decisions;
- interpretation decisions;
- coding decisions;
- thesis decisions;
- publication decisions;
- methodology decisions.
```

---

# 4. Create Retrospective Case Records

## `case-study/retrospective/goal-00-retrospective.md`

Create a concise reconstruction based only on existing repository evidence.

Required sections:

```markdown
# Goal 00 Retrospective

## Status

Retrospective reconstruction from repository artifacts.

## Inputs reviewed

## Work completed

## Human gate

## AI contributions

## Human decisions

## Validation

## Methodological findings

## Limitations of reconstruction
```

At minimum note:

- dossier converted into controlled plan;
- source register expanded;
- no source silently verified;
- scope and sacrifice were operationally defined;
- source acquisition plan created;
- provisional claims inventoried;
- validation passed;
- acquisition stopped at human corpus gate.

## `case-study/retrospective/goal-10-to-date.md`

Use the same structure and include:

- acquisition of manuscript witnesses;
- raw/normalized separation;
- hashing and provenance;
- OCR failure;
- human transcription;
- browser tooling limitation;
- Chronicling America scripts;
- reception sampling;
- derivative transcription qualification;
- corpus report;
- remaining source limitations.

---

# 5. Add Methodology Goals

## `goals/methodology/M00-methodology-foundation.md`

```markdown
# Methodology Goal M00 — Establish the Methodology Track

## Objective

Add the methodology paper and case-study track without changing the active historical research workflow.

## Required work

1. Create the methodology documents.
2. Create the artifact and governance models.
3. Create the evaluation plan.
4. Create case-study schemas.
5. Reconstruct completed process events.
6. Add prospective instrumentation rules to `AGENTS.md`.
7. Add the methodology paper scaffold.
8. Update the README and progress log.

## Completion criteria

- Existing historical files are not relocated.
- Historical corpus scope is unchanged.
- Retrospective events are explicitly labeled.
- New schemas are validated.
- Existing validation and tests pass.
```

## `goals/methodology/M10-instrument-current-workflow.md`

```markdown
# Methodology Goal M10 — Instrument the Active Workflow

## Objective

Record future material research actions prospectively while the Lincoln project continues.

## Required events

Record a methodology event when an action:

- requires human approval;
- changes corpus scope;
- accepts, revises, or rejects an AI recommendation;
- encounters a source, tool, rights, provenance, or validation failure;
- changes a definition, claim, thesis, or interpretation;
- substitutes human work for automation;
- or materially changes the paper.

## Completion criteria

- Events are recorded during the stage in which they occur.
- Events link to repository artifacts.
- Human interventions are separately recorded.
- Research integrity takes precedence over instrumentation.
```

## `goals/methodology/M20-evaluate-case-study.md`

```markdown
# Methodology Goal M20 — Evaluate the Case Study

## Objective

Evaluate the methodology after the historical project has completed evidence coding and initial thesis formation.

## Required work

1. Analyze process events and interventions.
2. Measure traceability and error detection.
3. Identify successful and failed AI contributions.
4. Evaluate documentation burden.
5. Identify changes caused by counterevidence.
6. Compare retrospective and prospective capture quality.
7. Produce `methodology/case-study-findings.md`.

## Stop condition

Stop at a human methodology-findings approval gate.
```

## `goals/methodology/M30-draft-methodology-paper.md`

```markdown
# Methodology Goal M30 — Draft the Methodology Paper

## Objective

Draft the methodology paper from approved methodology claims and case-study evidence.

## Required sections

1. Introduction
2. Related practices
3. Scholarly build-system model
4. Human–AI authority model
5. Artifact and governance model
6. Case-study design
7. Case-study findings
8. Discussion
9. Limitations
10. Conclusion

## Requirements

- Do not claim universal validation from one case.
- Distinguish retrospective from prospective evidence.
- Include failures and added burden.
- Do not present AI as an accountable scholar.
- Cite related methodology literature.
```

## `goals/methodology/M40-review-methodology.md`

```markdown
# Methodology Goal M40 — Review the Methodology Paper

## Objective

Conduct adversarial review of the methodology and its claimed originality.

## Required critiques

- The method is only a research compendium with new terminology.
- The artifact model falsely mechanizes interpretation.
- Human gates are ceremonial rather than effective.
- The case study is biased because the method was developed during the case.
- Process logging altered the research process.
- One case provides insufficient evidence.
- Documentation cost exceeds its scholarly value.
- AI disclosure remains inadequate.
- Reproducibility is confused with validity.

Revise the paper when critiques succeed.
```

---

# 6. Create the Methodology Paper Scaffold

## `methodology-paper/methodology-paper.qmd`

```markdown
---
title: "The Scholarly Build System"
subtitle: "A Governed Human–AI Method for Reproducible Interpretive Research"
author: "Andrew Hammer"
date: last-modified
abstract: |
  This manuscript is under development. It presents and evaluates a governed
  human–AI scholarly build system through a case study of research on Abraham
  Lincoln's Gettysburg Address.
keywords:
  - artificial intelligence
  - scholarly method
  - reproducible research
  - digital humanities
  - research compendium
  - human-in-the-loop
  - interpretive scholarship
bibliography: references.bib
---

# Introduction

# Related Practices

## Reproducible research

## Research compendia

## Executable and dynamic documents

## Argument mapping and provenance

## AI-assisted scholarship

# The Scholarly Build System

## Research as a governed knowledge base

## The artifact chain

## Human scholarly authority

## Goals, gates, and stop conditions

## Machine validation and scholarly validity

## Adversarial review

# Case-Study Design

## Historical research question

## Repository architecture

## Event and intervention logging

## Evaluation criteria

# Case-Study Findings

This section must remain provisional until methodology findings are approved.

# Discussion

# Limitations

# Conclusion
```

## `methodology-paper/references.bib`

Create an empty but valid BibTeX file with a comment:

```bibtex
% Add verified methodology and related-work references here.
```

## `methodology-paper/appendices/README.md`

```markdown
# Methodology Paper Appendices

Potential appendices include:

- artifact schemas;
- human–AI responsibility matrix;
- process-event summary;
- intervention summary;
- goal and gate definitions;
- validation rules;
- case-study timeline.
```

---

# 7. Patch `AGENTS.md`

Append this section without removing current instructions:

```markdown
## Methodology case-study instrumentation

This repository also evaluates the scholarly process itself.

Record a methodology event when a material action:

- requires human approval;
- changes corpus scope;
- accepts, revises, or rejects an AI recommendation;
- encounters a source, tool, copyright, provenance, or validation failure;
- changes a definition, claim, thesis, or interpretation;
- substitutes human judgment for automation;
- or materially changes a paper.

Record events in `case-study/process-events.csv`.

Record human interventions in `case-study/intervention-log.csv`.

Use `capture_mode=retrospective` only for events reconstructed from repository evidence. Use `capture_mode=prospective` for future events recorded during the active stage.

Do not distort the historical research workflow to produce favorable methodology results.

Research integrity takes precedence over methodology evaluation.

The methodology paper has its own human findings and publication approval gates.
```

---

# 8. Patch `README.md`

Add a section after the project description:

```markdown
## Two linked scholarly outputs

This repository now supports two related outputs:

1. a historical study of Lincoln's Gettysburg Address and the nature of war;
2. a methodology paper evaluating the governed human–AI process used to produce that study.

The historical project remains the active case study. Existing research files and goals retain their current meaning and location.

The methodology track records process events, human interventions, failures, corrections, and thesis development. It does not treat the method as validated in advance.

See:

- `methodology/methodology.md`
- `methodology/research-question.md`
- `case-study/README.md`
- `methodology-paper/methodology-paper.qmd`
```

Add a methodology goal list:

```markdown
## Methodology goal sequence

1. `goals/methodology/M00-methodology-foundation.md`
2. `goals/methodology/M10-instrument-current-workflow.md`
3. `goals/methodology/M20-evaluate-case-study.md`
4. `goals/methodology/M30-draft-methodology-paper.md`
5. `goals/methodology/M40-review-methodology.md`
```

Do not remove the existing historical goal sequence.

---

# 9. Extend Validation

Update the validation system so it checks the headers of:

- `case-study/process-events.csv`;
- `case-study/intervention-log.csv`.

Use the schema files:

- `config/schemas/process-events.fields`;
- `config/schemas/intervention-log.fields`.

Do not break existing schema validation.

Add tests confirming:

1. both methodology CSV files exist;
2. their headers exactly match schemas;
3. `event_id` values begin with `METH-`;
4. `intervention_id` values begin with `INT-`;
5. `capture_mode` is either `retrospective` or `prospective`;
6. an intervention references an existing event when `event_id` is populated.

Do not require every retrospective event to have a commit SHA.

---

# 10. Update the Progress Log

Append a new section:

```markdown
## Methodology-track integration

- Added a parallel methodology-paper track around the active Lincoln historical project.
- Preserved the existing corpus, goals, source register, research method, and paper structure.
- Added a general methodology specification, human–AI boundary, artifact model, governance model, evaluation plan, and limitations.
- Added retrospective case-study records for completed Goal 00 and Goal 10 work to date.
- Added prospective process-event and human-intervention instrumentation.
- Added methodology-specific goals and a Quarto methodology-paper scaffold.
- Updated repository instructions and README without changing historical research scope.
- Validation and tests passed.
```

Use the actual date and actual test results.

---

# 11. Validation and Completion

Run:

```bash
python -m lincoln_research validate
pytest
```

If the project has formatting or lint commands, run them as well.

Do not render the methodology paper as final scholarship. It is a scaffold with provisional content.

## Completion criteria

This patch is complete only when:

- all new directories and files exist;
- existing historical research files remain in place;
- existing corpus status is unchanged;
- retrospective and prospective events are distinguishable;
- methodology schemas are validated;
- new tests pass;
- existing tests still pass;
- README and AGENTS instructions are updated;
- progress log records the patch;
- Git diff shows no unintended raw-corpus changes.

## Stop conditions

Stop and report instead of improvising if:

- existing repository structure materially differs from this patch;
- current validation architecture cannot be extended safely;
- process history cannot be reconstructed from repository evidence;
- a proposed retrospective event would require invented details;
- the patch would alter approved corpus or source verification;
- or tests cannot be made to pass without weakening existing controls.

---

# Suggested Codex Invocation

Use this document as the active goal:

```text
/goal Execute the repository patch described in REPO-METHODOLOGY-PATCH.md. Preserve the current Lincoln corpus-acquisition state, do not relocate existing historical artifacts, reconstruct prior methodology events only from repository evidence, add prospective instrumentation, update validation and tests, and stop on any documented stop condition.
```
