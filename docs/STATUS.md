# Project status

As of 2026-09-16: the muscat research-source audit and manuscript-first
structural conversion are complete. The conversion was merged into GitHub
`main` at `5def110d009545551e89b7efc9746c61122e8918`; the author reports that
the GitHub-to-Overleaf handoff worked. No Overleaf build log or artifact has
been independently inspected. Material-specific reuse permission remains
unverified and is not implied by that distribution event. The read-only
scholarly audit and the scientific/editorial revision of Chapters 2--5 are
complete. Chapter-sized changes are merged through Chapter 5 at
`5d08241`; the global typography and prose pass is complete locally and is the
current review unit. Dissertation-level framing is next.

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
- The conversion intentionally retains article-style prose, repeated background,
  and some “paper” signposting. These are Phase-2 editorial issues, not reasons
  to reconstruct the chapters from scratch.
- The introduction, dissertation-wide synthesis, abstract, final title,
  committee fields, and administrative dates remain placeholders.

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
- `G5` scientific/editorial integration: research-chapter revision and the
  cross-chapter prose/typography review are complete; dissertation-level
  framing remains. Shared background must be synthesized in the introduction,
  synthesis, and abstract without weakening source qualifications.
- `G6` reuse and submission clearance: open. Confirm granular roles, reuse
  permissions, committee counting, and administrative metadata before final
  circulation or submission. The existing synchronization is not rights
  clearance.

## Next task

Write the dissertation introduction, synthesis, and abstract from the stable
research chapters. Keep contribution language collective while granular roles
remain unresolved, and preserve the conservative TCSP and theory-only MTI-
extension boundaries. Then perform the release-tier build and systematic
frontmatter/chapter-opening/ending inspection. Major reviewed units use the
explicit GitHub/Overleaf handoff in `WORKFLOW.md`.

Granular candidate/coauthor roles, committee confirmation for counting exdqlm,
and final publication permissions remain open. Working text must use accurate
collective attribution until those roles are confirmed.

Administrative fields remain unresolved: ORCID, official title/date, committee
roles and applicability, dean/signature/checklist wording, defense and Fall
2026 deadlines, and the applicable AI-use rule. The official long name is Jose
Antonio Aguirre Perez de Leon; the scholarly name is Antonio de Leon.

Future entries should state date, source commits, decisions, changed files,
checks actually performed, evidence still missing, and next concrete action.
