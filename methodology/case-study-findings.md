# Case Study Findings

Date: 2026-07-16

Goal: `goals/methodology/M20-evaluate-case-study.md`

Case: Lincoln/Gettysburg historical working-paper project through public
working-paper release.

## Status

These findings were approved by the scholar on 2026-07-16 as the M20
methodology findings.

They may be used as case-study evidence for methodology-paper drafting, while
remaining subject to later methodology review.

## Evidence Base

This evaluation uses current repository artifacts rather than memory of the
conversation:

- `case-study/process-events.csv`
- `case-study/intervention-log.csv`
- `logs/progress.md`
- `research/data/source-register.csv`
- `research/data/evidence-matrix.csv`
- `research/data/claims.csv`
- `research/reviews/*.md`
- `outputs/publication-audit.md`
- `outputs/reproducibility-report.md`

## Quantitative Summary

| Measure | Count |
|---|---:|
| Process events recorded | 27 |
| Retrospective process events | 11 |
| Prospective process events | 16 |
| Human process events | 12 |
| AI process events | 15 |
| Human interventions recorded | 13 |
| Accepted interventions | 13 |
| Source-register rows | 42 |
| Verified source rows | 29 |
| Partially verified source rows | 1 |
| Verified derivative-transcription rows | 1 |
| Unverified source rows | 11 |
| Evidence rows | 32 |
| Disconfirming evidence rows | 8 |
| Claims | 9 |
| Claims changed to reviewed-approved status in adversarial review | 3 |
| Tests in repository suite | 10 |

## 1. Traceability

Finding: the artifact chain substantially improved traceability.

Evidence:

- The source register preserves source identity, local raw and normalized paths,
  retrieval date, hashes, rights status, acquisition method, verification
  status, and notes.
- The evidence matrix contains 32 verbatim evidence rows. Each row separates
  passage, observation, interpretation, alternative reading, confidence, and
  review status.
- The claims table contains 9 claims, and the validation audit found no broken
  claim-to-evidence references.
- The final paper and publication package cite through
  `paper/references.bib`, and prior audits found 25 used citation keys matched
  by 25 bibliography entries.

Interpretation:

The process made it possible to answer "why does this sentence appear in the
paper?" by following a chain from paper claim to claim record to evidence row
to source register entry. This is stronger than a conventional draft folder
because uncertainty and review status are attached to the evidence itself, not
only to prose notes.

Limit:

Traceability is uneven for secondary scholarship. Ten secondary-source rows
remain unverified or library/purchase targets. The working paper is therefore
well traced to the acquired primary-source corpus but not to a comprehensive
secondary literature base.

## 2. Error Detection

Finding: the methodology exposed several errors or risks before they became
silent premises.

Examples:

- OCR failed for the Smithsonian Bliss Copy. The process recorded the failure,
  created a human transcription target, and preserved a quotation-level
  manuscript-image caveat.
- Public access to the original Harrisburg *Patriot and Union* image was not
  available. The project first marked the source blocked, then accepted the
  Dickinson derivative transcription only with a pending-image limitation.
- Chrome/browser tooling limitations were recorded instead of being hidden.
- A completion audit during Goal 20 found that the first evidence-coding pass
  under-covered comparative Lincoln texts; the matrix was expanded before the
  goal was declared complete.
- Goal 50 adversarial review caught overbroad phrasing around "refound,"
  "political theology," private belief, and war as such.
- Publication-package review caught stale commit metadata in the local output
  package and corrected it before approval.
- The public landing page was later found to be stale and was updated after the
  working-paper package was approved.

Interpretation:

The project did not merely validate successful output. It used failed OCR,
blocked access, derivative-source status, adversarial critique, and stale public
metadata as data about the research process.

## 3. Successful AI Contributions

Finding: AI was most successful in bounded, inspectable tasks.

High-value contributions included:

- creating repeatable source-acquisition and normalization scripts;
- maintaining the source register and evidence/claim tables;
- running validation and consistency checks;
- expanding evidence coverage after a completion audit;
- generating adversarial reviews and narrowing the manuscript accordingly;
- rendering and packaging the working paper;
- updating the public site only after human publication approval.

Interpretation:

The strongest AI role was not autonomous interpretation. It was structured
research engineering: making artifacts, detecting inconsistencies, preparing
audits, and forcing decisions to become explicit.

## 4. Failed or Limited AI Contributions

Finding: AI and automation repeatedly needed correction, supplementation, or
human authority.

Examples:

- OCR could not reliably produce the Bliss Copy text.
- Browser-assisted source acquisition was limited by available tooling and
access conditions.
- The first evidence-coding pass needed expansion after an audit found
  comparative coverage too narrow.
- Publication metadata became stale after later commits and needed correction.
- The landing page remained stale after the working paper was published.

Interpretation:

The system worked best when failure was preserved and routed into a gate,
audit, or revision. It would have been weaker if these failures were hidden in
finished prose.

## 5. Documentation Burden

Finding: the methodology created real documentation burden.

Evidence:

- The project now contains process-event logs, intervention logs, progress
  logs, source registers, evidence matrices, claim maps, reviews, audits,
  reproducibility reports, and publication package files.
- The process-event log contains 27 events, and the intervention log contains
  13 human interventions.
- Several later tasks were maintenance tasks: correcting stale package
  metadata, publishing output dependencies, and updating the landing page.

Interpretation:

The burden was not incidental. It was part of the method: every gate, source
limit, and thesis change needed a record. That record improved accountability,
but it also required active maintenance. Without discipline, documentation
could become a parallel project that competes with scholarship.

Practical lesson:

The method should keep logs concise and use structured artifacts only where
they answer real review questions. More metadata is not automatically better.

## 6. Counterevidence and Thesis Change

Finding: counterevidence materially narrowed the argument.

Evidence:

- 8 of 32 evidence rows are marked disconfirming.
- Goal 30 produced a disconfirmation review and stopped at a thesis approval
  gate.
- Goal 50 changed three claims to `reviewed-approved-thesis` and narrowed the
  manuscript.
- The final public page and publication package describe the output as a
  working paper with limitations, not as final scholarship.

Examples of narrowing:

- Gettysburg was framed as public rhetoric rather than direct access to
  Lincoln's private belief.
- The claim was bounded to this Civil War rather than war in general.
- Everett was used to prevent overclaiming Lincoln's uniqueness.
- The Second Inaugural was preserved as a different theological frame rather
  than a mere fuller version of Gettysburg.
- "Refound" was replaced in summary-level language by "new birth of freedom."

Interpretation:

The process did not simply support an initial thesis. It narrowed the thesis
under pressure from evidence, genre, manuscript variants, and countervoices.

## 7. Retrospective vs Prospective Capture

Finding: prospective capture is stronger than retrospective reconstruction.

Evidence:

- 11 process events are retrospective.
- 16 process events are prospective.
- Retrospective events frequently rely on progress logs and commit history.
- Prospective events more often include immediate rationale, artifact links,
  and action context.

Interpretation:

Retrospective capture was useful for reconstructing Goal 00 and Goal 10, but it
is thinner and more dependent on already preserved artifacts. Prospective
capture better records why a decision mattered at the moment it was made.

Limit:

Prospective capture may change behavior by making the researcher more conscious
of what will later be evaluated. That is a possible observer effect and should
be named in the methodology paper.

## 8. Human Authority

Finding: human authority remained visible and consequential.

Evidence:

- The human scholar approved corpus acquisition, derivative use of `SRC-0011`,
  thesis lock, drafting, publication package preparation, public working-paper
  release, and landing-page update.
- The AI stopped at corpus, thesis, and publication gates.
- Publication approval was recorded as a human intervention before outputs were
  committed and pushed.

Interpretation:

The case supports the boundary rule: AI may produce or transform artifacts, but
the human scholar determines whether they count as scholarly knowledge or may
be publicly released.

Limit:

All recorded interventions are marked accepted. The record therefore provides
weak evidence about how the system handles rejected human decisions or rejected
AI proposals. Future cases should log rejected and deferred recommendations as
carefully as accepted ones.

## 9. Reproducibility

Finding: technical reproducibility was strong for project validation and
rendering, but source reproducibility still depends on external repositories.

Evidence:

- `python -m lincoln_research validate` and `pytest` were run at major gates.
- Publication outputs were rendered with Quarto.
- The reproducibility report records commands and software versions.
- Source acquisition scripts exist for repeatable fetching and normalization.

Limit:

Some sources depend on external websites, access rules, OCR services, or
repository availability. Reproducible local transformation does not guarantee
future availability of external source pages.

## 10. Methodological Claims Supported by This Case

Supported:

- A governed artifact chain improves auditability of scholarly claims.
- Human gates prevent AI from silently settling corpus, thesis, and publication
  decisions.
- Adversarial review can narrow overbroad interpretive language before public
  release.
- Explicit uncertainty records preserve source limits rather than hiding them.
- Reproducibility checks are valuable but do not validate interpretation.

Partially supported:

- The method improves efficiency. It clearly accelerated repetitive structuring
  and review work, but added documentation and maintenance burden.
- The method improves reliability. It caught several errors, but it still
  depended on human transcription, source judgment, and publication decisions.

Not established:

- General applicability beyond this one humanities case.
- Adequacy for journal-final scholarship without deeper secondary-source
  engagement.
- Robustness when the human scholar rejects major AI recommendations, since the
  intervention log currently records accepted interventions only.

## Required Human Review Questions

The scholar should approve, revise, or reject these findings before
methodology-paper drafting:

1. Are the counts and examples accurate enough to serve as case-study evidence?
2. Is the burden finding too mild, too strong, or fair?
3. Should the methodology paper characterize the historical output as a
   working paper, a case artifact, or both?
4. Should the accepted-only intervention log be treated as a limitation or as
   an artifact of the project's collaborative style?

## Stop

Methodology-findings approval gate cleared on 2026-07-16.
