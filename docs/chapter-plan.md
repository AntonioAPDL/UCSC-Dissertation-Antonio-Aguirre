# Evidence-backed dissertation architecture

Status: **recommended architecture; author/committee approval pending**
Prepared: 2026-09-15
Evidence basis: `research-audit.md`, `research-audit-validation.md`,
`claim-evidence.json`, and `../source-manifest.json`

Record approvals and replacements in `research-decisions.md`; do not edit
pending values by inference.

## 1. Recommendation

Use three research chapters connected by one statistical theme:

> How can conditional quantiles and fixed-content interval targets be learned,
> computed, and validated when dependence, nonlinear dynamics, heterogeneous
> forecast products, and limited computational budgets make a full response-
> distribution model difficult or undesirable?

The recommended chapters are the Environmetrics hydrologic application,
QDESN, and one combined MTI chapter. Treat the exdqlm article/package as shared
computational infrastructure and, if useful, a software/reproducibility
appendix. This is the most defensible current arrangement because it preserves
three distinct research questions without counting closely overlapping
variants twice.

## 2. Provisional table of contents

### Chapter 1 — Introduction and common framework

Purpose: state the dissertation question, identify the candidate's approved
contributions, and define only the concepts that are genuinely shared.

Include:

- conditional quantiles, check loss, AL/exAL working likelihoods, and dynamic
  quantile state-space background;
- the distinction between likelihood-based Bayes and loss-based generalized
  Bayes;
- a taxonomy of credible, predictive, confidence, conformal, and tolerance
  intervals;
- evaluation tools used across chapters: quantile/check loss, CRPS,
  calibration/coverage, and computational diagnostics;
- a compact exDQLM/exAL antecedent map, explicitly crediting Yan and Barata et
  al.; and
- the final, author-approved contribution and source map.

Do not force one probability model over every chapter. In particular, the MTI
loss update and TCSP tolerance action must remain distinct from response-
likelihood and posterior-predictive language.

### Chapter 2 — Source-aware correction and synthesis of hydrologic products

Primary source: `SRC-ENVIRON` at the author-approved inclusion snapshot.
Supporting sources: `SRC-SAN-LORENZO-REPRO`, `SRC-ENVIRON-CORR`, and
`SRC-EXDQLM-PKG` version 1.1.0.

Research question: how can observations, retrospective products, operational
ensemble forecasts, and forecast covariates be linked through dynamic
quantile-specific discrepancy learning and synthesized into useful predictive
distributions?

Provisional structure:

1. hydrologic decision setting and source/horizon contract;
2. source-specific exDQLM discrepancy model and transfer covariates;
3. LDVB computation and its relationship to inherited exDQLM inference;
4. post-fit quantile synthesis and scoring;
5. five-origin design, 28-day and 8-day comparisons;
6. component sensitivity and interpretability;
7. limitations: deterministic exogenous summaries, versioned inputs, five
   origins, and raw-archive reconstruction; and
8. reproducibility statement tied to the approved staged bundle.

Essential claims: the source-aware formulation, selected-model empirical
comparison, and transparent horizon split. Retain mixed 8-day evidence. Do not
claim a dense hindcast, operational deployment, or fully propagated exogenous
forecast uncertainty.

New dissertation exposition: connect the applied design to Chapter 1; explain
the exact candidate contribution; compress manuscript-specific revision prose;
and provide a self-contained data/source table without making the thesis build
depend on the reproducibility repository.

### Chapter 3 — Bayesian quantile deep echo-state networks

Primary source: `SRC-QDESN` at the author-approved inclusion snapshot.
Supporting source: the exact exdqlm comparator versions named in the source
manifests.

Research question: can fixed nonlinear reservoir features support scalable
Bayesian conditional-quantile inference and forecasting, both one quantile at a
time and across a vector of quantile levels?

Provisional structure:

1. DESN feature construction and quantile readout;
2. single-quantile AL/exAL working likelihoods and shrinkage;
3. MCMC and variational computation;
4. multi-level/composite formulation, adjacent-level shrinkage, and
   noncrossing treatment;
5. single-quantile and multi-level simulation designs;
6. GloFAS application;
7. PriceFM regional/fold comparison; and
8. limitations and future work, including composite-likelihood calibration and
   the unfinished Search Phase II campaign.

Single-quantile, joint-quantile, GloFAS, and PriceFM material should remain one
chapter. They share the fixed-reservoir quantile-readout core and do not become
independent dissertation contributions merely because they have separate
validation campaigns.

Essential interpretation: distinguish fitted conditional-quantile draws from
response trajectories; state the tail rule required for a complete predictive
distribution; and call the multi-level product a composite working likelihood,
not an ordinary joint likelihood for repeated observations. Preserve WARN/FAIL
cells, uneven coverage, and region/fold heterogeneity.

New dissertation exposition: provide one authority table for all result lines;
replace machine-specific provenance with stable source IDs and hashes; explain
how this QDESN GloFAS work differs from Chapter 2's source-correction problem;
isolate unpromoted branches as future work; and use corrected-v4 as the current
joint authority only after the stale historical manifest and Phase 181
manuscript-wiring checks are archived or repaired.

### Chapter 4 — Mean-tilted intervals: targets, tolerance actions, and dynamic extensions

Primary sources: `SRC-RQR` and `SRC-MTI-EXT` at author-approved snapshots.
Supporting source: only the immutable implementation snapshots that the source
manifests authorize.

Research question: how can fixed-content intervals be placed by a retained-mean
criterion, computed under a generalized loss update, calibrated for tolerance
use, and extended to covariate-indexed or time-varying endpoints?

Provisional structure:

1. fixed-content geometry, MPI, and the MTI tilt family;
2. score characterization and quantile-window results;
3. generalized posterior and pseudo-AL computation;
4. TCSP empirical tolerance action and calibration;
5. iid simulation and pharmaceutical illustration;
6. static endpoint regression and deterministic basis expansions;
7. dynamic endpoint states and alternating FFBS;
8. precise separation among endpoint uncertainty, response prediction, and
   tolerance confidence; and
9. limitations, including the open exact scan recursion/action-matched proof
   and absent extension validation.

The foundation and extensions should be combined now because they share the
same loss and interval geometry, while the extensions snapshot has no
implementation or empirical evidence. A separate extensions chapter becomes a
viable alternative only after it has a snapshot-matched code path, targeted
static and dynamic validation, a contribution record distinct from the
tolerance paper, and committee approval.

Critical drafting gate: before presenting TCSP as having an exact
distribution-free finite-sample guarantee, either complete and verify the proof
for the reported closed-window action or narrow the language to the numerical
calibration actually established. Simulation cannot fill this proof gap.

### Chapter 5 — Synthesis, limitations, and future research

Compare the three chapters along target, dependence representation,
computation, calibration evidence, and reproducibility—not by declaring one
method universally best. Explain when a quantile model, a synthesized response
distribution, or a tolerance action is the relevant object. Discuss open
calibration, joint-quantile, exogenous-uncertainty, regression-tolerance, and
dynamic-tolerance problems without reporting unfinished campaigns as results.

No new unsupported empirical or theoretical claim belongs here. This chapter
does not count as a replacement research unit.

### Appendices

- **A. Mathematical details:** auxiliary derivations not essential to the main
  argument; keep central theorems and assumptions in their chapters.
- **B. Computation and exdqlm infrastructure:** package version graph, LDVB and
  MCMC implementation details, diagnostics, synthesis API, and bounded tests.
- **C. Additional empirical evidence:** robustness tables, trace diagnostics,
  and secondary application panels with claim locators.
- **D. Reproducibility and provenance:** source manifest, configurations,
  software environments, seed/thread policies, artifact hashes, and explicit
  non-reproduced items.

Appendices must remain referenced from the main text. They cannot hide an
assumption, proof gap, or result needed to support a central claim.

## 3. Source-to-chapter map

| Source | Ch. 1 | Ch. 2 | Ch. 3 | Ch. 4 | Ch. 5 | Appendices | Default disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Environmetrics revised article | background | primary | — | — | comparison | data/provenance | include after gates |
| San Lorenzo reproducibility bundle | — | provenance | — | — | — | reproducibility | cite; import only approved assets |
| Environmetrics corrections | — | revision evidence | — | — | — | provenance if needed | supporting only |
| QDESN Version 2 | background | related-work distinction | primary | — | comparison | technical/robustness | include after gates |
| RQR-GIBBS current MTI paper | interval taxonomy | — | — | primary | comparison | proofs/validation | include after proof-language gate |
| MTI-EXTENSIONS | generalized-Bayes background | — | — | primary extension sections | future work | derivations | include after implementation decision |
| exdqlm article | antecedent/software map | computation support | comparator support | only if an exact dependency exists | software synthesis | primary software appendix | not an independent chapter by default |
| exdqlm package | versioned infrastructure | pin 1.1.0 | pin declared versions | immutable archive only if used | — | implementation/tests | never a live build dependency |
| Barata dissertation/AOAS paper | antecedent | attribution | attribution | — | relationship | — | cite, do not reattribute |

Historical QDESN repositories, stale worktrees, failed RQR dynamic campaigns,
and unpromoted Search Phase II work remain lineage or future-work evidence. They
do not feed chapter text or assets unless a later decision adds a fixed snapshot
and claim-driven reason.

## 4. Contribution statements to complete

Before a research chapter is drafted, fill one record per source using evidence
and coauthor confirmation:

| Dimension | Required statement |
| --- | --- |
| Conceptual | Which research question, estimand, or model formulation did the candidate originate or materially develop? |
| Theory | Which propositions, proofs, counterexamples, or corrections did the candidate produce? |
| Computation | Which algorithms, package interfaces, implementations, tests, and performance work are attributable to the candidate? |
| Empirical | Which data curation, study design, simulations, validation, figures, and interpretation did the candidate conduct? |
| Writing | Which manuscript sections and revisions did the candidate lead? |
| Inherited work | Which pieces come from named coauthors, prior publications, packages, or public methods? |
| Approval | Which coauthors/advisors/committee members confirmed the statement, and when? |

Until those records exist, use “candidate contribution to confirm,” never
author order or repository ownership as a proxy.

## 5. Drafting readiness by chapter

| Chapter | Scientific source readiness | Blocking decisions | First safe drafting unit after approval |
| --- | --- | --- | --- |
| 2 Environmetrics | High; strong manifests and bounded public validation | inclusion commit, contribution, reuse rights | problem setting and source/horizon design |
| 3 QDESN | Medium-high; rich evidence and passing current contracts, but complex authority/provenance | inclusion commit, contribution, corrected-v4 result-line approval, stale-control repair, path sanitization | target and fixed-reservoir architecture |
| 4 MTI | Medium; theory and validation present, extension evidence incomplete | contribution, TCSP claim repair, extension inclusion decision | interval targets and inferential distinctions |
| exdqlm appendix | Medium; source/article clear, archive/version gap | exact candidate contribution and 1.1.1 archive disposition | version graph and inherited-method boundary |

Chapter 2 is the recommended first drafting unit once Gates G1-G3 are closed.
It has the clearest manuscript authority, strongest public provenance bundle,
and most mature application narrative. Start with its problem/data design, not
with copied article prose or figures.

## 6. Alternative and rejection criteria

The only consequential alternative is a four-research-chapter structure that
promotes the exdqlm software article to its own chapter or separates the MTI
extensions.

Promote exdqlm only if all of the following are documented:

- candidate-specific software and methodological contributions are substantial
  and distinct from Barata's prior exDQLM work;
- the 1.1.1 article archive is tied to an immutable commit and checksums;
- the committee agrees that the software contribution is journal-suitable
  dissertation research; and
- the chapter adds an analytical contribution narrative rather than repeating
  package documentation.

Separate MTI-EXTENSIONS only if it gains:

- an immutable implementation corresponding to the manuscript equations;
- targeted static and dynamic validation with declared estimands and failure
  criteria;
- a contribution statement distinct from the tolerance paper; and
- enough independent exposition and evidence to avoid splitting one method for
  chapter count.

If neither gate passes, retain the recommended three-unit structure. If the
committee rejects any of the three recommended units, report the resulting
research-chapter gap; do not manufacture independence by relabeling an
application, variant, or appendix.

## 7. Execution order after approval

1. Author confirms the five inclusion snapshots or supplies replacements.
2. Author/coauthors complete contribution and material-specific rights records.
3. RQR source owners repair the TCSP claim boundary and stale evidence ledger.
4. Author/committee approve this architecture and whether the exdqlm/MTI
   alternatives remain appendices or future options.
5. Author separately authorizes one drafting unit; Chapter 2's problem and
   data/source design is recommended first.
6. For each unit: create an import manifest, bring in only approved material,
   rewrite for dissertation context, normalize notation, compile, inspect,
   validate claims/provenance, and make a focused local commit.
7. Push or synchronize with GitHub/Overleaf only at an explicit handoff.

The source repositories remain evidence, never runtime dependencies of the
dissertation build.
