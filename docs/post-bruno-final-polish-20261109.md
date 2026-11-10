# Post-Bruno final dissertation polish: 9 November 2026

## Purpose and status

This record controls the bounded final pass requested after the detailed Bruno
revision was interrupted. It reconstructs the completed work, records the
remaining corrections, and separates manuscript changes from evidence and
release checks. The pass does not reopen the accepted scientific sources,
invent unreceived advisor comments, or alter results.

The implementation baseline is commit
`3fc5fa94177eac7595b40059e8d62eaff9f1377f`. At that point the branch contained
the completed Q--DESN and MTI responses, their itemized evidence, and a clean
184-page release. The branch was seven commits ahead of `main` and zero behind;
no remote operation was performed during this pass.

## Governing evidence

- Raquel's comments are controlled by
  `docs/advisor-comments-ledger-20261109.md`.
- Bruno's 116 normalized actions are controlled by
  `docs/bruno-revision-response-matrix-20261109.json` and
  `docs/bruno-revision-integration-plan-20261109.md`.
- Bruno's Chapter 4 review ends at Section 4.4. Sections 4.5--4.8 are outside
  the received review and are not represented as advisor-approved.
- Item `B5-058`, an unidentified “Tony et al.” reference, remains deferred.
  No citation is added without an identifiable source.
- The academic-writing profile is
  `/data/jaguir26/local/src/RQR-GIBBS/STYLE_PROFILE.md`, SHA-256
  `b9483cf55e108f5615c203dfff6c0940b7ecc5c001aaad679507004b70352513`.

## Editorial decision rule

A sentence is changed only when it has a demonstrable defect in statistical
meaning, grammar, reader orientation, cross-reference accuracy, or rendered
presentation. Technically necessary terms such as likelihood, posterior,
recurrent feature, software, and computation are retained. Generic claims,
promotional language, project-management language, and self-conscious
statements about the writing process are excluded from the dissertation text.
Qualifications remain adjacent to the claims they delimit.

The following invariants apply:

1. preserve the fixed source authorities and the contribution boundaries;
2. preserve numerical results, citations, labels, assets, and input files;
3. distinguish conditional quantiles, predictive distributions, loss-defined
   intervals, and repeated-sampling tolerance guarantees;
4. describe empirical findings as findings for the stated designs rather than
   as universal properties; and
5. prefer direct statistical prose to engineering, product, or artificial-
   intelligence terminology unless the term is technically required.

## Findings and resolutions

| Finding | Resolution | Scientific effect |
| --- | --- | --- |
| Two reader-facing chapter references followed physical filenames rather than the compiled chapter order. | Q--DESN now refers explicitly to Chapters 2 and 3; Appendix A uses the complete Chapters 2--4 range. | None; the links now identify the intended chapters. |
| The hydrology component equations still used reduced type despite Raquel's normal-size requirement. | Define the gauge and source quantile locations first, use those symbols in the channel equations, and retain body-size type with modest display spacing. | None; this is an algebraically equivalent presentation of the existing model. |
| A few transitions used generic synthesis or product-oriented wording. | Name the statistical comparison or reported evidence directly. | None; claims and qualifications are unchanged. |
| The MTI extensions heading was hyphenated across display lines. | Shorten the heading without changing the section's proposed status, which remains explicit in its opening and in the abstract. | None. |
| Appendix A did not immediately orient the reader to its limited role. | State that it is a concordance across different inferential targets, not a common model. | None. |
| The advisor ledger still described Bruno's completed revisions as planned. | Reconcile the ledger with the response matrix and the validated Q--DESN and MTI commits. | Documentation only. |

## Advisor and style closure

The response matrix closes 115 of 116 actions: 83 are implemented and
validated, and 32 were already satisfied and revalidated. The remaining item
is the source-identification deferral `B5-058`. This pass does not change those
dispositions. It instead verifies that the integrated text still follows the
advisor requirements: hydrology precedes software, contributions appear before
limitations, Chapter 5 separates its inherited and new results, and technical
details remain in the corresponding appendices.

The prose review covers the abstract, all four research chapters, the
synthesis, Appendix A, and the changed part of Appendix E. It checks for
formulaic transitions, promotional language, internal revision vocabulary,
unsupported novelty claims, and artificial-intelligence or engineering framing.
The check is contextual; it does not delete legitimate technical language or
use an automated authorship detector.

## Validation record

The final record must include:

- revision-ledger and fixed-source validation;
- unchanged citation, label, input, and figure tokens except for the two
  intentional chapter-reference corrections;
- clean TeX diagnostics, references, citations, and duplicate-label checks;
- page count and PDF metadata;
- extracted-text terminology and duplication scans; and
- rendered inspection of every changed page.

Fast and release validation passed against the immutable audit root. The
accepted artifact is `build/release-20261110T010745Z/main.pdf`: 184 US-Letter
pages, 4,143,945 bytes, PDF 1.7, SHA-256
`5cae23dfc0b9a9072d5ddc4089d6fe8694e7deab0b39a373b1352e899a75ec38`.
All 32 fonts are embedded and no Type 3 font occurs. The final log has 12
underfull and zero overfull boxes, with no unresolved reference, citation,
duplicate-label, rerun, or fatal diagnostic. Extracted text contains none of
the screened internal, formulaic, or promotional language. The 14 changed
pages were rendered from the release artifact, matched the inspected build
pixel for pixel, and showed no clipping, collision, unreadable display, or
stranded heading. The PDF remains searchable and untagged; accessibility
remains a filing-stage task rather than a defect in this committee copy.

Manuscript commit `d5f634aa0abff98f59a5ed920057ff37d752365e` contains the
bounded polish. No push, merge, or Overleaf synchronization was performed.
