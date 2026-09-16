# Project status

As of 2026-09-15: the muscat research-source audit and the approved local
manuscript-first structural conversion are complete. All four research chapter
bodies now compile from tracked dissertation files. Main-article prose was
preserved as the initial baseline, unique supporting material was integrated
by topic, and selected final display assets were copied with exact provenance.
No code, data, computation, push, publication, or Overleaf synchronization was
performed.

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
  fragments; every record remains `UNVERIFIED_LOCAL_ONLY`.
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
- Several dense imported tables and long QDESN derivations use provisional
  compact sizing to fit the dissertation page. They compile and were sampled
  visually, but should be reviewed for final reading size and possible splitting.
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
- `G4` manuscript conversion: complete locally under the seven approved
  defaults; no remote synchronization performed.
- `G5` scientific/editorial integration: open. Review one converted chapter at
  a time, then deduplicate shared background and write the introduction and
  synthesis without weakening source qualifications.
- `G6` reuse and submission clearance: open. Confirm granular roles, reuse
  permissions, committee counting, and administrative metadata before push,
  Overleaf synchronization, circulation, or submission.

## Next task

Review the structural chapters in this order: exdqlm, Environmetrics, QDESN,
then combined RQR/MTI. For each chapter, confirm that the source selection and
supporting-material placement are scientifically complete before substantive
editing. Then perform the cross-chapter deduplication and transition pass,
write the introduction and synthesis, and resolve the G6 decisions. Nothing
should be pushed or synchronized until direct-reuse status is reviewed.

Granular candidate/coauthor roles, committee confirmation for counting exdqlm,
and final publication permissions may remain open during the local structural
conversion, provided the working text uses accurate collective attribution and
the imported material is not externally synchronized.

Administrative fields remain unresolved: ORCID, official title/date, committee
roles and applicability, dean/signature/checklist wording, defense and Fall
2026 deadlines, and the applicable AI-use rule. The official long name is Jose
Antonio Aguirre Perez de Leon; the scholarly name is Antonio de Leon.

Future entries should state date, source commits, decisions, changed files,
checks actually performed, evidence still missing, and next concrete action.
