# Manuscript-first dissertation integration plan

Status: **seven defaults approved; local structural conversion implemented**
Prepared: 2026-09-15
Applies to: the four-project architecture in `chapter-plan.md`
Evidence: `research-audit.md`, `research-audit-validation.md`,
`research-decisions.md`, `claim-evidence.json`, and `../source-manifest.json`

## 1. Objective

Build the dissertation from the completed manuscript record rather than
rewriting four projects from scratch. Each main article supplies the initial
chapter body. Unique supplement material is inserted next to the theorem,
method, simulation, application, table, or figure it supports. The final thesis
should read as one integrated monograph with four research chapters, not as a
collection of articles followed by detached supplements.

The thesis repository will contain only what the PDF needs:

- adapted chapter text, equations, proofs, algorithms, and citations;
- final selected figure files and final table inputs;
- a consolidated bibliography;
- small provenance/import records; and
- dissertation-specific transitions, attribution, and synthesis.

It will not become a replication repository. Code, data, simulations, model
fits, intermediate outputs, package sources, worktrees, Git histories, caches,
and complete artifact archives remain in their existing research repositories.
Those repositories are authoritative evidence sources, not build dependencies.

## 2. Non-goals and hard boundaries

This integration will not:

- clone or embed any research repository inside the thesis;
- use submodules, symlinks, absolute server paths, or live cross-repository
  `\input`/`\includegraphics` references;
- copy analysis code, raw data, fitted objects, environments, caches, logs, or
  complete output directories merely to make the thesis reproducible;
- rerun simulations or model fitting as part of the thesis build;
- make the PDF depend on R, Python, external storage, GitHub, or network access;
- import journal document classes, package manuals, response letters, build
  systems, CI files, or repository-specific instructions;
- preserve duplicated article introductions, repeated literature reviews,
  separate article abstracts, independent bibliographies, or submission
  metadata; or
- hide a central proof, limitation, or required empirical qualification in a
  detached dissertation supplement.

Reproducibility in the dissertation means that every imported claim and asset
has an exact source commit/path/locator and that the thesis itself builds from
tracked files. It does not mean duplicating the scientific computation.

## 3. Fixed working sources

| Thesis project | Primary manuscript snapshot | Supporting source role |
| --- | --- | --- |
| Chapter 2, exdqlm | `SRC-EXDQLM-ARTICLE` at `d5534e97db8414fd875022261d4c530eae4676e4` | `SRC-EXDQLM-PKG` supplies exact versioned implementation documentation; package code remains external |
| Chapter 3, Environmetrics | `SRC-ENVIRON` at `1272bfc10442a28add5a4c74ff641e9b9a8e9666` | San Lorenzo and corrections repositories supply provenance and adjudication, not thesis build inputs |
| Chapter 4, QDESN | `SRC-QDESN` at `757522db0f85815244370ec92a194de132268883` | Exact exdqlm comparator snapshots and tracked authority manifests support result selection |
| Chapter 5, MTI | `SRC-RQR` at `73887b9c86ef767aa1567c660718667945630aef` and `SRC-MTI-EXT` at `f345d946aa5a81b94795838bec58d874a0fdd0c9` | RQR supplies the foundation, tolerance evidence, and application; MTI-EXTENSIONS supplies regression/dynamic theory |

These are working conversion snapshots, not irreversible final freezes. If a
new submitted manuscript is later selected, compare it against the working
snapshot and import only the deliberate delta.

## 4. Target thesis structure

The final body will be:

1. Introduction and common inferential framework;
2. Computational infrastructure for flexible dynamic quantile models;
3. Source-aware correction and synthesis of hydrologic products;
4. Bayesian quantile deep echo-state networks;
5. Mean-tilted intervals: targets, tolerance actions, regression, and dynamics;
6. Synthesis, limitations, and future research; and
7. one dissertation-wide bibliography.

There will be no scientific appendix or separate dissertation supplement by
default. The starter's formatting-demonstration appendix will be removed once
the imported chapters exercise the required formatting features. Material from
article supplements will be placed in the chapter body according to the maps
below.

To preserve readable flow, integrated supplement material may appear as:

- a proof immediately after its theorem;
- a “Computational details” subsection immediately after the method;
- a “Validation details” subsection immediately after the empirical design;
- additional tables and figures immediately after the primary result they
  qualify; or
- a chapter-closing “Technical qualifications and limitations” section.

This is still one thesis body. Section depth and cross-references provide
layered reading without creating a detached appendix.

## 5. Universal conversion rules

### 5.1 Preserve first, edit second

The first pass is a faithful structural conversion, not a rewrite. Preserve
the manuscript's scientific sentences, equations, theorem statements, proofs,
results, qualifications, captions, and citations unless a documented conflict
requires correction. Mechanical changes may:

- replace the article title with a chapter heading;
- remove the article abstract, author block, keywords, journal metadata,
  acknowledgments, funding, conflict, data, and code-availability boilerplate;
- convert article section levels to chapter section levels;
- remove local bibliography commands;
- replace journal-specific commands/environments with thesis-native forms;
- namespace labels and resolve citation keys;
- change figure/table paths to curated thesis paths; and
- replace references to “the article” or “the supplement” with accurate
  chapter-local wording.

Only after all four converted chapters compile together should editorial work
deduplicate background, add transitions, harmonize notation, and improve the
monograph narrative. This prevents accidental scientific loss during import.

### 5.2 One chapter, one scientific story

Each chapter receives one opening, one contribution statement, one roadmap,
and one conclusion. Article/supplement duplicates are merged. The chapter must
preserve coauthor credit and distinguish inherited work, but it should not read
like multiple PDFs concatenated together.

### 5.3 Main and supporting material tiers

| Tier | Treatment |
| --- | --- |
| A — main-article material | Import the full scientific body and all main figures/tables unless an item is a true duplicate, submission-only artifact, or superseded result. |
| B — supplement material supporting a central claim | Integrate beside the corresponding main method/result, including essential derivations, proofs, algorithms, validation details, and qualifying tables/figures. |
| C — exhaustive diagnostics or replication-only material | Keep connected by source manifest and citation; import only if needed for a chapter claim, committee request, or readable interpretation. |
| D — code/data/provenance machinery | Do not import. Record the external source commit/path and summarize the reproducibility boundary. |

The default is therefore not “copy every tracked file.” It is “preserve the
complete scholarly argument and the evidence needed to support it.”

### 5.4 Local-working versus publication boundary

The structural conversion may be prepared and committed locally without a
push. Before any GitHub/Overleaf synchronization or dissertation publication,
record the applicable coauthor/publisher decision for verbatim text and each
directly reused figure/table. Until then, provenance records mark those items
as local working imports rather than externally cleared reuse.

## 6. Chapter 2 — exdqlm integration map

### 6.1 Source packet

- Main article: `exdqlm-jss.tex`.
- Bibliography: article `references.bib`, merged into the dissertation-wide
  bibliography.
- Implementation authority: exact versioned `SRC-EXDQLM-PKG` documentation.
- Article scale at the audited snapshot: approximately 2,397 source lines,
  nine figure environments, and ten table environments.

Do not copy the package source tree, package tests, example caches, fitted
objects, replication archive, or missing submission tarballs into the thesis.

### 6.2 Target chapter flow

1. problem, software gap, and contribution boundary;
2. inherited exAL/exDQLM foundations;
3. package architecture and composable model specification;
4. posterior computation: MCMC, LDVB, and ISVB;
5. fitted objects, diagnostics, scoring, forecasting, and synthesis;
6. static AL/exAL regression and shrinkage;
7. worked examples and empirical tradeoffs;
8. versioned reproducibility record and limitations; and
9. chapter conclusion and link to Chapters 3 and 4.

### 6.3 Existing technical appendix placement

The technical appendix already embedded in the article will not remain an
appendix in the dissertation:

| Article technical material | Thesis placement |
| --- | --- |
| Distributional conventions | immediately after the inherited model foundation |
| Dynamic DQLM/exDQLM posterior targets | within the dynamic-model and inference section |
| Transfer-function state augmentation | with composable transfer-function models |
| Static AL/exAL posterior target | with static regression |
| LDVB scale-skewness derivation | directly after the LDVB overview |
| Nishimura-Suchard regularized horseshoe | with static shrinkage |
| Forecasting, diagnostics, and predictive synthesis algorithms | immediately after the associated user-facing interfaces |
| Nonconjugate-VB and backend notes | in computation qualifications and limitations |

The four examples remain examples of the software contribution, not four
separate research units. Preserve the negative evidence: Big Tree does not
show uniform transfer-model superiority, and LDVB trades speed against the
MCMC reference in the sparse-static example.

## 7. Chapter 3 — Environmetrics integration map

### 7.1 Source packet

- Main and supporting material currently coexist in `wileyNJD-APA.tex`.
- Eight generated table inputs are referenced under
  `tables/generated_tex/`.
- Thirteen manuscript figure paths passed the source validator.
- The San Lorenzo reproducibility and correction repositories are provenance
  sources only.

Do not import the staged data bundle, retrieval/preprocessing histories,
private workflow paths, full model outputs, or scripts. The chapter receives
only the final approved tables/figures it displays.

### 7.2 Target chapter flow

1. hydrologic problem and source/horizon contract;
2. exDQLM discrepancy and transfer formulation;
3. posterior computation and relationship to Chapter 2;
4. predictive synthesis and CRPS evaluation;
5. San Lorenzo observations and external product design;
6. rolling-origin evaluation;
7. forecast validation results;
8. selected-model interpretation and component sensitivity;
9. additional cutoff evidence and limitations; and
10. chapter conclusion.

### 7.3 Supporting-material placement

| Current supporting section | Thesis placement |
| --- | --- |
| MCMC algorithms | after the model/posterior formulation, before the application |
| Variational-Bayes algorithms | immediately after MCMC and before predictive synthesis |
| Component-removal sensitivity | after comparative forecast performance |
| Source-specific shape and scale summaries | after selected-model parameter interpretation |
| Univariate transfer-active synthesis | after the main multivariate synthesis result as a reference comparison |
| Additional cutoff-specific synthesis panels | within the rolling-origin results, after the representative cutoff |

All five-origin limitations remain in the body. The chapter must not imply a
dense hindcast, operational deployment, raw-data reconstruction, or joint
propagation of exogenous forecast uncertainty.

## 8. Chapter 4 — QDESN integration map

### 8.1 Source packet

- Main article: `main.tex`.
- Main supplement: `qdesn-supplement.tex`.
- Gaussian baseline/initialization supplement:
  `gaussian_desn_scaled_ridge_supplement.tex`.
- Bibliography: `refs.bib`, merged once.
- Final tables/figures: only the current corrected-v4, GloFAS, PriceFM R98,
  and single-quantile authority records selected by the audit.

Do not import ignored output forests, execution branches, caches, full
simulation results, stale historical manifests as current evidence, or Search
Phase II material that has not passed promotion gates.

### 8.2 Target chapter flow

1. inferential problem and fixed-reservoir contribution;
2. DESN feature construction and reservoir selection;
3. single-level AL/exAL QDESN and shrinkage;
4. Gaussian scaled-ridge baseline and initialization;
5. MCMC, VB, and monitoring;
6. joint quantile-vector model and crossing treatment;
7. forecasting, scoring, and model selection;
8. single-quantile simulation;
9. joint multi-quantile simulation;
10. GloFAS application;
11. PriceFM comparison;
12. computational/empirical qualifications and future work; and
13. conclusion.

### 8.3 Main-supplement placement

| QDESN supplement material | Thesis placement |
| --- | --- |
| Reservoir specification, selection, initialization, and diagnostics | expand the DESN feature section before the quantile model |
| Distributional conventions | at the start of the model section |
| Working likelihoods, priors, and augmented posterior | immediately after the single-level model |
| Reference global-shrinkage calibration | inside the prior subsection |
| MCMC full conditionals | immediately after the MCMC overview |
| VB/Laplace-Delta and ELBO monitoring | immediately after the VB overview |
| Joint quantile-vector posterior and computation | inside the joint-model section |
| Crossing diagnostics | after joint computation and before evaluation |
| Multi-step forecasting and rearrangement | inside forecasting/scoring |
| Single-quantile detailed tables/diagnostics | after the primary single-quantile results |
| Joint study details and figures | after the primary joint-study results |
| Additional PriceFM results | after the main PriceFM comparison |
| GloFAS latent-path ensemble model and numerical qualification | inside the GloFAS methods/results sequence |

### 8.4 Gaussian-supplement placement

| Gaussian-DESN supplement material | Thesis placement |
| --- | --- |
| Fixed design and distribution conventions | concise setup inside the Gaussian baseline section |
| Exact scaled-ridge model and posterior | baseline derivation before QDESN initialization |
| Posterior predictive distribution | with baseline forecasting |
| Exact log marginal likelihood | with model selection/initialization |
| Direct sampler | with computation |
| Use as AL/exAL initialization | bridge from Gaussian baseline to QDESN computation |
| Omitted variants and validation checks | technical qualifications after the baseline; omit repetitive checklist prose |

This creates one QDESN chapter. Independent/joint fits, GloFAS, PriceFM, and
Gaussian initialization remain parts of the same method line.

## 9. Chapter 5 — MTI integration map

### 9.1 Source packet

- Foundation/tolerance main article: RQR-GIBBS `main.tex`.
- Foundation/tolerance supplement: `rqr-gibbs-supplement.tex`.
- Regression/dynamic main article: MTI-EXTENSIONS `main.tex`.
- Regression/dynamic supplement: `mti-extensions-supplement.tex`.
- Bibliographies: their `refs.bib` records, deduplicated into the thesis.

At the audited snapshots, the RQR main article has six figure and three table
environments; its supplement has three figure and seven table environments.
MTI-EXTENSIONS is mathematical text without tracked numerical figures/tables.

Do not import failed dynamic campaigns, large validation outputs, application
code, or any implied extension result that the manuscript does not contain.

### 9.2 Target chapter flow

1. interval targets and residual-product antecedent;
2. MPI characterization and proof;
3. MTI tilt family, paths, and tail sensitivity;
4. empirical balance and fixed-target generalized-Bayes computation;
5. TCSP calibration and tolerance action;
6. confirmatory validation;
7. pharmaceutical application;
8. static endpoint regression;
9. pseudo-AL augmentation, Gibbs/ECM computation, and shrinkage;
10. deterministic basis expansions;
11. dynamic endpoint states and alternating FFBS;
12. diagnostics, validation boundaries, and open theory; and
13. conclusion.

This is one chapter with two connected movements: target/tolerance foundations,
then regression/dynamic endpoint extensions. It needs one introduction and one
conclusion, not two manuscript introductions and discussions.

### 9.3 RQR supplement placement

| RQR supplement material | Thesis placement |
| --- | --- |
| Notation/inferential-object guide | merge into the chapter opening and common-framework cross-reference |
| Fixed-content target theory | directly after the corresponding definitions |
| Mean-preserving score proofs | immediately after the MPI propositions/theorems |
| Interval paths and tail sensitivity | after the MTI family |
| Fixed-content MTI target and Cornish-Fisher approximation | inside the MTI theory section |
| Empirical/fractional balance | with empirical balance |
| Width-regularized loss | retain only if used by a chapter claim; otherwise cite its source locator |
| Fixed-target MTI-ECM and DP content check | inside generalized-Bayes computation |
| Validation protocol, feasibility, calibration, and detailed tables | immediately after validation design/results |
| Pharmaceutical details and sensitivity | immediately after the primary application |
| Reproducibility and validation limits | in the chapter limitations section |

### 9.4 MTI-EXTENSIONS supplement placement

| MTI-EXTENSIONS supplement material | Thesis placement |
| --- | --- |
| Notation and targets | reuse the established chapter notation; import only unique definitions |
| Root labels and endpoint summaries | inside static endpoint regression |
| Pseudo-AL augmentation and Gaussian root updates | inside computation |
| ECM mode calculation | directly after the Gibbs construction |
| Conditionally Gaussian shrinkage | after static regression computation, with the zero-tilt restriction |
| Deterministic basis expansions | inside the basis-expansion section |
| Dynamic endpoint-state updates | directly after the dynamic model |
| Diagnostics and validation limits | before the combined chapter conclusion |

TCSP wording remains action-accurate and conservative. The empirical
calibration and simulations cannot be rewritten as an exact action-matched
finite-sample theorem. Regression/dynamic extensions receive no invented
performance or tolerance guarantee.

## 10. Figures and tables

### 10.1 Selection rule

- Include every non-superseded main-article figure/table unless it is redundant
  after chapter merging.
- Include supplement figures/tables that prove, qualify, diagnose, or interpret
  a central chapter claim.
- Keep exhaustive diagnostics external when they do not change the chapter's
  argument; cite the repository/manuscript location when useful.
- Prefer final manuscript assets and generated table inputs already named by an
  authority manifest. Do not regenerate them during the thesis build.

### 10.2 Thesis layout

Use chapter-scoped paths:

```text
figures/ch02-exdqlm/
figures/ch03-environ/
figures/ch04-qdesn/
figures/ch05-mti/
tables/ch02-exdqlm/
tables/ch03-environ/
tables/ch04-qdesn/
tables/ch05-mti/
```

Copy only the displayed final asset or final table fragment. Every copied file
receives a manifest entry with source ID, exact commit/path, source hash,
destination, transformation, caption status, and reuse status. Captions are
made dissertation-native and retain source-specific qualifications.

### 10.3 Collision controls

- Namespace labels as `fig:exdqlm-*`, `fig:env-*`, `fig:qdesn-*`, and
  `fig:mti-*`; apply the same rule to tables, equations, theorems, and sections.
- Do not overwrite two different files with the same basename.
- Prefer vector PDF for line art and high-resolution PNG only where raster is
  intrinsic.
- Visually inspect every imported figure/table page at readable scale.
- Confirm that legends, text, colors, and captions remain interpretable in the
  dissertation layout and in grayscale where important.

## 11. Bibliography integration

Create one controlled merge into `references.bib`:

1. extract entries actually cited by the imported chapters from the source
   bibliographies;
2. match duplicates by DOI first, then normalized title/author/year;
3. retain one stable thesis citation key per work;
4. record old-to-new key mappings by source;
5. preserve title capitalization, accents, DOI, URL, publication status, and
   arXiv/version distinctions;
6. distinguish software/package citations from method papers; and
7. reject unresolved duplicate keys or cited-but-missing entries before commit.

Do not import every unused bibliography entry. Do not silently change a
preprint into a published citation or merge distinct versions merely because
their titles are similar.

## 12. LaTeX and notation normalization

Before text import, create a conversion map for:

- distribution and vector/matrix macros;
- theorem/proposition/corollary environments;
- algorithm and code environments;
- table column types and sizing commands;
- journal-specific author, address, abstract, keyword, and citation commands;
- figure path aliases and table `\input` commands;
- section, equation, theorem, figure, and table labels; and
- notation that has genuinely different meanings across projects.

Prefer thesis-native macros in `notation.tex` and `preamble.tex`, but do not
force unsafe unification. For example, AL/exAL likelihood parameters, QDESN
working-likelihood quantities, MTI loss parameters, and tolerance confidence
must remain distinct even if their source symbols collide.

The first conversion pass should be mechanical and reviewable. Scientific
notation changes occur only through an explicit old-to-new map.

## 13. Provenance connection without repository duplication

Create one compact import manifest per chapter under `docs/imports/`:

```text
docs/imports/ch02-exdqlm.json
docs/imports/ch03-environ.json
docs/imports/ch04-qdesn.json
docs/imports/ch05-mti.json
```

Each record should contain:

- source ID and exact commit;
- source document/path and section/label locator;
- material type: prose, equation, proof, algorithm, figure, table, or citation;
- destination chapter/path and destination label;
- handling: preserved, adapted, condensed, merged, or omitted-with-reason;
- source and destination hashes for copied binary/table assets;
- relevant claim-evidence ID;
- collaborator/antecedent attribution note where material;
- reuse-rights status; and
- validation status.

The import manifests connect the thesis to the source repositories without
exposing server paths or copying their computational state. A validator should
check schema, source IDs, commit formats, unique destinations, referenced
thesis files, forbidden absolute paths, and unresolved rights/status fields.

## 14. Implementation sequence

### Phase 0 — conversion preparation

1. Create a dedicated local integration branch from the current dissertation
   branch.
2. Preserve the current PDF and verify a clean baseline build.
3. Create the four import manifests and label/citation/macro maps.
4. Inventory every main/supplement section and every displayed table/figure as
   include, merge, condense, or omit-with-reason.
5. Resolve any source file or asset that is missing at the declared commit
   before importing around the gap.

### Phase 1 — bulk structural conversion

Convert all four project chapters before substantial rewriting:

1. extract manuscript bodies from exact commits without editing source repos;
2. remove document wrappers and submission-only front/back matter;
3. namespace labels and map citations/macros;
4. insert supplement material according to Sections 6–9 of this plan;
5. copy only selected final tables/figures into chapter-scoped directories;
6. connect the four chapter files in `main.tex`; and
7. compile after each chapter, then compile the whole thesis.

This phase should preserve source prose and scientific order as much as
possible. Its goal is a complete, faithful, self-contained working thesis—not
final stylistic polish.

### Phase 2 — monograph integration

After all four chapters compile:

1. remove duplicated abstracts, introductions, literature summaries, and
   conclusions;
2. write one dissertation introduction and one final synthesis;
3. add chapter openings that identify collaborators, antecedents, and the
   chapter's contribution;
4. add cross-chapter transitions and references;
5. centralize shared exAL/exDQLM, evaluation, and interval taxonomy material;
6. harmonize terminology and only safely equivalent notation;
7. ensure all supplement-derived material reads as an ordinary chapter section;
8. retain negative findings and source limitations; and
9. update chapter-level contribution and reuse statements.

### Phase 3 — editorial and filing preparation

1. confirm granular candidate/coauthor roles;
2. record direct-reuse permissions and publisher-required statements;
3. confirm whether exdqlm counts as the fourth journal-suitable unit;
4. replace working snapshots if later submitted versions are selected;
5. complete dissertation title, committee, date, ORCID, and acknowledgments;
6. perform citation, notation, claim, and accessibility reviews; and
7. authorize the deliberate GitHub/Overleaf handoff.

## 15. Commit and recovery strategy

Use focused local commits so any conversion can be inspected or reverted
without affecting the research repositories:

1. integration scaffolding, manifests, and conversion maps;
2. exdqlm structural import;
3. Environmetrics structural import;
4. QDESN structural import;
5. combined MTI structural import;
6. supplement-to-body integration and asset/citation reconciliation;
7. cross-chapter deduplication and transitions; and
8. final validation/documentation update.

Do not combine source-repository repairs with thesis imports. If a source defect
must be fixed, handle it separately in its own repository and update the thesis
only after a new immutable source commit is approved.

## 16. Verification and acceptance criteria

The manuscript-first conversion is complete only when:

- all four chapter bodies compile from tracked thesis files with sibling
  repositories unavailable;
- no thesis `\input`, figure, or bibliography path escapes the repository;
- every included source section and supplement section has an import-manifest
  disposition;
- every main-article figure/table is included or has a documented reason for
  exclusion;
- every supplement figure/table supporting a central claim is integrated next
  to that claim;
- all citations resolve through one bibliography with no unreviewed duplicate
  keys;
- labels and destinations are unique and all cross-references resolve;
- no stale result line is presented as current authority;
- no code, data, cache, full output archive, credential, or machine-specific
  path has entered the public thesis tree;
- build logs contain no unresolved citations/references, duplicate labels,
  material overflow, or missing fonts;
- every affected chapter opening, equation/proof block, figure, table, and
  transition has been visually inspected;
- collaborator credit, inherited-method boundaries, negative results, and
  limitations remain visible; and
- `docs/STATUS.md`, the source manifest, claim evidence, import manifests, and
  assistance log agree with the built PDF.

## 17. Approved execution decisions

On 2026-09-15, the author approved these defaults:

1. perform one local manuscript-first conversion campaign for all four
   chapters;
2. preserve article prose initially rather than rewriting from scratch;
3. integrate unique supplement content into the corresponding chapter body;
4. include all non-superseded main figures/tables and only claim-relevant
   supplement assets;
5. keep all code, data, computations, and full provenance archives external;
6. commit locally in recoverable chapter-sized steps; and
7. do not push, sync, or externally publish imported text/assets until reuse
   status is reviewed.

The local implementation follows all seven decisions. No remote or Overleaf
synchronization was performed.

## 18. Local implementation record

The structural conversion is reproducible through
`scripts/import_manuscripts.py`. It reads only immutable Git blobs from the
five approved audit clones, verifies their exact commits, builds a deduplicated
bibliography, rewrites local citations/labels/dependencies, and emits the four
chapter files plus chapter-scoped assets. Its output is checked by
`scripts/validate_manuscript_imports.py`.

The generated records are:

- `docs/imports/ch02-exdqlm.json`;
- `docs/imports/ch03-environ.json`;
- `docs/imports/ch04-qdesn.json`; and
- `docs/imports/ch05-mti.json`.

Together they record nine source manuscripts, 96 top-level section
dispositions, and 102 imported records. The 93 display dependencies comprise
only selected TeX table/alias fragments and final PDF/PNG figure assets. No
research code, data, fitted objects, simulation outputs as datasets, caches,
environments, source histories, or live cross-repository paths were imported.
All direct reuse remains marked `UNVERIFIED_LOCAL_ONLY`.

Phase 1 is complete: all four article spines compile in the dissertation;
supporting proofs, algorithms, derivations, diagnostics, and selected empirical
displays are integrated by topic; the demonstration appendix is no longer in
the document; and one bibliography resolves all chapter citations. Dense
source tables and a small number of long derivations use provisional compact
typesetting to fit the thesis page and require a later readability pass.

Phases 2 and 3 remain deliberately open. The converted chapters still retain
article-style signposting and repeated background where fidelity was safer
than premature rewriting. Subsequent work must review scientific completeness
and ordering chapter by chapter, deduplicate shared exposition, write the
dissertation introduction and synthesis, confirm granular contribution roles,
resolve direct-reuse permissions, and complete administrative metadata before
any external synchronization or submission.
