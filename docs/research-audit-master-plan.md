# Research-audit master plan and readiness diagnosis

Status: **EXECUTED — audit complete; author decisions and drafting remain pending**
Prepared: 2026-09-15
Scope: the five author-nominated PhD research repositories and only those
additional sources needed to resolve their provenance, claims, or relationships.

The author approved full execution of this plan on 2026-09-15. It supersedes
`research-audit-plan.md` as the controlling execution plan while preserving
that file as the historical baseline. This approval authorizes the audit
activities listed here; it does not by itself authorize dissertation drafting,
publication, pushing, merging, Overleaf synchronization, or alteration of a
research repository.

Sections 1–20 preserve the pre-execution diagnosis and protocol; Sections
21–23 record what was completed and which decision gates remain open.

## 1. Executive determination

The proposed research audit is feasible, but it should not begin by reading
every file in every worktree or by choosing chapters from repository names.
The safest and most informative route is a **claim-complete, version-aware
audit**: freeze reproducible source snapshots, identify each manuscript's
authority chain, trace every candidate dissertation claim to evidence, and only
then decide whether the projects constitute distinct dissertation
contributions.

The earlier plan has a strong foundation: it protects original working trees,
requires exact commits, distinguishes inferential targets and interval types,
and postpones drafting until an author decision. The readiness diagnosis found
several design issues that should be repaired in the plan before execution:

1. The repository already has an institutional `docs/source-register.json`.
   It must not be repurposed as a research-source database.
2. The example and local research manifests have schema drift and do not yet
   define a stable public/private provenance contract.
3. Branch and worktree counts are large enough that exhaustive content review
   would create noise and risk. Metadata triage must precede selective deep
   review.
4. Several local copies are stale, non-canonical, or contain large ignored
   runtime artifacts. Original trees are unsuitable as mutable audit spaces.
5. Manuscript reuse rights, candidate contribution records, and intended
   versions are not yet established. These are decision gates, not facts to
   infer from authorship or repository ownership.
6. The current chapter plan is a placeholder and predates the source
   investigation. It must remain provisional until the evidence matrix is
   complete.
7. Reproducibility language needs a defined scale. “Located,” “verified,”
   “regenerated,” and “reproduced” must not be used interchangeably.
8. The thesis setup and research-planning changes do not yet have a clean Git
   checkpoint. This must be resolved before audit execution, without mixing in
   unrelated work or pushing automatically.

Accordingly, the optimal sequence is:

> establish a clean thesis checkpoint → freeze discovery snapshots → prepare
> version dossiers → audit the exDQLM/exAL baseline → audit each application or
> method at a fixed commit → reconcile overlap and contradictions → obtain
> contribution/rights decisions → recommend a chapter architecture → obtain a
> separate drafting authorization.

No scientific conclusion, novelty judgment, chapter selection, or permission
determination is made by this planning document.

## 2. Questions this plan must answer

The audit is successful only if it gives the author and committee defensible
answers to the following questions.

### 2.1 Source authority

- Which exact commit and manuscript file represents each project at the audit
  date?
- Is that snapshot merely the current default branch, or is it the author's
  intended dissertation source?
- Which supplements, response letters, manifests, code versions, and generated
  artifacts belong to that manuscript version?
- Which local worktrees contain meaningful unmerged work, and which are
  experiments, stale variants, or runtime state?

### 2.2 Scientific identity

- What is the inferential target in each project: conditional quantiles,
  simultaneous/joint quantiles, predictive distributions, tolerance coverage,
  or another estimand?
- What likelihood, loss, estimating equation, or generalized updating rule is
  used, and what is its interpretation?
- What is proved, what is empirically observed, and what is only proposed?
- Which interval is being reported: posterior credible, predictive, confidence,
  conformal, tolerance, or a project-specific construction?

### 2.3 Contribution and overlap

- What is the candidate's specific intellectual and implementation
  contribution to each project?
- What is inherited from Barata et al. (2021), exDQLM/exAL, the software
  package, or other antecedents?
- Are Q-DESN single-quantile, joint-quantile, GloFAS, and PriceFM materials one
  contribution with variants, or multiple defensibly independent units?
- Do RQR-GIBBS and MTI-EXTENSIONS represent two contributions, a method plus an
  extension, or one overlapping line of work?
- Is the exdqlm article itself a candidate research chapter, a software
  contribution, shared infrastructure, or background/supporting material?

### 2.4 Evidence and reuse

- Can every central numerical statement, figure, and table be traced to an
  immutable source snapshot and generation contract?
- Which results can be checked cheaply, and which require data, computing,
  credentials, or a large rerun?
- Which manuscript text, figures, tables, code, and data can lawfully and
  appropriately be reused in a public dissertation?
- What committee, coauthor, publisher, or program approval remains necessary?

### 2.5 Dissertation architecture

- Which projects satisfy the program's research-chapter expectations without
  counting overlapping variants twice?
- What shared background and notation should be centralized?
- What belongs in main chapters, appendices, a software/reproducibility
  appendix, or should be omitted?
- What new exposition is necessary to turn article-shaped material into a
  coherent dissertation rather than a bundle of manuscripts?

## 3. Scope and non-scope

### 3.1 Authorized seed sources

The audit may inspect these five nominated repositories:

| Source ID | Repository | Provisional role |
| --- | --- | --- |
| `qdesn` | `AntonioAPDL/Article-Q-DESN---Version-2` | Most recent Q-DESN line; method and applications |
| `environ` | `AntonioAPDL/Evironmetrics---REVISED-DOC-Corrected-2` | First application project |
| `rqr` | `AntonioAPDL/RQR-GIBBS` | Recent MTI/tolerance-interval line |
| `mti-ext` | `AntonioAPDL/MTI-EXTENSIONS` | Extensions to the MTI line |
| `exdqlm-article` | `AntonioAPDL/exdqlm---Article` | Article associated with the exdqlm package |

The exdqlm package repository is a required supporting source because the
article, application, and RQR work depend on particular package states. It is
not automatically a sixth dissertation contribution.

### 3.2 Controlled scope expansion

A related repository or paper may enter the deep audit only when at least one
of these conditions is recorded:

- a seed manuscript explicitly cites it for a central method or claim;
- a manifest or workflow declares it as the source of a dissertation-facing
  figure, table, data transformation, or software version;
- it resolves a conflict between manuscript, supplement, code, and results;
- it is an antecedent needed to distinguish the candidate contribution; or
- the author explicitly adds it.

The relationship, reason, proposed depth, and public/private status must be
entered before deep inspection. Merely sharing an account, topic word, date, or
repository prefix is not sufficient. Unrelated-looking candidates are reported
for author decision rather than audited broadly.

### 3.3 Activities excluded until separately authorized

- drafting or rewriting dissertation scientific prose;
- importing manuscript text, figures, tables, code, or private metadata;
- modifying, fetching in, switching, stashing, cleaning, or building an
  original research working tree;
- large simulations, complete output-archive downloads, or full independent
  reproduction runs;
- publication-status or novelty claims based only on names, dates, or remote
  metadata;
- deciding contribution credit, permission, or chapter eligibility on the
  author's behalf;
- pushing, merging, publishing, changing visibility, or synchronizing
  GitHub/Overleaf.

## 4. Method and limits of the readiness diagnosis

This plan was prepared from a read-only reconnaissance of repository metadata,
tracked file inventories, documented entry points, current public remote heads,
local branch/worktree status, and the existing dissertation instructions and
plans. No research repository was fetched, checked out, reset, stashed,
cleaned, built, or edited. No simulations were run. No private source material
was copied into the dissertation.

The reconnaissance is sufficient to design the audit and identify provenance
hazards. It is not a scientific audit and does not establish correctness,
novelty, reproducibility, publication status, author contribution, or reuse
permission.

## 5. Current-state diagnosis

### 5.1 Dissertation workspace

| Area | Verified state | Consequence |
| --- | --- | --- |
| Setup | Server checkout and 20-page starter build were previously validated | No setup rebuild is needed for planning-only changes |
| Branch | Setup work is on a local setup branch based on the current remote default-branch commit | Preserve the branch and review all pre-existing setup edits |
| Git checkpoint | Setup and planning files remain uncommitted; author identity is not configured | Create reviewed, focused local commits only after author approval and identity setup |
| Current chat | The active chat is scoped to a research worktree, not the thesis checkout | Execute the future audit from a fresh thesis-scoped chat |
| Research outputs | Full audit, public research manifest, claim ledger, and final chapter map do not exist | Do not treat planning reconnaissance as completed evidence |
| Chapter plan | Existing three-slot plan predates this investigation | Freeze it as provisional until cross-project reconciliation |

### 5.2 Source snapshots observed on 2026-09-15

These are discovery observations, not author-approved dissertation versions.
They must be rechecked at execution start and then frozen by commit.

| Source | Observed default-branch commit | Shape observed | Main audit risk | Planned access mode |
| --- | --- | --- | --- | --- |
| Q-DESN | `757522db0f85815244370ec92a194de132268883` | 192 remote heads; 172 local worktrees; large local ignored runtime state | Authority and variant sprawl; local tree is unsuitable as an audit sandbox | Fresh ordinary-Git audit clone at fixed commit; metadata-first branch triage |
| Evironmetrics | `1272bfc10442a28add5a4c74ff641e9b9a8e9666` | Six remote heads; matching clean local checkout | External/live workflow and project-specific package freeze may not be self-contained | Reuse matching tree read-only; isolated copy only for targeted checks |
| RQR-GIBBS | `73887b9c86ef767aa1567c660718667945630aef` | 49 remote heads; remote content is much larger and conceptually newer than local copy | Stale local scaffold could misidentify the current project | Fresh audit clone at fixed commit; compare histories before selecting variants |
| MTI-EXTENSIONS | `f345d946aa5a81b94795838bec58d874a0fdd0c9` | One head and eight tracked files | Theory claims are visible, but implementation/evidence is not in the visible repository | Small fresh audit clone; dependency search only when claims require it |
| exdqlm article | `d5534e97db8414fd875022261d4c530eae4676e4` | Six remote heads; matching canonical local checkout plus another stale worktree | Manuscript, archived replication promises, and tracked artifacts may not align | Reuse canonical matching tree read-only; never infer from stale chat worktree |
| exdqlm package | `e51045a4324901cced27ca2aaa22569afbc8e0e6` | 90 remote heads; 53 local worktrees; package version 1.1.2 | Article/application freezes, tags, local tarballs, and current package state differ | Inspect matching canonical tree read-only; build only an archived copy if justified |

Supporting repositories already documented by seed sources include the San
Lorenzo reproducibility repository and a corrections repository. They are
eligible for bounded inspection only after their exact role is entered in the
research manifest. Historical Q-DESN repositories and other candidates remain
discovery leads, not automatic audit subjects.

### 5.3 Material source-specific findings that shape the plan

#### Q-DESN

- The current repository contains several manuscript/result lines, including
  single-quantile, joint-quantile, GloFAS, and PriceFM materials.
- The canonical local working tree is not the observed remote default head and
  carries a very large amount of ignored runtime material. Its size is dominated
  by local trackers and application outputs rather than Git history.
- Repository instructions require command-line Git for source authority and
  prohibit using other synchronization routes as substitutes.
- Branch/worktree abundance cannot be treated as a contribution count.

Conclusion: use a fresh fixed-commit clone and a two-pass branch audit. Do not
traverse 172 worktrees deeply or rely on ignored runtime files without a
separate snapshot and provenance decision.

#### Evironmetrics application

- The current local checkout matches the observed default head and has a rich
  manifest/provenance structure.
- The manuscript points to a public reproducibility repository, corrections
  material, and a project-specific exdqlm package version.
- A live/private workflow referenced by the project is not established from
  the current server context, so some figures or tables may remain only
  partially reproducible from the public bundle.

Conclusion: begin from the manuscript and its declared manifest, preserve its
software freeze, and classify unavailable workflow evidence explicitly rather
than silently substituting a newer package.

#### RQR-GIBBS

- The matching local copy is materially stale: its tracked inventory and topic
  presentation differ from the current remote default branch.
- The current remote manuscript describes mean-tilted/short tolerance interval
  work, not merely the older RQR scaffold suggested by the repository name.
- A related exdqlm feature worktree exists, but it contains untracked author
  material and must remain untouched.

Conclusion: the current remote snapshot needs a clean audit clone. Terminology,
target, guarantee, and links to package code must be established from current
content, while older branches are treated as history rather than authority.

#### MTI-EXTENSIONS

- The visible repository is a compact manuscript/supplement bundle with no
  evident implementation, tests, generated-result archive, or full license.
- Its claimed regression and dynamic endpoint extensions may depend on code in
  another source or may currently be theory-only.

Conclusion: audit its mathematics and references first. The absence of visible
code is an evidence gap to resolve, not proof that the work is invalid or a
separate contribution.

#### exdqlm article and package

- The article repository has substantial analysis assets and reproducibility
  documentation, but some replication archives named in documentation are not
  tracked at the observed snapshot.
- The article and application refer to earlier package freezes while the
  package default branch is newer. Local package tarballs exist, but the newest
  versions are not all represented by matching release tags.
- Package authorship identifies shared contributions. Comparison with Barata
  et al. (2021) and the original exDQLM/exAL work is mandatory before describing
  novelty or candidate contribution.

Conclusion: build a version/provenance map before any cross-project update.
Newer software is not automatically the correct software for an older article.

### 5.4 Rights and contribution readiness

No top-level manuscript license or sufficiently specific candidate-contribution
statement was located during reconnaissance in the seed manuscript
repositories. The package has its own software license, which does not grant
automatic permission to reuse article text, figures, or coauthored materials.
One application-level license header is not a substitute for a manuscript-wide
rights determination.

Therefore, contribution and rights records are mandatory before source material
is imported or a coauthored manuscript is assigned as a dissertation chapter.
The audit may identify and summarize evidence before those decisions, but it
must label inclusion status as unresolved.

## 6. Audit of the previous plan

| Previous design element | Judgment | Required refinement |
| --- | --- | --- |
| Read-only treatment of research sources | Retain | Add before/after source guards and ban builds in original trees |
| Exact branch/commit/dirty recording | Retain | Separate discovery, audit, and author-approved snapshots |
| Tiered source inventory | Retain | Make scope expansion claim-driven to prevent unbounded literature/repository search |
| Manuscript-first reading | Retain | Define one ordered evidence ladder for every project |
| Statistical distinctions and Barata comparison | Retain | Encode each distinction as required fields in claim records |
| Worktree inspection | Refine | Pass 1 inventories all references/metadata; Pass 2 reads only authority-relevant variants |
| Author approval of versions | Refine | Produce a comparative version dossier first; approval selects inclusion snapshot, not initial discovery |
| Source manifest | Replace ambiguous wiring | Keep institutional source register untouched; create a separate sanitized research manifest |
| Local manifest | Normalize later | Reconcile field names and statuses with the public schema while retaining paths privately |
| Reproducibility checks | Refine | Use explicit evidence levels and reserve “reproduced” for a full independent rerun |
| Chapter alternatives | Retain | Evaluate only after overlap, contribution, rights, and evidence readiness are known |
| Completion criteria | Expand | Add project stop conditions, issue severity, source guards, validation, and author gates |
| Documentation updates | Reorder | Do not rewire kickoff/chapter files until this master plan is approved |

The earlier plan remains valuable as a detailed baseline. It should be retained
as an audit trail rather than overwritten. Once this plan is approved, the
earlier file should receive a short supersession note and link to this document.

## 7. Controlling information architecture

The audit must use one directional evidence flow:

```text
read-only original source / immutable audit clone
                  |
                  v
ignored raw observations and exact local paths
                  |
                  v
sanitized research source manifest
                  |
                  v
claim / figure / table evidence records
                  |
                  v
research-audit narrative and conflict register
                  |
                  v
author-approved chapter plan
                  |
                  v
separately authorized dissertation imports and drafting
```

### 7.1 Canonical artifact ownership

| Artifact | Authority and purpose | Public? | Action during future audit |
| --- | --- | --- | --- |
| `docs/research-audit-master-plan.md` | Controlling process after approval | Yes | Maintain decisions and deviations |
| `docs/research-audit-plan.md` | Historical baseline plan | Yes | Preserve; add supersession note after approval |
| `docs/source-register.json` | Institutional/template requirement sources | Yes | Do not repurpose or mix with research repositories |
| `docs/source-snapshots.json` | Institutional/template source snapshots | Yes | Do not repurpose |
| `source-manifest.local.json` | Exact paths, access notes, dirty snapshots, audit-clone locations | No; ignored | Normalize to the approved research schema |
| `source-manifest.json` | Sanitized research sources, immutable commits, roles, status | Yes | Create after schema approval |
| `audit-inputs/<run-id>/` | Raw command output, inventories, temporary comparisons | No; ignored | Create per run; hash important evidence |
| `docs/claim-evidence.json` | Structured claim/figure/table provenance and verification | Yes | Create and validate |
| `docs/research-audit.md` | Human-readable synthesis, conflicts, gaps, recommendations | Yes | Create from structured evidence |
| `docs/chapter-plan.md` | Author-approved architecture and source-to-chapter map | Yes | Update only after the decision gate |
| `docs/STATUS.md` | Current phase, evidence gaps, next decision | Yes | Update at each completed gate |
| `docs/ASSISTANCE-LOG.md` | Factual record of AI-assisted work | Yes | Append material audit activities |

### 7.2 Public/private boundary

Public records may contain public repository identifiers, immutable commits,
sanitized relative file locators, methods, evidence status, and approved
contribution summaries. They must not contain credentials, access tokens,
absolute server paths, private repository names not approved for disclosure,
unreleased manuscript text, personal notes, or unapproved coauthor material.

Exact local paths and sensitive access notes belong only in ignored records.
Private evidence may support an audit conclusion, but the public record must
describe that support at an approved level without exposing the source.

### 7.3 Stable identifiers

Every public research source, snapshot, manuscript, claim, figure, table,
conflict, decision, and audit run must have a stable ID. Recommended prefixes:

- `SRC-` source repository or paper;
- `SNP-` immutable repository snapshot;
- `DOC-` manuscript, supplement, response, or note;
- `CLM-` scientific or contribution claim;
- `ART-` figure, table, dataset, or generated artifact;
- `CON-` contradiction or unresolved conflict;
- `DEC-` author/committee decision;
- `RUN-` bounded validation or reproduction attempt.

Cross-file records refer to these IDs rather than relying on mutable filenames
or prose matching.

## 8. Snapshot model and source guards

Three snapshot roles prevent a default-branch head from becoming an accidental
editorial decision:

1. **Discovery snapshot** — the commit observed during reconnaissance. It is a
   starting point and may change before execution.
2. **Audit snapshot** — an immutable commit selected for detailed inspection,
   normally the freshly verified default head plus any explicitly justified
   variant. Audit can proceed under existing inspection authorization.
3. **Inclusion snapshot** — the manuscript/version the author approves as a
   dissertation source after reviewing the version dossier. Only this role may
   feed controlled imports and chapter drafting.

Every interaction with an original source records a source guard before and
after the session:

- repository identity and origin URL;
- current branch or detached state;
- `HEAD` commit;
- upstream, ahead/behind status when available;
- porcelain status including untracked-file names but not their content;
- a hash of the normalized status record;
- timestamp and audit run ID.

Any unexpected before/after difference stops work on that source and is
reported. Audit clones may be fetched only as explicitly planned; original
research trees are never fetched or switched.

## 9. Evidence and verification vocabulary

Every substantive claim receives a type, locator, status, and verification
level. The audit uses these levels consistently:

| Level | Meaning | Permitted wording |
| --- | --- | --- |
| `E0` | Mentioned or asserted; supporting source not yet located | “asserted,” “unverified” |
| `E1` | Exact manuscript/code/proof locator found at a fixed snapshot | “located,” “documented” |
| `E2` | Cross-file consistency, manifest/hash, inputs, and generation contract checked | “provenance verified” or “internally consistent,” with scope |
| `E3` | A bounded build, artifact-regeneration, or test contract was executed in an isolated environment and checked | “regenerated” only for regenerated artifacts, or “targeted test passed”; never blanket “reproduced” |
| `E4` | Full claimed workflow independently rerun from declared inputs with acceptance criteria met | “reproduced,” with environment and limitations |

Failure at a level is evidence, not a reason to inflate or erase the claim. A
result can be scientifically plausible but only `E1`; a workflow can reach
`E3` while contribution credit remains unresolved.

Each claim is also classified as one of:

- definition or setup;
- assumption;
- proved theorem/proposition/lemma;
- empirical result;
- numerical implementation claim;
- novelty/relationship claim;
- candidate-contribution claim;
- publication or reuse-status claim.

Proof claims record whether the statement, assumptions, proof, dependencies,
and any numerical illustration agree. Empirical claims record the estimand,
data snapshot, split/design, configuration, seed policy, software version,
artifact hash, and uncertainty measure. “Credible,” “predictive,” “confidence,”
“conformal,” and “tolerance” intervals are separate controlled values, not
interchangeable prose labels.

## 10. Prioritized issue register

### 10.1 Must be resolved before audit execution

| ID | Issue | Why it blocks | Planned resolution |
| --- | --- | --- | --- |
| `READY-01` | Future work must run in a thesis-scoped chat | Wrong scope can apply the wrong instructions and edit the wrong repository | Open a new thesis window/chat and verify host, path, repository, branch, and instructions |
| `READY-02` | No clean thesis planning checkpoint | Later diffs could mix setup work with audit evidence | Review existing changes, configure author identity by user-approved means, and make focused local commits; do not push |
| `READY-03` | Research manifest schema/ownership is ambiguous | Automated records could overwrite or conflict with institutional evidence | Approve the artifact map and schema; leave `docs/source-register.json` unchanged |
| `READY-04` | Audit-root and storage strategy not recorded | Large local trees and ignored outputs create risk and poor reproducibility | Use external audit clones/caches with ignored exact-path records and a free-space check |

### 10.2 Must be resolved before inclusion or chapter selection

| ID | Issue | Affected source(s) | Required evidence |
| --- | --- | --- | --- |
| `DECIDE-01` | Intended manuscript/version is unconfirmed | All | Version dossier and author selection |
| `DECIDE-02` | Candidate contribution and coauthor roles are unconfirmed | All coauthored work | Source evidence plus author/coauthor/committee record as applicable |
| `DECIDE-03` | Reuse/publication permissions are unconfirmed | Manuscript text, figures, tables, private assets | Rights checklist with source-specific decision |
| `DECIDE-04` | Q-DESN variants may overlap | Q-DESN | Method/data/claim/result delta matrix |
| `DECIDE-05` | RQR and MTI-EXTENSIONS independence is unknown | RQR, MTI extensions | Shared-theory/code/results matrix and contribution analysis |
| `DECIDE-06` | exdqlm package/article contribution boundary is unknown | exdqlm and application projects | Barata antecedent comparison and version map |

### 10.3 May remain as explicit limitations

- unavailable private/live workflows;
- expensive simulations not justified by a concrete central claim;
- historical branches with no evidence of authority or unique contribution;
- missing external data that cannot lawfully or practically be obtained;
- publication or administrative facts pending authoritative confirmation.

These do not block the whole audit. They block only claims or chapter choices
that depend on them and must be reported with owner and next decision.

## 11. Execution strategy after approval

### Phase 0 — authorize and checkpoint

**Entry:** author approves this plan or records requested changes.
**Actions:** start a fresh thesis-scoped chat; verify environment; review the
entire existing thesis diff; resolve Git identity; create focused local
planning/setup commits; record free space and audit-root policy.
**Outputs:** clean or explicitly understood thesis state, approved plan status,
and `RUN-` record for audit initiation.
**Exit:** no unexplained thesis changes; no source repository touched.
**Stop:** unexpected thesis origin, branch, or overlapping user edits.

### Phase 1 — approve schema and freeze discovery

**Entry:** Phase 0 complete.
**Actions:** define the sanitized research manifest and claim-evidence schemas;
normalize the ignored local manifest; re-run remote-head checks; create source
guards; estimate clone/storage requirements; create only the required audit
clones. For Q-DESN, use ordinary command-line Git as its instructions require.

**Outputs:** `source-manifest.json`, normalized local manifest, raw evidence
under a run directory, and immutable audit snapshots.
**Exit:** every seed source has a unique ID, fixed audit commit, access mode,
authority status, and verified main entry point.
**Stop:** authentication failure, insufficient storage, source changed during
snapshotting, or unclear origin identity.

### Phase 2 — prepare version dossiers

**Entry:** fixed audit snapshots.
**Actions:** inventory all heads/worktrees at metadata level; compare likely
manuscript variants by ancestry, changed files, titles, abstracts, response
letters, manifest dates, and declared submission/revision status. Deep-read
only variants that are cited, authority-marked, uniquely unmerged, or needed to
resolve a contradiction.
**Outputs:** one version dossier per project with a recommended audit target,
alternative candidates, differences, and uncertainty.
**Exit:** discovery and audit snapshots are distinct and documented.
**Decision:** the author selects or confirms the intended inclusion snapshot;
uncertain sources remain auditable but cannot be imported.

### Phase 3 — establish the exDQLM/exAL and software baseline

**Entry:** version dossiers available.
**Actions:** read Barata et al. (2021) and directly necessary antecedents; map
original targets, likelihood/update, algorithms, guarantees, applications, and
software. Map exdqlm package versions used by each project, including tags,
tarballs, commits, dependency lock information, and archive hashes when
available. Audit the exdqlm article against this baseline.
**Outputs:** antecedent matrix, package-version graph, article/package
contribution dossier, and initial claim records.
**Exit:** later projects can state precisely what they inherit, modify, or add.

**Stop:** inaccessible central antecedent or package state; record a targeted
gap rather than guessing.

### Phase 4 — project dossiers

Each project follows the same ordered evidence ladder:

1. repository instructions and declared authority files;
2. main manuscript;
3. supplement and theory notes;
4. response letters and revision records;
5. manifests, generation contracts, and data/configuration descriptors;
6. implementation and focused tests;
7. generated outputs and artifact hashes;
8. only the antecedents needed for central claims.

Scientific and provenance tracks run in parallel conceptually but produce one
joined dossier. The scientific track records estimand, model/update, theory,
empirical design, findings, limitations, novelty, and overlap. The provenance
track records source versions, inputs, code paths, configuration, randomness,
artifacts, checks, and reproducibility level.

#### Phase 4A — Evironmetrics application

Audit the authoritative manuscript, its asset manifest, supplement/revision
materials, experiment run map, forecast/software contracts, generated-table
manifest, San Lorenzo reproducibility link, corrections, and its exdqlm 1.1.0
freeze. Reconcile every dissertation-facing figure/table with the declared
source. Do not replace the historical software freeze with current package code.

Exit requires an application-contribution statement; a table/figure provenance
map; separation of scientific finding from implementation behavior; and an
explicit list of items unavailable without the live/private workflow.

#### Phase 4B — exdqlm article and package

Audit the article, supplement/reproducibility protocol, response materials,
examples, tests, generated outputs, DESCRIPTION/NAMESPACE/NEWS, and relevant
algorithm implementations. Compare article version 1.1.1, application version
1.1.0, and current package version 1.1.2 without collapsing them. Check whether
documented archives exist, whether local tarballs can be tied to commits, and
whether tags/releases support the stated provenance.

Exit requires a version table, claim-to-function/test map, missing-archive
status, Barata comparison, and candidate/coauthor contribution questions.

#### Phase 4C — Q-DESN

Audit the fixed default snapshot first. Establish the relationship among the
main manuscript, supplement, single-quantile v14 assets, corrected joint-
quantile v4 assets, shared-backbone manifest, GloFAS Part 4, and PriceFM R98.
Use authority ledgers and build/check scripts to identify the declared
publication path. Inspect other branches/worktrees deeply only if Phase 2
identifies a unique, relevant delta.

The dossier must distinguish single versus joint quantile targets; reservoir
state/readout contributions; probabilistic updating or loss interpretation;
calibration and scoring metrics; application-specific versus general evidence;
and every relationship to exDQLM/exAL. Large ignored tracker/output directories
are not evidence until separately inventoried, hashed, and connected to a
declared artifact.

Exit requires a variant delta matrix, one recommended inclusion snapshot or an
explicit unresolved choice, figure/table provenance, and a defensible statement
of which Q-DESN contribution is unique.

#### Phase 4D — RQR-GIBBS / short tolerance intervals

Audit a fresh current snapshot, not the stale local scaffold. Define the
estimand, interval type, nominal guarantee, finite-sample/asymptotic status,
assumptions, endpoint construction, Gibbs/generalized-update role, and the
meaning of RQR/MPI/MTI/TCSP terminology. Trace the pinned exdqlm feature code by
immutable commit through an isolated archive as repository instructions allow;
do not load or build the original package worktree.

Exit requires theorem-to-code links where they exist, simulation/application
design provenance, negative/robustness audit results, and an explicit boundary
between RQR work and MTI extensions.

#### Phase 4E — MTI-EXTENSIONS

Audit the main manuscript and supplement for regression and dynamic endpoint
extensions, their assumptions, algorithms, guarantees, and dependence on the
RQR foundation. Search for implementation only through references declared by
the manuscript or author. If none is found, record the work as theory-only or
implementation-unverified at the appropriate evidence level.

Exit requires a theorem/algorithm inventory, dependency map to RQR, evidence
availability statement, and a judgment-ready—not agent-decided—independence
analysis.

### Phase 5 — cross-project reconciliation

**Entry:** all project dossiers complete or explicitly limited.
**Actions:** build matrices for shared estimands, notation, likelihood/update,
algorithms, package versions, datasets, simulations, figures/tables,
antecedents, and contributions. Resolve or record contradictions. Identify
duplicate experiments and article variants so they are not counted twice.
**Outputs:** cross-project terminology map, overlap matrix, conflict register,
shared-background outline, and prioritized evidence gaps.
**Exit:** every candidate contribution has a defensible relationship to every
other candidate and to central antecedents.

### Phase 6 — contribution and rights decision

**Entry:** evidence-based overlap analysis.
**Actions:** present source-specific contribution prompts and reuse checklist to
the author; record coauthor, publisher, committee, and program questions;
separate public, private, and not-yet-approved materials.
**Outputs:** approved or unresolved contribution statements, rights status, and
inclusion eligibility by source.
**Exit:** no source is recommended for direct import without an explicit status.

**Stop:** material dispute or absent required permission blocks that source's
inclusion, not the rest of the audit.

### Phase 7 — chapter architecture decision

**Entry:** scientific, provenance, overlap, contribution, and rights dossiers
available.
**Actions:** prepare one primary architecture and at most one consequential
alternative. Score candidate chapters on distinct contribution, evidentiary
readiness, coherence, candidate role, rights, and amount of new exposition.
Centralize shared background and notation; place supporting proofs,
experiments, and software detail deliberately.
**Outputs:** proposed table of contents, source-to-chapter map, contribution
statement, appendix plan, omissions, and a short decision memo.
**Decision:** author approves, revises, or rejects the architecture.
**Exit:** update `docs/chapter-plan.md` only after that decision.

### Phase 8 — finalize the audit handoff

**Entry:** architecture decision recorded.
**Actions:** reconcile structured records with the narrative; run validators;
review public/private boundaries; update status and assistance log; compile only
if a build-facing file has changed.
**Outputs:** complete `docs/research-audit.md`, manifests, claim evidence,
chapter plan, validation report, prioritized drafting gaps, and exact next-unit
recommendation.
**Exit:** the audit is independently traceable and no drafting has begun.

## 12. Required cross-project comparisons

The final audit must include, at minimum, these matrices:

| Matrix | Required dimensions |
| --- | --- |
| Inferential target | response, conditioning information, quantile level(s), joint/single target, predictive/tolerance target |
| Statistical update | likelihood, loss or scoring rule, generalized posterior/update, prior/regularization, computation |
| Guarantee | posterior interpretation, calibration, coverage type, nominal level, finite/asymptotic/empirical support |
| Dynamic structure | state evolution, reservoir/readout, dependence handling, regression/dynamic extensions |
| Evidence | theorem, simulation, application, ablation/negative audit, sensitivity, limitation |
| Software | repository, commit, package version, entry point, test, archive/hash, environment |
| Data | source/version, preprocessing, split, outcome leakage controls, availability |
| Artifacts | figure/table ID, generating script, inputs, parameters, output hash, manuscript locator |
| Antecedent delta | inherited element, modification, new contribution, evidence, unresolved novelty question |
| Authorship | candidate role, coauthor role, documentary basis, author confirmation, reuse status |
| Dissertation placement | proposed chapter/section/appendix/omit, rationale, overlap risk, required new exposition |

The comparison must explicitly include Barata et al. (2021), exDQLM/exAL, and
any closer antecedent actually used by a central claim. It must not infer
novelty from the absence of a repository match.

## 13. Project dossier template

Each project entry in `docs/research-audit.md` will use the same structure:

1. identity and immutable snapshot;
2. authority chain and intended manuscript status;
3. main research question and inferential target;
4. model, assumptions, likelihood/loss/update, and computation;
5. theoretical claims and proof locators;
6. empirical design, results, and limitations;
7. figure/table/data/software provenance;
8. comparison with antecedents and sibling projects;
9. candidate and coauthor contribution evidence;
10. rights, privacy, and inclusion status;
11. contradictions and unresolved questions;
12. evidence levels reached and checks not performed;
13. dissertation value, overlap risk, and required new exposition;
14. recommendation: include, combine, appendix/support, omit, or author decision
    required.

Recommendations remain provisional until the author decision gate.

## 14. Branch and worktree triage protocol

Large repositories use two passes.

### Pass 1 — exhaustive metadata, bounded content

Record all local worktrees and remote heads, commits, ancestry relationships,
last commit metadata, clean/dirty state for local trees, and changed-path
summaries relative to the audit default snapshot. Do not open every output or
diff every branch in full.

### Pass 2 — selective deep comparison

Deep-inspect a branch/worktree only if it is:

- named by an authority file, manuscript, response, or handoff;
- the source of a central artifact or package freeze;
- not merged and plausibly contains a unique contribution;
- necessary to explain a contradiction; or
- selected by the author.

Every inspected variant receives a reason and disposition. All others receive a
metadata-only status. This makes the audit comprehensive with respect to
relevant evidence without equating comprehensiveness with reading all runtime
files.

## 15. Reproducibility protocol

### 15.1 Default: verify before rerunning

For each central artifact, first verify the declared inputs, scripts,
configuration, software snapshot, seed policy, manifest, and output hash. Only
then decide whether execution would resolve a material uncertainty.

### 15.2 Isolated execution

Any authorized build or targeted run occurs in a fresh audit clone, archive, or
copy outside both the thesis and original source trees. Environments and caches
are project-scoped. Original research worktrees remain untouched. Expensive
runs require a concrete claim, estimated time/storage, acceptance criteria, and
author approval.

### 15.3 Result comparison

Before execution, define whether success means exact hash equality, numerical
tolerance, statistical agreement, or structural agreement. Record software and
system versions, seeds, command, duration, outputs, deviations, and cleanup
status. Never silently replace missing dependencies or data with approximations.

### 15.4 Version preservation

Each project retains the package/data version associated with its manuscript.
Cross-version testing is a separate diagnostic and cannot overwrite historical
provenance. The exdqlm 1.1.0, 1.1.1, and 1.1.2 lines must remain distinguishable.

## 16. Validation and quality controls

After approval, one small repository-native validator should be added rather
than a collection of ad hoc scripts. Its proposed responsibilities are:

- parse all research-audit JSON;
- enforce unique stable IDs and valid cross-references;
- require full immutable commit identifiers for Git snapshots;
- enforce allowed statuses and evidence levels;
- ensure every included claim has a source and locator;
- ensure every dissertation-facing figure/table has an artifact record;
- reject “reproduced” below `E4`;
- confirm the local manifest and raw audit inputs remain ignored;
- flag absolute server paths, credentials, and known private identifiers in
  public files;
- ensure inclusion and chapter status are not marked approved without a
  decision record;
- confirm referenced imported assets exist only when import is later
  authorized.

The validator is a future implementation item; it is not created by this plan.
Manual review remains necessary for scientific meaning, rights, contribution,
and whether sanitization is adequate.

## 17. Issue classification and stop conditions

Issues use both severity and blocking scope:

- `critical`: source integrity, privacy, permission, or a central conclusion is
  at risk;
- `major`: chapter selection or a central claim cannot be supported;
- `moderate`: important provenance or exposition is incomplete but bounded;
- `minor`: editorial consistency or non-central cleanup.

Blocking scope is one of `audit-wide`, `source`, `claim`, `artifact`,
`inclusion`, or `drafting`. A missing optional artifact must not halt unrelated
projects; a source-integrity change may halt the affected audit.

Stop and report immediately when:

- an original source tree changes during an audit session;
- a command would alter an original source or expose a secret/private path;
- the repository identity or requested commit cannot be established;
- a required action would need sudo, broad account scanning, or materially more
  storage/compute than planned;
- private material would have to enter a public record;
- a contribution or rights dispute makes inclusion unsafe; or
- a scientific contradiction cannot be represented honestly without author or
  domain-expert input.

## 18. Decision framework for the dissertation

The audit recommends inclusion only after scoring each candidate unit on:

1. distinct research question and contribution;
2. separation from antecedents and sibling projects;
3. candidate contribution and ability to state it accurately;
4. theoretical and/or empirical evidence strength;
5. numerical provenance and reproducibility readiness;
6. rights and coauthor/committee suitability;
7. coherence with the unifying dissertation question;
8. amount of new exposition needed;
9. risk of double-counting a method, dataset, or result;
10. readiness within the dissertation timeline.

The current three-slot chapter plan is not evidence. A likely architecture may
eventually group projects into a foundational/software unit, an application
unit, a Q-DESN unit, and a tolerance-interval/MTI unit, but that structure is
only a hypothesis. The audit must test whether the software work is an
independent contribution and whether RQR plus MTI extensions form one or two
units. At least one consequential alternative should be shown only if it would
change those choices.

## 19. Author decision gates

| Gate | Author decides | What remains prohibited before approval |
| --- | --- | --- |
| `G0` Plan | Approve or revise this master plan | Audit execution |
| `G1` Versions | Confirm intended inclusion snapshots after dossiers | Importing or treating a default head as final |
| `G2` Contributions/rights | Confirm candidate roles, independence, and reuse status | Public reuse and final chapter eligibility |
| `G3` Architecture | Approve chapter structure and source-to-chapter map | Updating the plan as if final; scientific drafting |
| `G4` Drafting unit | Authorize one named section/chapter and its sources | Any substantive dissertation drafting |

Administrative or committee confirmation can remain pending where appropriate,
but it must be visible and must block the affected use.

## 20. Definition of done for the research audit

The audit is complete only when:

- all seed sources and justified related sources have immutable audit snapshots
  and documented authority status;
- every plausible manuscript version has a disposition, with deep inspection
  limited by the triage protocol;
- every project has a complete or explicitly limited dossier;
- central scientific, theoretical, empirical, novelty, and contribution claims
  have locators and evidence levels;
- every dissertation-facing figure and table has provenance or an explicit gap;
- exDQLM/exAL antecedents and package-version relationships are reconciled;
- Q-DESN variants and RQR/MTI overlap are addressed without double counting;
- contradictions are resolved or assigned an owner, blocking scope, and next
  decision;
- private/public boundaries, contribution status, and reuse status are explicit;
- the public manifest, claim ledger, narrative audit, and chapter map agree;
- automated validation and a manual public-data review pass;
- original research trees pass their before/after source guards;
- the author has made the version, contribution/rights, and architecture
  decisions; and
- no chapter prose has been drafted without a subsequent `G4` authorization.

“All files were read” is not a completion criterion. Traceability of all
material decisions and claims is.

## 21. Exact next actions if this plan is approved

Execution status for the actions authorized after preparation of this document:

1. Completed: verified the thesis execution context and applicable instructions.
2. Completed: reviewed the plan, setup records, local manifest, and Git state.
3. Completed: recorded approval and preserved the superseded historical plan.
4. Completed: created a focused local setup/planning checkpoint; no push.
5. Completed: implemented separate public/private research manifests, a claim
   ledger, validation-run records, and one audit validator.
6. Completed: re-verified remote heads, source guards, and storage constraints.
7. Completed: created eight isolated full Git clones and fixed audit snapshots.
8. Completed: produced version dossiers and explicit author inclusion gates.
9. Completed through the audit handoff: Phases 3–5 and 8 produced the evidence
   audit and chapter recommendation. Phases 6–7 reached their intended author
   decision gates; G1–G3 remain open because version selection, contribution,
   rights, and architecture approval cannot be inferred. G4 remains closed.

## 22. Plan acceptance record

- Decision: approved for full research-audit execution.
- Date: 2026-09-15.
- Authorization evidence: the author instructed the agent to implement the
  plan from start to finish.
- Amendments: none at authorization time.
- Repository scope: the five nominated seed repositories plus the bounded,
  claim-driven related sources defined here.
- Compute/private-source constraints: retain the plan's proportional-compute
  and public/private boundaries.
- Local checkpoint commits: authorized as normal execution steps; no push,
  merge, publication, or Overleaf synchronization authorized.
- Next authorized phase: Phases 0–8. Gates G1–G3 must record evidence and may
  remain pending where an exact version, contribution, rights, or architecture
  judgment requires the author or committee. Gate G4 drafting is not
  authorized.

## 23. Execution outcome

The evidence-producing portion of this plan is complete. The authoritative
outputs are `research-audit.md`, `chapter-plan.md`,
`research-audit-validation.md`, `research-decisions.md`,
`claim-evidence.json`, the public research manifest, and the ignored local
execution record. The audit found fixed source
snapshots, bounded validation evidence, a defensible three-research-chapter
architecture, and a prioritized repair register. It imported no research
material and altered no original source tree.

The definition of done cannot legitimately close G1–G3 without the author's
scientific and rights decisions. Those items are therefore explicit pending
decisions, not missing audit work. A separate G4 authorization is still needed
before any dissertation chapter or section is drafted.
