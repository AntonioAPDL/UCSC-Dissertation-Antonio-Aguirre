# Dissertation scientific and editorial integration

This is the controlling record for the post-import dissertation review. It
connects the immutable source audit, editable manuscript derivatives, chapter
revision issues, display decisions, bibliography normalization, and validation
evidence. It does not replace the historical source audit or the institutional
requirements report.

## Current scope and evidence boundary

- Repository: UCSC dissertation checkout on muscat.
- Structural baseline: integration commit `79dbb9cc8348d9cc0ece2f23d5ade33570275055`,
  merged to `main` by `5def110d009545551e89b7efc9746c61122e8918`.
- Sources: the eight fixed commits in `../source-manifest.json`; all 102 imported
  records were rechecked against retained exact-commit audit clones on
  2026-09-16.
- Distribution: conversion present on GitHub `main`; Overleaf handoff reported
  successful by the author but not independently verified from an Overleaf log
  or artifact.
- Rights: material-specific reuse remains unverified. Distribution is not
  treated as permission.
- Computation: no research simulations, refits, or data reconstruction are part
  of this editorial review.

## Phase 0 diagnosis and repair

The imported chapters were technically self-contained, but the workflow was
not safe for post-import editing. Three defects were resolved before prose
revision:

1. **Lifecycle drift.** Current documentation still said that the conversion
   was local and unsynchronized. Lifecycle records now distinguish local
   presence, Git history, GitHub synchronization, author-reported Overleaf
   handoff, and reuse permission.
2. **Obsolete audit validation.** The audit validator required one historical
   status string. It now checks allowed states and cross-state invariants; unit
   tests cover invalid conversion, review, GitHub, and Overleaf combinations.
3. **Unsafe import provenance.** Import manifests treated the current chapter
   bytes as the baseline and the importer could overwrite them. Schema 2 keeps
   immutable source/destination baseline hashes while
   `revision-ledger.json` records editable derivatives. The importer is
   check-only by default; explicit regeneration is restricted to a clean
   `regenerate/*` branch whose destinations still match the baseline.

## Validation tiers

Use `scripts/validate.sh` with Python 3.11:

- **Fast:** `bash scripts/validate.sh --tier fast [--audit-root PATH]`. Runs
  lifecycle tests, audit and import validation, optional immutable-blob checks,
  and `git diff --check`. Use during controlled edits.
- **Chapter milestone:** `bash scripts/validate.sh --tier chapter --audit-root
  PATH`. Adds the complete thesis build and blocking-log/PDF checks. Use after
  each chapter-sized unit.
- **Release:** `bash scripts/validate.sh --tier release --audit-root PATH`.
  Requires source-blob verification and builds into a new timestamped directory
  under `build/`, preserving earlier PDFs. Follow with systematic rendered-page
  inspection and the institutional checks in `VALIDATION.md`.

A PDF SHA identifies one build artifact; it is not evidence of bitwise
reproducibility because ordinary pdfTeX creation metadata changes.

## Phase sequence

1. Phase 0: lifecycle and edit-safe provenance — complete.
2. Phase 1: read-only scholarly audit and revision ledger — complete.
3. Phase 2: global architecture, notation, bibliography, and display decisions
   — complete.
4. Phase 3: chapter revisions in order 2, 3, 4, 5 — complete.
5. Phase 4: cross-chapter prose and typography review — next.
6. Phase 5: dissertation introduction, synthesis, and abstract.
7. Final release validation and explicit GitHub/Overleaf handoff.

Substantive chapter work must record a `REV-*` entry in
`revision-ledger.json`, update the corresponding current hash, pass the relevant
validation tier, and preserve the source-to-baseline mapping.

## Decision boundaries

Editorial work may proceed with collective or chapter-centered attribution.
The following facts may not be inferred:

- individual conceptual, theoretical, computational, empirical, or writing
  allocations among the candidate and coauthors;
- committee acceptance of the software chapter as an independent research
  unit;
- final publisher/coauthor reuse permission;
- a stronger TCSP guarantee than the source evidence proves;
- implementation or empirical validation of MTI extensions absent from their
  audited source;
- final administrative title, date, committee roles, dean wording, or AI-use
  disclosure requirement.

The detailed Phase 1 issue, display, notation, and bibliography records are
maintained below as the audit proceeds.

## Phase 1 scholarly audit result

The audit found 29 actionable issues in `editorial-issues.json`: two current
decision boundaries, 20 additional major issues, and seven moderate issues.
The two boundaries do not prevent conservative editing:

- candidate-specific contribution prose remains collective until the author
  confirms granular roles; and
- Chapter 5 must narrow TCSP/tolerance language to the proved and empirically
  validated scopes rather than assume the missing stronger result.

Administrative placeholders remain blocking for filing but not for research-
chapter integration.

### Baseline scale and reader burden

The successful 367-page build contains approximately 36 Roman-numbered
frontmatter pages and 331 body/bibliography pages. At the conversion baseline:

| Unit | Approximate PDF span | Source size | Principal audit finding |
| --- | ---: | ---: | --- |
| Chapter 1 | 2 pages | 16 lines | TODO scaffold only |
| Chapter 2 | 67 pages | 1,729 lines | sound software/article baseline; technical blocks interrupt the package narrative |
| Chapter 3 | 48 pages | 706 lines | coherent application; journal headings, interval terminology, and repeated support displays remain |
| Chapter 4 | 102 pages | 3,500 lines | core Q-DESN method follows a long Gaussian supplement; duplicate conventions and audit/supplement headings remain |
| Chapter 5 | 99 pages | 2,783 lines | duplicated theorem/proposition and protocol/application material; extension evidence is theory-only |
| Chapter 6 | 1 page | 9 lines | TODO scaffold only |

The 44 figures and 51 tables create roughly 28 frontmatter list pages. The
display ledger covers all 95 labeled environments: 46 KEEP, 30 MERGE, 18
TEXT-SUMMARY, and 1 OMIT. These decisions preserve central definitions,
comparisons, negative findings, and claim-bearing evidence while removing the
replication-archive feel of the imported supplements.

### Chapter-level revision architecture

**Chapter 2 — exdqlm.** Keep the contribution software-centered. Establish the
statistical model and version boundary, then organize the chapter around package
architecture, inference interfaces, diagnostics/forecasting, and the four
examples. Integrate derivations beside the implemented interface they justify.
Retain the Big Tree held-out result in which direct regression outperforms the
transfer model; do not imply predictive superiority from the training metrics.

**Chapter 3 — Environmetrics application.** Convert headings to thesis style,
replace paper navigation, and call central bands from synthesized future-response
distributions posterior predictive bands/intervals. Keep fitted quantile-curve
credible intervals distinct. Preserve the five-origin limit, separate 28-day
and common 8-day horizons, and avoid an operational-hindcast claim.

**Chapter 4 — Q-DESN.** Put the inferential target, fixed DESN feature map, and
Q-DESN formulation before the Gaussian baseline derivation. Use the Gaussian
model as an exact baseline and initialization device. Merge the two
distributional-convention sections; integrate supplement/audit material into
computation, simulation, application, or limitations. Keep overlapping score
intervals, review-status diagnostics, the cap-stabilized GloFAS fit, and the
heterogeneous PriceFM comparison explicit.

**Chapter 5 — RQR/MTI.** Merge each duplicated theorem/proposition statement
with its proof and consolidate the empirical-balance, tolerance-validation, and
pharmaceutical-application pairs. Preserve generalized updating as distinct
from an ordinary response likelihood and endpoint draws as distinct from
posterior predictive response draws. Present MTI extensions as theoretical or
proposed constructions because the audited repository has no implementation or
empirical validation.

### Common notation and terminology map

Global macros in `notation.tex` define only genuinely shared objects. Chapter-
specific symbols remain local when the same letter has a different conditioning
set or target.

| Concept | Dissertation convention | Boundary to preserve |
| --- | --- | --- |
| Quantile level | `\tau` for a generic target; ordered grids use `\tau_1<\cdots<\tau_L` | Do not silently replace source `p`/`p_0` inside package API names or fixed equations |
| Conditional quantile | `Q_\tau(Y\mid\mathcal F)` with the conditioning information stated locally | Fitted quantile-location curves are not predictive response intervals |
| Working likelihood | Explicitly call AL/exAL a likelihood or working likelihood according to the chapter's inferential use | Chapter 5 generalized Bayes is loss-based, not an ordinary response likelihood |
| Posterior approximation | MCMC, VB, and Laplace--Delta are named separately | Approximate intervals must not be described as exact posterior intervals |
| Prediction | Posterior predictive distribution/draw/interval only for a future-response distribution | Parameter, endpoint, and loss-target draws retain their own names |
| Tolerance statement | Content `c` and confidence `1-\alpha` stated together | Empirical attainment is not a distribution-free guarantee |
| Reservoir state | `h_t` or the source-defined bold variant, with dimension and fixed/random status stated | Do not unify reservoir and state-space latent states merely because both are time indexed |
| Scores | CRPS, average finite-grid check loss/aCRPS, MAE, RMSE, and PPLC named with orientation and evaluation sample | Oracle recovery diagnostics are not proper scores against realized observations |

### Bibliography diagnosis

The baseline has 233 entries and 124 cited keys. The canonical map records 11
semantic-overlap groups. Most are identical works imported under chapter
prefixes. Three require more than key deduplication:

- the QDESN Nishimura--Suchard entry contains the DOI and pagination of a
  different Bayesian Analysis paper;
- the Environmetrics Yang--Wang--He entry has incorrect full author names and
  omits the DOI; and
- the journal record for Bayesian predictive decision synthesis misnames Emily
  Tallman as Elliott.

The canonicalization pass must update citations before deleting duplicate
entries and retain this mapping as provenance.

### Acceptance criteria before Chapter 2 editing

- All three editorial ledgers validate.
- The source and import validators pass, including fixed-blob checks when the
  retained audit root is available.
- The chapter revisions can differ from the immutable import hashes without
  disabling provenance checks.
- No source repository is a thesis build dependency.
- Collective attribution, conservative TCSP wording, and unverified reuse
  status remain explicit.

## Phase 2 global integration result

The author-directed four-project architecture in `chapter-plan.md` is retained.
The notation and terminology table above is the controlling global map; symbols
remain chapter-local where their targets or conditioning sets differ. The
display ledger supplies an explicit disposition for every imported labeled
display, so display reduction can occur within each chapter without a second
global inventory.

The 11 bibliography groups in `bibliography-map.json` are implemented. Affected
citations now use the canonical keys, superseded or erroneous duplicate records
are removed, and the map retains the old-to-new provenance. The current thesis
uses 118 bibliography keys. The chapter milestone build resolves every cited
key and contains the corrected Nishimura--Suchard, Tallman--West, and
Yang--Wang--He records.

This pass intentionally did not flatten chapter-specific notation or relocate
technical content before the chapter-level scientific edits. Chapter 2 is the
next revision unit.

## Chapter 2 revision result

Chapter 2 now follows a dissertation-first software argument. The statistical
foundations lead to package architecture and object behavior before the detailed
posterior targets and numerical blocks. Article navigation and references to
omitted code listings were removed. The package-version boundary distinguishes
the Chapter 3 application snapshot (1.1.0), this chapter's recorded analysis
(1.1.1), and the later audited support snapshot (1.1.2).

All 19 Chapter 2 display decisions are implemented. Fourteen central displays
remain. Three interface/control tables were merged into exact prose, while the
Lake Huron trace display and the separate Big Tree state display were replaced
by numerical and inferential summaries already supported by the recorded
analysis. The Big Tree section continues to report that direct regression has
the lowest held-out check loss and CRPS; the training diagnostics are not used
to claim transfer-model superiority.

## Chapter 3 revision result

Chapter 3 now reads as a hydrologic application chapter rather than a journal
submission. Its argument proceeds from the forecast problem and quantile-based
model through computation, the five-origin validation design, comparative
results, component-removal sensitivity, and interpretation. Journal navigation
and all-capital headings have been removed. Central bands from synthesized
future-response distributions are called posterior predictive bands; credible
interval language remains only for fitted quantile-location curves and
parameter summaries.

All 21 Chapter 3 display decisions are implemented. The 12 KEEP records remain
as claim-bearing displays. The drought and wet-period diagnostics are paired in
one figure, and four forecast-origin support panels are paired in two figures.
The univariate transfer-active illustration and two secondary source-parameter
tables are summarized in prose. The chapter continues to state that its
comparison uses five rolling origins, distinguishes the 28-day GloFAS and
common 8-day NWS horizons, and is not a dense continuous hindcast.

## Chapter 4 revision result

Chapter 4 now introduces the nonlinear conditional-quantile problem, fixed
DESN feature map, and Q--DESN regression before using the Gaussian DESN as an
exact baseline and initialization device. One shared distributional-convention
section replaces the repeated source sections. Posterior computation, joint
quantile inference, scoring, simulations, the GloFAS study, and the PriceFM
comparison now form one thesis argument; source-packet navigation, audit
headings, and repeated feature-map exposition have been removed.

All 36 Chapter 4 display-ledger records are implemented: 13 KEEP, 17 MERGE,
five TEXT-SUMMARY, and one OMIT. Paired forecast and fit-recovery panels use
continued two-page thesis displays. The MCMC family tables remain the
claim-bearing interval summaries; separately selected variational panels are
not presented as a controlled approximation-error comparison. Secondary
GloFAS, PriceFM, five-chain, and joint-simulation displays are consolidated or
summarized with their exact conclusions retained.

## Chapter 5 revision result

Chapter 5 now presents one progression from contiguous fixed-content interval
functionals through MPI/MTI identification, empirical score balance,
fixed-target computation, the TCSP action and validation study, the
pharmaceutical illustration, and proposed regression and dynamic extensions.
The quantile-window theorem and fixed-content mean-tilt proposition each appear
once with an attached proof; the global result retains one theorem statement
and its profiling proof. Article/supplement duplicates in empirical balance,
validation, and the application have been integrated by topic.

All 21 Chapter 5 display decisions are implemented: seven KEEP, six MERGE, and
eight TEXT-SUMMARY. The tolerance and pharmaceutical table/figure pairs now
use the claim-bearing tables with the paired visual evidence stated in exact
prose. Secondary simulation, diagnostic, width, and sensitivity displays are
represented by exact numerical or inferential summaries. The source assets
remain covered by the immutable import provenance.

The audit also exposed an opposite tilt sign in the extension midpoint-loss
formula. It now agrees with the authoritative root-form loss, score derivative,
canonical-vector shift, and retained-mean target \(\mu+\delta\). TCSP is
described as numerically scan-calibrated and empirically validated: exact scan
recursion and a finite-sample proof matched to the adaptive closed-window action
remain open. MTI-ECM findings remain repeated-sampling evidence, and the
regression/dynamic extensions are explicitly proposed because the audited
snapshot has no matching implementation, experiments, tests, or provenance
manifest.

The chapter preserves the evidence boundaries identified by the audit. The
single-quantile intervals condition on one reproducible dynamic root per
family and quantile level; VB--LD evidence remains incomplete; diagnostic
review status is retained for 10 of 32 posterior-score cells and all 16 exAL
scale-asymmetry assessments. The GloFAS joint AL result is described as
cap-stabilized rather than strictly converged. The PriceFM comparison remains
heterogeneous: Q--DESN has lower AQL in 54 of 114 region--fold cases, PriceFM
in 60, with means 7.217 and 7.039, respectively.

## Phase 4 cross-chapter review result

The paragraph-level scan found few remaining promotional markers after the
chapter revisions. Uses that name established statistical concepts, such as
robust regression, were retained. Generic claims were replaced with the exact
operation or evidentiary scope: Chapter 3 now calls VB a lower-cost approximate
alternative to MCMC, and Chapter 4 describes what its fixed simulation and
retrospective studies document rather than treating them as general
demonstrations of performance. Collective authorship language and all negative
or limited findings were retained.

Typography is now selected by display. Tables and algorithms remain single
spaced, but the preamble no longer forces all of them to `scriptsize`.
Ordinary retained tables use `small`; the long Chapter 2 API reference,
Chapter 3 algorithms, reservoir-design table, and Chapter 5 tolerance table
use the compact style because normal type caused measured overflow or an
oversized float. Thirty-six Chapter 4 equation groups were restored from
blanket `scriptsize`; the DESN recursion alone uses local `small`, and the other
wide equations were split across aligned lines. The final TeX log reports zero
overfull boxes and zero oversized floats. The case-specific pages listed in
`VALIDATION.md` were rendered and inspected.

No notation was globally replaced where the chapters define different targets.
The controlling distinctions remain explicit: working versus ordinary
likelihoods, exact posterior simulation versus VB approximation, parameter or
endpoint uncertainty versus response prediction, and empirical tolerance
attainment versus a finite-sample guarantee. Chapters 2--5 are stable inputs
for the dissertation introduction, synthesis, and abstract.
