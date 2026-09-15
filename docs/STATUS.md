# Project status

As of 2026-09-15: the muscat research-source audit is complete and has been
revised around the author's four-project direction. The audited repositories
now supply the working manuscript snapshots, collaborator lists, project-level
contribution descriptions, methods, and section-level source packets. No
substantive dissertation research prose or source asset has been imported.

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
  project chapters and added a source-first adaptation strategy.
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

## Validation boundary

Bounded isolated checks reached `E3` for document builds, manifests, source
contracts, and focused tests. No full simulation campaign, selected-model
refit, raw-data reconstruction, or complete replication batch was run; nothing
is classified `E4`. See `research-audit-validation.md` for exact outcomes and
environment workarounds.

## Decision gates

- `G0` plan authorization: complete.
- `G1` working inclusion snapshots: sufficient for drafting preparation; final
  submission freezes remain replaceable.
- `G2` identity and project-level contributions: resolved; granular roles and
  direct-reuse rights remain open.
- `G3` four-project architecture: author-directed; committee counting review
  for exdqlm remains open.
- `G4` section/chapter drafting: closed until separately authorized.

## Next task

The author should now make only the focused confirmations in
`research-decisions.md`: correct any working snapshot, confirm the short
candidate-versus-collaborator role allocations, identify any assets already
cleared for direct reuse, and obtain committee confirmation for counting
exdqlm as a research chapter. Then authorize one unit at a time. The
Environmetrics problem and source/horizon design is the recommended first unit;
it will become Chapter 3 in the final reading order.

Administrative fields remain unresolved: ORCID, official title/date, committee
roles and applicability, dean/signature/checklist wording, defense and Fall
2026 deadlines, and the applicable AI-use rule. The official long name is Jose
Antonio Aguirre Perez de Leon; the scholarly name is Antonio de Leon.

Future entries should state date, source commits, decisions, changed files,
checks actually performed, evidence still missing, and next concrete action.
