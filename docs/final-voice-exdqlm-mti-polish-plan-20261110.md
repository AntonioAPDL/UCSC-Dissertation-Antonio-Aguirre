# Final voice, exdqlm, MTI, and prose revision plan

Date: 2026-11-10

Baseline commit: `f2074052b256893091c6105615a2515127fe76b1`

Baseline release: `build/release-20261110T102200Z/main.pdf`
Baseline SHA-256: `89855c527c712777cdc92dd0671a41d7076c275e5af57150ecd09c836cd81e1b`

## Scope

This revision implements the candidate's and advisors' final voice and
exposition decisions. It has four connected purposes:

1. remove first-person singular prose and use first-person plural consistently
   when an authorial subject is needed;
2. distinguish the original `exdqlm` package and inherited exAL/exDQLM methods
   from the later package work represented in the dissertation;
3. retain only the Chapter 5 theory and proofs needed to identify the MPI/MTI
   targets, justify the fitted calculation, and interpret the calibrated
   tolerance evidence; and
4. replace generic, product-oriented, or formulaic prose by statistical
   objects, assumptions, comparisons, and evidence.

The revision does not authorize new numerical experiments, altered results,
new citations, stronger novelty claims, or changes to the fixed research-source
authorities.

## Controlling evidence

- The original package comparison is `exdqlm` 0.1.1 at
  `49cea5a48b2992d58eceb583e333bf08333e9be6`.
- The current package authority is 1.1.2 at
  `e51045a4324901cced27ca2aaa22569afbc8e0e6`.
- The current software-article authority is
  `98cec593d11bf32715a690ae168086f16160e7f0`.
- The hydrologic results remain attached to package version 1.1.0.
- The academic-writing standard is the version 0.2 style profile recorded in
  the advisor-revision documentation.

Package chronology and authorship allocation are separate questions. Yan,
Zheng, and Kottas retain credit for the exAL family and static exAL regression.
Barata, Prado, and Sanso retain credit for exDQLM, the original MCMC and ISVB
procedures, and the transfer-function extension. The later contribution is
limited to the package work confirmed by the candidate and supported by the
current article and package records.

## Voice rule

Use `we` and `our` for authorial contributions, choices, and interpretations.
Prefer the model, theorem, experiment, or posterior quantity as the grammatical
subject when no authorial subject is needed. Formal bibliographic facts may use
the name Antonio de Leon, but the scientific narrative must not refer to the
candidate in the third person. Mathematical uses of `I` are not prose and must
not be changed.

## Chapter 5 result dispositions

- Retain the mean-preserving score characterization.
- Retain quantile-window identification.
- Fold the fixed-content mean-tilt proposition into the definition and global
  identification argument.
- Retain global identification of the MTI target.
- State the ET, MPI, and shortest-contiguous tilts in prose and equations rather
  than as a separate corollary.
- Omit the supplemental convex-order result and the unused DKW bound.
- Fold the profile-radius lemma into the proof of global identification.
- Present fractional empirical balance as a derivation rather than a theorem.
- Retain the convex midpoint profile because it justifies the computation.
- Retain the calibration design, direct posterior content calculation, and
  sample-range feasibility condition needed for the reported evidence.

Every retained result must be preceded by the question it answers and followed
by its role in the chapter, with the proof location and relevant assumptions.

## Style rule

The style review is contextual. Words such as *compiled*, *runtime*,
*benchmark*, *training*, *operational*, *network*, and *production* remain when
they identify an actual computation, data split, forecast setting, method, or
industrial batch. Generic uses of *framework*, *ecosystem*, *interface*,
*architecture*, *illustrates*, *demonstrates*, and document-about-document
phrasing are replaced when a more exact statistical noun or claim is available.
The accurate AI-assistance disclosure remains.

## Verification

Each manuscript unit receives source review, fast validation, a chapter build,
and diff inspection. The final gate is a clean release build with fixed-source
blob verification, log/font/geometry checks, extracted-PDF voice and phrase
scans, and rendered inspection of every affected page. Current ledgers and
status records are reconciled only after the manuscript is final.
