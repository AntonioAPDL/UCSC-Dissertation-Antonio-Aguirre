# Reader-first restructuring implementation record

**Implemented:** 2026-10-08

**Controlling specification:** `reader-first-restructure-plan.md`, version 3

**Planning baseline:** `c93d7b3ed9c228811b6b79f13a90b312319b9cf3`

**Scientific-content baseline:** `0c394122549e903b19edc8014709a6f4318bee26`

**GitHub main merge:** `a3ad55e587bfbbd8e5075fb9829fdb1a714421fe`

## Outcome

The dissertation now has two connected reading layers. Chapters 1--6 form the
continuous argument; Appendices A--E hold the specialist record. The four
research chapters preserve the manuscript-first source material but no longer
require a general reader to pass through every proof, posterior block,
algorithm, and secondary diagnostic before reaching the corresponding result.

This was a structural and editorial conversion, not a scientific rewrite.
No source snapshot, numerical result, research repository, code, data, fitted
object, or external computation was changed. Material-specific reuse rights,
granular candidate/coauthor roles, publication status, committee acceptance,
and administrative metadata were not inferred.

## Realized architecture

| Reading unit | Body contract | Connected technical record |
| --- | --- | --- |
| Chapter 2: exDQLM | Software contribution, model interpretation, package workflow, primary examples, mixed findings, limits | Appendix B: posterior targets, backend details, LDVB/RHS updates, forecasting and synthesis formulas |
| Chapter 3: hydrologic synthesis | Source/horizon contract, model, five-origin design, principal evidence, interpretation, limits | Appendix C: MCMC/VB algorithms, parameter summaries, cutoff and sensitivity diagnostics |
| Chapter 4: Q--DESN | Conditional-quantile target, fixed-feature contract, central models, primary simulation and applications, qualifications | Appendix D: distribution/prior algebra, Gaussian baseline derivation, MCMC/VB/ELBO detail, joint and multistep mechanics, secondary evidence |
| Chapter 5: MPI/MTI | Interval targets, principal formal statements, TCSP action/evidence, main application, proposed extensions, limits | Appendix E: proofs, score and path derivations, calibration mechanics, secondary application evidence, proposed-extension computation |
| Cross-chapter layer | Chapters retain project-specific definitions needed for interpretation | Appendix A: compatible notation and target/update/scoring/uncertainty concordance without claiming false model equivalence |

`main.tex` places the five appendices after Chapter 6 and before the single
consolidated bibliography. The old formatting demonstration remains tracked
but inactive; it is not part of the compiler graph.

## Migration and preservation controls

The one-time migration tool `scripts/restructure_reader_first.py` accepts only
the four approved pre-migration chapter hashes. It moved existing units before
local bridge editing and refuses a different input state. The resulting
`appendix-migration-map.json` records 14 units:

- one Chapter 2 posterior/computation unit;
- two Chapter 3 algorithm and secondary-diagnostic units;
- six Chapter 4 distributional, computational, joint/multistep, simulation,
  GloFAS, and PriceFM units; and
- five Chapter 5 derivation/proof, tolerance, application, and extension units.

Each record preserves the source-unit hash, before/after chapter hashes,
destination hash, semantic class, risk, appendix label, display links, and
review state. The immutable import manifests still describe the original Git
blobs. `revision-ledger.json` separately records the current editable chapter
derivatives and the newly derived appendices. This avoids rewriting source
history while making the body/appendix split reproducible.

Every moved unit has a surviving body bridge. The bridge states the idea or
finding needed for a body-only reading and points to the appendix for recovery.
The appendices follow their parent chapters' conceptual order. Negative or
mixed results, application boundaries, TCSP proof limits, the proposed status
of the MTI extensions, and likelihood/generalized-update distinctions remain
in the body.

## Active-project and validation wiring

`scripts/build.sh` requests TeX recorder output. On muscat's TeX Live 2018
fallback it uses pdfLaTeX, BibTeX, and three resolving pdfLaTeX passes; the
fourth total pdfLaTeX pass is necessary for a stable clean build with the
legacy UCSC class.

`scripts/validate_structure.py` combines recursive source discovery with the
compiler's `.fls` file. It verifies appendix order, active static inputs,
macro-expanded inputs, duplicate labels, migration markers and bridges,
machine-path exclusion, and complete visual-ledger coverage. Ten unit tests
cover the current active/inactive graph, compiler-resolved macro input, moved
display survival, path hygiene, missing-input rejection, and duplicate-label
detection. The manuscript and editorial validators now discover the active
appendices rather than assuming that all substantive TeX lives in Chapters
2--5.

The release tier additionally requires the ignored audit-clone root and checks
every imported blob at its fixed commit. It does not build or mutate a research
repository.

## Release evidence

The accepted local candidate is
`build/release-20261008T063557Z/main.pdf` (ignored generated output):

- 361 US Letter pages and 18,176,334 bytes;
- SHA-256 `80cee7e8e46f831029d6a810434b47fef742d1be95677e70830e6eca601d476c`;
- 102 of 102 immutable imported Git blobs rechecked;
- 48 active TeX files, including one compiler-resolved macro input;
- 421 unique active labels and 118 resolved bibliography keys;
- 14 migration records and 33 active visual-description records;
- zero undefined citations/references, duplicate labels, unstable-label
  notices, missing files, overfull boxes, fatal errors, Type 3/Type 0 fonts,
  or unembedded fonts; and
- 40 nonblocking underfull-box notices.

The body ends at numbered page 203. Appendices A--E begin at 204, 208, 222,
231, and 296; the bibliography begins at 323. Chapter openings, the body-to-
appendix transition, every appendix opening, and both bibliography endpoints
were rasterized and checked. No clipping, collision, stranded heading, or
unexpected margin behavior was found. Full command, artifact, and diagnostic
details are in `VALIDATION.md`.

## Accessibility boundary

`accessibility-ledger.json` contains a reviewed description for each of the 33
active graphic or input-only visual records. This is necessary source-level
preparation, not a conformance claim. The muscat engine is TeX Live 2018
pdfTeX; the resulting PDF reports `Tagged: no`. The server has no current
tagging-capable TeX environment or veraPDF-class conformance checker.

The visual baseline therefore remains pdfLaTeX. A filing candidate still needs
a modern tagging-capable build or equivalent supported remediation, an
external checker, and manual review of structure, reading order, mathematics,
tables, contrast, metadata, and alternative text. WCAG 2.1 AA and PDF/UA are
not claimed by this implementation.

## Remaining decisions and handoff

The structural implementation is complete. The following are independent
author, advisor, coauthor/publisher, or institutional gates:

1. replace the working title and confirm the official university-record name,
   committee, dean wording, conferral date, ORCID, and acknowledgments;
2. confirm granular contribution statements and whether the software chapter
   satisfies the program's independent research-chapter expectation;
3. record publication status and material-specific reuse permission for each
   manuscript-derived chapter and asset;
4. decide whether to retain or narrow the still-open TCSP theorem language and
   whether proposed MTI extensions need implementation before filing;
5. produce and validate an accessible filing candidate in a supported modern
   environment; and
6. after the verified GitHub `main` push, preserve any Overleaf-only edits,
   pull from GitHub, compile `main.tex`, and inspect the Overleaf log/PDF.

The verified branch and explicit merge commit are synchronized to GitHub
`main`. The new reader-first state has not been pulled or independently
verified in Overleaf. GitHub synchronization and Overleaf verification are
lifecycle states, not evidence of reuse permission or scientific reproduction.
`STATUS.md` and `source-manifest.json` hold the final state of this handoff.
