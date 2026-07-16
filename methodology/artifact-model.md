# Scholarly Artifact Model

## Historical artifact chain

```text
ResearchQuestion
  -> CorpusDefinition
  -> Source
  -> Passage
  -> Observation
  -> Interpretation
  -> Claim
  -> CounterEvidence
  -> Argument
  -> DraftSection
  -> Paper
```

## Methodology artifact chain

```text
AgentAction
  -> HumanReview
  -> Decision
  -> ArtifactChange
  -> ErrorOrRisk
  -> ProcessFinding
  -> MethodologicalClaim
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

The paper is not the only source of truth. It is a rendered view over the
governed artifact system.
