# Project status

As of 2026-09-15: the muscat research-source audit and evidence-backed chapter
recommendation are complete. The work is ready for the author's scientific,
contribution, rights, and architecture decisions. No dissertation research
content has been drafted or imported.

## Completed

- Established and validated the muscat thesis checkout; the 20-page starter
  builds cleanly apart from its documented legacy-class caption warning.
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
- Verified all original research checkouts retained their original branch,
  HEAD, and clean state. Exact paths and guards remain in ignored local records.

## Recommendation

Use three research chapters:

1. Environmetrics hydrologic correction and predictive synthesis;
2. QDESN single/multi-quantile methodology with GloFAS and PriceFM evidence;
3. one combined RQR/MTI chapter covering the interval foundation, TCSP, and
   regression/dynamic extensions.

Treat the exdqlm article/package as shared computational infrastructure and a
possible software/reproducibility appendix by default. A separate software
chapter or MTI-extensions chapter requires the additional evidence and
committee decisions in `chapter-plan.md`.

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
- Candidate-specific contribution records, exact inclusion versions, and
  material-specific reuse rights remain unconfirmed.

## Validation boundary

Bounded isolated checks reached `E3` for document builds, manifests, source
contracts, and focused tests. No full simulation campaign, selected-model
refit, raw-data reconstruction, or complete replication batch was run; nothing
is classified `E4`. See `research-audit-validation.md` for exact outcomes and
environment workarounds.

## Decision gates

- `G0` plan authorization: complete.
- `G1` exact inclusion snapshots: open.
- `G2` candidate contribution and reuse rights: open.
- `G3` chapter architecture: open.
- `G4` section/chapter drafting: closed until separately authorized.

## Next task

The author should complete `research-decisions.md`: confirm or replace the five
seed commits, confirm QDESN
Search Phase II remains future work, decide whether MTI-EXTENSIONS belongs in
the combined chapter, supply contribution/rights decisions, and approve or
modify the three-unit architecture. After those decisions, authorize one unit
at a time; the Chapter 2 problem/data-source design is the recommended first
unit.

Administrative fields remain unresolved: official title/name/date, committee
roles and applicability, dean/signature/checklist wording, defense and Fall
2026 deadlines, and the applicable AI-use rule.

Future entries should state date, source commits, decisions, changed files,
checks actually performed, evidence still missing, and next concrete action.
