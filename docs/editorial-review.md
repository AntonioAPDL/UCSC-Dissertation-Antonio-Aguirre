# Dissertation scientific and editorial integration

This is the controlling record for the post-import dissertation review. It
connects the immutable source audit, editable manuscript derivatives, chapter
revision issues, display decisions, bibliography normalization, and validation
evidence. It does not replace the historical source audit or the institutional
requirements report.

## Current scope and evidence boundary

- Repository: UCSC dissertation checkout on muscat.
- Structural baseline: integration commit `79dbb9cc8348d9cc0ece2f23d5ade33570275055`,
  merged to `main` by `5def110d009545551e89b7efc9746c61122e8918`.
- Sources: the eight fixed commits in `../source-manifest.json`; all 102 imported
  records were rechecked against retained exact-commit audit clones on
  2026-09-16.
- Distribution: conversion present on GitHub `main`; Overleaf handoff reported
  successful by the author but not independently verified from an Overleaf log
  or artifact.
- Rights: material-specific reuse remains unverified. Distribution is not
  treated as permission.
- Computation: no research simulations, refits, or data reconstruction are part
  of this editorial review.

## Phase 0 diagnosis and repair

The imported chapters were technically self-contained, but the workflow was
not safe for post-import editing. Three defects were resolved before prose
revision:

1. **Lifecycle drift.** Current documentation still said that the conversion
   was local and unsynchronized. Lifecycle records now distinguish local
   presence, Git history, GitHub synchronization, author-reported Overleaf
   handoff, and reuse permission.
2. **Obsolete audit validation.** The audit validator required one historical
   status string. It now checks allowed states and cross-state invariants; unit
   tests cover invalid conversion, review, GitHub, and Overleaf combinations.
3. **Unsafe import provenance.** Import manifests treated the current chapter
   bytes as the baseline and the importer could overwrite them. Schema 2 keeps
   immutable source/destination baseline hashes while
   `revision-ledger.json` records editable derivatives. The importer is
   check-only by default; explicit regeneration is restricted to a clean
   `regenerate/*` branch whose destinations still match the baseline.

## Validation tiers

Use `scripts/validate.sh` with Python 3.11:

- **Fast:** `bash scripts/validate.sh --tier fast [--audit-root PATH]`. Runs
  lifecycle tests, audit and import validation, optional immutable-blob checks,
  and `git diff --check`. Use during controlled edits.
- **Chapter milestone:** `bash scripts/validate.sh --tier chapter --audit-root
  PATH`. Adds the complete thesis build and blocking-log/PDF checks. Use after
  each chapter-sized unit.
- **Release:** `bash scripts/validate.sh --tier release --audit-root PATH`.
  Requires source-blob verification and builds into a new timestamped directory
  under `build/`, preserving earlier PDFs. Follow with systematic rendered-page
  inspection and the institutional checks in `VALIDATION.md`.

A PDF SHA identifies one build artifact; it is not evidence of bitwise
reproducibility because ordinary pdfTeX creation metadata changes.

## Phase sequence

1. Phase 0: lifecycle and edit-safe provenance — complete.
2. Phase 1: read-only scholarly audit and revision ledger — in progress.
3. Phase 2: global architecture, notation, bibliography, and display decisions.
4. Phase 3: chapter revisions in order 2, 3, 4, 5.
5. Phase 4: cross-chapter prose and typography review.
6. Phase 5: dissertation introduction, synthesis, and abstract.
7. Final release validation and explicit GitHub/Overleaf handoff.

Substantive chapter work must record a `REV-*` entry in
`revision-ledger.json`, update the corresponding current hash, pass the relevant
validation tier, and preserve the source-to-baseline mapping.

## Decision boundaries

Editorial work may proceed with collective or chapter-centered attribution.
The following facts may not be inferred:

- individual conceptual, theoretical, computational, empirical, or writing
  allocations among the candidate and coauthors;
- committee acceptance of the software chapter as an independent research
  unit;
- final publisher/coauthor reuse permission;
- a stronger TCSP guarantee than the source evidence proves;
- implementation or empirical validation of MTI extensions absent from their
  audited source;
- final administrative title, date, committee roles, dean wording, or AI-use
  disclosure requirement.

The detailed Phase 1 issue, display, notation, and bibliography records are
maintained below as the audit proceeds.
