# PhD research audit execution plan

> Historical baseline. Superseded on 2026-09-15 by
> `docs/research-audit-master-plan.md` after author approval. Retained for the
> audit trail; do not use this file as the controlling execution plan.

Prepared 2026-09-15. This is an execution plan based on bounded, read-only
reconnaissance. It is not the completed scientific audit, a chapter-selection
decision, or approval of any observed default-branch head. The completed work
will be written to `docs/research-audit.md` and `docs/chapter-plan.md` only after
the version, contribution, provenance, and overlap checks below are performed.

## 1. Objective and governing questions

The audit will establish a defensible dissertation corpus from five
author-authorized seed repositories:

1. `AntonioAPDL/Article-Q-DESN---Version-2`;
2. `AntonioAPDL/Evironmetrics---REVISED-DOC-Corrected-2`;
3. `AntonioAPDL/RQR-GIBBS`;
4. `AntonioAPDL/MTI-EXTENSIONS`; and
5. `AntonioAPDL/exdqlm---Article`.

It will answer four questions before chapter drafting begins:

- What is the intended manuscript and evidence version for each project?
- Which scientific, computational, empirical, and writing contributions are
  attributable to the candidate, the coauthors, or antecedent work?
- Which projects are independently defensible research units, and which are
  variants, implementation layers, applications, or supporting evidence for
  another unit?
- Can every central equation, guarantee, empirical claim, figure, and table be
  traced to a compatible source version with the necessary qualifications?

The working unifying hypothesis is that the projects develop Bayesian methods
for dynamic quantiles and interval endpoints under different inferential
targets and computational constraints. The audit must test that hypothesis; it
must not erase distinctions merely to obtain a smoother dissertation story.

## 2. Scope and safety boundary

The dissertation checkout is the only writing target. Original research
repositories and all of their worktrees are read-only evidence:

- do not fetch, switch, reset, stash, clean, build, install into, or edit an
  original research checkout;
- record existing branches, commits, upstreams, dirty changes, untracked names,
  and incomplete histories without altering them;
- use an isolated audit clone or a manifest-controlled temporary source copy
  when a current remote snapshot, compilation, or test is required;
- keep audit clones outside the dissertation and outside original article
  repositories;
- keep large data, caches, runtime output, fitted objects, private source
  details, and machine paths outside the public dissertation tree;
- do not treat source access as permission to publish text, data, or assets;
- do not rerun expensive simulations during the inventory stage; and
- do not import or draft substantive dissertation material before the author
  approves the chapter architecture and relevant source versions.

The authoritative Q-DESN snapshot contains an `AGENTS.md` that additionally
requires command-line Git only and forbids GitHub CLI and Overleaf/browser sync
for that project. After discovery of that instruction, all Q-DESN version and
history work must use ordinary Git in the isolated audit clone. No integration
or publication workflow is authorized by this dissertation audit.

A targeted related-repository search is allowed only to resolve a documented
dependency, provenance chain, manuscript lineage, or antecedent. It is not an
account-wide scientific audit.

## 3. Seed-source reconnaissance ledger

The following heads were observed on GitHub on 2026-09-15. They are discovery
checkpoints, not approved manuscript versions.

| Source | Observed `main` head | Principal material seen | Initial handling |
| --- | --- | --- | --- |
| Q-DESN article | `757522db0f85815244370ec92a194de132268883` | `main.tex`, main supplement, Gaussian-DESN note, simulation/application tables, code, manifests, extensive audit history | Create an isolated snapshot of the observed authority; separately classify the large worktree lineage. |
| Environmetrics revision | `1272bfc10442a28add5a4c74ff641e9b9a8e9666` | Wiley manuscript with appended supplement, generated tables, frozen figures, artifact and provenance manifests | Reuse the matching clean local checkout read-only; follow its external workflow and reproducibility links. |
| RQR-GIBBS / MTI tolerance paper | `73887b9c86ef767aa1567c660718667945630aef` | Current MPI/MTI/TCSP tolerance manuscript, supplement, implementation, simulations, figures and tables | Create a current audit clone because the available local checkout is stale and reflects an earlier RQR framing. |
| MTI extensions | `f345d946aa5a81b94795838bec58d874a0fdd0c9` | Regression/dynamic endpoint manuscript and derivation supplement | Create an audit clone; no suitable local checkout was found in the inspected project area. |
| exdqlm JSS article | `d5534e97db8414fd875022261d4c530eae4676e4` | JSS manuscript, flat replication script, modular author-side analysis, reproducibility index, response to editor | Reuse the matching clean canonical checkout read-only; inspect the separate package repository as a required dependency. |

### Version hazards already established

- The Q-DESN repository's own authority documentation says `origin/main` is
  the sole manuscript/research authority. Its canonical local directory is
  currently on a clean experimental GloFAS branch, not `main`; that branch is
  far behind the cached `origin/main`. The repository has 172 registered
  worktrees. Therefore neither the directory name nor its checked-out branch
  identifies the intended manuscript.
- The current RQR GitHub manuscript has been reframed as *Mean-Tilted
  Intervals: Short Tolerance Intervals*. The available local `main` and cached
  remote ref predate the observed GitHub head and retain an earlier standalone
  RQR/Gibbs framing. Only a fresh audit snapshot can represent the current
  remote manuscript safely.
- The Environmetrics software manifest records `exdqlm` 1.1.0, the JSS article
  and replication text target 1.1.1, and the current package `main` identifies
  itself as 1.1.2. These may be legitimate project-specific freeze points, but
  they must remain distinct until compatibility and provenance are checked.
- The RQR materials pin `AntonioAPDL/exdqlm`, branch
  `feature/rqr-desn-readout-20260716`, commit
  `dffb71ee70b597d6a716ee74be1cbc99731cd453`. The matching local worktree is at
  that commit but contains untracked author material. It must be inventoried
  read-only and never used as a clean build surface.
- The Environmetrics article explicitly says it is not self-contained for full
  figure/table generation. It freezes publication assets but delegates the
  authoritative generation path to a larger workflow and a public San Lorenzo
  reproducibility bundle.

## 4. Evidence-backed source graph

Repositories are assigned to tiers so that related material is investigated
without counting every branch or repository as a new scientific contribution.

### Tier A: full scientific audit

- the five authorized seed repositories;
- `AntonioAPDL/exdqlm`, because it is the implementation dependency of the JSS
  article, the Environmetrics work, and the pinned RQR branch;
- the exact Barata 2021 dissertation sections and original exDQLM/exAL papers
  cited by these projects, because contribution and novelty cannot be assessed
  without them; and
- any submitted/accepted manuscript PDF, response letter, or version supplied
  by the author as the preferred scholarly record.

### Tier B: provenance and lineage audit

- `AntonioAPDL/san-lorenzo-exdqlm-reproducibility` and
  `AntonioAPDL/Corrections---Project-1`, explicitly named by the Environmetrics
  manuscript's software and revision contracts;
- the private/live Environmetrics workflow only to the extent needed to resolve
  table, figure, model, and data provenance, subject to actual access;
- the pinned exdqlm RQR feature branch and the Q-DESN/exdqlm validation branches
  explicitly cited by article manifests or handoff records;
- the historical Q-DESN repository and accidental single-hyphen v2 snapshot
  only for lineage questions not resolved by the authoritative repository; and
- external PriceFM material only for the precise data/model comparison contract
  used in Q-DESN, not as an unrestricted audit of that project.

### Tier C: candidate-only material

The following names are relevant enough for a shallow identity/relationship
check, but are not approved as independent dissertation sources:

- `Q-DESN---Theory-for-implementation`;
- `QDESN---Multivariate-Application`;
- `exDQLM---Ensemble`;
- `univ-exDQLM---Ensemble`;
- `NDLM---Ensemble`; and
- older Environmetrics revision repositories.

They will be promoted to Tier B or A only when an authoritative manuscript,
manifest, bibliography, commit, or author decision establishes a concrete
relationship. A private interval-regression name found by the targeted metadata
search is recorded only in the ignored local manifest and requires an author
decision before deep inspection or public mention.

## 5. Snapshot and storage strategy

GitHub's reported repository sizes are discovery estimates, not predicted clone
or working-tree sizes. The observed values motivate the following handling:

| Repository | Reported size (KiB) | Planned approach |
| --- | ---: | --- |
| Q-DESN | 30,639 | Fresh full audit clone is proportionate and avoids changing 172 original worktrees. |
| RQR-GIBBS | 35,201 | Fresh full audit clone is required to obtain the current reframed manuscript. |
| MTI-EXTENSIONS | 78 | Fresh full audit clone. |
| Environmetrics revision | 708,823 | Reuse the clean matching checkout read-only; copy only the manifest-defined manuscript dependency closure for compilation. |
| exdqlm JSS article | 358,316 | Reuse the clean matching checkout read-only; use a bounded replication/source copy for tests. |
| exdqlm package | 314,444 | Reuse matching read-only worktrees; use an isolated package copy for any checks. |
| San Lorenzo reproducibility | 69,133 | Clone only after its role and reuse status are confirmed; begin with manifest and fast validation paths. |

Before any clone, verify free space and estimate object/working-tree size. Use
normal Git history rather than ZIP downloads. Record shallow/partial-clone
limitations if a bounded clone becomes necessary. If the known muscat `fsync`
problem recurs, stop and record it rather than applying a persistent Git
configuration change.

## 6. Worktree and branch lineage protocol

The Q-DESN repository has 172 registered worktrees, the exdqlm package has 53,
the historical Q-DESN checkout has five, and the JSS article has two. The audit
will first build a metadata ledger rather than read each tree as a separate
paper.

For every registered worktree, record:

- repository/common-Git-directory identity;
- path in the ignored local record;
- branch or detached state, exact commit, tree hash, commit date and subject;
- upstream and cached ahead/behind state;
- dirty tracked-file summary and untracked names, without copying contents by
  default;
- merge base and reachability relative to the selected authority;
- manuscript/result/implementation references that point to the branch; and
- disposition: authority, promoted evidence, active unmerged candidate,
  historical experiment, validation lane, integration lane, recovery/sync
  artifact, or duplicate tree.

Deep inspection is limited to worktrees that satisfy at least one of these
conditions:

1. they contain the approved manuscript commit;
2. a tracked manuscript asset or manifest cites them;
3. they contain an unmerged scientific result that the author wants considered;
4. they are the documented implementation source of truth; or
5. a contradiction cannot be resolved from the authoritative line.

Identical commits/trees are collapsed. Dates and branch names are never used as
proof that a result was accepted, promoted, valid, or novel. Recent unmerged
Q-DESN GloFAS Search II and PriceFM continuation branches are candidates, not
automatic replacements for the published `main` snapshot.

## 7. Execution phases

### Phase 0: freeze the audit context

1. Confirm hostname and dissertation working directory.
2. Read all dissertation and source-repository instructions in scope.
3. Rebuild the untouched dissertation scaffold as a baseline if necessary.
4. Create or refresh the ignored local source manifest and external audit-root
   inventory.
5. Record remote heads without updating original repositories.

Exit criterion: every source has a stable identifier and an explicit read/write
boundary; no scientific conclusion has yet been drawn.

### Phase 1: resolve manuscript versions

For each seed source:

1. compare the observed default-branch manuscript with authority notes,
   submission bundles, response letters, tags, releases, PDFs, Overleaf
   snapshots, and newer experimental branches;
2. identify whether text, supplement, code, tables, and figures belong to the
   same version;
3. document unresolved divergence instead of selecting the most favorable
   result; and
4. ask the author to approve the exact branch/commit or supplied manuscript
   version before it becomes a dissertation source.

Exit criterion: one approved scholarly snapshot per included project, plus
separately identified implementation and evidence snapshots where required.

### Phase 2: manuscript-first scientific reading

Read each approved main manuscript from beginning to end, then its supplement,
bibliography, response/revision record, and repository documentation. Produce a
structured synopsis with:

- research question and inferential target;
- assumptions and working likelihood or loss;
- model hierarchy and parameterization;
- computational algorithms and approximation claims;
- theoretical statements and their proofs or missing proof support;
- data, experimental design, comparators and scoring rules;
- empirical findings, negative findings and limitations;
- relationship to prior work; and
- candidate/coauthor contribution questions.

Exit criterion: every project can be explained accurately without relying on a
repository name, abstract alone, or inferred novelty.

### Phase 3: implementation and derivation audit

Trace central manuscript equations and algorithms into code and tests. Check
dimensions, parameterizations, conditionals, transformations, priors,
initialization, convergence criteria, and numerical safeguards. Use existing
tests and audit scripts before proposing new checks. Classify each relationship
as exact implementation, approximation, diagnostic, legacy path, or not found.

For the RQR dependency check, follow its repository instruction precisely:
materialize the pinned exdqlm commit with `git archive`, then build/install/test
that material only inside the ignored cache of the isolated RQR audit clone.
Never load or compile directly from the external exdqlm source worktree.

Do not equate:

- AL/exAL working likelihood quantile inference with loss-based generalized
  updating;
- quantile ordinates with interval-root targets;
- generalized-posterior endpoint draws with posterior predictive response
  draws;
- credible or metric intervals with predictive or tolerance intervals; or
- simulation evidence with a mathematical guarantee.

Exit criterion: each central method claim has an equation-to-code disposition
and any mismatch is prioritized.

### Phase 4: numerical and asset provenance audit

For each central result, table, and figure, record:

- source repository, commit, path, label/locator and file hash where useful;
- data identity/version, preprocessing and model-ready input contract;
- model variant, prior/hyperparameters and inference engine;
- training/test windows, forecast origin/horizon and information set;
- seed design, replication count, chain/optimization diagnostics and exclusions;
- uncertainty summary and exact score definition/direction;
- generator script/config, raw or compact source output and promotion manifest;
- whether the check is documentary, hash-verified, regenerated, smoke-tested,
  or fully reproduced; and
- contradictions, caveats and authorization for dissertation reuse.

Start with cheap manifest/hash/row-count consistency checks. Run selected
targeted tests only in isolated copies. A full exdqlm replication is documented
as roughly an hour on its reference platform and will not be run merely to call
the inventory complete.

Exit criterion: no central numerical statement is labeled reproduced unless it
was actually reproduced; missing raw inputs remain visible gaps.

### Phase 5: novelty, attribution and antecedents

Build a claim-level contribution matrix covering theory, model formulation,
algorithm development, software, experiment design/execution, application,
writing and project leadership. Cross-check author statements with manuscript
authorship, package roles, repository history, response letters and antecedent
texts, while recognizing that Git commits alone do not measure scholarly
contribution.

Mandatory comparisons include:

- Barata's 2021 dissertation and the original exDQLM paper;
- the original exAL source and any later exAL regression work cited;
- DESN and Bayesian quantile-DESN antecedents;
- quantile synthesis and noncrossing/rearrangement antecedents;
- Pouplin et al.'s residual-product criterion and classical tolerance-interval
  methods for MPI/MTI/TCSP; and
- prior forecast-correction/synthesis methods used by the Environmetrics work.

Publication status, reuse permission, novelty and candidate contribution remain
`UNVERIFIED` until supported by evidence or an explicit author/advisor record.

Exit criterion: each candidate chapter has a defensible contribution statement
and an attribution/rights status, or it is marked not ready.

### Phase 6: cross-project reconciliation

Create one comparison matrix across projects for targets, likelihoods/losses,
priors, algorithms, data, metrics, guarantees and limitations. In particular:

- separate exdqlm software/method work from inherited exDQLM foundations;
- determine where the San Lorenzo/Big Tree material is reused across the
  package article, Environmetrics article and Q-DESN GloFAS application;
- determine whether Q-DESN's single-level and joint-quantile material is one
  integrated contribution or supports a genuinely separate unit;
- separate TCSP's distribution-free tolerance guarantee from fixed-target
  MTI generalized-Bayes computation; and
- test whether the tolerance paper and MTI regression/dynamic paper have enough
  distinct theory, computation and evidence to stand as two research units.

Prepare a notation and citation-key crosswalk before importing anything.
Preserve source-specific notation when a global replacement would change a
target or assumption.

Exit criterion: overlapping claims and reused evidence have one explicit home,
with cross-references rather than duplicate contribution claims.

### Phase 7: chapter architecture and author decision

Evaluate at least these consequential architectures:

- **Separate interval papers:** Environmetrics application; exdqlm/Q-DESN as
  independently supported units; TCSP tolerance intervals; MTI regression and
  dynamic endpoints.
- **Combined interval chapter:** combine the tolerance geometry/procedure and
  MTI endpoint extensions when their shared core or incomplete extension
  evidence makes two chapters misleading.
- **Software as supporting infrastructure:** treat exdqlm as shared background
  and reproducibility infrastructure if its candidate-specific contribution
  cannot be distinguished adequately from Barata's dissertation and prior
  exDQLM work.

The Q-DESN joint-quantile extension will stay inside the Q-DESN unit unless the
audit establishes a distinct question, contribution, evidence base and advisor-
approved chapter boundary. The existing three-slot template will be expanded
only if the evidence supports more independent units; it will not force five
projects into three artificial categories.

Exit criterion: `docs/chapter-plan.md` states one recommended architecture, one
alternative only when consequential, and the exact scientific decisions needed
from the author/advisors.

### Phase 8: verification and handoff

1. Write the final research audit and update the chapter plan.
2. Validate all JSON and source locators; check links and hashes proportionately.
3. Confirm that no absolute path, private detail, copied private text, large
   source artifact, or source Git history entered tracked dissertation files.
4. Review the complete dissertation diff and run `git diff --check`.
5. Build and inspect the dissertation if any build-facing file changed.
6. Update `docs/STATUS.md` and `docs/ASSISTANCE-LOG.md`.
7. Present the recommendation and wait for the author's chapter/version
   decisions before drafting.

## 8. Project-specific deep-audit checklist

### Q-DESN

Read the approved `main.tex`, `qdesn-supplement.tex`, Gaussian-DESN supplement,
authority/contribution documentation, application contracts and current
manuscript input closure. Trace the current single-quantile validation,
joint-quantile comparison, GloFAS results and PriceFM results to their promoted
manifests. Audit fixed-feature conditioning, reservoir selection, AL versus
quantile-fixed exAL interpretation, regularized-horseshoe parameterization,
MCMC versus VB roles, noncrossing/rearrangement, multi-step forecasts, score
definitions and all qualified/negative findings. Compare the current `main`
tree with only the worktree branches that feed or challenge its claims.

### Environmetrics application

Treat `wileyNJD-APA.tex` as the discovered manuscript root and `main.tex` as a
wrapper. Read the appended algorithms/supplement, asset manifest, generated
table documentation, figure/table provenance, software contract and corrections
response. Trace the five rolling-origin cases, exAL-M-T1 selection, forecast
information set, CRPS and quantile-loss tables, component-removal analysis and
interpretation figures through the public reproducibility bundle and available
workflow evidence. Preserve the distinction between frozen article assets,
selected-model rerun support and unavailable raw-archive reconstruction.

### RQR-GIBBS / MTI tolerance paper

Audit the current remote manuscript rather than the stale local scaffold. Trace
the fixed-content geometry, MPI and MTI definitions, TCSP scan calibration,
MTI-ECM comparator, direct content-probability check, feasibility exclusions,
iid validation and pharmaceutical illustration into proofs, code, configs,
tests and outputs. State exactly which interval receives a distribution-free
tolerance guarantee. Reconstruct the terminology transition from RQR to MPI/MTI
only as needed for provenance and attribution.

### MTI extensions

Audit the fixed-content/fixed-tilt target, residual-product generalized update,
pseudo-AL augmentation, Gibbs conditionals, ECM equations, ridge and shrinkage
paths, deterministic basis expansion, dynamic endpoint state model and FFBS
schedule. The observed repository contains manuscript/derivation files but no
standalone code or empirical output; locating and validating the implementation
and evidence source is therefore a first-order gap, not an invitation to infer
results. Keep tolerance guarantees and response prediction outside this unit
unless separately established.

### exdqlm JSS article and package

Audit the JSS article, appendices, response to editor, `code.R`, modular analysis
workflow and reproducibility index against the exact package source used for
the manuscript. Reconcile the article's 1.1.1 target with package 1.1.2 and the
older versions used by other projects. Trace MCMC, LDVB, legacy ISVB, static
exAL, transfer functions, shrinkage, diagnostics, forecasting and posterior-
predictive synthesis to package code/tests. Establish which contributions are
new candidate work versus Barata's exDQLM model, earlier computation and package
foundation. Verify how the claimed upload tarballs/replication archive are
constructed, because they are described by the README but are not tracked in
the inspected article tree.

## 9. Required audit deliverables

`docs/research-audit.md` will contain:

1. an executive conclusion and scope statement;
2. the exact source/version inventory and source graph;
3. a manuscript and contribution synopsis per project;
4. an inferential-target/method comparison matrix;
5. a numerical and asset provenance summary;
6. candidate/coauthor/antecedent contribution findings;
7. conflicts, contradictions and missing evidence ranked critical/high/medium/
   low;
8. a source-to-chapter map with include/exclude/support recommendations; and
9. explicit author/advisor decisions still required.

Supporting records will include:

- ignored `source-manifest.local.json` for exact paths, worktree state and
  private candidate details;
- a sanitized tracked source register/manifest only when it contains no private
  or machine-specific information;
- proportionate claim/equation/figure/table evidence records derived from
  `docs/claim-evidence.example.json`;
- notation and citation-key maps, either as compact sections of the audit or
  separate files if their size warrants it;
- updated `docs/chapter-plan.md`, `docs/STATUS.md` and assistance record.

## 10. Completion criteria

The research-audit stage is complete only when:

- every included source has an author-approved scholarly version and recorded
  exact commit/snapshot;
- every proposed research chapter has a distinct question, contribution,
  evidence base, attribution statement, limitations and rights status;
- all central numerical displays have traceable generators/inputs or a visible
  provenance gap;
- central claims are classified correctly as proved, likelihood-based,
  generalized-Bayes, posterior-predictive, empirical, descriptive or
  unverified;
- repeated material has one principal chapter home and documented reuse;
- the Barata/exDQLM/exAL antecedent comparison is complete;
- private or local-only material has not leaked into tracked dissertation
  sources;
- the dissertation remains self-contained and builds without sibling research
  repositories; and
- the author has received a concrete recommendation and a short list of genuine
  scientific decisions before any chapter prose is drafted.

## 11. Decisions to request during execution

The audit can start from the observed heads, but final inclusion requires the
author to confirm:

- whether the observed Q-DESN `main` head, current RQR tolerance manuscript,
  current MTI extensions manuscript, Environmetrics submission freeze and JSS
  article head are the intended scholarly versions;
- whether newer unmerged Q-DESN experiment branches should be evaluated as
  dissertation candidates or only recorded as future/unpublished work;
- the status of each paper and the version/reuse terms permitted in the
  dissertation;
- the candidate's and coauthors' roles by project;
- whether the private interval-regression candidate is part of the MTI lineage;
  and
- whether the two MTI papers are intended as separate dissertation research
  units, subject to the audit's independence findings.
