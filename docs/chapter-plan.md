# Evidence-backed four-project dissertation architecture

Status: **author-directed working architecture; committee and reuse review pending**
Prepared: 2026-09-15
Revised: 2026-09-15 after the author's identity and four-project direction
Evidence basis: `research-audit.md`, `research-audit-validation.md`,
`research-decisions.md`, `claim-evidence.json`, `../source-manifest.json`, and
the fixed-snapshot manuscripts and supplements named below

## 1. Decision and rationale

Use four research chapters, each corresponding to a distinct project line:

1. the `exdqlm` software and computational workflow;
2. source-aware correction and synthesis of hydrologic products;
3. Bayesian quantile deep echo-state networks; and
4. mean-tilted intervals, combining the short-tolerance foundation with the
   regression and dynamic extensions.

This replaces the earlier three-unit recommendation. The change is justified
by the author's direction to treat the work as four main projects and by the
current `exdqlm` article, which supplies a complete, explicitly software-centered
contribution statement, a substantial methods appendix, four examples, an R
package, and its own validation record. The chapter must still distinguish the
candidate's package contribution from Yan's exAL work and Barata et al.'s
exDQLM, MCMC, ISVB, and transfer-function foundations.

The two MTI manuscripts remain one project chapter. They share the same
residual-product geometry, fixed-content targets, pseudo-AL computation, and
inferential distinctions. The foundation paper supplies theory, tolerance
calibration, simulation, and the pharmaceutical illustration; the extensions
paper supplies regression and dynamic endpoint models but currently has no
snapshot-matched implementation or empirical validation. Treating those papers
as two chapters would overstate their present independence.

The unifying question is:

> How can conditional quantiles and fixed-content interval targets be
> specified, computed, and validated when dynamics, nonlinear structure,
> heterogeneous forecast products, and practical computational constraints
> make full response-distribution modeling difficult or undesirable?

The architecture is a working scholarly decision, not proof that all four
chapters satisfy the program expectation independently. The committee should
confirm that the software-centered `exdqlm` contribution is an acceptable
journal-suitable research unit. That confirmation affects chapter counting,
not whether its verified methods may be used as shared dissertation material.

## 2. Identity, collaborators, and evidence boundary

Use **Antonio de Leon** as the dissertation's scholarly name. Use **Jose
Antonio Aguirre Perez de Leon** on the formal dissertation title and approval
pages, subject only to matching the final university record. The author has
confirmed that manuscript forms such as “Antonio De Leon” and package metadata
using “Antonio Aguirre” refer to the same candidate. Preserve source spellings
in immutable bibliographic metadata when changing them would misquote a source.

| Project | Authors/collaborators documented at the audited snapshot | What the repository establishes |
| --- | --- | --- |
| `exdqlm` | Antonio De Leon, Raquel Barata, Raquel Prado, Bruno Sansó | The article is first-authored by the candidate and describes a five-part software contribution. Package metadata lists Raquel Barata as author/creator/maintainer, Antonio Aguirre as author, and Prado and Sanso in thesis-advisor roles. |
| Environmetrics | Antonio De Leon, Raquel Prado, Bruno Sansó | The candidate is first and corresponding author; the acknowledgment identifies the work as part of the candidate's dissertation. The paper states a joint project contribution but contains no completed individual-contribution section. |
| QDESN | Antonio De Leon, Raquel Prado, Bruno Sansó | The candidate is first author. The manuscript gives a precise project-level contribution paragraph covering the model, computation, simulation, and applications; it does not allocate those tasks among authors. |
| MTI foundation and extensions | Antonio De Leon, Raquel Prado, Bruno Sansó | The candidate is first author on both manuscripts. Each paper has a precise project-level contribution paragraph; neither supplies an individual CRediT allocation. |

These records are enough to identify the research content, collaborators,
project purpose, and joint scholarly contributions. They support source-based
drafting in a neutral project-level voice. They do not justify statements such
as “the candidate alone proved,” “implemented,” or “designed” a specific item.
Granular personal-role language belongs in the contribution preface or
acknowledgments only after the short confirmation in `research-decisions.md`.

## 3. Provisional table of contents

### Chapter 1 — Introduction and common inferential framework

Purpose: state the dissertation question, locate the four projects, and define
only background genuinely shared across them.

Include:

- conditional quantiles, check loss, AL/exAL models, and dynamic quantile
  state-space notation;
- likelihood-based posterior inference versus generalized Bayes based on an
  exponentiated loss;
- credible, predictive, confidence, and tolerance intervals;
- common evaluation concepts: quantile/check loss, CRPS, calibration/coverage,
  computational diagnostics, and provenance levels;
- an antecedent map crediting Yan for exAL, Barata et al. for exDQLM and its
  original inference/transfer developments, and the relevant ESN, generalized-
  Bayes, and tolerance literature; and
- an author-confirmed contribution and chapter map.

Do not impose one probability model on all four projects. In particular, the
MTI generalized posterior and TCSP action are not response-likelihood or
posterior-predictive objects.

### Chapter 2 — Computational infrastructure for flexible dynamic quantile models

Primary sources: `SRC-EXDQLM-ARTICLE` at
`d5534e97db8414fd875022261d4c530eae4676e4` and the exact package snapshots in
`SRC-EXDQLM-PKG`.

Research question: how can established exDQLM methodology be made available as
a coherent, diagnosable, and reproducible software workflow for dynamic and
static Bayesian quantile analysis?

Repository-documented project contribution:

1. composable trend, seasonal, regression, and transfer-function model
   construction;
2. coordinated MCMC, scale-collapsed MCMC, LDVB, and legacy ISVB interfaces;
3. fitted-object, forecasting, post-processing, plotting, and diagnostic APIs;
4. distribution utilities, scores, calibration checks, compiled computation,
   and R fallbacks; and
5. static AL/exAL regression, shrinkage options, examples, tests, and
   article-reproduction materials.

Provisional structure:

1. inherited exAL/exDQLM foundations and the candidate project boundary;
2. software architecture and model-construction interface;
3. MCMC, LDVB, and ISVB interfaces and their inferential meanings;
4. diagnostics, scoring, forecasting, and posterior-predictive synthesis;
5. static regression and shrinkage support;
6. Lake Huron, Sunspots, Big Tree, and sparse-static examples as workflow
   demonstrations rather than four new contributions;
7. version graph and reproducibility contract; and
8. limitations and the relationship to the later application/method chapters.

Do not restate Barata's methodological contributions as new. Do not call
post-fit `quantileSynthesis()` a joint posterior across quantiles. Preserve the
mixed Big Tree and LDVB-versus-MCMC findings. The missing immutable 1.1.1
submission archives limit full reproduction claims but do not prevent a
carefully qualified methods/software draft from the tracked article and package.

### Chapter 3 — Source-aware correction and synthesis of hydrologic products

Primary source: `SRC-ENVIRON` at
`1272bfc10442a28add5a4c74ff641e9b9a8e9666`. Supporting sources:
`SRC-SAN-LORENZO-REPRO`, `SRC-ENVIRON-CORR`, and `SRC-EXDQLM-PKG` version
1.1.0.

Research question: how can observations, retrospective products, operational
ensemble forecasts, and forecast covariates be linked through dynamic
quantile-specific discrepancy learning and synthesized into useful predictive
distributions?

Provisional structure:

1. hydrologic decision setting and source/horizon contract;
2. source-specific exDQLM discrepancy model and transfer covariates;
3. LDVB computation and its relationship to Chapter 2;
4. post-fit quantile synthesis and scoring;
5. five-origin design with separate 28-day and 8-day comparisons;
6. component sensitivity and interpretation;
7. limitations: deterministic exogenous summaries, versioned inputs, five
   origins, and unavailable raw-archive reconstruction; and
8. reproducibility statement tied to the approved staged bundle.

Retain the mixed eight-day evidence. Do not claim a dense hindcast,
operational deployment, or joint propagation of exogenous forecast
uncertainty. Fitted-quantile credible bands and synthesized predictive bands
must remain distinct.

### Chapter 4 — Bayesian quantile deep echo-state networks

Primary source: `SRC-QDESN` at
`757522db0f85815244370ec92a194de132268883`. Supporting sources: the package
snapshots and antecedent papers explicitly named by its manifests.

Research question: can fixed nonlinear reservoir features support scalable
Bayesian conditional-quantile inference and forecasting, both one quantile at
a time and across a vector of probability levels?

Provisional structure:

1. DESN feature construction and fixed-design interpretation;
2. single-level AL/exAL QDESN with ridge and regularized horseshoe priors;
3. MCMC and model-specific variational computation;
4. joint quantile-vector working likelihood, adjacent-level shrinkage, and
   noncrossing treatment;
5. single-quantile and multi-level simulations;
6. GloFAS application;
7. PriceFM region-frozen comparison; and
8. limitations and future work.

The main article, QDESN supplement, and Gaussian-DESN supplement are one source
packet. Use the corrected-v4 joint evidence as the current authority and treat
the stale 14-row historical manifest and Phase 181 wiring checks as historical
controls. Preserve WARN/FAIL cells, GloFAS's single-origin limit, iteration-cap
qualification, and PriceFM region/fold heterogeneity. Search Phase II remains
future work unless it is later promoted and re-audited.

### Chapter 5 — Mean-tilted intervals: targets, tolerance actions, regression, and dynamics

Primary sources: `SRC-RQR` at
`73887b9c86ef767aa1567c660718667945630aef` and `SRC-MTI-EXT` at
`f345d946aa5a81b94795838bec58d874a0fdd0c9`.

Research question: how can fixed-content intervals be placed by retained-mean
balance, computed through generalized updating, calibrated for tolerance use,
and extended to covariate-indexed or time-varying endpoints?

Provisional structure:

1. residual-product antecedent, MPI characterization, and MTI tilt family;
2. score and quantile-window results;
3. generalized posterior and pseudo-AL computation;
4. TCSP retained-count calibration and empirical tolerance action;
5. iid simulation and pharmaceutical illustration;
6. static endpoint regression and deterministic basis expansions;
7. dynamic endpoint states and alternating root-specific FFBS;
8. separation among endpoint uncertainty, response prediction, and tolerance
   confidence; and
9. limitations and missing extension validation.

Use conservative, action-accurate TCSP language: the tracked simulation and
calibration evidence is empirical; an exact recursion and a finite-sample proof
matched to the reported closed-window action remain open. The extensions may be
drafted as theory/computation sections, but no empirical performance or
tolerance guarantee may be invented from the absence of an implementation.

### Chapter 6 — Synthesis, limitations, and future research

Compare the four projects by target, dependence representation, computation,
calibration evidence, and reproducibility. Explain when the relevant object is
a fitted conditional quantile, a synthesized predictive distribution, a
software workflow, a loss-defined endpoint functional, or a tolerance action.
Do not rank methods across incomparable targets or convert unfinished work into
results.

### Appendices

- mathematical derivations that support but are not essential to the chapter
  argument;
- algorithms, software versions, diagnostics, and environment details;
- secondary empirical tables and figures with claim locators; and
- reproducibility/provenance records, including exact sources, configurations,
  hashes, seeds/thread policies, and explicitly unexecuted workflows.

## 4. Source-first adaptation plan

The dissertation will not start from blank prose or from memory. Each chapter
will be assembled from a fixed source packet. The packet is evidence, not a
runtime dependency of the dissertation build.

| Reuse class | Default treatment | Required control |
| --- | --- | --- |
| Research purpose, method, assumptions, limitations, and project-level contribution statements | Synthesize from the audited manuscripts in new dissertation connective prose | Cite source commit/path/section in the working provenance record |
| Equations and definitions | Adapt from the verified source, harmonize notation only through an explicit mapping, and preserve attribution | Equation-level locator for central or inherited results |
| Numerical claims | Reuse only the audited result line and its qualification | Claim-evidence entry with model, data, split/horizon, metric, and validation status |
| Tables | Prefer regeneration or adaptation from tracked source data; do not manually transcribe when a machine-readable authority exists | Approved asset class, source hash/locator, and caption rewrite |
| Figures | Prefer approved source figure or deterministic regeneration from tracked outputs | Rights decision, source hash, generation contract, and visual inspection |
| Algorithms/code | Explain in pseudocode or dissertation notation; keep package/source code in its own licensed repository | Exact implementation version and license/attribution note |
| Verbatim article prose | Avoid by default; use only when coauthor/publisher policy is recorded and verbatim reuse is editorially preferable | Material-specific permission and visible attribution |

This policy uses the repositories heavily while preventing an article bundle
from being pasted into the thesis without integration. Shared background is
written once. Journal introductions, duplicated literature reviews, response
letters, and submission-specific formatting are not imported. Central methods,
proofs, validated results, and approved figures/tables are adapted rather than
rediscovered.

The cross-chapter writing control is the repository-supplied *Academic Writing
Style Profile for AI-Assisted Statistical Writing*, version 0.2, in
`SRC-QDESN:Academic_Writing_Style_Profile_v0.2.md` and the nearly identical
`SRC-MTI-EXT:STYLE_PROFILE.md`. Draft from the scientific problem rather than
the algorithm; use precise, restrained contribution language; define and
interpret notation; separate model, prior, likelihood/loss, computation and
approximation; and report empirical designs, negative findings, diagnostics,
and limitations with the claim they support. Thesis-wide requirements and the
author's later explicit instructions take precedence if a local manuscript
profile conflicts with them.

### Section-level source packets

| Dissertation chapter | Main source sections | Supplementary/supporting material | Material excluded by default |
| --- | --- | --- | --- |
| 2 `exdqlm` | article Sections 2–5; package `DESCRIPTION`, `NEWS.md`, help/tests for named claims | technical appendix; four example manifests and tracked outputs | missing submission archives, live package `main` substituted for older analyses, duplicated package manual text |
| 3 Environmetrics | manuscript methodology, San Lorenzo design, validation, interpretation, conclusion | embedded MCMC/VB appendices; asset manifest; correction and staged-repro records | raw retrieval histories, unapproved restricted assets, five-origin claims generalized to dense operations |
| 4 QDESN | article Sections 2–7 | QDESN derivation supplement; Gaussian-DESN supplement; corrected-v4, GloFAS, and PriceFM authority records | unpromoted Search Phase II; ignored output forests; superseded historical manifests as current evidence |
| 5 MTI | RQR Sections 2–8 and its theory/validation supplement; MTI-EXTENSIONS Sections 2–6 and supplement | exact tracked table/figure contracts and application protocol | failed dynamic campaigns, an unavailable exact TCSP theorem, empirical claims for the unimplemented extensions |

## 5. Source-to-chapter and overlap map

| Source | Ch. 1 | Ch. 2 | Ch. 3 | Ch. 4 | Ch. 5 | Ch. 6 / appendices |
| --- | --- | --- | --- | --- | --- | --- |
| exdqlm article/package | antecedent boundary | primary | computation dependency, pinned 1.1.0 | comparator/dependency, pinned 1.1.1 where declared | only exact dependencies | version graph and software reproducibility |
| Environmetrics article | applied motivation | example relationship only | primary | distinguish GloFAS tasks | — | provenance and limitations |
| San Lorenzo bundle/corrections | — | — | provenance/revision evidence | — | — | approved reproducibility material |
| QDESN article/supplements | nonlinear motivation | software comparator | distinguish application design | primary | — | derivations and secondary evidence |
| RQR-GIBBS | interval taxonomy | — | — | — | foundation, tolerance, validation | proofs and validation details |
| MTI-EXTENSIONS | generalized-Bayes taxonomy | — | — | — | regression/dynamic extension | derivations; future implementation plan |
| Yan and Barata antecedents | common credit | explicit foundation | inherited method boundary | exAL/exDQLM comparator credit | — | bibliography only |

The main overlap controls are:

- Chapter 2 explains reusable software; Chapter 3 owns the hydrologic scientific
  question and does not repeat the package tutorial.
- Chapter 3 and Chapter 4 both use hydrologic material, but their forecast
  products, information sets, model roles, and evidence bases differ and must
  be compared explicitly.
- Chapter 4's independent and joint fits are variants inside one QDESN project.
- Chapter 5's two manuscripts are complementary parts of one MTI project until
  the extension work gains independent implementation and evidence.

## 6. Drafting readiness and order

| Chapter | Readiness | Remaining control before factual drafting | First source-based unit |
| --- | --- | --- | --- |
| 2 `exdqlm` | Medium-high | confirm granular candidate role; preserve version graph; do not claim full archive reproduction | inherited-method boundary and software architecture |
| 3 Environmetrics | High | confirm material-specific rights before importing assets | problem setting and source/horizon design |
| 4 QDESN | Medium-high | sanitize provenance; use current corrected authority; retain qualifications | target and fixed-reservoir architecture |
| 5 MTI | Medium | use conservative TCSP wording; identify extension sections as theory/computation without validation | fixed-content targets and inferential distinctions |

Recommended drafting order is **Chapter 3 problem/data design**, then Chapter 2,
Chapter 4, and Chapter 5. This starts with the most mature source/provenance
packet while allowing the shared Chapter 2 terminology to be harmonized before
the later chapters are finalized. Chapter numbers describe final reading order,
not drafting order.

## 7. Remaining decisions requiring the author

Repository evidence has removed the need for the author to re-explain every
project from scratch. Only the following decisions remain:

1. confirm that the five audited manuscript commits are acceptable working
   drafting snapshots or provide a replacement commit/file;
2. confirm or correct the short candidate-role summaries in
   `research-decisions.md`, especially the division of implementation, theory,
   empirical work, and writing among collaborators;
3. identify any article text, figures, or tables already approved for direct
   dissertation reuse; otherwise the default is new integrated prose and no
   copied assets;
4. obtain committee confirmation that `exdqlm` counts as the fourth research
   chapter; and
5. authorize one drafting unit and its permitted asset classes.

Until a proof replaces the current evidence, conservative TCSP wording is a
technical requirement rather than an optional stylistic choice. The ORCID,
formal title, committee roles, and conferral fields remain administrative
metadata decisions.

## 8. Controlled execution after authorization

For each authorized unit:

1. freeze the source packet and create a section-level import manifest;
2. extract the relevant claims, equations, citations, results, limitations,
   and collaborator attribution from the fixed commit;
3. write the dissertation-native narrative and notation map;
4. import only approved tables/figures, recording source hashes and adaptation;
5. update claim and source provenance;
6. compile and inspect the affected pages, references, labels, fonts, and
   overflow;
7. review for target/likelihood/interval and empirical/theoretical claim
   accuracy; and
8. make a focused local commit before any separately authorized GitHub or
   Overleaf synchronization.

The thesis must remain self-contained. Research repositories remain immutable
evidence sources and never become build-time dependencies.
