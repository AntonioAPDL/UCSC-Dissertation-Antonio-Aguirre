# Final controlling plan for reader-first dissertation restructuring

**Status:** approved and implemented on 2026-10-08. This file remains the
controlling execution specification and historical decision record; the
realized architecture, validation evidence, and remaining author/institutional
gates are recorded in `reader-first-restructure-implementation.md`.

**Plan version:** 3.0 (final planning revision)

**Prepared:** 2026-10-08

**Planning baseline:** Git commit
fcb2ca5723a7411e12f677e308dfdd6aed06e93e on main, equal to origin/main and
clean after a fresh fetch when this revision began.

**Scientific-content baseline:** Git commit
0c394122549e903b19edc8014709a6f4318bee26. Later commits through the planning
baseline contain documentation and an Overleaf-originated executable-bit
change, but no later scientific-content revision.

**Accepted before-state artifact:** build/release-20260916T081243Z/main.pdf,
344 US Letter pages, SHA-256
30b4e0bb3c3230544e941f7eae82dcabb44f08e9283ae9809aaade45196c9900.

**Authority:** this document supersedes versions 1 and 2 of the
reader-first-restructure plan. Git history retains those proposals; no second
active plan should be created. Once approved, this file is the controlling
operational specification. It does not supersede institutional requirements,
immutable source-import history, research-repository provenance, claim
qualifications, or supported scientific decisions.

**Change control after approval:** implementation may fill planned records and
record ordinary local choices without rewriting this plan. A material
departure in architecture, scientific placement, source snapshot, evidence
boundary, accessibility route, or merge policy requires a dated decision in
docs/research-decisions.md, the approving authority, the reason, and the
affected gates. Do not respond to a new issue by creating another overlapping
master plan.

## 1. Executive decision

The optimal next step is not to rewrite the dissertation and not to shorten it
by deleting technical material. It is to reorganize the existing
manuscript-first dissertation into two complementary reading layers:

1. a coherent main body containing the scientific questions, inferential
   targets, essential model definitions, contributions, primary evidence,
   interpretation, and limitations; and
2. substantial dissertation appendices containing the proofs, full
   derivations, posterior blocks, detailed algorithms, secondary diagnostic
   evidence, and other material needed for specialist verification.

The versioned research repositories remain the authority for code, data,
fitted objects, complete experiment output, and computational regeneration.
The thesis remains self-contained as a document, but it does not become a
duplicate computational archive.

This recommendation implements the advisors' request while preserving the
earlier manuscript-first strategy. Existing article and supplement prose is
the source material. It will be moved, merged, and edited in controlled units;
the chapters will not be recreated from a blank page.

The four-project research architecture remains appropriate:

1. exDQLM software and computational workflow;
2. source-aware hydrologic correction and synthesis;
3. Bayesian quantile deep echo-state networks;
4. mean-preserving and mean-tilted intervals.

Four research chapters exceed the program's stated minimum of three chapters
suitable for publication. The restructuring changes presentation, not the
number or identity of the research projects.

Implementation should begin only after this plan is approved. The first
implementation milestone is validator and migration-map infrastructure, not a
large prose move. No partially migrated dissertation should be merged to main.

### 1.1 Final audit conclusion

Version 2 chose the correct scientific architecture. This final audit changes
execution details that materially improve safety and efficiency:

1. freeze the intended research-source snapshots before restructuring, rather
   than silently following newer repository heads;
2. correct current operational documentation immediately after approval, so
   Codex does not receive simultaneous body-only and appendix-based
   instructions;
3. validate the active TeX project with both a static dependency scan and the
   compiler's recorded file list, because the current manuscript contains a
   macro-expanded input that a literal recursive scanner cannot resolve;
4. map structural units, not every unchanged paragraph, while applying
   paragraph-level review to units that are split, merged, condensed, or
   scientifically high risk;
5. perform an accessibility feasibility spike before large content movement,
   while retaining the accepted pdfLaTeX build as a visual regression baseline;
6. use one remote integration branch with small atomic commits and milestone
   review packets, keeping main and Overleaf coherent until the complete
   restructuring passes; and
7. make authority, stop conditions, and change control explicit.

The critical path is therefore:

| Order | Work | Why it precedes the next step |
| --- | --- | --- |
| 1 | Approval, source freeze, Git/Overleaf freeze, and current-documentation reconciliation | Establishes one truthful instruction state. |
| 2 | Validator repair and accessibility feasibility | Prevents invisible appendix faults and a late filing-toolchain surprise. |
| 3 | Exhaustive structural migration map | Makes every move reviewable before prose changes. |
| 4 | Appendix skeleton and Chapter 3 pilot | Tests numbering, provenance, tooling, and reader flow on the lowest-risk chapter. |
| 5 | Compatibility audit and Chapters 2, 4, and 5 | Scales only a demonstrated process, with Chapter 4 and theorem/proof work isolated into risk-sized commits. |
| 6 | Global narrative, documentation, accessibility, and release audit | Finalizes cross-project flow after locations are stable. |
| 7 | Complete merge and Overleaf verification | Publishes only one coherent state. |

After approval, further planning is not a phase. Codex should execute this
critical path and stop only at the decision boundaries specified below.

### 1.2 Authority and decision ownership

When instructions conflict, apply this order:

1. current University and program requirements;
2. approved committee/advisor scientific direction and the author's factual
   decisions;
3. fixed-source evidence, claim qualifications, and rights constraints;
4. this operational plan;
5. current supporting documentation;
6. historical planning and audit statements.

A lower level may explain but cannot silently override a higher level.

| Decision or task | Primary authority | Codex role |
| --- | --- | --- |
| Scientific meaning, intended emphasis, candidate contribution | Author and advisors, grounded in source evidence | Diagnose, propose, preserve uncertainty, and stop when an ambiguity changes a claim. |
| Chapter architecture and whether exDQLM counts as an independent unit | Advisors/program | Implement the approved four-chapter design; do not assert program acceptance. |
| Structural placement under approved rules | Codex, subject to author review gates | Execute autonomously, validate, and document exceptions. |
| Source version replacement | Author, with provenance evidence | Keep current fixed commits unless a replacement is explicitly selected and audited. |
| Theorem, target, numerical, or attribution correction | Source evidence plus author/advisor review | Isolate from structural edits and obtain approval. |
| Reuse permission and publication status | Author, coauthors, publishers, committee as applicable | Track; never infer from repository access or distribution. |
| Filing and accessibility acceptance | UCSC Graduate Division and applicable checker/reviewer | Implement and test candidate output; never claim institutional approval. |
| Administrative metadata and official name spelling | Author and university record | Preserve placeholders until supplied. |

The scholarly name remains Antonio de Leon. The official long name remains
Jose Antonio Aguirre Perez de Leon, subject to the exact university-record
spelling and diacritics.

### 1.3 Efficiency constraints

Comprehensiveness must not become unnecessary work. Implementation should:

- reuse the completed eight-source audit and fixed commits instead of
  rescanning the account or following newer heads;
- generate inventories and review summaries from authoritative JSON rather
  than maintaining duplicate hand-written reports;
- apply intensive paragraph review only to moved, condensed, merged,
  omitted, claim-bearing, or high-risk content;
- run focused and fast checks during editing, chapter-tier builds at completed
  chapter/appendix milestones, and a clean full release only at release gates;
- render affected transitions and high-risk pages during milestones, reserving
  systematic whole-document inspection for the final candidate;
- move existing prose before rewriting it, then edit only enough to restore
  coherent dissertation flow;
- avoid research recomputation unless a concrete scientific uncertainty
  cannot be resolved from the audited evidence and the author separately
  authorizes the targeted check;
- update existing authoritative documentation instead of creating parallel
  plans or status reports.

These constraints reduce work without reducing scientific or filing controls.

## 2. Audit basis and current state

### 2.1 Repository and artifact state

The current thesis is a mature imported-and-revised dissertation, not a
starter template:

- Chapters 2--5 were imported from fixed research-source commits, integrated
  from main articles and selected supplement material, and then revised as
  dissertation chapters.
- Nine source manuscripts are represented by 102 import records.
- The source/import baseline is immutable. Current editable derivatives are
  tracked separately in docs/revision-ledger.json.
- The scholarly audit records 29 editorial issues, 97 display decisions, and
  11 bibliography-reconciliation groups.
- The accepted release has 398 unique labels and 118 cited bibliography keys.
- The accepted PDF passed the recorded 2026-09-16 technical and rendered-page
  review, including fonts, page size, margins, references, citations, and
  display placement under the then-current requirements.
- The current main.tex contains Chapters 1--6 followed directly by the
  consolidated bibliography. It does not activate dissertation appendices.
- appendices/a-format-demonstration.tex remains tracked but inactive. It is a
  template-era demonstration, not scientific appendix content.

The accepted artifact is the comparison baseline even if an ordinary build
directory contains a newer or stale local PDF. All before/after comparisons
must use the exact accepted artifact and hash above.

### 2.2 Validation, build, and documentation state

The final planning audit verified the following facts:

- main and origin/main both pointed to the planning baseline after a fresh
  fetch; the worktree was clean;
- the accepted PDF still matches its recorded SHA-256, has 344 US Letter
  pages, is unencrypted, and reports Tagged: no;
- the local production engine is pdfTeX from TeX Live 2018;
- the build script does not currently request TeX's recorder output, and the
  retained builds contain no main.fls dependency record;
- the source uses 36 includegraphics occurrences and 13 figalt occurrences
  across the manuscript tree, while figalt is currently a no-op; occurrence
  counts are not a claim that 13 unique active figures have usable
  alternative text;
- Chapter 4 includes a table through a macro-defined path. A scanner limited
  to literal input arguments cannot prove the full active dependency graph;
- fast validation currently passes for eight audited sources, 32 claim records,
  29 editorial issues, 97 display decisions, 11 bibliography groups, 102
  imported records, 398 unique labels, and 118 cited keys; and
- eight fixed audit clones remain recorded in the ignored local manifest, but
  the research snapshots should not be refreshed or replaced without a new
  author decision.

The current documentation also contains expected historical drift:

- README.md, docs/chapter-plan.md, and
  docs/manuscript-integration-plan.md still present body-only integration as
  the current placement rule;
- source-manifest.json still describes scientific integration as in progress
  and its author-direction integration mode still says supplement material is
  integrated into chapter sections;
- the structured compliance JSON retains starter-era statuses such as an
  absent abstract and demonstration-only appendix even where the Markdown and
  current thesis have advanced;
- the requirements report and compliance matrix predate the current UCSC
  WCAG 2.1 AA filing notice; and
- the status file's older “Next task” section does not include the newly
  approved advisor-directed restructuring.

These are documentation defects, not evidence that the accepted scientific
content changed. Once this plan is approved, the current operational portions
must be reconciled before content movement. Historical descriptions should be
kept as dated history or in Git, not left as competing instructions.

### 2.3 Current scale

| Unit | Approximate words | Current PDF pages | Structural diagnosis |
| --- | ---: | ---: | --- |
| Chapter 1 | 2,561 | 12 | Strong target-first framing; some general computation and evidence language is repeated locally and in Chapter 6. |
| Chapter 2 | 13,843 | 64 | The software contribution is central, but posterior blocks, LDVB derivations, prior updates, and detailed diagnostics interrupt the software workflow. |
| Chapter 3 | 9,078 | 45 | The source/horizon contract and hydrologic findings are central; expanded matrices, complete algorithms, parameter summaries, and extra cutoff panels are mainly verification material. |
| Chapter 4 | 16,693 | 97 | The longest chapter combines the Q--DESN contribution and applications with a full Gaussian baseline, MCMC/VB algebra, ELBO detail, multistep derivations, and extensive sensitivity work. |
| Chapter 5 | 14,217 | 78 | Central interval targets and theorem statements coexist with seven proofs, repeated score derivations, TCSP mechanics, and extensive proposed-extension calculations. |
| Chapter 6 | 2,376 | 11 | The comparison is useful, but some project recap repeats chapter conclusions and Chapter 1 qualifications. |

The four research chapters occupy about 284 pages. Length alone is not the
problem. The problem is that the primary scientific path repeatedly pauses for
technical verification layers before returning to the contribution or result.

### 2.4 What the repetition actually is

The audit did not find widespread paragraph-level copying. The principal
repetition is conceptual, functional, and organizational:

- conditional quantiles, AL/exAL working likelihoods, generalized updating,
  predictive uncertainty, and tolerance distinctions are explained at several
  levels;
- MCMC, VB/LDVB, shrinkage, scoring, and calibration are introduced globally
  and reintroduced within individual projects;
- a concise model statement is often followed immediately by full
  augmentation, conditional distributions, algorithmic details, and
  diagnostics before the scientific argument resumes;
- Chapter 5 repeats closely related MPI/MTI definitions across theory,
  score-derivation, proof, and computation blocks;
- introductions, chapter conclusions, limitations, and synthesis sometimes
  perform the same recap instead of having distinct rhetorical jobs; and
- article and supplement integration correctly preserved evidence but did not
  yet impose the reader hierarchy now requested by the advisors.

Arbitrary page cutting would therefore fail. Every repeated idea needs one
authoritative home, and each other occurrence needs either a short local
reminder, a project-specific distinction, or removal as a documented
duplicate.

### 2.5 Existing strengths that must not be disturbed

The restructuring must preserve:

- the target-first distinction among conditional quantiles, synthesized
  response distributions, loss-defined endpoints, and tolerance actions;
- the distinction among ordinary likelihood, working likelihood, and
  generalized updating;
- inherited-method attribution and collective/coauthor attribution;
- negative and mixed findings, including transfer failures or uneven
  improvements;
- the exact application windows, horizons, source roles, sample sizes, and
  version qualifications already audited;
- the bounded status of TCSP, including the absent exact scan recursion and
  action-matched finite-sample proof;
- the proposed and currently unimplemented status of the MTI regression and
  dynamic extensions;
- the external-computation boundary;
- the consolidated bibliography;
- the immutable source and import hashes; and
- the unresolved material-specific reuse, publication, authorship,
  administrative, and committee decisions.

## 3. Diagnosis of the previous plan

### 3.1 Decisions that remain correct

The previous plan correctly concluded that:

- the four research chapters should remain in their current scientific order;
- existing article and supplement prose should be reused rather than replaced
  by a from-scratch rewrite;
- the body should retain targets, contributions, primary results,
  interpretations, and limitations;
- technical appendices may be long when that improves the main reading path;
- code, data, fitted objects, and full computations should remain in the
  research repositories;
- primary displays should stay near the claims they establish, while secondary
  checks may move;
- movement should be recorded at a unit level and performed in recoverable
  commits;
- Chapter 3 is the safest pilot and Chapters 4 and 5 carry the greatest
  structural risk; and
- bibliography placement must remain after the appendices.

These conclusions are retained.

### 3.2 Earlier decisions that are now superseded

The advisors' direction supersedes the prior rules that:

- there should be no scientific appendices;
- all claim-relevant supplement material should remain beside the main result
  in the chapter body; and
- technical material is considered fully integrated only when it remains in a
  research-chapter file.

Supplement-derived content may now be integrated into a dissertation appendix
when its conclusion remains visible in the body and the appendix contains the
recoverable support. Moving content to an appendix does not restore a
publisher-style supplement. The appendices are part of the dissertation.

### 3.3 Gaps in version 1 that must be corrected

Version 1 established the right editorial direction but was not safe enough to
execute without additional design. The deeper audit found six material gaps.

#### Gap 1: active appendices would be partly invisible to validation

scripts/validate_manuscript_imports.py currently scans the four research
chapter files and TeX fragments under tables and figures. It does not discover
the active TeX graph from main.tex and would not automatically scan new
appendix files.

scripts/validate_editorial_audit.py likewise seeds display discovery from the
four research chapter files. A display moved from a chapter into an appendix
could therefore be reported as absent even though it remains in the
dissertation, or an appendix problem could escape the scan.

scripts/validate.sh runs only one named unit-test file. New appendix-validator
tests would not run automatically unless the test command is extended.

This must be fixed before any content is moved.

#### Gap 2: provenance after a chapter/appendix split was underspecified

The immutable import manifests correctly describe the original destination
files. New appendices are derivative locations, not new source imports.
Regenerating or rewriting import history would be wrong, but leaving appendix
files outside the revision ledger would also be wrong.

The plan therefore needs a backwards-compatible derivative model: preserve all
baseline fields and hashes, record current body and appendix components, and
represent newly created appendix files as derived dissertation artifacts.

#### Gap 3: Appendix A could silently conflate nonidentical conventions

The projects use related but not always identical notation and
parameterizations:

- Chapters 2 and 4 use an AL/exAL mixture with a latent exponential variable
  expressed on the response scale.
- Chapter 3 uses a unit-rate latent exponential representation whose variance
  has an additional scale factor. The representations can be equivalent under
  an explicit change of variable, but they must not be treated as identical
  without documenting that map.
- Q--DESN has branch-specific derivative and regularity conventions.
- Chapter 3 uses an empirical full-CRPS approximation, whereas Chapter 4 uses
  a finite-grid or truncated aCRPS construction with quadrature weights.
- Chapter 5's pseudo-AL device is a computational identity for a product
  residual, not a response likelihood.

Appendix A must therefore be a carefully audited concordance, not a universal
model into which superficially similar equations are merged.

#### Gap 4: display disposition and physical placement are different decisions

The existing display ledger records KEEP, MERGE, TEXT-SUMMARY, and OMIT
decisions from the scholarly revision. Those decisions answer whether and how
a source display survives. They do not answer whether the surviving display
belongs in the body or an appendix.

The earlier ledger must remain historically intact. Body/appendix placement
needs a separate field in the new migration map, linked to the existing
display identifier.

#### Gap 5: page ranges were too prominent

The earlier suggested page bands are useful diagnostics, but they must not
become acceptance criteria. A fixed page target before the pilot could
encourage unjustified compression. The body-only and recovery tests are the
real acceptance conditions. Page counts should be recorded after the pilot and
used to detect imbalance, not to force a quota.

#### Gap 6: current filing accessibility was not incorporated

The current UCSC Graduate Division applications-and-forms page states that,
as of April 2026, all electronic theses and dissertations must conform to WCAG
2.1 AA before submission. The current accepted PDF reports Tagged: no. The
current figalt helper is a no-op, and the source has more graphics inclusions
than meaningful alternative-text declarations.

This does not invalidate the scientific release audit performed in September.
It means the repository's requirements investigation is now stale for the
filing environment and the current PDF must not be described as filing-ready.
Accessibility is a parallel release requirement, not a reason to delay the
reader-first structural plan, but its feasibility must be tested early enough
to avoid an end-stage toolchain crisis.

Official references:

- [UCSC Graduate Division applications and forms](https://graduate.ucsc.edu/academics/applications-and-forms/)
- [UCSC Statistical Science Ph.D. catalog](https://catalog.ucsc.edu/en/2024-2025/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd)

### 3.4 Final corrections to version 2

Version 2 resolved the six gaps above but left six execution ambiguities.
Version 3 closes them as follows.

| Version-2 ambiguity | Final resolution |
| --- | --- |
| Recursive scanning was described only at the source level. | Use a hybrid graph: static pre-build discovery plus project-local files recorded by TeX's recorder after a build. Dynamic macro inputs must be visible in the recorded graph or explicitly rejected. |
| The migration map could be read as requiring paragraph-by-paragraph bureaucracy. | Require complete coverage of structural units and labeled objects; create paragraph records only for split, merge, omission, high-risk, or claim-bearing edits. |
| Stale current documentation was scheduled too late. | Immediately after approval, mark the final plan controlling and reconcile current instruction/status fields; update location-specific facts incrementally as moves occur. |
| Accessibility feasibility was deferred conceptually. | Run an early disposable dual-toolchain spike using current official LaTeX/Overleaf guidance, while keeping pdfLaTeX as the accepted visual baseline until a candidate route proves compatible. |
| Source-version stability was implicit. | Freeze the eight audited commits as the restructuring sources unless the author explicitly selects and audits a replacement. |
| Review and Git ownership were not precise enough. | Define author/advisor/institutional decision ownership, milestone review packets, one shared integration branch, no rebase after publishing it, and one complete merge to main. |

These corrections make the plan executable without changing its scientific
architecture.

## 4. Reader contract and nonnegotiable scientific rules

### 4.1 Body-only contract

A statistically literate reader who skips all appendices must still be able to
answer, for every project:

1. What is the scientific or statistical problem?
2. What is the inferential target and conditioning information?
3. Which model, loss, or update defines the method?
4. What is newly contributed and what is inherited?
5. At a conceptual level, how is the method computed and checked?
6. What evidence directly supports the principal claims?
7. Which negative findings, assumptions, limitations, and unresolved issues
   constrain the conclusion?

The body must not require an appendix to learn the primary result, discover a
material caveat, understand the meaning of an interval, or determine whether a
method was implemented.

### 4.2 Recovery contract

A specialist following an appendix pointer must be able to recover:

- the complete proof or derivation;
- all assumptions and parameterizations needed to interpret it;
- the full algorithm or update equations;
- the secondary diagnostic or sensitivity evidence summarized in the body;
- the source/provenance identity of the material; and
- the exact body claim or section supported.

An appendix is not a storage bin. Its ordering should parallel the parent
chapter, and each appendix section should name the body section it supports.

### 4.3 Scientific invariants

Structural editing must not silently change:

- a target, conditioning set, likelihood interpretation, loss, learning rate,
  or interval type;
- a theorem, assumption, proof obligation, or claimed guarantee;
- a numerical value, sample definition, forecast origin, horizon, or data
  source;
- a contribution, attribution, publication status, or reuse status;
- a positive, negative, or mixed empirical conclusion; or
- the boundary between implemented evidence and proposed work.

Any genuine correction discovered during restructuring must stop the local
move, be documented as a separate scientific correction, be checked against
the authoritative research source, and receive its own review and revision
record.

## 5. Target architecture

### 5.1 Main body

The existing six-chapter order remains:

1. Introduction and common framework.
2. exDQLM software and computational workflow.
3. Source-aware hydrologic correction and synthesis.
4. Bayesian quantile deep echo-state networks.
5. Mean-preserving and mean-tilted intervals.
6. Synthesis, limitations, and future work.

The research chapters remain independent contributions. Chapter 1 supplies
shared interpretive concepts. Chapter 6 compares the contributions instead of
repeating their abstracts.

### 5.2 Appendices

The proposed active file structure is:

| Appendix | Proposed file | Role |
| --- | --- | --- |
| A | appendices/a-shared-conventions.tex | Concordance and only those reusable conventions shown to be compatible. |
| B | appendices/b-exdqlm-technical.tex | Technical details supporting Chapter 2. |
| C | appendices/c-hydrology-technical.tex | Technical details and secondary evidence supporting Chapter 3. |
| D | appendices/d-qdesn-technical.tex | Technical details and secondary evidence supporting Chapter 4. |
| E | appendices/e-mti-technical.tex | Proofs, computation, and secondary evidence supporting Chapter 5. |

The document order becomes front matter, Chapters 1--6, Appendices A--E, and
the single consolidated bibliography.

Use one top-level file per appendix initially. Add subfiles only if an appendix
becomes genuinely unmanageable. Reuse the existing tracked table and figure
inputs rather than duplicating them under appendix directories.

The inactive formatting demonstration should be removed only after real
appendices demonstrate the required theorem, equation, figure, table, and
algorithm formatting. Git history makes its removal recoverable.

### 5.3 Appendix A compatibility gate

Appendix A should begin as a concordance and notation map. A convention may be
centralized only if the implementation records one of the following:

- textual and mathematical identity across consumers;
- an explicit invertible reparameterization, including scale and rate
  conventions; or
- a deliberately generic definition followed by unambiguous project-specific
  specializations.

If equivalence cannot be demonstrated cleanly, retain the exact definition in
the relevant project appendix and let Appendix A point to it. In particular:

- document the latent-variable change of scale between the Chapter 3 and
  Chapters 2/4 AL representations before consolidating them;
- keep full-CRPS and finite-grid aCRPS definitions distinct;
- keep Q--DESN derivative conventions local when branch-specific;
- keep the Chapter 5 pseudo-AL computational identity separate from a response
  working likelihood; and
- provide a role table that distinguishes the quantile level, interval
  content, and generalized-update learning rate even where source manuscripts
  reused similar symbols.

## 6. Chapter-level migration specification

This section defines the initial disposition hypothesis. The migration map,
not this prose summary, will hold the final unit-by-unit decision.

### 6.1 Chapter 1: common framework

Retain in the body:

- the unifying research question;
- target-first distinctions;
- update-type and uncertainty-object distinctions;
- the contribution/evidence map;
- the external computation and provenance boundary; and
- the roadmap to the four projects.

Condense only after Chapters 2--5 have stable boundaries:

- generic descriptions of MCMC and variational approximation;
- generic scoring language repeated in project chapters;
- repeated evidence-hierarchy qualifications; and
- organization text that no longer matches the final appendix structure.

Do not move the conceptual distinction among working likelihood, ordinary
Bayes, generalized Bayes, predictive distribution, confidence, credibility,
and tolerance. Those ideas are necessary for every body-only reading.

### 6.2 Chapter 2 and Appendix B: exDQLM

Retain in the body:

- the software research contribution and version boundary;
- a concise exDQLM specification and its inferential interpretation;
- package architecture when it is part of the contribution;
- model-building, fitting, forecasting, and diagnostic workflow;
- the primary examples and their conclusions;
- the held-out negative or mixed result;
- implementation limitations and scope.

Move or condense into Appendix B:

- exact distributional conventions not safely centralized in Appendix A;
- complete latent representations and posterior target blocks;
- the four detailed posterior-update subsections;
- nonconjugate backend algebra;
- LDVB scale and skewness derivations;
- regularized-horseshoe update details;
- detailed forecasting, diagnostic, and synthesis formulas beyond the
  conceptual workflow;
- secondary API or implementation detail not needed to establish the software
  research claim.

Safeguard: this is a software-centered research chapter. Its architecture,
interface contract, and analysis workflow are substantive content and must not
be removed wholesale merely because they resemble documentation.

### 6.3 Chapter 3 and Appendix C: hydrologic application

Retain in the body:

- hydrologic motivation and decision context;
- distinct roles of observations, retrospectives, issued ensembles, and
  forecast covariates;
- the source and horizon contract;
- a concise source-aware state-space model;
- why and how transfer information is introduced;
- a conceptual computation and distribution-synthesis summary;
- the five-origin design and the distinct 28-day and common 8-day comparisons;
- principal evidence, including mixed findings;
- deterministic-future-covariate and operational-evidence limitations.

Move or condense into Appendix C:

- expanded state and design matrices;
- full MCMC and VB algorithms;
- complete source-parameter summaries;
- component-removal details;
- extra cutoff panels;
- secondary sensitivity evidence;
- detailed feasibility and calibration mechanics.

Safeguard: at least one representative synthesis display remains in the body,
and the body states the conclusion from every moved origin or diagnostic. No
movement may blur posterior predictive bands, credible intervals for latent
quantile curves, and parameter uncertainty.

Chapter 3 is the pilot because its body/appendix boundary is comparatively
clear. The pilot must validate the process before it becomes the pattern for
the larger chapters.

### 6.4 Chapter 4 and Appendix D: Q--DESN

Retain in the body:

- motivation, inferential target, and information set;
- reservoir construction at the level needed to define the fixed-feature
  contract;
- central single-level and joint-quantile model equations;
- prior structure at a conceptual level;
- why MCMC and VB--LD are used and what their approximation boundaries are;
- primary simulation results;
- principal GloFAS and PriceFM evidence;
- crossing, future-input, fixed-root, cap-stabilization, and computational
  qualifications.

Move or condense into Appendix D:

- local distributional algebra not centralized in Appendix A;
- global-shrinkage calibration derivations;
- the full Gaussian-DESN baseline, completing-the-square calculation, exact
  posterior, marginal likelihood, alternative-prior calculation, and
  initialization details;
- all MCMC full conditionals;
- detailed VB--LD, Laplace, delta-method, and ELBO calculations;
- stacked joint-design derivations;
- multistep recursion and rearrangement mechanics;
- simulation diagnostics and secondary sensitivity work;
- the full GloFAS latent-path ensemble likelihood and Laplace--delta path
  calculation;
- secondary PriceFM sensitivity detail.

Safeguards:

- explain the Gaussian baseline's scientific role in the body before pointing
  to its derivation;
- retain the body conclusion supported by every moved diagnostic;
- preserve the distinction between fixed reservoir features and posterior
  uncertainty;
- preserve the status and limits of VB--LD comparisons;
- do not let removal of formulas hide the assumptions behind future-input
  handling or quantile rearrangement.

Chapter 4 is the largest and highest-risk migration. It should use separate
validated subcommits for the Gaussian baseline, inference, joint/forecast
machinery, and application/sensitivity details within the same review branch.

### 6.5 Chapter 5 and Appendix E: MPI/MTI

Retain in the body:

- the interval-target taxonomy;
- MPI and MTI definitions;
- assumptions and formal statements of all principal theorems, propositions,
  and corollaries;
- interpretation of mean-preserving and mean-tilted paths;
- the TCSP action and principal validation evidence;
- the main pharmaceutical illustration;
- concise, explicitly proposed statements of regression and dynamic endpoint
  extensions;
- all limitations distinguishing tolerance, prediction, posterior content,
  confidence, and generalized endpoint uncertainty.

Move or condense into Appendix E:

- endpoint-score derivations;
- complete proofs;
- convex-order and interval-path calculations;
- restricted-score equations;
- Cornish--Fisher derivations;
- empirical-balance proofs;
- the direct DP content-law proof;
- detailed MTI-ECM calculations;
- TCSP calibration, protocol, and feasibility mechanics;
- secondary pharmaceutical responses and sensitivities;
- complete pseudo-AL augmentation and Gaussian-root updates;
- shrinkage, basis-expansion, and dynamic-state derivations;
- detailed diagnostic specifications.

Safeguards:

- every theorem statement retains the assumptions needed to understand its
  scope;
- each moved proof has an explicit statement-to-proof link and no orphaned
  notation;
- the body retains TCSP limitations and does not imply a missing exact
  guarantee;
- proposed extensions remain labeled proposed and unvalidated;
- the pseudo-AL calculation is not redescribed as a generative response
  likelihood;
- the inherited sign correction already made remains intact.

### 6.6 Chapter 6: synthesis

Retain:

- the comparative table;
- what is learned only by considering all four projects together;
- common limitations and concrete future research;
- the distinction among the four inferential targets.

Condense:

- project-by-project miniature abstracts;
- qualifications already stated adequately in the responsible chapter;
- repeated Chapter 1 definitions.

Chapter 6 should synthesize tensions and common lessons rather than serve as a
second set of chapter conclusions.

## 7. Canonical-home map

| Concept | Authoritative narrative home | Treatment elsewhere |
| --- | --- | --- |
| Conditional quantile, check loss, and information set | Chapter 1 | One local reminder plus the project-specific target. |
| Credible, predictive, confidence, and tolerance distinctions | Chapter 1 | State the local distinction only where it changes interpretation. |
| Working likelihood, response model, and generalized update | Chapter 1 | Each project declares its actual status; no repeated tutorial. |
| Compatible AL/exAL latent conventions | Appendix A after equivalence review | Body retains the central model meaning; local appendix retains non-equivalent details. |
| CRPS and aCRPS variants | Project body or appendix according to use | Do not merge formulas with different empirical or grid meanings. |
| exDQLM foundations and version graph | Chapter 2 | Chapter 3 states only source-specific modifications and the pinned dependency. |
| Reservoir feature construction | Chapter 4 | Other chapters refer only to their distinct deterministic-basis use. |
| Generic MCMC/VB interpretation | Chapter 1 | Bodies state why the method is used and what was checked; appendices hold updates. |
| Project-specific algorithms | Project appendix | Body gives purpose, inputs, outputs, and approximation boundary. |
| Evidence hierarchy | Chapter 1 | Chapters state achieved evidence; Chapter 6 compares implications. |
| Negative and mixed findings | Responsible research chapter | Chapter 6 synthesizes their consequences without repeating inventories. |
| Source and external-computation boundary | Chapter 1 and repository documentation | Local chapters state only material version dependencies. |
| Complete proofs | Project appendix | Body retains assumptions, statements, interpretation, and limitations. |

This map governs paragraph-level editing. A cross-reference does not replace a
locally intelligible sentence, but a local reminder must not grow into another
general methods review.

## 8. Unit-level decision grammar

Every active section, subsection, proof, algorithm, labeled equation group,
figure, and table receives exactly one structural disposition:

| Decision | Meaning | Required action |
| --- | --- | --- |
| KEEP_BODY | Necessary for the main scientific argument | Retain and edit for flow; remove redundant reintroductions. |
| CONDENSE_BODY | Central but over-detailed | Keep target, assumptions, key equation/result, interpretation, and topical appendix pointer. |
| MOVE_APPENDIX | Verification or specialist detail | Move rather than copy; preserve semantic labels and add a body bridge. |
| SPLIT_BODY_APPENDIX | One unit contains both narrative and technical layers | Retain a complete body summary and move the delimited technical support. |
| MERGE_CANONICAL | Repeats a concept with another unit | Choose one home and preserve all unique qualifications. |
| EXTERNAL_ONLY | Code, data, fitted object, full output, or operational detail | Retain an exact provenance pointer; do not import the object. |
| OMIT_DUPLICATE | Superseded or genuinely redundant | Require rationale, no-loss review, and dependency check. |

Default decisions:

- theorem and proposition statements stay in the body; full proofs move unless
  a short proof is itself essential exposition;
- central model equations stay in the body; augmentations, full conditionals,
  block algebra, and numerical-stability derivations move;
- the body explains an algorithm's purpose, inputs, outputs, and approximation
  status; full pseudocode and update equations move;
- primary claim-defining figures and tables stay; secondary sensitivities,
  parameter summaries, extra origins, and diagnostic panels may move;
- material caveats remain adjacent to the claim they constrain;
- moved technical material is removed from the body rather than duplicated;
- unique supplement evidence is never deleted merely because it is not
  primary;
- no content is omitted on page-count grounds.

## 9. Migration-map design

### 9.1 New durable record

Create docs/appendix-migration-map.json before moving content. Its schema
should have a plan identifier, scientific baseline commit, implementation
branch, source release artifact/hash, validation version, and records array.

The unit of coverage is deliberately structural:

- one record for each section or subsection;
- one record for each theorem/proof pair, algorithm, labeled equation group,
  figure, and table;
- one record for a contiguous block that will be split or merged; and
- a paragraph-level record only when that paragraph carries a claim, caveat,
  attribution, numerical result, omission, or cross-unit merge.

Unchanged connective paragraphs inherit their enclosing structural record.
This keeps the map exhaustive without turning it into an expensive duplicate
of the manuscript.

Each record should contain:

- stable migration identifier;
- chapter/project identifier;
- current file and a stable heading or label anchor;
- normalized pre-move source-span SHA-256 hash and, after implementation, a
  normalized destination-span hash;
- content kind: section, subsection, proof, algorithm, equation group, figure,
  table, or connective prose;
- scientific role;
- source-manifest and source-document identifiers where applicable;
- linked claim-evidence identifiers;
- linked display-ledger identifiers;
- labels defined and labels referenced;
- citations and file dependencies;
- initial and final structural disposition;
- semantic-change class: NONE, EDITORIAL_ONLY, or
  SCIENTIFIC_CORRECTION_REQUIRES_SEPARATE_APPROVAL;
- target file and target section;
- canonical concept home, if merged;
- body-bridge requirement and completion status;
- risk level and reason;
- no-loss review state;
- author/advisor review state;
- implementation commit and validation evidence.

Use heading, label, and normalized-content hashes as locators. Line numbers may
be recorded for convenience but must not be the only locator because they
change after every move.

Generate the initial inventory mechanically from the active TeX graph, then
review and classify it. Do not hand-copy the same map into a second Markdown
report. The validator should emit a concise human-readable summary on demand;
the JSON map is the durable authority.

### 9.2 Coverage and integrity rules

The map validator must fail when:

- a research-chapter unit or active research display is uncovered;
- an identifier, target anchor, or destination is duplicated;
- a target path escapes the repository or uses a machine-specific absolute
  path;
- MOVE_APPENDIX or SPLIT_BODY_APPENDIX lacks a target;
- a claim-relevant move lacks a body bridge;
- OMIT_DUPLICATE lacks a rationale and no-loss approval;
- a high-risk theorem, target, parameterization, or numerical-result move
  lacks review;
- a moved label disappears or becomes multiply defined;
- a mapped source hash no longer matches the pre-move unit without an
  explicitly recorded editorial revision.

The map is an operational safety control, not an additional prose report.

## 10. Validation and provenance changes required before migration

### 10.1 Active TeX dependency traversal

Use a hybrid dependency model.

**Pre-build static closure:** begin at main.tex, follow literal input/include
dependencies, ignore commented commands, detect missing files and cycles, and
flag macro-expanded or otherwise dynamic file arguments. This gives fast
feedback before compilation.

**Post-build recorded closure:** add TeX's recorder option to both latexmk and
the fallback engine path, then parse the generated main.fls. Normalize and
filter entries to the repository root so system packages are not mistaken for
project sources. Compare the recorded project-local inputs with the static
closure and the tracked-file policy.

The combined closure must:

- cover active chapters, appendices, tables, TeX figure fragments, graphics,
  bibliography inputs, and macro-expanded project-local dependencies;
- reject missing active inputs and unexpected absolute or repository-external
  project dependencies;
- avoid scanning inactive template files as though they were compiled;
- supply the active source set for label, reference, citation, path, secret,
  graphics, and display validation; and
- report any dynamic dependency that cannot be demonstrated by an actual
  build.

This is necessary because Chapter 4 currently inputs a score table through a
macro-defined path. A literal recursive parser alone would be incomplete.
The inactive formatting demonstration must not become a false positive;
conversely, a new appendix must not be invisible merely because it is outside
the chapters directory.

### 10.2 Editorial-display validation

Change display discovery from a hard-coded chapter dictionary to the active
research body and appendix graph. Preserve the existing display ledger's
historical KEEP, MERGE, TEXT-SUMMARY, and OMIT decisions.

Physical placement belongs in the migration map. A KEEP display moved to an
appendix remains KEEP and must be recognized as present.

### 10.3 Revision ledger

Evolve docs/revision-ledger.json in a backwards-compatible way:

- preserve the manuscript-first baseline identifier, integration commit, and
  baseline hashes;
- retain existing chapter and bibliography artifacts;
- permit current chapter derivatives to have associated component files;
- add new appendix artifacts with a state such as DERIVED_NEW, current hash,
  revision identifiers, and derived-from paths or project identifiers;
- require every tracked current derivative to have a current hash;
- record each structural milestone as a revision with paths, summary,
  evidence, and validation.

Do not assign a fictional baseline source hash to a newly created appendix.

### 10.4 Import manifests

Keep every immutable source item, source hash, destination hash, and import
baseline unchanged. Add only optional current-derivative metadata, for example:

- current_components listing the body and appendix files that now carry the
  editable derivative; and
- a link to docs/appendix-migration-map.json.

This records current placement without rewriting history.

### 10.5 Claims, displays, and sources

- Keep claim identities and evidence levels unchanged unless a separate
  scientific correction is approved.
- Add current dissertation locations only where required for reliable
  navigation.
- Keep existing display dispositions unchanged; link placement through the
  migration map.
- Update source-manifest integration language from body-only integration to
  body-plus-dissertation-appendix integration, without changing source
  snapshots.
- Do not copy private source prose or assets beyond the already governed
  dissertation derivative without material-specific approval.

### 10.6 Required tests

Add focused automated tests showing that:

1. an active appendix label, citation, and dependency are discovered;
2. a duplicate label split across body and appendix fails;
3. an absolute machine path in an appendix fails;
4. a secret-like credential in an appendix fails;
5. a missing appendix input fails;
6. a moved KEEP display remains recognized;
7. an inactive demonstration file is not treated as active;
8. a migration-map record with a missing target or bridge fails;
9. a DERIVED_NEW appendix artifact validates without altering baseline hashes;
10. a source manifest's current components cannot escape the repository;
11. a macro-expanded active input is present in the recorded closure;
12. an unexpected project-local file in main.fls is reported; and
13. static and recorded dependency results are normalized consistently;
14. every active graphic has exactly one accessibility-ledger record; and
15. accessibility records reject an unresolved final state that lacks alt
    text, actual text, or an artifact decision.

Change scripts/validate.sh from a single named unit-test file to controlled
test discovery or an explicit complete test list, so the new tests cannot be
silently skipped.

This tooling work is a no-content implementation milestone. It must pass
before an appendix skeleton or manuscript move is accepted.

## 11. Exact file-impact matrix for later implementation

No file in this section is to be changed merely because it is listed here.
The table defines the expected implementation scope.

### 11.1 Manuscript structure and prose

| File or group | Intended change |
| --- | --- |
| main.tex | Add appendix mode and Appendices A--E after Chapter 6 and before the bibliography. |
| chapters/01-introduction.tex | Final common-concept deduplication after research boundaries stabilize. |
| chapters/02-research-a.tex | Condense/move exDQLM technical units; repair body flow. |
| chapters/03-research-b.tex | Pilot hydrology migration and body-flow repair. |
| chapters/04-research-c.tex | Staged Q--DESN migration with high-risk parameterization checks. |
| chapters/05-research-d.tex | Move proofs/derivations; preserve theorem and evidence boundaries. |
| chapters/06-synthesis.tex | Replace repeated recap with comparative synthesis after all migrations. |
| appendices/a-shared-conventions.tex | New compatibility-reviewed concordance. |
| appendices/b-exdqlm-technical.tex | New Chapter 2 technical appendix. |
| appendices/c-hydrology-technical.tex | New Chapter 3 technical/evidence appendix. |
| appendices/d-qdesn-technical.tex | New Chapter 4 technical/evidence appendix. |
| appendices/e-mti-technical.tex | New Chapter 5 proofs/computation/evidence appendix. |
| appendices/a-format-demonstration.tex | Remove only after real appendix formatting coverage is verified. |
| notation.tex | Change only for safely equivalent shared notation. |
| preamble.tex | Change only for proven appendix or accessibility infrastructure, not convenience refactoring. |

### 11.2 Validation and tests

| File or group | Intended change |
| --- | --- |
| scripts/validate_manuscript_imports.py | Hybrid static/recorded active graph and appendix-aware safety checks. |
| scripts/validate_editorial_audit.py | Appendix-aware display discovery. |
| scripts/build.sh | Request recorder output in both build paths; preserve the existing project-relative output guard. |
| scripts/validate.sh | Ensure all relevant tests execute. |
| scripts/validate_appendix_migration.py | Add only if a small dedicated validator is clearer than overloading an existing validator. |
| scripts/validate_accessibility_ledger.py | Check active graphic coverage and ledger state; do not present this as a WCAG conformance checker. |
| tests/test_validate_manuscript_imports.py | Add active-graph and appendix safety cases. |
| tests/test_validate_editorial_audit.py | Add moved-display and inactive-file cases. |
| tests/test_validate_appendix_migration.py | Add map-schema and coverage cases if a dedicated validator is created. |
| tests/test_validate_accessibility_ledger.py | Cover active, inactive, duplicate, alt-text, actual-text, and artifact records. |
| tests for dependency recording | Cover literal, macro-expanded, inactive, missing, and escaping inputs. |

Avoid a new validation framework. Reuse existing parsers and conventions where
that remains clear and testable.

### 11.3 Provenance and operational documentation

| File or group | Intended change |
| --- | --- |
| docs/appendix-migration-map.json | New authoritative unit-level placement record. |
| docs/accessibility-ledger.json | New compact inventory of active graphics, tables, structural exceptions, alt/artifact decisions, and remediation/verification status. |
| docs/revision-ledger.json | Add derivative components, appendices, revision hashes, and milestones. |
| docs/imports/*.json | Add current-component and migration-map links only; preserve immutable imports. |
| docs/claim-evidence.json | Add current locations only when needed; do not change evidence strength through relocation. |
| docs/display-ledger.json | Preserve original decisions; add linkage only if necessary. |
| source-manifest.json | Update current integration-mode wording; do not change source commits. |
| docs/research-decisions.md | Record approved appendix architecture and any placement exceptions. |
| docs/STATUS.md | Record phase, gates passed, unresolved decisions, and next action. |
| docs/ASSISTANCE-LOG.md | Record AI-supported planning and each later structural edit. |

### 11.4 Current guidance that will become stale

Immediately after approval, mark the final plan and current requirements as
controlling and mark incompatible body-only instructions as superseded. Then
reconcile location-dependent details incrementally during implementation in:

- README.md;
- docs/chapter-plan.md;
- docs/manuscript-integration-plan.md;
- docs/VALIDATION.md;
- docs/REQUIREMENTS-REPORT.md;
- docs/compliance-matrix.md and docs/compliance-matrix.json;
- docs/research-audit.md where it describes current physical placement;
- docs/research-decisions.md;
- source-manifest.json.

Historical, dated audit statements should not be rewritten as if the past
workflow never occurred. Mark their placement rule as historical or
superseded, and put current instructions in the controlling sections.

docs/WORKFLOW.md needs revision only if the GitHub/Overleaf handoff itself
changes. Do not duplicate that workflow in multiple files.

## 12. Implementation runbook and gates

### Gate P0 — author approval

Approval covers:

- the four-chapter plus five-appendix architecture;
- continued use of the eight audited source commits unless an explicitly
  selected replacement is separately audited;
- the unit-level disposition grammar;
- validator-first sequencing;
- the Appendix A compatibility gate;
- the early accessibility feasibility and later completion workstreams;
- one review branch with small recoverable commits;
- no scientific deletion without an approved no-loss record; and
- the authority, review, and change-control rules in Section 1.

No manuscript change occurs before P0.

### Phase I0 — synchronize and freeze

Actions:

1. Pause or coordinate Overleaf editing under docs/WORKFLOW.md.
2. Preserve Overleaf comments and tracked changes before pulling source.
3. Fetch GitHub and reconcile only by a safe fast-forward or reviewed merge.
4. Require a clean main.
5. Record HEAD, origin/main, accepted PDF path/hash, source-audit root, TeX
   versions, and branch.
6. Create one dedicated remote review branch.
7. Verify, without fetching or changing original research repositories, that
   the eight audited commit objects and retained audit snapshots remain
   available.
8. Record the source freeze. A later default-branch head is discovery
   information, not an automatic replacement.
9. Record this plan as approved in docs/research-decisions.md and
   docs/STATUS.md.
10. Reconcile current instruction-level contradictions: make this plan the
    named controller, mark body-only placement rules superseded, update the
    source-manifest lifecycle status, and update the requirements/compliance
    records for the current WCAG notice. Preserve historical facts.

Gate:

- baseline is exact, clean, reproducible, and documented;
- source snapshots are fixed and available;
- current operational documents no longer direct Codex toward incompatible
  architectures;
- Markdown and JSON compliance records agree on current status; and
- no research-repository working tree has changed.

Stop if main or Overleaf has unreviewed divergence.

### Phase I1 — validation safety without manuscript movement

Actions:

1. Implement the hybrid static/recorded TeX dependency traversal.
2. Make display validation appendix-aware.
3. Implement the migration-map schema and validator.
4. Evolve derivative-ledger validation without altering baseline hashes.
5. Add and run all tests in Section 10.6.
6. On a disposable branch or worktree, run an accessibility feasibility spike
   against a representative subset containing front matter, headings,
   mathematics, a proof, an algorithm, a simple table, a complex table, TikZ,
   and imported graphics.
7. Compare at least the modern pdfLaTeX tagging route and the officially
   recommended LuaLaTeX/MathML route where available. Do not change the
   production engine at this phase.
8. Record class/package incompatibilities, layout/font changes, compilation
   time, and the viable candidate route. Delete no source to make the spike
   pass.

Gate:

- existing dissertation still validates;
- all new positive and negative tests pass;
- accepted PDF content is unchanged;
- the recorded dependency graph includes the current macro-expanded Chapter 4
  input;
- an evidence-backed accessibility candidate route or a precise escalated
  blocker is recorded; and
- production diff contains documentation, tooling, tests, and schema support
  only.

Rollback: revert this isolated tooling commit without touching the manuscript.

### Phase I2 — complete migration map without prose movement

Actions:

1. Generate and review the structural inventory defined in Section 9; do not
   create paragraph records for unchanged connective prose.
2. Build label/reference, citation, display, and file-dependency graphs.
3. Assign proposed dispositions and destinations.
4. Link each unit to claims, displays, and source records.
5. Record required body bridges and high-risk review status.
6. Review all OMIT_DUPLICATE, theorem/proof, target, parameterization, and
   numerical-result decisions.
7. Produce a concise review packet from the map: proposed body outline,
   appendix outline, high-risk decisions, planned omissions, primary-display
   placements, and unresolved items. The JSON map remains authoritative.

Gate:

- 100 percent unit and display coverage;
- zero unresolved dependencies;
- every move has a destination;
- every claim-relevant move has a planned bridge;
- author/advisor approval of high-level placements.

No prose movement is allowed to compensate for an incomplete map.

### Phase I3 — appendix framework on the review branch

Actions:

1. Create five minimal appendix files with purpose/parent-chapter statements.
2. Wire them into main.tex before the bibliography.
3. Verify ToC/LoF/LoT, counters, lettered numbering, headers/footers, Arabic
   pagination, margins, and bibliography order.
4. Keep or remove the old demonstration only after real-format coverage is
   confirmed.

Gate:

- clean chapter-tier build;
- no missing/duplicate labels;
- rendered transition from Chapter 6 to Appendix A is correct;
- first/last appendix and bibliography pages are correctly ordered.

Do not merge this skeleton alone to main. It is only an intermediate branch
state.

### Phase I4 — Chapter 3 pilot

Use the two-pass protocol in Section 13:

1. move expanded matrices, complete algorithms, source summaries, and
   secondary panels;
2. create complete body summaries and topical bridges;
3. update map and ledgers;
4. perform body-only and recovery tests;
5. build and inspect the complete Chapter 3/Appendix C path.
6. Keep Chapter 3 conventions local during the pilot. Do not pre-empt the
   Appendix A equivalence decision.

Gate:

- the chapter reads continuously without Appendix C;
- every moved item is recoverable;
- source/horizon, uncertainty, and evidence distinctions are intact;
- validators demonstrate that appendix content is in scope.

If the pilot fails the reader tests, revise the rules before scaling.
If it passes, present the generated pilot review packet and obtain author
approval of the demonstrated body/appendix pattern before Chapters 2, 4, and 5
are migrated.

### Phase I5 — shared-convention equivalence audit

Actions:

1. compare exact AL/exAL, latent-scale, scoring, derivative, and symbol
   conventions;
2. record equivalence or non-equivalence with equations and source links;
3. populate Appendix A only with safe concordances;
4. update all consumers atomically.

Gate:

- no project-specific meaning has been collapsed;
- each shared convention has an explicit compatibility basis;
- all local reminders remain intelligible.

Appendix A must not be committed as a duplicated convention block before its
consumers are updated.

### Phase I6 — Chapter 2 and Appendix B

Actions:

1. preserve the software contribution and workflow;
2. move posterior, LDVB, shrinkage, and detailed diagnostic algebra;
3. preserve the negative transfer result and implementation limits;
4. repair transitions and update all records.

Gate:

- a reader can identify the software research contribution without reading
  Appendix B;
- a specialist can recover every computational detail;
- package architecture has not been mistaken for disposable engineering text.

### Phase I7 — Chapter 4 and Appendix D

Use four reviewable subcommits:

1. Gaussian baseline;
2. MCMC and variational inference;
3. joint and multistep forecast machinery;
4. diagnostic, sensitivity, and application detail.

Gate after each subcommit:

- target and parameterization invariants pass;
- body conclusion remains for every moved check;
- fixed-feature, future-input, rearrangement, and approximation boundaries
  remain explicit;
- affected pages and appendix entry points are rendered.

Do not merge a partially migrated Chapter 4 to main.

### Phase I8 — Chapter 5 and Appendix E

Actions:

1. map theorem assumptions, statements, proofs, and downstream references;
2. move proofs and long derivations while retaining complete statements;
3. move TCSP mechanics but retain action, evidence, and limitations;
4. move proposed-extension computations while keeping their status explicit;
5. reconcile repeated definitions.

Gate:

- theorem/proof graph is complete;
- no guarantee is strengthened;
- no proposed extension appears implemented;
- tolerance and predictive concepts remain distinct;
- primary empirical conclusions remain in the body.

### Milestone review packet for Phases I4 and I6--I8

At each completed chapter/appendix pair, generate a concise review packet from
the authoritative records. Do not commit a duplicate narrative report. The
packet contains:

- baseline and milestone commits;
- before/after body outline and local page/word counts;
- migration IDs grouped by KEEP, CONDENSE, MOVE, SPLIT, MERGE, and OMIT;
- all high-risk units and their review state;
- claim, theorem/proof, algorithm, display, citation, and label reconciliation
  counts;
- primary displays retained in the body and secondary displays moved;
- body-bridge and recovery-test results;
- exact validation commands and rendered pages;
- open author/advisor decisions.

Review occurs in two passes: first read the body without appendices for logic
and emphasis; then follow every technical pointer needed to test recovery.
Approval of a chapter packet permits the next phase on the integration branch.
It does not merge the partial restructuring to main.

### Phase I9 — global narrative pass

Only after all research boundaries are stable:

1. deduplicate Chapter 1 against the research chapters;
2. give every chapter introduction the problem, contribution, evidence, and
   roadmap once;
3. make discussions interpret rather than repeat introductions;
4. strengthen transitions among Chapters 2--5;
5. revise Chapter 6 toward comparison rather than recap;
6. apply the statistical-writing profile paragraph by paragraph;
7. remove article/supplement navigation and implementation-process language;
8. retain qualifications adjacent to claims.

Gate:

- body-only reader test passes end to end;
- terminology and notation audit passes;
- prose does not introduce new claims;
- page counts are recorded as diagnostics, not targets.

### Phase I10 — provenance and documentation reconciliation

Actions:

1. finalize migration map and revision hashes;
2. reconcile import current-components, source manifest, claims, and displays;
3. update all location-dependent operational documentation to the final
   physical structure;
4. verify that historical no-appendix decisions are clearly marked
   superseded rather than rewritten;
5. update STATUS and ASSISTANCE-LOG.

Gate:

- no contradictory current instruction remains;
- immutable baseline facts are unchanged;
- every active manuscript derivative is tracked.

### Phase I11 — accessibility completion

Accessibility feasibility occurs in Phase I1. Content-level remediation and
the production build transition wait until placement stabilizes.

Actions:

1. Reconfirm current UCSC guidance and the checker/filing expectations close
   to release.
2. Use docs/accessibility-ledger.json to inventory all active figures, tables,
   headings, lists, links, language metadata,
   reading order, color reliance, and alternative text;
3. implement the Phase-I1 candidate route first in a controlled production
   branch state, without modifying the vendored class unless the recorded
   compatibility evidence requires and justifies it;
4. replace no-op alternative-text handling with tested accessible output;
5. add meaningful, context-specific alternative text or explicit artifact
   status to every active graphic;
6. identify data-table headers, distinguish layout tables, and verify table
   reading order;
7. verify mathematics tagging/MathML, algorithms, proofs, lists, links, and
   heading hierarchy;
8. verify embedded fonts, no password, printing permission, metadata, and
   document structure;
9. run the accepted accessibility checker and perform human keyboard,
   navigation, or screen-reader-oriented review as required by the filing
   process.

The current muscat TeX Live 2018 build remains the visual regression baseline;
it is not the accessibility candidate. Current official Overleaf guidance says
TeX Live 2025 supports automated PDF tagging and recommends LuaLaTeX for
MathML. That is a candidate implementation route, not proof that the legacy
class, algorithm stack, complex tables, TikZ, math fonts, and imported assets
will work unchanged. Keep the accepted pdfLaTeX build and the candidate
accessible build as separate validation targets until layout and scientific
content parity are demonstrated.

UCSC requires WCAG 2.1 AA; it does not, in the reviewed notice, prescribe
PDF/UA-2 as the only route. PDF/UA-2 may provide a strong technical basis but
must not be mislabeled as a separately stated university requirement.

Technical references:

- [Overleaf: Creating accessible PDFs in LaTeX](https://docs.overleaf.com/writing-and-editing/creating-accessible-pdfs)
- [LaTeX Tagging Project usage instructions](https://tagging-project.latex-project.org/documentation/usage-instructions)

Gate:

- the generated submission candidate meets the documented current standard;
- evidence and tool versions are recorded;
- no claim of WCAG conformance is made from visual inspection alone.

If the legacy class/toolchain cannot produce an acceptable PDF, stop and
escalate with tested alternatives. Do not perform an unreviewed class rewrite.

### Phase I12 — release audit

Run:

- fast validation after every coherent unit;
- chapter validation after every chapter/appendix pair;
- release validation from a new empty timestamped directory with the fixed
  audit root;
- TeX-log checks for citations, references, duplicate labels, missing files,
  fatal errors, overfull boxes, and floats;
- PDF page-size, font, tagging, metadata, permission, and accessibility checks;
- pre/post inventories of claims, theorems, proofs, algorithms, displays,
  citations, and labels;
- systematic rendered-page review.

Required rendered pages include:

- front matter and contents/list endpoints;
- all chapter openings and endings;
- Chapter 6 to Appendix A transition;
- first and last page of each appendix;
- representative proofs, algorithms, wide equations, figures, and tables;
- every reflowed primary display;
- every page with a TeX diagnostic;
- first and last bibliography pages.

Gate:

- body-only and recovery tests both pass;
- scientific no-loss reconciliation is complete;
- filing and accessibility requirements pass;
- author/advisor body review is resolved;
- accepted artifact and hash are recorded.

### Phase I13 — merge and Overleaf handoff

Use one long-lived review branch with small, chapter-sized or risk-sized
commits. Push the branch after validated milestones for backup and review.

Do not merge each half-migrated chapter independently to main. The shared
appendix structure, numbering, provenance, and documentation must remain
coherent. Merge to main only after all active chapters, appendices, records,
and release checks pass together.

Then:

1. fetch and resolve any approved remote changes;
2. review the complete branch diff and commit history;
3. merge through the established GitHub workflow;
4. push main;
5. have Overleaf pull from GitHub under docs/WORKFLOW.md;
6. build and inspect the Overleaf artifact independently;
7. record the handoff and any toolchain difference.

## 13. Per-unit editing protocol

Each migration unit uses two passes.

### Pass A: structural move

1. Confirm the map record and pre-move normalized hash.
2. Identify definitions, assumptions, labels, citations, displays, and
   downstream references.
3. Move the exact technical content; do not copy it into a second home.
4. Preserve semantic labels when their meaning is unchanged.
5. Add the minimum complete body bridge.
6. Add an appendix parent/scope statement.
7. Update map and derivative records.
8. Run focused tests, fast validation, build, and rendered inspection.

A good bridge states what the appendix establishes and why it supports the
current argument. A bare “see Appendix” sentence is not enough.

### Pass B: editorial integration

1. Condense the body around target, essential equation, result, and meaning.
2. Merge repeated definitions into the canonical home.
3. Rewrite transitions so the appendix can be skipped.
4. Remove journal/supplement navigation.
5. Replace engineering or process language with precise statistical prose
   where warranted, without obscuring computational facts.
6. Verify that all caveats remain visible.
7. Re-run validation and the reader tests.

### Unit completion checklist

- Target and conditioning information remain clear.
- Assumptions needed for the body claim remain visible.
- Main result and interpretation remain in the body.
- Moved support is complete and recoverable.
- Negative or mixed findings remain visible.
- Attribution and evidence strength are unchanged.
- Labels, citations, and dependencies resolve.
- Claim, display, migration, and revision records agree.
- Build and relevant rendered pages pass.
- No research code or source repository changed.

## 14. Quality and acceptance criteria

### 14.1 Body-only test

Without opening an appendix, a reader can follow every chapter's question,
target, method, contribution, primary evidence, interpretation, and
limitations. No sentence depends on an undefined appendix-only object for its
basic meaning.

### 14.2 Recovery test

Every technical summary or appendix pointer leads to the complete derivation,
proof, algorithm, or secondary evidence needed to audit it. Appendix sections
state their parent chapter and assumptions.

### 14.3 Scientific no-loss test

Pre/post inventories reconcile:

- inferential targets and update types;
- assumptions and theorem statements;
- proofs and algorithms;
- numerical results and design constants;
- primary and secondary displays;
- citations and attribution;
- negative/mixed findings;
- limitations and open problems;
- implemented versus proposed status.

### 14.4 Reader-flow test

For each chapter:

- introduction states problem, contribution, and evidence once;
- section order follows question, method, evidence, interpretation;
- technical detours no longer interrupt the main claim;
- every transition names why the next section matters;
- discussion synthesizes rather than repeats;
- notation is introduced before use and not redefined inconsistently.

### 14.5 Statistical-style test

Paragraph-level review should remove:

- unsupported novelty or generality claims;
- causal language unsupported by the design;
- “works,” “robust,” “optimal,” or “significant” without a defined criterion;
- engineering process narration that is irrelevant to the statistical
  argument;
- anthropomorphic or promotional AI-style phrasing;
- vague pronouns and unqualified comparison language.

It should preserve:

- exact inferential objects;
- conditional statements and evidence scope;
- method/source attribution;
- numerical and design qualifications;
- explicit approximation boundaries;
- concise computational facts where scientifically relevant.

### 14.6 Length diagnostics

Record body and appendix pages after the Chapter 3 pilot and after each
chapter pair. The earlier provisional body bands may be retained as warning
signals, but no unit passes or fails because of a fixed page count. The total
dissertation may remain near its current length.

### 14.7 Documentation and dependency truth

At every milestone:

- the static and recorded active-file inventories agree or have a documented
  explanation;
- no active project input is untracked, repository-external, or omitted from
  safety scans;
- STATUS names the exact phase and next gate;
- current instructions do not contradict the implemented placement;
- structured JSON and human-readable summaries agree;
- historical records remain distinguishable from current directions.

### 14.8 Accessibility and visual-parity test

The accessible candidate must pass both machine and human checks. A Tagged:
yes result is necessary but not sufficient. Conversely, a checker warning
must be interpreted against the actual standard and document structure rather
than hidden or waived without evidence.

Before replacing the accepted production route, compare the same source under
the baseline and candidate engines for page size, margins, page numbering,
font embedding, displayed mathematics, citations, links, figure/table
placement, and text extraction. Scientifically meaningful content must match;
pagination may change only after review.

## 15. Git, review, and rollback design

### 15.1 Commit strategy

Recommended commit sequence:

1. approved architecture, source freeze, and current-documentation truth;
2. validation/test infrastructure and recorded dependency support;
3. accessibility feasibility evidence, with no production-engine change;
4. migration map and reviewed placements;
5. appendix skeleton;
6. Chapter 3/Appendix C pilot;
7. Appendix A compatibility conversion;
8. Chapter 2/Appendix B;
9. Chapter 4/Appendix D subcommits;
10. Chapter 5/Appendix E;
11. global narrative pass;
12. provenance/documentation reconciliation;
13. accessibility remediation;
14. release evidence.

Each commit must be buildable or explicitly documented as an intermediate
branch-only commit with the next dependent commit immediately available.

### 15.2 Rollback

Rollback is by focused commit reversal, not by reset, clean, stash, or source
regeneration. The immutable accepted PDF and content baseline remain available
for comparison. Before reverting a content move, verify whether later commits
depend on its labels or appendix location.

### 15.3 Main and Overleaf

Create one named integration branch from the frozen main and push it after
validated milestones. Once published, do not rebase or force-push it. If main
advances through an authorized Overleaf or administrative update, preserve
that state and merge origin/main into the integration branch at a documented
gate; do not replay structural history blindly.

main should receive only the complete coherent restructuring. Near final
integration, establish a short explicit editing freeze, fetch again, resolve
all divergence on the integration branch, rerun the release gates, and then
merge. Overleaf synchronization occurs after the main merge, not as a
mechanism for resolving structural conflicts.

This modifies the earlier “merge every large chapter change immediately”
habit for this one cross-cutting migration. Small commits remain; premature
main merges do not.

## 16. Risks, stop conditions, and controls

| Risk | Preventive control | Stop condition |
| --- | --- | --- |
| Shorter but logically incomplete body | Seven-question body contract and body bridges | Reader needs appendix to know target, main result, or caveat. |
| Content loss during movement | Pre-move hashes, full map, move-not-copy rule, inventory reconciliation | Unmapped or unreconciled unit. |
| Appendix becomes a dump | Parallel project structure, parent links, canonical homes | Appendix unit has no body parent or purpose. |
| Duplicate technical content survives | MERGE_CANONICAL and duplicate-concept review | Two authoritative definitions remain. |
| Non-equivalent models are centralized | Appendix A compatibility gate | Scale/rate/target equivalence is unproved. |
| Proof is detached from assumptions | Theorem/proof graph | Statement scope no longer matches proof. |
| Central evidence becomes invisible | Claim-linked placement and body conclusion rule | Primary claim lacks visible evidence or conclusion. |
| Validation misses appendix faults | Hybrid static/recorded TeX graph and negative tests | Appendix or dynamic input is absent from validator scope. |
| Historical provenance is rewritten | Immutable baseline and derivative-component model | Any baseline source/destination hash changes without source regeneration authorization. |
| Accessibility is deferred too late | Early feasibility spike and final content audit | No demonstrated tagged-PDF path before release phase. |
| Toolchain change damages class formatting | Disposable feasibility branch and rendered comparison | Untested class or preamble rewrite is proposed. |
| Half-migration reaches Overleaf/main | One review branch and complete-release merge gate | Main would contain missing bridges, skeleton appendices, or incomplete ledgers. |
| Page count drives deletion | Reader/recovery tests are acceptance criteria | Omission is justified only by length. |
| Scientific correction is hidden in structural edit | Separate correction record and source check | Formula/result changes without independent evidence. |

## 17. Parallel work not solved by restructuring

The reorganization does not resolve:

1. advisor confirmation that the software-centered exDQLM chapter satisfies
   the intended independent-research role;
2. the unresolved TCSP exact scan recursion and action-matched finite-sample
   proof;
3. absent implementation/validation for proposed MTI regression and dynamic
   extensions;
4. exact candidate and coauthor contribution statements;
5. material-specific coauthor/publisher reuse permissions;
6. final publication status for each project;
7. title, committee/dean fields, conferral date, ORCID, acknowledgments, and
   other administrative fields;
8. final bibliography and citation-style review;
9. current WCAG 2.1 AA filing conformance;
10. independently inspected Overleaf output.

These remain separate tracked decisions. A cleaner structure must not be
reported as evidence that they are resolved.

The author identity policy remains:

- scholarly/main name: Antonio de Leon;
- official long name: Jose Antonio Aguirre Perez de Leon, subject to exact
  accents/capitalization required by university records.

No author-list or contribution inference should be made solely from repository
names.

## 18. Definition of done

The restructuring is complete only when:

- all four research chapters and five appendices are active and coherent;
- every mapped unit has a final disposition and review state;
- the body-only and recovery tests pass;
- no scientific target, claim, evidence boundary, attribution, or negative
  result was lost or strengthened;
- all active TeX is covered by validation;
- static and compiler-recorded project dependency graphs reconcile;
- labels, citations, inputs, displays, and bibliography resolve;
- provenance records preserve immutable baselines and track current
  derivatives;
- current documentation contains no contradictory body-only/no-appendix rule;
- accessibility and current UCSC filing checks pass with recorded evidence;
- the baseline and accessible candidate builds have documented content/layout
  parity or approved, inspected differences;
- a clean release build and systematic rendered-page review pass;
- author/advisor review comments are resolved;
- main is merged and pushed only after the complete coherent review branch
  passes;
- the GitHub-to-Overleaf handoff is performed deliberately and the Overleaf
  artifact is independently inspected.

## 19. Approval package

The recommended defaults are:

1. retain four research chapters;
2. adopt Appendices A--E;
3. preserve article prose initially and edit in two controlled passes;
4. retain theorem/proposition statements in the body and move full proofs;
5. retain primary claim-defining displays and move only secondary support;
6. keep code, data, fitted objects, and full computations external;
7. centralize shared conventions only after an equivalence audit;
8. make validation and the migration map precede manuscript movement;
9. treat page counts as diagnostics, not quotas;
10. perform accessibility work as a parallel filing requirement;
11. use one review branch with recoverable commits and merge only the complete
    coherent restructuring;
12. omit no scientific content without an explicit no-loss decision;
13. freeze the eight audited source commits unless a replacement is explicitly
    selected and audited;
14. use hybrid static/recorded TeX dependency validation;
15. reconcile current documentation immediately after approval and maintain
    one controlling plan;
16. use the authority, milestone-review, and change-control rules in this
    document.

If these defaults are approved, Codex can begin with Phases I0--I2:
synchronize/freeze, strengthen validation, and produce the exhaustive
migration map. It should then present the completed map and Chapter 3 pilot
boundary for review before moving prose.

The unambiguous authorization phrase is:

**Approve the sixteen final defaults and the existing eight-source snapshot
freeze. Implement the final reader-first restructuring plan end to end,
observing its review gates.**

That authorization permits ordinary structural choices already governed by
the map and placement rules. It does not authorize an unsupported scientific
correction, a new research-source version, deletion without a no-loss record,
rights assertions, institutional approval claims, or destructive Git
operations.

Until that approval, this plan is the deliverable. No manuscript,
appendix, validator, provenance schema, or build behavior is to be implemented.
