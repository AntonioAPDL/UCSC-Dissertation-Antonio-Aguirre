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

### Integrated technical material — no separate scientific appendix

The research chapters will contain their own derivations, proofs, algorithms,
validation details, and claim-relevant secondary figures/tables. Supplement
material will be inserted beside the main result it supports rather than placed
in a detached dissertation supplement or appendix. The starter's formatting
demonstration appendix will be removed once the converted chapters replace its
technical-format examples.

## 4. Manuscript-first adaptation plan

The dissertation will not start from blank prose or memory. Each article is the
initial chapter body, and unique supplement content is merged into the relevant
section. The detailed source-by-source map, asset boundary, provenance design,
and execution gates are in `manuscript-integration-plan.md`.

The source packet is evidence, not a runtime dependency of the dissertation
build. Research repositories retain code, data, computation, and full
provenance; the thesis imports only its readable scientific body and selected
final assets.

| Reuse class | Default treatment | Required control |
| --- | --- | --- |
| Main-article scientific prose | Preserve during the local structural conversion, then edit only for integration, duplication, accuracy, and dissertation voice | Exact source commit/path/section, contributor credit, and external-reuse status |
| Supplement prose, equations, proofs, and algorithms | Insert beside the main theorem, method, or result they support; merge duplicates | Section-level import disposition and explicit notation/label mapping |
| Equations and definitions | Preserve or adapt from the verified source; harmonize notation only through an explicit mapping | Equation-level locator for central or inherited results |
| Numerical claims | Reuse only the audited result line and its qualification | Claim-evidence entry with model, data, split/horizon, metric, and validation status |
| Main tables and figures | Import the non-superseded final manuscript assets; omit only with a documented reason | Source hash/locator, authority record, caption adaptation, rights status, and visual inspection |
| Supplement tables and figures | Import when they prove, qualify, diagnose, or interpret a central claim | Same controls as main assets plus a recorded include/omit decision |
| Algorithms/code | Explain in pseudocode or dissertation notation; keep package/source code in its own licensed repository | Exact implementation version and license/attribution note |
| Code, data, fitted objects, runs, and full output archives | Keep external; summarize only the evidence boundary required by the chapter | Source repository/commit/path and validation status |

The first pass preserves the article record. The second pass removes repeated
abstracts, introductions, literature reviews, conclusions, and submission
formatting; adds transitions and attribution; and centralizes truly shared
background. This avoids both a blank rewrite and an unreadable concatenation of
article PDFs.

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
| 2 `exdqlm` | complete article scientific body and examples | integrate the article's technical appendix beside the corresponding model/computation sections | package source tree, caches, fitted objects, missing submission archives, duplicated manual text |
| 3 Environmetrics | complete article scientific body | integrate MCMC/VB algorithms, sensitivity results, parameter summaries, and additional cutoff panels beside their main sections | staged data, raw retrieval histories, scripts, full outputs, five-origin claims generalized to dense operations |
| 4 QDESN | complete main-article scientific body | integrate the QDESN derivation and Gaussian-DESN supplements by model, computation, simulation, and application topic | unpromoted Search Phase II; ignored output forests; superseded historical manifests as current evidence |
| 5 MTI | complete RQR and MTI-EXTENSIONS scientific bodies | integrate both supplements by theorem, computation, validation, application, and dynamic-model topic | failed dynamic campaigns, validation output archives, an unavailable exact TCSP theorem, empirical claims for unimplemented extensions |

## 5. Source-to-chapter and overlap map

| Source | Ch. 1 | Ch. 2 | Ch. 3 | Ch. 4 | Ch. 5 | Ch. 6 / integrated technical role |
| --- | --- | --- | --- | --- | --- | --- |
| exdqlm article/package | antecedent boundary | complete article plus integrated technical detail | computation dependency, pinned 1.1.0 | comparator/dependency, pinned 1.1.1 where declared | only exact dependencies | version graph and software reproducibility |
| Environmetrics article | applied motivation | example relationship only | primary | distinguish GloFAS tasks | — | provenance and limitations |
| San Lorenzo bundle/corrections | — | — | provenance/revision evidence | — | — | approved reproducibility material |
| QDESN article/supplements | nonlinear motivation | software comparator | distinguish application design | complete article with both supplements integrated | — | limitations and cross-project implications |
| RQR-GIBBS | interval taxonomy | — | — | — | foundation, proofs, tolerance, validation, and application | limitations and open theory |
| MTI-EXTENSIONS | generalized-Bayes taxonomy | — | — | — | integrated regression/dynamic extension and derivations | future implementation plan |
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

## 6. Integration readiness and order

| Chapter | Structural conversion readiness | Controls during import |
| --- | --- | --- |
| 2 `exdqlm` | Medium-high: complete article, figures/tables, package, and technical appendix are available | preserve the version graph and inherited-method boundary; do not claim the missing archive was reproduced |
| 3 Environmetrics | High: main/supporting sections, generated tables, 13 validated figure paths, and provenance records are available | import only final displayed assets; retain five-origin, horizon, and deterministic-covariate limitations |
| 4 QDESN | Medium-high: main article, two supplements, and current authority manifests are available | use corrected-v4/current application authorities; exclude Search Phase II, ignored output forests, and stale controls |
| 5 MTI | Medium: both articles and supplements are available; extensions remain theory/computation only | use conservative TCSP wording and do not invent extension validation or tolerance guarantees |

Recommended implementation is a **bulk structural conversion of all four
chapters before substantial rewriting**. Preserve manuscript content, integrate
supplements, normalize LaTeX/citations/assets, and compile after each chapter.
Only then deduplicate shared background and write monograph transitions. Local
commits remain chapter-sized so each import is reviewable and recoverable.

## 7. Remaining decisions requiring the author

Repository evidence has removed the need for the author to re-explain every
project from scratch. Only the following decisions remain:

1. confirm that the five audited manuscript commits are acceptable working
   drafting snapshots or provide a replacement commit/file;
2. confirm or correct the short candidate-role summaries in
   `research-decisions.md`, especially the division of implementation, theory,
   empirical work, and writing among collaborators;
3. resolve material-specific reuse status for final circulation and submission;
   the conversion is already on GitHub and the author reports an Overleaf
   handoff, which does not itself establish reuse clearance;
4. obtain committee confirmation that `exdqlm` counts as the fourth research
   chapter; and
5. review the chapter-level scientific and editorial revision ledger before
   finalizing dissertation-wide contribution language.

Until a proof replaces the current evidence, conservative TCSP wording is a
technical requirement rather than an optional stylistic choice. The ORCID,
formal title, committee roles, and conferral fields remain administrative
metadata decisions.

## 8. Controlled execution after authorization

1. create chapter import manifests and citation/label/macro maps;
2. convert all four article bodies without substantial rewriting;
3. integrate supplement sections according to the project maps in
   `manuscript-integration-plan.md`;
4. copy only selected final tables/figures, recording hashes and status;
5. compile each chapter and then the full thesis;
6. perform the monograph pass: deduplication, transitions, common background,
   notation review, and attribution;
7. validate claims, references, labels, fonts, overflow, and rendered pages;
8. make focused local commits throughout; and
9. push or synchronize only at a separately authorized, rights-reviewed
   handoff.

The thesis must remain self-contained. Research repositories remain immutable
evidence sources and never become build-time dependencies.
