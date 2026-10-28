# Final reader and statistical revision plan

## Purpose and fixed baseline

This document controls the final dissertation-wide reader revision requested
after the advisor review.  Implementation begins from clean commit
`f82c7bce192d51dbc686070533647780cacbd5dc` on the dedicated branch
`editorial/final-reader-statistical-revision-20261027`.  The scientific source
snapshots, numerical results, imported displays, and external computation
remain fixed.  This pass may correct transcription and interpretation errors,
reclassify the strength of existing evidence, remove duplication, and move
technical exposition to the connected appendices.  It must not create new
results, silently strengthen a claim, or present an unperformed rerun.

## Diagnosis and decisions

The current thesis already has a sound four-project argument and connected
technical appendices.  The remaining problems are concentrated rather than
architectural:

1. Chapter 5 repeats a second article after its first discussion even though
   the corresponding regression and dynamic derivations are already preserved
   in Appendix E.  This is the largest interruption to the dissertation's
   narrative.
2. Chapters 3 and 4 state evaluation protocols more strongly than their model-
   selection histories support.  Chapter 3 uses a globally selected transfer
   parameter (and globally specified seasonal frequencies) in a five-origin
   retrospective comparison.  Chapter 4's primary simulation horizon was
   chosen after examining a longer evaluation series.  These are valid
   development-informed studies, but not untouched prospective validations.
3. Several local statements conflate a proper score with separate calibration
   and sharpness diagnoses, call a small-hyperparameter inverse-gamma prior
   “diffuse,” or use an ambiguous inverse-gamma parameterization.
4. Internal production language—repository audits, source archives, handoff
   mechanics, and document engineering—appears in reader-facing chapters.
   Provenance remains essential in project records, but only scientifically
   meaningful version and information-set conditions belong in the thesis.
5. The lists of figures and tables are dominated by technical-appendix entries.
   Appendix displays remain numbered and locally referenced, but are excluded
   from the global front-matter lists so those lists describe the main
   dissertation argument.
6. A few malformed appendix references and one sign-reversed duplicate MTI
   formula are objective defects and receive priority over stylistic editing.

The chosen structure preserves the four research chapters.  It does not
rewrite the articles from zero.  It treats their current prose as source
material, keeps target definitions, principal evidence, negative findings, and
limitations in the chapter bodies, and uses the existing appendices for proofs,
conditional distributions, algorithms, secondary diagnostics, and detailed
implementation contracts.

## Work packages

### 1. Scientific correctness and evaluation contracts

- Correct the Chapter 5 duplicate fixed-tilt loss so its sign agrees with the
  authoritative midpoint loss, root-form equations, conditional canonical
  shift, and Appendix E.
- Repair the malformed Chapter 4 and Chapter 5 appendix references.
- Describe Chapter 3 as a retrospective, globally specified five-origin
  comparison: response/product fitting at each origin excludes future USGS
  outcomes, while the globally frozen specification used development
  information through the representative 2022 origin.
- Describe Chapter 4's single-quantile simulation as development-informed and
  exploratory because the 300-target primary window followed assessment of the
  500-target series.  Do not imply an untouched confirmation series or
  independent replication where none exists.
- Standardize inverse-gamma notation, proper-score interpretation, KL scope,
  and small-hyperparameter prior language.

### 2. Reader-first chapter structure

- Retain Chapter 1's target-first statistical framework and collective
  attribution, but remove public-document language about repository audits,
  rights administration, and synchronization.
- Retitle Chapter 2 to emphasize statistical computation and software rather
  than infrastructure.  Compress the function-by-function interface catalogue
  into statistical design principles and direct package-specific details to
  Appendix B and the package documentation.
- Rename Chapter 3 sections with source-specific statistical nouns, shorten the
  generic variational derivation, and remove file/archive terminology.
- Standardize Chapter 4 headings to sentence case and distinguish model
  fitting, development, and evaluation from generic “training/test” language
  where the latter is not technically required.
- Reorganize Chapter 5 into one argument: fixed targets, MPI/MTI, fixed-target
  computation, calibrated tolerance inference, validation, application,
  compact proposed extensions, and one final discussion.  Detailed extension
  algebra remains in Appendix E.
- Rewrite Chapter 6's provenance discussion around versioned statistical
  protocols and add an explicit comparison of evaluation maturity across the
  four projects.

### 3. Navigation and prose quality

- Exclude appendix-only figures and tables from the global lists while
  preserving numbering, captions, labels, and local references.
- Split the longest expository paragraphs and replace vague terms such as
  “framework,” “workflow,” and “architecture” when a specific statistical noun
  is available.  Method names such as deep echo-state network and justified
  machine-learning terminology are retained.
- Remove article self-reference (“this paper,” “present paper,” “companion
  manuscript”) from the dissertation body.
- Preserve statistical terminology, qualifications, citations, equations, and
  negative empirical findings.  No cosmetic edit may broaden novelty,
  calibration, operational, or tolerance claims.

### 4. Durable records and verification

- Update the revision ledger, appendix migration map where the body/appendix
  division changes, assistance log, status, and validation report.
- Recompute derivative hashes only after the text is final; immutable source-
  import hashes remain unchanged.
- Run fast and chapter validation, then a clean release build when the retained
  audit sources permit it.  Review undefined references, citations, duplicate
  labels, overfull boxes, fonts, page geometry, and the final PDF text.
- Render and inspect the front matter, each chapter opening, the Chapter 3 and
  Chapter 4 evaluation passages, the Chapter 5 transition and discussion, and
  the bibliography endpoint.
- Commit the verified revision on the editorial branch.  Merge and push only
  after the branch diff and rendered artifact pass the acceptance criteria.

## Acceptance criteria

The revision is complete only if all of the following hold:

- the duplicate MTI loss has one mathematically consistent sign;
- no malformed appendix-reference text remains;
- the Chapter 3 and Chapter 4 evaluation claims disclose their development
  history and do not claim prospective or untouched validation;
- Chapter 5 has one introduction and one final discussion, with extension
  derivations represented once in Appendix E;
- reader-facing chapters contain no Git, repository-audit, handoff, or private
  path language except scientifically necessary version information;
- proper scores, calibration, posterior uncertainty, prediction, and tolerance
  confidence remain distinct;
- the thesis compiles from tracked sources, blocking validation checks pass,
  and affected pages are visually inspected;
- documentation identifies exactly what changed, what was not recomputed, and
  what scientific or administrative limitations remain.
