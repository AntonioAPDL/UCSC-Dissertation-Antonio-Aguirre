# Final reader and statistical revision implementation

## Scope

This record implements
`docs/final-reader-statistical-revision-plan.md` from baseline commit
`f82c7bce192d51dbc686070533647780cacbd5dc`.  The pass reorganizes and edits the
existing dissertation; it does not rerun a research model, simulation,
forecast experiment, or data analysis, and it does not change any authorized
research-source snapshot.

## Scientific corrections

- Corrected the duplicated Chapter 5 MTI midpoint loss to
  `-2 c delta (m-y)`, consistent with the primary loss, population scores,
  Gaussian canonical shift, and Appendix E.
- Repaired malformed Chapter 4 and Chapter 5 appendix references and the
  resulting broken PDF text.
- Reclassified Chapter 3 as a retrospective five-origin comparison under one
  globally specified model.  Origin-specific response and product fitting
  continues to exclude future USGS outcomes, but transfer persistence and
  exploratory seasonal frequencies use global development information.
- Reclassified Chapter 4's single-quantile simulation as development-informed:
  the 300-target window and reported reservoirs followed exploratory assessment
  of the evaluation series.  The text now states that origin--horizon pairs
  within a simulated trajectory are dependent and are not independent
  simulation replications.
- Standardized the inverse-gamma parameterization, replaced “diffuse” prior
  language by the actual small shape/scale specification and sensitivity set,
  limited the KL diagnostic to marginal agreement with its plug-in Gaussian
  reference, and separated CRPS performance from calibration and sharpness
  diagnoses.

## Structural and editorial changes

- Chapter 2 is retitled around statistical computation and software.  The
  function-by-function S3/API table is removed because it duplicates package
  reference documentation and carries no scientific claim.  The chapter keeps
  model/software design principles, statistical operations, numerical choices,
  examples, negative findings, and limitations; Appendix B retains posterior
  and implementation details.
- Chapter 3 uses source-specific statistical headings and a shorter VB--LD
  explanation.  Archive and file-compatibility language is removed from the
  reader-facing account.
- Chapter 4 uses sentence-case headings, fitting/development/evaluation terms,
  and explicit selection-history and replication qualifications.  Method-
  essential DESN, reservoir, feature, and PriceFM terminology is retained.
- Chapter 5 is reduced from two visible article sequences to one dissertation
  argument.  The former second introduction, repeated fixed-target development,
  conditional-update derivations, and second discussion are replaced by a
  compact proposed-extension section and one final discussion.  The detailed
  regression, pseudo-AL, ECM, shrinkage, basis, and state-space derivations
  remain in Appendix E.
- Chapter 6 now compares evaluation maturity directly across the four projects
  and treats versions, information sets, origins, horizons, and selection rules
  as parts of statistical meaning.  Git/repository/build administration is kept
  in project documentation rather than the scientific chapter.
- Appendix figures and tables remain numbered, captioned, and locally
  referenced, but are omitted from the global lists.  This reduces the
  front-matter navigation burden without removing scientific content.

## Preservation and boundaries

Principal claims, equations, citations, displays, coauthor attribution,
negative results, and limitations remain.  The Chapter 2 API catalogue is the
only labeled display intentionally omitted, and its disposition is recorded in
`docs/display-ledger.json`.  No technical appendix source was deleted.  The
claim-evidence ledger records the strengthened Chapter 3 and Chapter 4 scope
qualifications.  Administrative reuse, individual contribution, metadata,
accessibility, and Overleaf verification gates remain separate.

## Verification contract

Verification consists of the repository's fast, chapter, and release checks;
LaTeX log review; PDF page, font, and geometry checks; PDF-text scans for the
known malformed strings and internal production language; and rendered review
of the front matter, chapter openings, corrected evaluation passages, Chapter
5 transition, and bibliography endpoints.  Exact artifact measurements and
remaining benign warnings are recorded in `docs/VALIDATION.md` after the final
clean release build.

## Verification outcome

All contracted checks passed on 2026-10-28.  The release tier rechecked 102
immutable research-source blobs and all import, evidence, display, structure,
citation, dependency, rights, path, and secret controls.  The accepted local
artifact is `build/release-20261028T044714Z/main.pdf`, a 414-page US-Letter PDF
with SHA-256
`49b0bc25f5c4b46c474379d3b7f33bfbfd01a3a28cb77660db63a4a8c5f0e409`.
The final log has no blocking diagnostics or overfull boxes; all 52 reported
font rows are embedded and none is Type 3.  PDF-text scans found none of the
known malformed appendix strings or the internal production terms targeted by
this pass.  The front matter, every chapter and appendix opening, corrected
reader-facing passages, and bibliography endpoints were rendered and reviewed.
The complete release record and the still-open filing gates are in
`docs/VALIDATION.md`.
