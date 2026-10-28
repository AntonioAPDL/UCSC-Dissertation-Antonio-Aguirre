# Project status

## 2026-10-28 final comprehensive polish release validated

The final reader-facing polish is implemented on
`editorial/final-dissertation-polish-20261028` from the verified `main` and
`origin/main` baseline
`6541686e44891982dbc4591ed11558d2f87ccc9a`. The controlling audit and exact
intervention are in `final-dissertation-polish-plan.md`. The plan,
deduplication, and bounded prose/ledger commits are `9c63586`, `00915a4`, and
`4b63ff9`, respectively.

The revision removes the four repeated research-chapter overview sections and
two redundant computational bridge sections, preserves the unique inputs,
historical labels, and appendix links they contained, and replaces remaining
tutorial or generic implementation phrasing with exact statistical
exposition. The Chapter 3 exAL stochastic representation is now displayed and
readable. Four active source-level figure descriptions were checked against
the rendered displays. No scientific result, equation, theorem, table or
figure value, evaluation design, citation set, attribution, or source snapshot
changed. Appendices A--E remain 52 numbered pages.

The clean release gate passed 18 tests, rechecked all 102 immutable imported
Git blobs, resolved all 116 cited keys, and covered 43 active TeX files, 257
active labels, six migration records, and 30 active visual records. The
accepted ignored artifact is
`build/release-20261028T190946Z/main.pdf`: 254 US-Letter pages, 16,491,650
bytes, SHA-256
`28898586b38c3db7ccc4c16d88fd846bdb0578aef0f3fe0fa9bb5d679e1300e7`.
It has zero overfull boxes or blocking diagnostics, 25 underfull-box notices,
32 embedded font rows, and no Type 3 font. Twenty-one representative release
pages passed rendered inspection. The PDF remains untagged.

The official title, committee/dean/date fields, acknowledgments, ORCID,
granular candidate/coauthor roles, material-specific reuse permission, and a
modern tagged-PDF accessibility check remain open. The release-validated
feature branch is ready for the authorized GitHub handoff. An Overleaf pull,
compile, and rendered review remain a separate user action.

## 2026-10-28 essential-appendix revision complete

The advisor-directed appendix revision is implemented on
`editorial/essential-appendices-20261028` from the accepted thesis baseline
`37b9da0fdb16168dff07efdc9454886f8467f6cd`. The controlling specification is
`essential-appendix-revision-plan.md`; the unit-level decisions and recovery
paths are in `appendix-essentiality-map.json`. All 340 mapped units are marked
`IMPLEMENTED`: 104 were retained, 161 condensed, 16 summarized, and 59
deactivated from the compiled graph. Historical migration, display, import,
accessibility, and source records remain intact.

The five chapter-linked appendices remain in place, but now occupy 52 numbered
pages (175--226) instead of 204. Appendix A uses four pages, Appendix B six,
Appendix C three, Appendix D 21, and Appendix E 18. The complete dissertation
is 261 pages rather than 414. Appendix D retains exactly eight claim-bearing
supporting displays; Appendix E retains exactly five. Complete result decks,
repeated standard algebra, software-maintainer inventory, and development
diagnostics no longer interrupt the compiled dissertation, while their source
history and recovery locations remain recorded.

The body-to-appendix links now point to topical sections. The three principal
Chapter 5 results retain authoritative statements in the chapter and proof-only
destinations in Appendix E; four supporting formal results retain complete
statements and proofs. The direct Dirichlet-process content result is stated as
the exact Beta law with its interpretation. No inferential target, likelihood
interpretation, theorem scope, numerical result, attribution, or evidence
strength was changed. Proposed MTI regression and dynamic extensions remain
explicitly theoretical and unvalidated.

The full release gate passed with 18 unit tests, all 102 immutable imported
source blobs rechecked, 43 active TeX files, 257 unique active labels, six
migration records, 30 active visual records, and all 116 cited keys resolved.
The accepted ignored release is a 261-page US-Letter PDF with zero overfull
boxes or blocking citation/reference diagnostics. All 32 reported font rows
are embedded and no Type 3 font occurs. Systematic rendered inspection covered
appendix openings, retained tables and figures, the Appendix E ending, and the
bibliography transition. Exact artifact details are in `VALIDATION.md`.

No research computation was rerun and no research repository was modified.
At the end of this historical appendix-only stage, push, merge, GitHub
synchronization, and Overleaf synchronization had not yet been performed; the
newer lifecycle state is recorded above.

## 2026-10-27 final reader and statistical revision

The advisor-directed final reader revision is implemented on branch
`editorial/final-reader-statistical-revision-20261027` from clean baseline
`f82c7bce192d51dbc686070533647780cacbd5dc`.  The controlling plan and exact
implementation record are `final-reader-statistical-revision-plan.md` and
`final-reader-statistical-revision-implementation.md`.

The six-chapter architecture and four research projects are retained.  Chapter
2 now emphasizes statistical computation and software rather than an API
manual; Chapter 3 discloses the globally specified retrospective design;
Chapter 4 discloses its development-informed simulation selection and the
dependence among origin--horizon pairs; Chapter 5 has one narrative and one
discussion, with detailed regression/dynamic derivations represented once in
Appendix E; and Chapter 6 compares evaluation maturity across projects.  The
duplicate MTI sign error and malformed appendix references are corrected.

Appendix displays remain active and locally referenced but no longer dominate
the global lists of figures and tables.  The final release gate passed on a
414-page US-Letter PDF; the abstract begins on Roman page xxii rather than
xxxviii in the accepted 2026-10-26 artifact.  The release rechecked all 102
immutable source blobs, has no blocking diagnostics or overfull boxes, embeds
all 52 reported font rows with no Type 3 font, and passed targeted rendered-page
inspection.  The accepted ignored artifact and exact hash are recorded in
`VALIDATION.md`.  No research computation was rerun and no source repository
was changed.  The revision was merged and pushed to GitHub `main` through
`bb9d346061c598f802a4827683499892083e306a`, and the remote branch tip was
verified.  A deliberate Overleaf pull, compile, and rendered review remain a
separate handoff.

## 2026-10-26 current-research refresh

The current remote default branches were compared with the dissertation's
prior working sources in isolated audit clones. Q--DESN advanced from
`757522d` to `483e6ed`, RQR-GIBBS from `73887b9` to `4223c6a`, and the
`exdqlm` article from `d5534e9` to `98cec59`. Environmetrics,
MTI-EXTENSIONS, the `exdqlm` package, the San Lorenzo reproducibility source,
and the corrections repository are unchanged.

The manuscript-only refresh is implemented on
`refresh/current-research-20261026`. Chapter 4 now uses the current Q--DESN
article, including the 300-target primary evaluation, 500-target sensitivity,
MQ--DESN crossing/score distinction, Search III GloFAS evidence, and the
114-case PriceFM comparison. Chapter 5 now uses the calibrated profiled MTI
procedure and its independent validation instead of the older TCSP framing;
the unchanged regression/dynamic extension remains explicitly proposed.
Chapter 2 now reflects the `exdqlm` 1.1.2 rerun and its nine current figures.
The current main texts remain reader-facing chapter spines, while detailed
derivations, proofs, algorithms, and supporting diagnostics remain in the
linked appendices.

The projection is hash guarded and recorded in
`current-source-refresh-audit.md` and `source-refresh-20261026.json`. It
imports only manuscript prose and active display dependencies; research code,
data, fitted objects, caches, simulations, histories, and full output archives
remain external. Original research working trees were not modified. Public
source and claim records have been reconciled. The full release gate and
rendered inspection passed on a 439-page US-Letter PDF with SHA-256
`92e4c36c451ecfceca2e0674e7d904f40f9b63e863f5799ba4b310dc262391d1`;
the final log has zero overfull boxes or blocking diagnostics, and all fonts are
embedded with no Type 3 font. The refresh was merged into `main` through
`98acf4758b65f37b7676cbbcba78d05abde4f6ff`; GitHub remote verification and
the deliberate Overleaf pull remain separate handoffs. Material-specific reuse
permission and granular coauthor-role confirmation remain open.

## 2026-10-08 reader-first restructuring implementation

The author approved all sixteen defaults and the fixed eight-source evidence
set in `reader-first-restructure-plan.md`. The reader-first restructuring is
implemented, release-validated, and merged into GitHub `main` through merge
commit `a3ad55e587bfbbd8e5075fb9829fdb1a714421fe`. The work began from
`c93d7b3ed9c228811b6b79f13a90b312319b9cf3`; the focused branch remains on the
remote as a recoverable review record.

The approved planning baseline is `c93d7b3ed9c228811b6b79f13a90b312319b9cf3`;
the scientific-content baseline
remains 0c394122549e903b19edc8014709a6f4318bee26. The accepted before-state
artifact remains the recorded 344-page release with SHA-256
30b4e0bb3c3230544e941f7eae82dcabb44f08e9283ae9809aaade45196c9900.

The six-chapter reading sequence is retained. Fourteen mapped technical units
have been moved from Chapters 2--5 into one compatibility-reviewed concordance
appendix and four project appendices. Body bridges retain the target, central
model, principal evidence, interpretation, negative findings, and limitations.
The move is mechanical and manuscript-first; no research computation or source
repository was changed.

The clean release build succeeds at 361 US Letter pages: the reading body ends
at numbered page 203, Appendices A--E occupy numbered pages 204--322, and the
bibliography remains last on numbered pages 323--333. Hybrid
static/compiler-recorded validation covers macro-expanded inputs, 421 active
labels, all 14 migration records, and all 33 active visual descriptions. The
release gate rechecked all 102 immutable source blobs, and the targeted
chapter/appendix/bibliography boundary render review passed. The exact artifact
and checks are recorded in `VALIDATION.md` and
`reader-first-restructure-implementation.md`.

Muscat's TeX Live 2018 PDF remains searchable but untagged. No modern TeX,
veraPDF, Acrobat, or other conformance checker is available on the server, so
WCAG 2.1 AA is not claimed. The complete visual-description ledger is ready for
a modern tagged build and external/manual accessibility review. All source,
rights, attribution, and external-computation controls remain in force. The
remaining immediate handoff is an explicit Overleaf pull and compile; pushing
GitHub does not itself update or verify an Overleaf artifact.

As of 2026-09-16: the muscat research-source audit and manuscript-first
structural conversion are complete. The conversion was merged into GitHub
`main` at `5def110d009545551e89b7efc9746c61122e8918`; the author reports that
the GitHub-to-Overleaf handoff worked. No Overleaf build log or artifact has
been independently inspected. Material-specific reuse permission remains
unverified and is not implied by that distribution event. The read-only
scholarly audit and the scientific/editorial revision of Chapters 2--5 are
complete and merged through the global prose/typography pass at `2310613`.
The substantive dissertation introduction, synthesis, and 319-word abstract
are complete. The clean release-tier build, independent PDF audit, and
systematic rendered-page review pass. This audit record is the final GitHub
handoff unit; no Overleaf build or artifact was independently inspected.

## Completed

- Established and validated the muscat thesis checkout; after adding the fourth
  project placeholder, the 22-page starter builds cleanly apart from its
  documented legacy-class caption warning.
- Created local branch `setup/muscat-audit-20260915` and checkpointed the setup
  and audit-plan state at `cdd06d7`. No push, merge, publication, or Overleaf
  synchronization was performed.
- Executed the approved audit against full Git clones of the five nominated
  sources and three claim-driven dependencies. Fixed commits, document IDs,
  inventory metrics, validation runs, and inclusion/rights states are in
  `../source-manifest.json`.
- Produced `research-audit.md`, `research-audit-validation.md`,
  `claim-evidence.json`, `chapter-plan.md`, and the pending-decision record
  `research-decisions.md`; normalized the ignored local manifest and added a
  safe exact-commit clone helper plus audit validator.
- Reconciled the current manuscript author lists and contribution paragraphs.
  Recorded the author-supplied official name, scholarly name, and cross-source
  identity mapping; converted the chapter plan from three units to four
  project chapters.
- Added `manuscript-integration-plan.md`: a manuscript-first conversion design
  that preserves each article as the chapter baseline, integrates unique
  supplement material into the corresponding body sections, imports only
  selected final display assets, and keeps code/data/computation external.
- Recorded the author's approval of all seven conversion defaults and created
  local branch `integration/manuscript-first-20260915`.
- Added `scripts/import_manuscripts.py`, which reads exact Git blobs at the five
  approved audit commits, generates the four chapters, integrates supporting
  sections, copies only recursively referenced final displays, namespaces
  labels/citations, and creates one consolidated bibliography.
- Added four `docs/imports/*.json` records covering nine source manuscripts,
  96 top-level section dispositions, and 102 imported records. The 93 display
  dependencies contain only final PDF/PNG figures and TeX table/alias
  fragments; every material-specific rights record remains `UNVERIFIED`.
- Reconciled the post-handoff lifecycle state. GitHub/Overleaf distribution is
  now recorded separately from reuse rights, and the author's Overleaf report
  is distinguished from an independently inspected build.
- Replaced byte-identity coupling with a two-layer provenance model: immutable
  import-baseline hashes remain in `docs/imports/*.json`, while current editable
  derivatives and revision IDs are tracked in `docs/revision-ledger.json`.
- Made the manuscript importer check-only by default and restricted explicit
  baseline regeneration to a clean `regenerate/*` branch with unchanged
  baseline destinations.
- Repaired lifecycle validation with cross-state invariants and focused tests;
  both audit validators now pass under Python 3.11, including rechecking all
  102 immutable source blobs against the retained audit clones.
- Completed the post-import scholarly audit: 29 prioritized issues, a common
  terminology/notation map, 11 bibliography reconciliation groups, and
  explicit dispositions for all 95 displays are recorded in the connected
  editorial ledgers.
- Completed the global integration decisions: retained the four-project
  architecture, adopted the common terminology boundaries, and implemented
  all 11 bibliography reconciliations.
- Completed the Chapter 2 dissertation revision and all 19 of its display
  dispositions. The chapter milestone build and representative page inspection
  passed.
- Completed the Chapter 3 hydrologic-application revision and all 21 of its
  display dispositions. Predictive-band terminology, the five-origin evidence
  boundary, and the distinct 28-day and common 8-day horizons are explicit.
  The chapter milestone build and representative page inspection passed.
- Completed the Chapter 4 Q--DESN revision and all 36 of its display-ledger
  records. The chapter now places Q--DESN before its Gaussian baseline,
  integrates source support by topic, and retains the simulation, VB--LD,
  GloFAS, and PriceFM qualifications. The chapter milestone build and
  representative page inspection passed.
- Completed the Chapter 5 RQR/MTI revision and all 21 display decisions. Each
  central theorem/proposition now has one authoritative statement and attached
  proof; empirical-balance, validation, and pharmaceutical evidence is
  integrated by topic. TCSP proof limits, generalized-Bayes distinctions, and
  the theory-only status of the regression/dynamic extensions are explicit.
  An inherited opposite-sign midpoint tilt formula was corrected against the
  authoritative root form and score equations.
- Completed the cross-chapter prose and typography pass. Blanket `scriptsize`
  rules were removed from tables and algorithms, 36 Chapter 4 equation groups
  were restored to ordinary display size, and only the dense API table,
  Chapter 3 algorithms, selected wide tables, and one Q--DESN state recursion
  retain locally justified compact sizing. Wide formulas were line-broken.
  The 323-page milestone build has no overfull boxes or oversized floats, and
  targeted rendered-page inspection found no clipping or collisions.
- Replaced the Chapter 1, Chapter 6, and abstract placeholders with a target-
  first common framework, an evidence-bounded comparison of all four projects,
  and a 319-word global abstract. The framing preserves the distinctions among
  conditional quantiles, synthesized response distributions, loss-defined
  endpoints, and tolerance actions; it also retains collective attribution and
  the documented negative or mixed empirical findings.
- Added a compact pre-submission authorship/version/reuse matrix to
  `research-decisions.md`. Granular individual roles, exact publication status,
  coauthor/publisher permissions, and committee acceptance of the software
  chapter remain explicit confirmations rather than inferred facts.
- Corrected the only Type 3 font found in the assembled dissertation. The
  immutable PriceFM source figure remains preserved; the thesis uses a recorded
  vector-outline derivative with identical plotted content. The full PDF font
  audit now finds no Type 3 or Type 0 fonts.
- Completed the final release audit from an empty timestamped output directory.
  The exact 344-page PDF has no unresolved citation/reference, duplicate-label,
  missing-file, overfull-box, Type 3/Type 0, unembedded-font, page-size, text-
  envelope, or footer-placement failure. Front matter, every chapter boundary,
  and both bibliography endpoints were rasterized and inspected.
- Removed a stranded final DOI-only bibliography page by changing only the
  inter-entry separation from 12 pt to 11.5 pt. Entries remain single spaced
  with visible near-baseline separation; no reference content changed.
- Added `scripts/validate_manuscript_imports.py`. Against the retained audit
  clones it rechecked all 102 source-blob hashes and passed manifest, destination
  hash, dependency, label, citation, file-type, rights-boundary, absolute-path,
  and secret scans.
- Removed the starter demonstration appendix from the document body; imported
  proofs, algorithms, derivations, validation details, tables, and figures now
  exercise the substantive thesis layout.
- Built the converted dissertation to a 367-page US Letter PDF with all 35
  fonts embedded. The final log has no undefined citations/references,
  duplicate labels, changed-label notices, oversized floats, overfull boxes,
  pdfTeX warnings, or missing files. Exact hash and remaining benign
  line-breaking warnings are recorded in VALIDATION.md.
- Verified all original research checkouts retained their original branch,
  HEAD, and clean state. Exact paths and guards remain in ignored local records.

## Recommendation

Use four project research chapters in final reading order:

1. exdqlm software and computational infrastructure;
2. Environmetrics hydrologic correction and predictive synthesis;
3. QDESN single/multi-quantile methodology with GloFAS and PriceFM evidence;
4. one combined RQR/MTI chapter covering the interval foundation, TCSP, and
   regression/dynamic extensions.

The author has selected this as the working architecture. Committee/advisor
confirmation remains necessary if the software-centered exdqlm chapter is to
count as an independent journal-suitable research unit. The MTI papers remain
combined until the extensions gain independent implementation and evidence.

## Main issues

- RQR's exact scan recursion and a proof matched to the reported closed-window
  TCSP action remain open; narrow the guarantee or complete and verify the
  theorem before drafting that claim.
- The RQR August 13 claim ledger is stale relative to its completed validation.
- QDESN's current corrected-v4, PriceFM, GloFAS, and build checks pass, but a
  historical 14-row joint manifest has 13 mismatches and two Phase 181 scripts
  test superseded manuscript wiring.
- MTI-EXTENSIONS has theory manuscripts but no implementation, numerical
  evidence, tests, provenance manifest, or license at its audited snapshot.
- The exdqlm application/article/package states are 1.1.0, 1.1.1, and 1.1.2;
  the named 1.1.1 article archives are not tracked at the article snapshot.
- Repository evidence now establishes project-level contributions and
  collaborators, but granular candidate/coauthor role allocation and
  material-specific direct-reuse rights remain unconfirmed.
- A final human scholarly read remains necessary. Automated and rendered-page
  review cannot decide whether every transition reflects the candidate's
  intended emphasis or whether all collaborator contribution descriptions are
  complete.
- The final title, committee fields, dean wording, conferral date, ORCID,
  acknowledgments, granular contribution statements, publication status, and
  material-specific reuse permissions remain unresolved. The substantive
  abstract, introduction, and synthesis are no longer placeholders.

## Validation boundary

Bounded isolated checks reached `E3` for source document builds, manifests,
source contracts, and focused tests. The structural conversion validator also
rechecked every imported source blob and destination. The dissertation builds
without access to a sibling research working tree. No full simulation campaign,
selected-model refit, raw-data reconstruction, or complete replication batch
was run; nothing is classified `E4`. See `research-audit-validation.md` and
`VALIDATION.md` for the two distinct validation boundaries.

## Decision gates

- `G0` plan authorization: complete.
- `G1` working inclusion snapshots: sufficient for drafting preparation; final
  submission freezes remain replaceable.
- `G2` identity and project-level contributions: resolved; granular roles and
  direct-reuse rights remain open.
- `G3` four-project architecture: author-directed; committee counting review
  for exdqlm remains open.
- `G4` manuscript conversion: complete, merged into GitHub `main`, and reported
  by the author as synchronized to Overleaf.
- `G5` scientific/editorial integration: complete. Research-chapter revision,
  cross-chapter prose/typography review, dissertation framing, and the release-
  tier technical/visual audit all pass within the stated evidence boundary.
- `G6` reuse and submission clearance: open. Confirm granular roles, reuse
  permissions, committee counting, and administrative metadata before final
  circulation or submission. The existing synchronization is not rights
  clearance.

## Next task

The next restructuring decision is whether to approve the sixteen defaults in
Section 13 of `essential-appendix-revision-plan.md` and identify any appendix
unit that an advisor specifically requires in full. The plan itself does not
authorize scientific or compiler-graph changes. If approved, the first
implementation deliverable is backward-compatible essentiality schema,
validator, and test support with no TeX change, followed by the complete
`appendix-essentiality-map.json`. Appendix C is then the manuscript pilot;
Appendices A and B follow only after its rendered review, and Appendices D and
E remain separate high-risk milestones.

The title/administrative, contribution, committee, reuse, TCSP/MTI, and
publication-status tracks remain open in parallel. Keep collective attribution
until granular roles are confirmed. Any later major reviewed unit must use the
explicit GitHub/Overleaf handoff in WORKFLOW.md and inspect the actual Overleaf
artifact rather than treating synchronization as build parity.

Granular candidate/coauthor roles, committee confirmation for counting exdqlm,
and final publication permissions remain open. Working text must use accurate
collective attribution until those roles are confirmed.

Administrative fields remain unresolved: ORCID, official title/date, committee
roles and applicability, dean/signature/checklist wording, defense and Fall
2026 deadlines, and the applicable AI-use rule. The official long name is Jose
Antonio Aguirre Perez de Leon; the scholarly name is Antonio de Leon.

Future entries should state date, source commits, decisions, changed files,
checks actually performed, evidence still missing, and next concrete action.
