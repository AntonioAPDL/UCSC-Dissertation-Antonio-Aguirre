# Author-comments revision plan (10 November 2026)

## Purpose and authority

This is the controlling specification for the 22 numbered author comments
received after the Bruno revision.  It supplements, but does not rewrite, the
immutable Bruno response record.  The pre-edit manuscript is commit
`2c513fa0fc7c95881628eb108b3a957d1ac9afeb` on
`editorial/bruno-revision-intake-20261109`.  Scientific statements remain
bounded by the fixed research-source commits in
`docs/author-comments-preedit-baseline-20261110.json`.

The revision has three aims: make the inferential objects understandable to a
committee reader, state Antonio de Leon's documented contributions precisely,
and replace defensive or generic prose with evidence-bounded statistical
language.  It does not authorize new numerical experiments, altered results,
invented theory, or promotional claims.

## Writing and scientific invariants

- Follow the version 0.2 academic-writing profile recorded in the baseline.
  The governing rule is to replace generic fluency with statistical
  specificity, not to optimize prose for an automated detector.
- Define the response, conditioning information, inferential target, interval
  event, approximation, and evaluation unit before interpreting a result.
- Distinguish conditional-quantile recovery, observation calibration,
  frequentist coverage of intervals for a quantile, and posterior summaries of
  a score.  Use the clarification report only where one of these distinctions
  resolves an actual ambiguity.
- Preserve empirical claims, numerical values, equations, citations, labels,
  and source projections unless an item below explicitly authorizes a change.
  The only planned label deletion is `tab:intro-interval-objects`.
- Attribute antecedent work by citation and state Antonio's later software and
  computational contribution directly.  Do not claim that the complete
  package is written in C++ or report an unmeasured speedup.
- Keep limitations where they are scientifically material, but state each
  limitation once, alongside the contribution and the next empirical or
  methodological step.  Do not append a defensive qualification to every
  result.
- Use standard statistical terminology.  Describe reservoir states as fixed
  nonlinear features or a recurrent representation; avoid product, deployment,
  engineering, or generic machine-learning language.
- Preserve the current assistance disclosure unless a factual correction is
  required.  No claim is made that AI was absent; the record states its limited
  uses accurately.

## Item-level implementation decisions

The machine-readable response contract is
`docs/author-comments-response-matrix-20261110.json`.  The selected resolutions
are summarized here.

1. Rewrite the abstract comparison so that score ranking and calibration are
   named explicitly.  Present the multiquantile crossing reduction as a
   flexibility--ordering tradeoff and the PriceFM result as comparable,
   slightly better AQL from fixed-feature Bayesian regressions.  Do not call
   PriceFM categorically expensive because no matched total runtime exists.
2. Replace project-level attribution disclaimers with documented, specific
   contribution statements.
3. Recast Chapter 1 around non-mean distributional targets---conditional
   quantiles and fixed-content intervals---and the computation required for
   routine use.
4. State the exdqlm contribution as substantial later package restructuring:
   improved LDVB and nonconjugate scale--skewness updates, compiled C++
   backends for intensive operations, filtering and smoothing corrections,
   forecasting and diagnostics, posterior-predictive synthesis, and static
   regularized AL/exAL regression under the regularized horseshoe prior.
5. Replace the interval-object table in Section 1.3 with short prose that
   defines the distinctions and establishes the section's role.
6. Audit first use of GloFAS, PriceFM, AL, exAL, ISVB, LDVB, MCMC, VB, DESN,
   RHS, MTI, AQL, CRPS, and PPLC independently in the abstract and each chapter.
7. In hydrology, state that each origin uses a supplied deterministic
   precipitation and soil-water forecast path and that covariate uncertainty is
   not propagated.  Do not guess its aggregation rule.  State that the limited
   number of origins reflects the cost of repeated full dynamic fits and that a
   matched MCMC comparison remains future work for uncertainty assessment.
8. Explain the three selected harmonic periods as dominant exploratory
   spectral frequencies.  Give physical interpretations only to the annual
   and semiannual components; describe the slow component without inventing a
   mechanism.
9. Add percentages beside every coverage fraction in hydrology Table 2.3.
   Bold only values optimal under the declared criterion: closeness to nominal
   95% coverage for coverage, and the minimum for interval score.  Width is not
   optimized in isolation.
10. Strengthen equation exposition by identifying the role of each hydrology
    model block and reviewing the other chapters for unexplained equation
    sequences.
11. In Chapter 3, use the article citations for Yan, Zheng and Kottas and for
    Barata, Prado and Sansó.  Define importance-sampling variational Bayes
    (ISVB) and Laplace--Delta variational Bayes (LDVB) at first use.  Separate
    inherited exAL/exDQLM methodology from Antonio's later software work.
12. Review calligraphic notation locally.  Retain standard probability and
    statistical objects such as `\mathcal N`, `\mathcal F`, `\mathcal D`, and
    `\mathcal L`; simplify decorative index sets only when doing so improves
    consistency.
13. Revise Chapter 4 so that the multiquantile evidence states the observed
    tradeoff exactly: crossing rates fall from 5.488% to 0.021% under AL and
    from 0.606% to 0% under exAL, while independent fits have the lower mean
    oracle score in six of eight mechanisms.
14. Describe the PriceFM comparison with the matched evidence: selected DESN
    mean AQL 6.687 versus 7.039 for reproduced PriceFM forecasts across 114
    region--fold cases, with lower fold-summary means in all three folds.  The
    computational contrast is architectural---fixed recurrent features and
    Bayesian readouts rather than end-to-end recurrent-weight training---not a
    measured runtime claim.
15. Replace the categorical MTI limitation about regulatory use with a direct
    data-scope statement and a concrete need for further prospective study.
16. Remove the four bold run-in labels in the MTI exposition unless a true
    hierarchy is needed; retain the four parallel contribution headings in the
    introduction and review the one exdqlm run-in separately.
17. Redesign Table 6.1 around four columns: project and target, dissertation
    contribution, principal evidence, and scope.  Make Antonio's contribution
    visible without collapsing antecedents or limitations.
18. Give Table D.1 the column heading `Scientific question`, a positive caption,
    and concise evidence-based entries.  Preserve its label and four-column
    structure.
19. Replace the closing slogan with a synthesis of the four contributions:
    distributional targets require target-specific models, computation, and
    validation, and the four projects provide complementary tools for those
    tasks.
20. Audit all research chapters for repeated caveats, internal workflow
    language, unexplained acronyms, product terminology, generic transitions,
    and inconsistent heading treatment.  Consolidate rather than delete
    scientifically necessary limitations.
21. Update the evidence, decision, display, import, appendix, and revision
    records only where the manuscript change makes them current.  Historical
    advisor records remain immutable.
22. Rebuild, inspect every affected page, and require a clean citation,
    reference, label, font, page-size, and provenance audit before release.

## Work packages and commit boundaries

1. **Controls.** Repair the display updater; freeze inputs, hashes, response
   items, and acceptance criteria; add the author-response validator to the
   fast gate.
2. **Hydrology.** Implement deterministic-covariate, spectral, computational,
   equation-guidance, and calibration-table changes.  Refresh only the current
   projected table destination and its manifest hash.
3. **exdqlm.** Clarify antecedents, Antonio's contribution, acronyms,
   computation, and conclusion.  Preserve the article/package authority split.
4. **Q--DESN.** Revise crossing and PriceFM interpretations, acronym first use,
   and Table D.1.  Preserve all numerical source results.
5. **MTI.** Replace categorical limitations and normalize run-in formatting.
6. **Introduction.** Rebuild the common theme, contribution account, and target
   distinctions; remove only the authorized interval-object table.
7. **Synthesis and front matter.** Redesign Table 6.1, replace the conclusion,
   then rewrite the abstract last so it matches the implemented chapters.
8. **Global audit.** Check acronym first use, notation, headings, table bolding,
   internal language, repeated caveats, and academic style; update current
   documentation and close all 22 response items.

Every research-chapter commit must pass fast validation and a chapter build.
Release validation must recheck the fixed source blobs, the 116 Bruno items,
the 22 author items, 35 display records (33 KEEP and 2 OMIT), all import
projections, and the complete active TeX graph.

## Stop conditions

Stop rather than infer if a source commit is unavailable; the deterministic
covariate aggregation cannot be verified; a requested statement requires a new
experiment; a contribution claim conflicts with authorship evidence; an import
refresh changes an unapproved asset; a notation edit changes a scientific
object; an editorial updater drops provenance; or remote `main` advances before
any later integration.  Push, merge, and Overleaf synchronization remain
outside this implementation unless separately authorized.

