# Chapter 5: ECM and Gibbs computation

Date: 2026-11-11. Author-directed scientific-source migration.

## Scope and authorities

This revision replaces Chapter 5's active convex-profile computation and
empirical packet with the authenticated finite-iteration ECM account. It
promotes the shared generalized-posterior augmentation and Gibbs derivation
into the main computational exposition. It does not fabricate a numerical
Gibbs comparison or run a new experiment.

The dissertation starts from remote main
`3f264eaf4fa9b398753945fc3cb20f70178e383d`. Its chapter source is identical to
the audited `cb8e99e3978350a240e32c1047c9551e0a17d81a`; the intervening
Overleaf merge changed only the mode of the Figure 5.1 generator.

The new foundation source is `AntonioAPDL/RQR-GIBBS` at
`cab844d0695fe13fa3f610615d282972112eba51`. Archived ECM numerical code is
identified by `9462d7342225be50be6f28cccbd5d1f854a705a5`, with recovered
matched comparisons recorded at
`288461cfce8493fe16aac5a778b27ec2b059568b`. Source hashes and the exact
current artifact inventory are in the companion JSON record.

The separately maintained extension source is `AntonioAPDL/MTI-EXTENSIONS` at
the corrected commit `66a63ddc389b1492444e6c9e4611c5076ed1ad19`. Its
two-parent main merge is `488d072507f977362ba6c2890e02692e81df9d72`.
Immutable earlier imports and advisor-review records are retained.

## Tilt convention and effect on numerical work

The retained-mean convention is `mu + delta`. In midpoint coordinates its
linear loss term is `-2 q delta (m-y)`, equivalently `+2 q delta (y-m)`.
The root form is `-q delta (a+b-2y)`. The Gaussian canonical vectors have
the corresponding positive tilt shift.

The extension main manuscript formerly reversed the midpoint term while its
root-form supplement and Gaussian updates used the correct convention. The
correction changes that displayed formula and adds five standard-library
regression tests. Both extension documents compile after the correction.

The authenticated archived ECM C++ objective and root updates already use
the correct sign. Its C++ implementation, shared R objective, and root-system
utility are byte-identical to the updated foundation source. The audited
Gibbs source uses the same correct loss and positive canonical shift. No
rerun is justified by the manuscript typo. This source comparison does not
inspect the installed package or commit of every live external process.

## Reader-facing changes

- Chapter 5's introduction now connects interval targets, generalized
  updating, ECM/Gibbs computation, and the separately assessed tolerance rule.
- The computational section specifies the fixed loss, proper Gaussian
  priors, augmentation, Gaussian/GIG conditionals, and the distinct roles of
  ECM mode estimates and Gibbs endpoint uncertainty.
- Appendix E replaces the active numerical convex-solver proposition with
  propriety, conditional derivations, two compact algorithms, penalized
  empirical balance, and actual ECM numerical controls.
- The three curated population results and their mathematical profiling
  arguments remain. The author-selected Figure 5.1 remains unchanged.
- The tolerance section now uses the actual ECM candidate construction and
  calibration evidence instead of the old profile procedure's stronger
  simultaneous calibration statement.
- Simulation and pharmaceutical tables, numerical macros, figures, captions,
  and prose are replaced as a coherent packet. The abstract, acknowledgments,
  introduction, and synthesis are reconciled to that account.
- The two simulation graphics are presentation derivatives of frozen compact
  summaries. A base-R generator and two hash-checked CSV inputs reproduce
  their larger labels and shared axes without fitting or recalibration.
- Regression/dynamic extensions retain their separate scope. No complete
  empirical validation or tolerance guarantee for those extensions is added.

The exact old/new prose diff is retained in the ignored implementation-review
area. Public source, claim, revision, appendix, display, and accessibility
records identify the active derivatives. No bulk baseline regeneration was
used and unrelated research chapters remain unchanged.

## Empirical interpretation

The updated comparison covers 72 distribution/design cases and 1,000 common
datasets per case. MTI--ECM content attainment ranges from 95.1% to 99.9%;
its mean width is smaller than Young--Mathew in 39 of 72 cases. Across the
six asymmetric distributions it is smaller in 36 of 54 cases. Simultaneous
validation bounds have 53 lower bounds above .95 and 19 intervals containing
.95. The two adverse pointwise calibration minima remain visible.

Of the 72,000 selected ECM fits, 42,116 meet the stopping criterion and
29,884 reach the cap. These are finite-iteration results, not a collection
of certified global posterior modes. All returned intervals remain included.

In the primary pharmaceutical example, ECM median width is .553 versus
.533 for Young--Mathew, with median held-out content 96.6% versus 95.4%.
This reverses the former profile-based favorable width comparison. Width,
content, and placement are interpreted together. Only 90/1000 primary
tensile fits and 14/1000 primary RSD fits meet the ECM stopping criterion;
across all partitions/responses the count is 170/3004.

The frozen source's Gibbs comparison files are empty. No numerical agreement,
timing ratio, or Gibbs tolerance result is asserted. The prepared comparison
holds ECM-selected content and tilt fixed; it is not itself an independently
validated Gibbs tolerance-selection procedure. Assessed future results
require a new source/claim update.

## Validation and release record

The five extension regression tests pass, including rejection of the reversed
sign. The extension main and supplement compile to 7 and 4 pages respectively.
The dissertation has a migration-specific validator and mutation tests for
required methods, sign, retired numerical-profile claims, and the Gibbs
empirical boundary. The existing source, historical-advisor, voice, display,
structure, and accessibility controls remain active.

The final dissertation test/build/visual receipts and publication identifiers
are recorded in `docs/VALIDATION.md` and `docs/STATUS.md` after their gates
complete. Neither a source build nor a GitHub push is an independent Overleaf
compile, committee approval, or accessibility-conformant filing assessment.
