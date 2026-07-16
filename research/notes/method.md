# Method

## Status

This method controls the next phases of research. It does not verify the dossier's claims. It explains how proposed sources will be acquired, normalized, coded, interpreted, challenged, and mapped to claims.

## Source Hierarchy

Primary-source claims about Lincoln's language and action will rely on locally preserved source text, not on search results or unpreserved web pages.

Preferred source order:

1. Authoritative manuscript image or scan from a repository such as the Library of Congress or National Archives.
2. Authoritative transcription supplied by the holding repository.
3. Scholarly edition or government edition with stable bibliographic metadata.
4. Reputable educational or documentary site used only as a discovery aid until verified against a stronger source.

Secondary works will be used to identify interpretive schools, context, disputes, and counterarguments. They will not substitute for primary-source evidence when the claim concerns Lincoln's wording.

## Acquisition and Preservation

Raw acquired files are immutable. Each acquired source must have a source-register row with repository, URL or locator, retrieval date, acquisition method, rights status, local raw path, and SHA-256 hash. Normalized text must be stored separately from raw source material.

No source may be marked verified until it has been inspected locally and the preserved raw file has a hash. If provenance, access rights, or identity is uncertain, the source remains unverified and the uncertainty is recorded.

## Textual Method

The Gettysburg Address must be treated as a variant textual object. The Nicolay, Hay, Everett, Bancroft, and Bliss copies will be preserved as distinct sources. Claims must specify which copy or textual layer they rely on.

Delivered-text claims require special caution. If a word or phrase appears in later copies but not in the likely delivery copy, the claim must identify that variant status instead of harmonizing the manuscripts.

## Coding Method

Evidence rows will code passages for:

- nation ontology;
- nature of war;
- death representation;
- temporal structure;
- religious register;
- political function;
- agency;
- bodily reality;
- alternative readings;
- evidentiary weight.

Sacrifice coding must follow the operational definition in `research/notes/question-and-scope.md`. The coding basis must quote or faithfully paraphrase the source passage and identify the feature that justifies the code.

## Claim Control

Every material claim must be entered in `research/data/claims.csv` before drafting. Each claim must identify supporting evidence, counterevidence, status, confidence, and draft location when applicable.

Claim scope must be explicit:

- Gettysburg Address only;
- Lincoln public rhetoric;
- Lincoln private reflection;
- Civil War;
- war in general;
- reception or memory.

Claims about private belief, providence, sacrifice, and the moral meaning of death require heightened caution and must record alternative readings.

## Comparative Method

Comparative Lincoln sources will be used to test whether Gettysburg's rhetoric is isolated, continuous, or in tension with other wartime frames. Comparison will track change over time rather than assuming a fixed doctrine:

- constitutional preservation;
- democratic experiment and global stakes;
- emancipation and transformation;
- providential uncertainty;
- judgment for slavery;
- reconciliation and reconstruction.

Everett and ceremonial materials will test whether Lincoln's sacred vocabulary is distinctive or generic to cemetery dedication rhetoric.

## Reception Method

Reception evidence will be sampled by political orientation, region, date, and genre where possible. Event reports must be distinguished from editorial judgments. Later canonical reverence must not be projected backward onto November 1863.

## Adversarial Review

Before drafting a final thesis, the evidence must be tested against these objections:

- The address uses ordinary commemorative language rather than a distinctive sacrificial structure.
- The analyst is imposing sacrifice where the source only says death.
- Lincoln addresses this war only, not war in general.
- The argument ignores soldier agency or imposes state meaning on diverse deaths.
- Political theology is overstated in a short public ceremony.
- Rhetorical effect is being confused with authorial intention.

Contradictory evidence must remain in the evidence matrix and claim map.

## Human Gates

Goal 00 stops at corpus approval. Later phases may not acquire or code a final corpus until the scholar approves proposed inclusions, exclusions, unresolved identities, and risks.
