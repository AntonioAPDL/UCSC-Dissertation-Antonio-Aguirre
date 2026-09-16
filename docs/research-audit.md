# PhD research-source audit

Status: **completed at fixed discovery snapshots; revised for the author's
four-project direction; focused confirmations pending**
Audit date: 2026-09-15
Controlling method: `research-audit-master-plan.md`
Machine-readable records: `../source-manifest.json` and
`claim-evidence.json`; bounded check record: `research-audit-validation.md`

## 1. Decision summary

The inspected work supports a coherent dissertation centered on **statistical
learning for conditional quantiles and interval targets under dynamic,
computational, and data-product constraints**. After reviewing the current
manuscript contribution statements and the author's instruction to organize
the dissertation around four main projects, the working architecture is:

1. the `exdqlm` software and computational workflow;
2. source-aware quantile correction and predictive synthesis for hydrologic
   products;
3. Q-DESN for nonlinear time-series quantiles, including its single- and
   multi-quantile formulations and two applications; and
4. mean-tilted intervals, combining the short-tolerance-interval foundation
   with the regression and dynamic extensions.

The `exdqlm` promotion is evidence-based but provisional. Its audited article
states five substantial software contributions and includes a methods appendix,
four examples, an R package, and a reproducibility contract. It is distinct in
purpose from the hydrologic and QDESN chapters. It must nevertheless preserve
the boundary around inherited work: the exAL distribution, exDQLM state-space
model, original MCMC/ISVB, and transfer-function foundations come from Yan and
Barata et al. Raquel Barata's dissertation and the AOAS article document those
foundations ([dissertation](https://escholarship.org/uc/item/0bq4107v),
[AOAS article](https://doi.org/10.1214/21-AOAS1497)). The committee should
confirm that the candidate's software-centered contribution counts as a
journal-suitable research unit.

The two MTI papers remain one project chapter at their current evidence level.
This avoids counting QDESN variants or closely linked MTI manuscripts as
independent contributions merely to increase the chapter count. The source
record supports project-level content and collaborator identification; granular
individual contribution allocation and material-specific reuse rights still
require focused confirmation.

The audit found five issues that should be fixed before drafting:

- **Critical claim boundary:** the RQR/MTI tolerance paper's exact scan
  recursion and a finite-sample proof matched to the reported closed-window
  TCSP action remain open. Numerical scan calibration and simulation evidence
  cannot be promoted to an exact theorem.
- **Stale RQR evidence ledger:** an August 13 ledger describes confirmatory
  validation as planned, while the current manuscript and tracked artifacts
  report it completed. The ledger must be refreshed or explicitly archived.
- **Stale QDESN validation wiring:** the current corrected-v4 joint projection
  passes its hash and focused checks, but a historical joint-asset manifest has
  13 mismatches in 14 rows and two Phase 181 check scripts still expect
  superseded manuscript inputs. Archive or update those historical controls
  before using them as dissertation provenance.
- **Working source authority and unresolved rights:** the author has directed
  use of the audited current documentation as the working drafting base. A
  later submitted snapshot may still replace it, and coauthor, publisher, and
  repository-level direct-reuse permissions remain unverified.
- **Software/provenance fragmentation:** the hydrology application pins
  `exdqlm` 1.1.0, the software article describes 1.1.1, and current package
  `main` is 1.1.2. Some QDESN and Environmetrics provenance records retain
  machine-specific paths, while the exdqlm article's named replication
  archives are not tracked at its audited commit.

No dissertation prose or research asset was imported. No original research
working tree was changed. No full simulation campaign or selected-model refit
was run, so no source is assigned evidence level `E4`.

## 2. Scope, method, and limits

The author nominated five seed repositories: QDESN Version 2, the revised
Environmetrics application, RQR-GIBBS, MTI-EXTENSIONS, and the exdqlm article.
Three additional public repositories entered scope because the seed sources
explicitly require them: the exdqlm package, the San Lorenzo reproducibility
bundle, and the Environmetrics corrections repository. Historical or similarly
named repositories were treated as leads only; account-wide inspection was not
performed.

For each included source, the audit:

1. fixed a discovery and audit commit;
2. separated default-branch state from unfinished branches and local runtime
   worktrees;
3. read repository instructions, the main manuscript, supplements, authority
   records, manifests, and the implementation paths needed for central claims;
4. classified the statistical target, likelihood or loss update, uncertainty
   object, theoretical claims, empirical design, limitations, and antecedents;
5. checked tracked provenance and ran only bounded validation in isolated audit
   copies; and
6. recorded claims and conflicts in `claim-evidence.json` using levels `E0` to
   `E4` defined by the master plan.

This was a source, provenance, and scientific-claims audit. It was not an
independent peer review, proof verification line by line, raw-data
reconstruction, or full computational replication. An `E3` result means a
specific build or test contract passed in an isolated copy; it does not
validate every scientific conclusion in the repository.

## 3. Fixed source inventory and version dossiers

| ID | Fixed audit commit | Authority diagnosis | Dissertation role |
| --- | --- | --- | --- |
| `SRC-ENVIRON` | `1272bfc10442a28add5a4c74ff641e9b9a8e9666` | Current revised `main`; manuscript and asset manifest agree | Recommended chapter |
| `SRC-QDESN` | `757522db0f85815244370ec92a194de132268883` | Current article `main`; newer Search Phase II branches are unpromoted work | Recommended chapter |
| `SRC-RQR` | `73887b9c86ef767aa1567c660718667945630aef` | Current `main` and current short-tolerance manuscript; old local checkout was stale | Recommended combined MTI chapter |
| `SRC-MTI-EXT` | `f345d946aa5a81b94795838bec58d874a0fdd0c9` | Sole branch; compact theory manuscript without implementation/results | Combine with MTI foundation |
| `SRC-EXDQLM-ARTICLE` | `d5534e97db8414fd875022261d4c530eae4676e4` | Current JSS-facing article `main` | Provisional fourth research chapter; committee counting confirmation pending |
| `SRC-EXDQLM-PKG` | `e51045a4324901cced27ca2aaa22569afbc8e0e6` | Current package `main`, version 1.1.2; not the freeze for every paper | Shared implementation dependency |
| `SRC-SAN-LORENZO-REPRO` | `a8797b804271b46c62bd04dab7dba6b84a10ab7d` | Public staged reproducibility bundle | Environmetrics provenance |
| `SRC-ENVIRON-CORR` | `b1ceeb610d20f8287e4ca44e146c9cfdbcda1ee6` | Revision/response and table cross-check evidence | Environmetrics supporting source |

### 3.1 Authorship identifiers

| Source | Names in the audited manuscript/package metadata |
| --- | --- |
| Environmetrics | Antonio De Leon, Raquel Prado, Bruno Sansó |
| QDESN | Antonio De Leon, Raquel Prado, Bruno Sansó |
| RQR-GIBBS | Antonio De Leon, Raquel Prado, Bruno Sansó |
| MTI-EXTENSIONS | Antonio De Leon, Raquel Prado, Bruno Sansó |
| exdqlm article | Antonio De Leon, Raquel Barata, Raquel Prado, Bruno Sansó |
| exdqlm package | Raquel Barata (`aut`, `cre`), Raquel Prado (`ths`), Bruno Sanso (`ths`), Antonio Aguirre (`aut`) |

These records identify named authors, not complete contribution allocation.
The author has resolved the identity mismatch: use **Antonio de Leon** as the
primary scholarly name and **Jose Antonio Aguirre Perez de Leon** as the
official long dissertation name. “Antonio De Leon” in manuscripts and “Antonio
Aguirre” in package metadata refer to the same candidate. Preserve immutable
source spellings where required for accurate citation; an ORCID remains to be
supplied.

The repositories contain enough evidence to recover each project's purpose,
methods, joint contribution statement, and collaborators. Environmetrics also
identifies the candidate as corresponding author and explicitly calls the work
part of the candidate's dissertation; the other project manuscripts list the
candidate first. The project contribution paragraphs use collective language
and do not assign individual theory, implementation, empirical, or writing
tasks. Source-based chapter drafting can therefore proceed with neutral
project-level wording, but final singular candidate-role statements still need
author/coauthor confirmation.

### 3.2 Branch and worktree triage

QDESN has 192 public heads. At the audit date, 36 cached remote branches were
not ancestors of `main`; most are archives, execution branches, or narrowly
scoped validation work. The newest GloFAS Search Phase II RHS branch is six
commits ahead of the audit snapshot but changes application code, tests, and
execution notes rather than the article. Its own records prohibit manuscript
promotion until declared screening and confirmation gates pass. It therefore
does not supersede `main`. An article-only Overleaf snapshot is deeply divergent
and is not a scientific authority.

The original QDESN checkout also has 172 registered worktrees and a large
ignored runtime footprint. Those worktrees are operational history, not 172
candidate research products. The audit used repository metadata to identify
relevant deltas and did not traverse or mutate them.

RQR-GIBBS has 49 public heads spanning the older RQR/DESN development line,
failed or non-promoted dynamic-model campaigns, tolerance validation, and
Overleaf snapshots. The pre-existing local checkout exposed only an older
cached `main` and could not establish the current manuscript. The fixed remote
`main` and its public arXiv v3 are the appropriate audit sources; branch-only
failed campaigns remain negative/lineage evidence.

The Environmetrics repository has six heads and a clean matching default-branch
checkout. MTI-EXTENSIONS has one head. The exdqlm article has six substantive
heads; current `main` is newer and more complete than its one unmerged analysis
branch. The exdqlm package has 90 heads and 76 not merged into current `main`;
these include project-specific validation and release branches. They are useful
for lineage, but each manuscript must use its declared package freeze rather
than the newest branch tip.

### 3.3 Public manuscript status

The current Environmetrics manuscript is publicly represented by arXiv
[`2608.11222`](https://arxiv.org/abs/2608.11222); the exdqlm article by arXiv
[`2607.22760`](https://arxiv.org/abs/2607.22760); and the short-tolerance MTI
manuscript by arXiv [`2607.26098`](https://arxiv.org/abs/2607.26098). The
author's research page describes the
first two and the MTI extensions as submitted and QDESN as a working paper
([research page](https://antonio-de-leon.com/research/)). These are useful
version/status signals, not evidence of acceptance or a substitute for the
author's submission records. Exact submitted files and later revisions remain
an inclusion decision.

## 4. Scientific target map

| Project | Target | Update/model | Uncertainty or interval object | Non-negotiable interpretation |
| --- | --- | --- | --- | --- |
| Environmetrics | Time-varying conditional flow quantiles and a synthesized marginal predictive distribution | exAL/DQLM observation model, dynamic source discrepancies, LDVB; separate quantile fits plus post-fit synthesis | Credible bands for fitted quantile curves; posterior-predictive bands/draws after synthesis | Five-origin empirical validation is not a dense operational hindcast |
| QDESN single | Conditional time-series quantiles on fixed DESN features | AL or quantile-fixed exAL working likelihood with ridge/RHS; MCMC or VB | Quantile/readout uncertainty; optional response draws need a declared tail rule | Fitted quantile draws and response trajectories are different |
| QDESN joint | Vector of conditional quantile levels with shared features | Product/composite working likelihood plus adjacent-level shrinkage | Joint coefficient/quantile summaries; monotone scoring/rearrangement as declared | Repeating a response across factors is not an ordinary joint response likelihood |
| RQR/MTI foundation | Fixed-content interval endpoints; MPI is zero tilt and MTI varies retained-mean tilt | Generalized Bayes from residual-product loss; pseudo-AL augmentation for computation | Endpoint-functional generalized-posterior summaries | Endpoint draws are not response-predictive draws |
| TCSP | Shortest closed sample interval after retained-count calibration | Uniform scan calibration followed by shortest order-statistic window | A frequentist tolerance action | Its guarantee does not come from the MTI generalized posterior |
| MTI extensions | Covariate-indexed or time-varying endpoint roots | Static generalized posterior; basis expansion; alternating conditional-Gaussian/FFBS dynamic updates | Endpoint coefficient/state uncertainty | Response prediction and tolerance coverage require separate models/calibration |
| exdqlm package | Dynamic or static response quantiles, generally one level at a time | exAL/DQLM likelihood with MCMC, LDVB, or legacy ISVB | Posterior or variational summaries and response predictive simulation | `quantileSynthesis()` is post hoc across separate fits, not a joint multi-quantile posterior |

This map is the dissertation's main safeguard against false synthesis. The
projects can share notation and computational background, but their targets and
guarantees cannot be collapsed into one generic “uncertainty interval.”

## 5. Project dossiers

### 5.1 Environmetrics: hydrologic correction and synthesis

The manuscript, *Bayesian Quantile-Based Correction and Synthesis of Hydrologic
Products*, links USGS observations, retrospective products, operational
forecasts, and forecast covariates through a shared latent quantile process and
source-specific dynamic discrepancies. Quantile levels are fitted separately;
their predictive outputs are adjusted and synthesized into a per-time marginal
predictive distribution. The article also adapts Laplace-delta variational
inference for exDQLM scale/skewness computation.

Its application design is unusually well documented. Five rolling forecast
origins use post-cutoff USGS values strictly as verification. The 28-day table
compares horizon-compatible GloFAS and Bayesian predictive distributions. A
separate leads-1-to-8 table permits comparison with the shorter NWS ensemble.
The manuscript reports exAL-M-T1 as the lowest-CRPS Bayesian candidate at all
five 28-day origins, while the 8-day findings are mixed. Component-removal
results support retaining the selected trend, transfer, and multi-frequency
seasonal blocks within this fixed design. These are empirical findings at five
versioned origins, not universal superiority claims.

The source has a strong internal provenance layer: a manuscript asset manifest,
frozen HE2 publication inputs, generated-table contracts, figure/table
crosswalks, software and forecast-design contracts, and a companion public
bundle. The public bundle starts from curated model-ready inputs and includes
expected outputs and hashes. Its fast validator passes in the isolated audit
copy, reaching `E3` for that bounded artifact contract. The full fitting
campaign and raw archive construction were not run. Raw climate-center
retrievals and intermediate covariate preprocessing are deliberately absent.

Important limitations to preserve:

- GEFS precipitation and shallow-soil-water forecasts enter as deterministic
  summaries rather than a joint exogenous uncertainty model;
- five feasible/versioned origins are not a dense hindcast;
- source availability, product version, horizon, and spatial extraction are
  part of the estimand and cannot be normalized away; and
- fitted-quantile credible bands differ from synthesized predictive bands.

The current reproducibility bundle's LICENSE grants inspection/evaluation only
while the final license is pending. No assets should be copied until the
authors approve the specific material and license. The article's commented-out
author-contribution section leaves candidate credit unresolved. Subject to
those gates, this is the most mature and self-contained dissertation chapter.

### 5.2 QDESN: nonlinear conditional quantile forecasting

The current manuscript, *Bayesian Quantile Deep Echo State Networks for
Nonlinear Time Series*, combines deterministic deep echo-state features with
Bayesian quantile readouts. It presents:

- independent single-quantile AL and quantile-fixed exAL fits with ridge or
  regularized-horseshoe-family shrinkage;
- a multi-level formulation using a composite working likelihood and
  adjacent-level shrinkage;
- MCMC and variational computation;
- single- and joint-quantile simulations; and
- GloFAS and PriceFM applications.

These elements form one linked contribution line: the same reservoir/readout
idea is evaluated under different fitting and application regimes. Splitting
single quantile, joint quantile, GloFAS, and PriceFM into separate dissertation
chapters would duplicate the core method and over-count variants. They fit best
as one research chapter with a clearly staged method section and two
application subsections.

The tracked evidence is extensive. The single-quantile authority manifest fixes
train-only preprocessing and rolling-origin evaluation and retains PASS, WARN,
and FAIL outcomes; all 14 files in its artifact block match their hashes. The
current corrected-v4 joint projection has 17 tracked assets whose hashes and
focused checker pass. The GloFAS presentation manifest ties 12 tracked figures,
tables, scripts, and evidence files to the Part 4 Joint-AL issued-window
selection, and all 12 hashes pass; FR09 remains the stronger historical-fit
guardrail. PriceFM's R98 projection covers 38 regions and three folds: QDESN
has lower AQL in 54 of 114 region-fold comparisons and PriceFM in 60; all 10
projected output hashes and the R98 article checker pass. This supports
heterogeneous evidence, not uniform dominance.

The repository also retains superseded controls that must not be mistaken for
the current authority. Thirteen of 14 entries in
`joint_qdesn_article_validation_asset_manifest.csv` no longer match the tracked
files, consistent with a later promotion record, and two Phase 181 check scripts
fail because they require manuscript inputs that the corrected-v4 integration
replaced. The current corrected-v4 checker and focused test both pass. These are
stale validation-wiring defects, not evidence that the current projection
failed.

The GloFAS evidence is narrow: the current main article uses one forecast
window and reports empirical interval/quantile behavior. One candidate has poor
reported coverage, and an inference iteration cap remains visible. PriceFM is
region- and fold-dependent. The discussion already acknowledges that joint
composite-likelihood calibration, broader GloFAS evaluation, and broader
PriceFM evidence remain open. Those limitations are strengths of the source
record and should survive dissertation adaptation.

The largest provenance weakness is portability. Some tracked result ledgers
contain absolute paths into historical worktrees. Their hashes and immutable
commits are still useful, but dissertation records must replace paths with
stable source IDs and relative locators. Large ignored QDESN output trees are
not evidence unless a later author decision identifies a concrete artifact,
snapshot, and generation contract.

All three QDESN documents build under the server's TeX Live 2018 environment:
the main article is 22 pages, the main supplement 49 pages, and the Gaussian
DESN supplement 9 pages, with no unresolved citation or cross-reference
warnings after the required passes. This is document/build evidence only; the
expensive simulation and application campaigns were not rerun.

The audit recommends the fixed `main` commit above as the current audit
snapshot. The newer Search Phase II branches contain a prospective GloFAS
search whose own gates are unfinished; they must not enter the chapter unless
later completed, integrated, audited, and selected by the author.

### 5.3 RQR/MTI: interval targets and tolerance actions

The current RQR-GIBBS manuscript is *Mean-Tilted Intervals: Short Tolerance
Intervals*. The old “relaxed quantile regression” name survives in code and
lineage documents, but the present scientific object is a fixed-content
interval family indexed by retained-mean tilt. At zero tilt, the population
target is the mean-preserving interval under the stated regularity conditions.
The manuscript develops score characterizations and quantile-window
identification, then separates three layers:

1. the population/empirical interval target;
2. generalized-Bayes endpoint computation under exponentiated loss; and
3. the TCSP tolerance action, which calibrates a retained order-statistic count
   and then selects the shortest closed window.

This separation is essential. The pseudo-AL construction is an algebraic
augmentation of the loss update, not a response likelihood. Generalized-
posterior endpoint draws are not response draws. The finite-sample tolerance
statement is attached to the empirical TCSP action, not the generalized
posterior or its MTI-ECM mode comparator.

The current manuscript reports a completed 1000-replication paired study over
eight distributions, four sample sizes, three content levels where feasible,
and 95% confidence. The supplement says 288,000 result rows contribute to the
reported summaries. Across 72 feasible cells, it reports TCSP attainment
between 95.3% and 99.6%, MTI-ECM between 95.1% and 99.9%, Young-Mathew between
94.1% and 97.2%, and Wilks between 95.3% and 100%; MTI-ECM has lower cellwise
median width than TCSP in 38 cells. Bounded table/figure contract tests pass in
the isolated audit copy (`E3`). These remain empirical validation findings.

The central unresolved issue is theoretical, not computational: the manuscript
explicitly leaves an exact scan recursion and a finite-sample proof matched to
the closed-window convention as open problems. Its wording elsewhere calls
TCSP distribution-free. Before dissertation drafting, the claim should be
made action-accurate in one of two ways: supply and verify the missing theorem,
or state that the retained count is conservatively calibrated by Monte Carlo
with a confidence bound and describe the corresponding guarantee without
claiming an unavailable exact recursion.

The pharmaceutical illustration uses 187 batches for product code 23 and 1000
paired splits with 100 training and 87 holdout batches. The manuscript treats
held-out content as a descriptive stability measure, not a regulatory result;
the dissertation should do the same.

The companion MTI-EXTENSIONS paper develops static endpoint regression,
deterministic basis expansions, and dynamic endpoint-state models. Its dynamic
augmented target is jointly quartic in the two root paths but conditionally
linear-Gaussian in one path given the other, motivating alternating FFBS.
Regularized-horseshoe computation is restricted to the zero-tilt case unless
further propriety work is supplied. The paper explicitly withholds predictive
and tolerance guarantees.

At the audited commit MTI-EXTENSIONS has only eight tracked files: the main and
supplement manuscripts, bibliography, instructions, build files, and ignore
rules. It contains no implementation, tests, results, manifest, or license.
Older RQR-GIBBS code supplies lineage but is not wired to this exact manuscript
snapshot. Consequently, the extensions strengthen one combined MTI chapter but
do not yet justify a separate chapter. A later separation would require a
snapshot-matched implementation, targeted static and dynamic validation,
distinct contribution statement, and committee agreement that the extension
is an independent journal-suitable unit.

### 5.4 exdqlm article and package

The exdqlm article's boundary is unusually clear. It identifies Yan's exAL
distribution/static regression, Barata et al.'s exDQLM/MCMC/ISVB/transfer
work, and general nonconjugate VB as its foundations. It describes its own
contribution as an integrated R software workflow with composable model
construction, coordinated inference engines, fitted-object methods,
diagnostics, forecasting, post-fit synthesis, static shrinkage routines, C++
acceleration, and reproducibility materials.

The article also retains useful negative evidence. In the Big Tree holdout,
direct regression beats the transfer-function model on check loss and CRPS;
the transfer example demonstrates the interface rather than predictive
superiority. In the sparse static benchmark, LDVB is faster, while MCMC has
lower holdout quantile RMSE at all three fitted levels. Post-fit synthesis is
not a joint multi-quantile posterior. These statements should be retained if
the dissertation uses this material.

The version graph cannot be flattened:

| Use | Version | Snapshot evidence | Consequence |
| --- | --- | --- | --- |
| Environmetrics application | 1.1.0 | Tag `cran-v1.1.0`, commit `4c50b078abec33b9d752160911f7dfe841f818a7` | Preserve for application results |
| exdqlm article and QDESN v14 comparator | 1.1.1 | Commit `6dba6f2863705e0e90f0ce19e0c75d106d022a52` plus article/manifest records | RNG and scale-skewness update; no matching release tag in the audited package repo |
| RQR documented development source | 0.6.0.9000 | Branch snapshot `dffb71ee70b597d6a716ee74be1cbc99731cd453` | Preserve only for the exact RQR implementation claims that name it; do not replace with package `main` |
| Current package `main` | 1.1.2 | `DESCRIPTION` and `NEWS.md` | Adds Cholesky FFBS reproducibility repair; not a drop-in provenance replacement |

The article describes `exdqlm_1.1.1.tar.gz`, a replication archive,
`code.Rout`, and `Rplots.pdf`. None is tracked in the article repository at the
audited commit. They may exist in the journal submission bundle, but a public
commit-to-archive checksum chain is not established. The full batch is reported
to take about 64 minutes under R 4.6.0 with fixed RNG and native-thread
settings; it was not run here. The article script parses and the manuscript
completes a 55-page BibTeX/pdflatex build from tracked inputs. The package
builds and installs as version 1.1.2, and focused scale/skewness and
RNG-repeatability tests pass. These bounded checks do not replace the missing
bundle, full batch, or cross-platform package checks.

The article and package now support a provisional software research chapter:
the source explicitly defines a five-part software contribution, supplies four
worked analyses and a technical appendix, and is distinct in purpose from the
application and nonlinear-method chapters. The chapter must remain centered on
software architecture, inference interfaces, diagnostics, reproducibility, and
the evidence/limitations of those capabilities—not re-present inherited exDQLM
theory as new. Before the candidate-contribution preface is finalized, record
which APIs, algorithms, C++ paths, tests, examples, and manuscript sections the
candidate personally led and which were coauthored or inherited. Committee
confirmation is still required if this chapter is to count as an independent
journal-suitable research unit.

## 6. Cross-project contribution and overlap diagnosis

| Material | Inherited/shared core | Distinct candidate contribution to establish | Recommended placement |
| --- | --- | --- | --- |
| Environmetrics | exDQLM/exAL and general LDVB strategy | Source-aware discrepancy/synthesis formulation, hydrologic design, implementation, validation, and writing roles | Research chapter |
| QDESN | exAL/AL quantile readouts, exdqlm comparators, ESN/DESN literature | Deep-reservoir quantile architecture, multi-level shrinkage formulation, computation, and application/validation roles | Research chapter |
| RQR/MTI | Residual-product criterion from Pouplin et al.; generalized-Bayes and tolerance literature | Mean-preserving characterization, tilt family, TCSP action/calibration, validation, and application roles | Research chapter, subject to proof-language repair |
| MTI extensions | Same MTI loss and geometry | Regression/dynamic extension, conditional computation, implementation, and validation roles | Integrated sections within the MTI chapter; no separate appendix |
| exdqlm | Yan exAL and Barata exDQLM/MCMC/ISVB/transfer foundations | Later LDVB, API, static/shrinkage, C++, diagnostics, synthesis, testing, examples, and writing roles | Provisional software research chapter with its technical material integrated by topic |

The hydrology and QDESN projects share dynamic-quantile machinery but have
different research questions: source-aware correction/synthesis versus
nonlinear feature learning and multi-level quantile structure. Their common
background should be centralized, while their data designs and empirical claims
remain chapter-local. QDESN's GloFAS use is not a duplicate of the Environmetrics
San Lorenzo analysis: the source systems, forecast contract, model role, and
evidence base differ, but the dissertation should explain the relationship to
avoid appearing to recycle one application.

RQR/MTI targets intervals under a loss and a separate tolerance action; it does
not estimate the same conditional response-quantile object as the exdqlm,
Environmetrics, or QDESN chapters. That conceptual shift is strong enough for
an independent research unit, provided the theorem/calibration wording is
repaired.

## 7. Reproducibility and provenance diagnosis

| Source | Highest bounded level reached | What was checked | What was not checked |
| --- | --- | --- | --- |
| Environmetrics article | `E3` for bounded checks | 13 manuscript figure paths and authoritative-output lineage contract | Live/private workflow and full model rerun |
| San Lorenzo bundle | `E3` | Required files, hashes, size rules, and public-hygiene validator | Selected fits and raw archive reconstruction |
| QDESN | `E3` for bounded checks | 53 current declared hashes, corrected-v4/PriceFM/GloFAS contracts, and three TeX builds | Large ignored outputs and simulation/application reruns; stale historical manifest/check scripts |
| RQR-GIBBS | `E3` | Theory/table/figure/language contract tests against tracked inputs | 1000-replication campaign and missing action-matched proof |
| MTI-EXTENSIONS | `E3` for TeX only | Main and supplement build | No implementation exists to test |
| exdqlm article | `E3` for bounded checks | Script parsing, 55-page article build, document contract, tracked-file inventory | Named submission archives and 64-minute full batch |
| exdqlm package | `E3` for focused tests | 1.1.2 package build/install and selected RNG/scale-skewness tests | Full cross-platform CI and complete package check matrix |

Absolute machine paths occur in tracked provenance in both QDESN and the
Environmetrics article. The public San Lorenzo export demonstrates a better
pattern: public placeholders plus a source-file crosswalk. Dissertation
provenance should use only source IDs, commits, relative paths, locators, and
hashes; exact server paths remain in the ignored local manifest.

## 8. Prioritized issue and repair register

| Priority | Issue | Required action | Owner / gate |
| --- | --- | --- | --- |
| P0 | TCSP exact-guarantee wording exceeds completed proof record | Prove and audit the closed-window result, or narrow every guarantee to the validated numerical calibration actually supplied | Method authors before MTI drafting |
| P0 | Granular candidate contribution allocation is absent | Use the source-documented joint contributions for drafting; confirm candidate versus collaborator roles before final contribution/acknowledgment language | Author, coauthors, committee; Gate G2 |
| P0 | Working inclusion versions are not final submission freezes | Use the audited commits for source-packet drafting; replace them if a later submitted manuscript is intended | Author; Gate G1 |
| P0 | Reuse rights unapproved | Record permissions/licenses for text, figures, tables, code, and staged data separately | Author/coauthors/publishers; Gate G2 |
| P1 | RQR August 13 evidence records are stale | Regenerate the claim/support ledgers from the current completed-validation snapshot or mark them historical | RQR source maintenance |
| P1 | QDESN historical validation controls are stale | Archive or refresh the 14-row historical joint manifest and retarget or retire the two Phase 181 manuscript-wiring checks; retain corrected-v4 as current authority | QDESN source maintenance |
| P1 | MTI extensions lack implementation/evidence wiring | Create a snapshot-matched code and test contract; add targeted static/dynamic simulations before claiming empirical performance | MTI source maintenance |
| P1 | exdqlm 1.1.1 archive provenance incomplete | Locate the submitted tarballs, record SHA-256 and source commit, or publish an approved archival release | exdqlm source maintenance |
| P1 | Portable provenance gaps | Replace absolute-path fields in dissertation-facing exports with source IDs/relative paths; preserve raw records privately | Per-project import preparation |
| P1 | Candidate name differs across sources | Resolved by author: official long name is Jose Antonio Aguirre Perez de Leon and scholarly name is Antonio de Leon; add ORCID when supplied and preserve immutable source spellings | Metadata and attribution review |
| P2 | QDESN Search Phase II unfinished | Leave out of current chapter; revisit only after its own promotion gates pass | Future QDESN decision |
| P2 | Environmetrics dense-hindcast/raw reconstruction absent | State limitation; rerun only if a concrete chapter claim requires it and data/version costs are accepted | Author/advisors |

These actions prepare source repositories for later controlled import; they do
not authorize changes to those repositories in this thesis audit.

## 9. Decisions required before drafting

Gate G1 — source selection:

- the five audited commits are the author-directed working drafting snapshots;
- QDESN Search Phase II remains future work until promoted and re-audited;
- MTI-EXTENSIONS is the intended companion manuscript despite its present
  implementation gap; and
- a later submitted manuscript may replace a working snapshot before final
  chapter freeze.

Gate G2 — contribution and rights:

- repository author lists and contribution paragraphs now supply the
  collaborator list and project-level contribution descriptions;
- confirm the remaining individual allocation of conceptual, theoretical,
  computational, empirical, and writing roles before final contribution prose;
- identify reused material authored principally by collaborators;
- obtain the required coauthor/committee/publisher permissions for direct
  reuse; and
- approve which public assets, if any, may be copied into the thesis.

Gate G3 — architecture:

- the author has selected the four-project working architecture in
  `chapter-plan.md`: exdqlm, Environmetrics, QDESN, and combined MTI;
- committee/advisor confirmation is still needed for counting the
  software-centered exdqlm chapter as a journal-suitable research unit;
- use conservative TCSP language unless the missing action-matched proof is
  completed and audited; and
- approve or modify the manuscript-first conversion defaults in
  `manuscript-integration-plan.md`.

Gate G4 — this was deliberately closed when the audit was written. It was
subsequently opened by the author's approval of all seven conversion defaults.
The four-chapter structural conversion is complete on GitHub `main`, and the
author reports a successful Overleaf handoff. This historical audit remains the
source diagnosis; current lifecycle state is maintained in `STATUS.md`,
`research-decisions.md`, and `source-manifest.json`.

## 10. Completion assessment

The audit has achieved its planning objective: it identifies the fixed source
snapshots, authority and branch risks, statistical targets, evidentiary limits,
antecedent relationships, package-version graph, principal contradictions,
reproducibility levels, and a concrete chapter architecture. It is ready for
scientific decision and source repair.

It has intentionally not resolved matters that require author, coauthor, or
committee judgment: any replacement for the working inclusion versions,
granular individual contribution allocation, direct-reuse permissions, whether
software work counts independently, and final chapter approval. Those open
gates are not audit failures and must not be filled by inference.
