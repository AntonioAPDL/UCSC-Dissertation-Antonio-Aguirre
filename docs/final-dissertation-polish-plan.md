# Final dissertation polish plan

Status: IMPLEMENTATION AUTHORIZED; manuscript edits have not begun  
Prepared: 2026-10-28  
Working branch: `editorial/final-dissertation-polish-20261028`  
Baseline: `main` and `origin/main` at
`6541686e44891982dbc4591ed11558d2f87ccc9a`

## 1. Purpose and controlling constraints

This plan governs the final reader-facing polish requested after the research
refresh, reader-first restructuring, and essential-appendix revision. The aim
is not another scientific rewrite. It is a bounded editorial pass that removes
remaining article-to-dissertation seams, reduces repetition, improves
statistical phrasing, confirms figure descriptions, and leaves a reproducible
release record.

The following content is protected unless a concrete validation failure
requires reconsideration:

- the four-project architecture and the shared introduction and synthesis;
- inferential targets, likelihoods and generalized updates, priors, equations,
  propositions, proofs, algorithms, numerical results, qualifiers, and
  attribution;
- active figures, tables, citations, cross-references, source identities, and
  provenance records;
- the 52-page essential appendix sequence and its body-to-appendix bridges;
- the distinction between empirical evidence, repeated-sampling calibration,
  posterior statements, theoretical results, and proposed extensions;
- the scholarly name `Antonio de Leon` and the official long name
  `Jose Antonio Aguirre Perez de Leon` in their documented roles.

This pass will not recompute research results, alter a research repository,
import code or data, revive deactivated supplemental material, resolve
committee or other administrative placeholders, claim accessibility
conformance, synchronize Overleaf directly, or broaden a scientific claim.

## 2. Audited baseline

The audit covered `AGENTS.md`, the active front matter, Chapters 1--6,
Appendices A--E, active display fragments, the bibliography and build
configuration, the current provenance and editorial ledgers, prior reader and
appendix plans, and both applicable academic-writing profiles. The accepted
release is:

- `build/release-20261028T064248Z/main.pdf`;
- SHA-256
  `19ffa613857ba95d95e905e6c7782abb0d35321f434ee449ee8f94cf9ff14e1f`;
- 261 US-Letter pages, PDF 1.7, unencrypted and untagged;
- Appendices A--E on numbered pages 175--226, followed by the bibliography;
- TeX Live 2018, pdfTeX 1.40.19, on `muscat.be.ucsc.edu`.

The fast validation baseline passes all 18 checks. Its inventories report 8
sources and 30 evidence records, 29 historical editorial issues, 102 display
records, 4 chapter manifests, 96 section dispositions, 102 imports, 115
imported TeX records, 116 citations, 257 labels, 6 migration records, and 30
active visuals. This pass must not reduce those scientific and provenance
guarantees accidentally.

## 3. Diagnosis and exact intervention

### 3.1 Dissertation structure and repetition

Chapters 2--5 each begin with a section titled `Chapter overview` and then
repeat the same problem, method, and principal results in their substantive
opening sections. These embedded article-style abstracts interrupt the
dissertation sequence and add four unnecessary entries to the table of
contents. They will be removed. Any unique technical inputs currently placed
in an overview will remain in the chapter preamble; in Chapter 4, the two
current-source input files will move before `Introduction`.

Two additional bridge sections repeat material immediately around them:

- Chapter 2, `Inference, diagnostics, and predictive use`, repeats the
  inference and assessment sections and principally points to Appendix B.
  Its useful appendix pointer will be retained at the end of the preceding
  section, and the redundant heading and repeated prose will be removed.
- Chapter 3, `Computational implementation`, repeats the MCMC/VB subsection
  and its Appendix C pointer. The section will be removed because the exact
  computational qualification is already present in the inference subsection.

No chapter, appendix, figure, table, or scientific subsection will otherwise
be moved in this pass.

### 3.2 Statistical prose and exposition

Edits will be local and meaning-preserving:

- replace generic `framework`, `system`, or `workflow` only where a more exact
  statistical noun such as model, procedure, analysis, package, or sequence is
  available; retain legitimate state-space, software-workflow, neural-network,
  reservoir, and forecast-system terminology;
- remove tutorial remnants in Chapter 2 that describe unshown commands or a
  `print()` call, while retaining the reproducible model specification and
  direct interpretation of every result;
- replace internal chronology (`we begin`, `initially, we explored`) with the
  statistical object or operation when the chronology has no inferential role;
- display and introduce the exAL stochastic representation in Chapter 3 rather
  than leaving the full distributional definition in one dense paragraph;
- correct the Chapter 3 roadmap order and isolated imprecise phrases in the
  introduction and synthesis;
- preserve first-person language where it states a genuine modeling or
  evaluative choice and preserve established terminology where replacement
  would reduce precision.

The abstract will receive only line-level copyediting unless a manuscript edit
makes one of its claims inaccurate. Appendices A--E already have the required
technical orientation and will not be subjected to stylistic churn.

### 3.3 Displays, references, and accessibility records

All active captions and display references will be checked after pagination
changes. Four active visuals currently carry `AUTHOR_REVIEW_REQUIRED` in the
accessibility ledger: the Chapter 4 multiquantile forecast display and the
three primary Chapter 5 validation/application displays. Each will be rendered
or opened and compared with its caption, source, macros, and surrounding
interpretation. The ledger description will be corrected and marked
`REVIEWED` only when visual evidence supports it. Inactive historical records
will remain unchanged. Because the current TeX toolchain produces an untagged
PDF and `\figalt` is not embedded as tagged-PDF alternate text, the ledger
will be described as a source-level accessibility record, not a conformance
claim.

### 3.4 Lifecycle documentation

`docs/STATUS.md`, `docs/VALIDATION.md`, `docs/ASSISTANCE-LOG.md`, the source
manifest, and the revision ledger will be updated with the final commit and
release evidence. Stale statements saying that the completed appendix revision
has not been implemented or pushed will be corrected. Administrative and
reuse-permission items will remain open. GitHub synchronization and Overleaf
synchronization will remain distinct: this task may push the verified main
branch, but a later Overleaf pull is a separate user action.

## 4. Implementation phases and gates

### Phase 0 -- freeze the plan

Commit this plan alone. Gate: clean diff, correct baseline commit, and no TeX
or ledger change in the plan commit.

### Phase 1 -- structural deduplication

Remove the four overview sections and the two redundant bridge sections,
preserving unique inputs and appendix references. Run fast validation and
build a diagnostic PDF. Gate: no missing input, citation, reference, label, or
active display; all four research chapters retain their attribution notices,
introductions, contribution statements, evidence, limitations, and summaries.

### Phase 2 -- line-level scholarly polish

Apply the bounded prose changes in Section 3.2 and confirm the abstract and
synthesis against the resulting chapters. Review the four active visuals and
update only evidence-supported accessibility records. Run fast validation and
a second diagnostic build. Gate: no changed number, equation, inferential
target, conclusion, attribution, citation set, or figure/table content without
a documented scientific reason; any such unexpected change stops the pass.

### Phase 3 -- full release audit

Run the release validation tier against the recorded audit source root, create
a new timestamped release directory, and retain its logs, PDF metadata, hashes,
and validator output. Inspect the title/front matter, the opening and closing
pages of every chapter, all changed pages, chapter-to-appendix transitions,
appendix-to-bibliography transition, floats near changed text, and a systematic
sample through the remainder. Gate: no clipped or overlapping text, blank
content pages, float-only anomaly caused by the edits, unresolved reference or
citation, duplicate label, missing glyph, or unexplained material warning.

### Phase 4 -- durable handoff and synchronization

Update the lifecycle documents and ledgers from the actual release evidence,
review the complete diff, and commit coherent editorial and documentation
units. Fast-forward `main` only after the branch is clean and all gates pass.
Push `main`, then verify that local `main`, `origin/main`, and
`git ls-remote origin refs/heads/main` resolve to the same commit. Do not force
push. If the remote has advanced, stop before integration and inspect the
divergence rather than overwriting it. Overleaf is ready to pull only after
this remote equality check; this task does not perform the Overleaf pull.

## 5. Reproducibility, rollback, and stop conditions

Every substantive phase is committed separately so it can be inspected or
reverted without disturbing earlier work. Generated release output remains in
ignored `build/` directories; durable evidence is recorded in tracked
documentation and JSON ledgers. No existing useful release PDF is deleted.

Implementation stops before merge or push if any of the following occurs:

- a source/result conflict cannot be resolved from the recorded evidence;
- a protected scientific statement would need to change rather than be
  restated;
- an active source, figure, table, citation, label, or appendix bridge becomes
  orphaned;
- release validation or visual inspection produces a material unexplained
  failure;
- the main branch or its remote advances unexpectedly; or
- a requested action would expose private paths, credentials, or unapproved
  source material.

## 6. Definition of done

The polish is complete only when the repeated overview and bridge material is
removed without loss, the remaining prose reads as a self-contained
statistics dissertation, scientific and provenance boundaries are unchanged,
all active visuals and references remain coherent, fast and release validation
pass, the new PDF is inspected and recorded, lifecycle documentation describes
the actual state, and the verified main-branch commit is available on GitHub
for a deliberate Overleaf pull.
