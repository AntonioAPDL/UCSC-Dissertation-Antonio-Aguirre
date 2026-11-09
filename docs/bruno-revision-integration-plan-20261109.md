# Bruno Sansó revision integration plan: 9 November 2026

Status: **evidence frozen and itemized; manuscript changes not yet implemented**

This is the controlling supplement to
`docs/advisor-revision-plan-20261109.md` for the detailed review that arrived
after the earlier advisor-revision release. It does not replace Raquel Prado's
ledger or reopen revisions that remain correct. It records Bruno Sansó's new
comments, compares them with the current dissertation rather than the older
review copy alone, and specifies how each unresolved point should be handled.

## 1. Evidence and scope

Bruno's message was received in the existing Gmail thread at 2:55 p.m.
Pacific on 9 November 2026. The attached file was delivered through Apple Mail
Drop rather than as a native Gmail attachment. The message states that Chapter
4 was reviewed only through Section 4.4 and that Chapter 5 was reviewed in
detail. The original file is stored locally at
`audit-inputs/advisor-review-20261109/bruno-annotated-ch04-ch05-20261109.pdf`.
It is ignored by Git and must not be committed.

| Evidence field | Frozen value |
| --- | --- |
| Gmail message ID | `1a1c285ff3794970` |
| Message date | 9 November 2026 |
| Original filename | `UCSC_Dissertation___Antonio_Aguirre.pdf` |
| File size | 58,778,165 bytes |
| SHA-256 | `4824065866f8a60c547339e1349b2adeca23a4b459badece319d7395e183d035` |
| PDF properties | 221 pages; PDF 1.3; iOS Quartz; unencrypted |
| Reviewed thesis baseline | 221-page committee copy, hash `7145eae7fa840801d8526155327ae2ab81aafaebb002d8496eea6faa5fb6eaa9` |
| Current integration baseline | clean local and remote `main` at `11984bfb89b1df1ca882bf7759b605719df4cd0d` |
| Annotation representation | one Apple stamp appearance on each reviewed page; 36 annotated pages in total |
| Chapter 4 annotation pages | physical 109--118, corresponding to printed pp. 95--104 and Sections 4.1--4.4 |
| Chapter 5 annotation pages | physical 137--140, 142--148, 150--151, and 153--160, corresponding to printed pp. 123--146 |
| Appendix E annotation pages | physical 201 and 204--207, corresponding to printed pp. 187 and 190--193 |

There are exactly 36 non-link annotation objects: ten in the reviewed portion
of Chapter 4, twenty-one in Chapter 5, and five in Appendix E. Thus the page
coverage above accounts for every annotation object in the file. The plan
normalizes the handwriting into 116 action items: 40 for Chapter 4, 65 for
Chapter 5, and 11 for Appendix E. Closely connected marks are grouped only
when they require the same source edit and acceptance test.

The reviewed PDF predates the current 183-page release. Page numbers in this
plan therefore identify evidence, not current output locations. Stable LaTeX
labels and source files identify the implementation targets.

## 2. Executive diagnosis

The review supports a targeted reconstruction rather than a blind rollback to
the 221-page text.

1. Several high-level requests are already satisfied on current `main`. The
   obsolete chapter-source notices are gone; both chapters now state their
   contributions; Chapter 5 begins with the tolerance-interval problem; and
   its introduction distinguishes mathematical identification, the
   model-based content probability, empirical tolerance evidence, and proposed
   extensions. These passages should be preserved unless a remaining item
   requires a local change.
2. Chapter 4 still needs a definition-and-notation pass through Section 4.4.
   The principal issues are the time-series setup, the reservoir recursion and
   its dimensions, the distinction between independent and multiquantile
   targets, the composite likelihood, the augmented MCMC description, and the
   recursive forecasting indices. Bruno did not review Sections 4.5--4.8;
   those sections must not be described as advisor-approved.
3. Chapter 5 requires the larger intervention. Its opening is substantially
   clearer than the reviewed version, but much of the mathematical and
   computational core retains the terminology that Bruno found difficult:
   conditional notation is introduced late, proof locations are not always
   signposted, generalized Bayes and the learning rate appear too abruptly,
   the Dirichlet-process content calculation is under-motivated, and the
   calibration/validation design uses terms such as *cell*, *row*, *cutoff*,
   and *feasible* before their roles are fully specified.
4. The best solution is not to add more prose everywhere. Definitions and the
   inferential sequence belong in the chapter; proof details, propriety
   arguments, profile derivations, shortest-path continuation, and calibration
   bookkeeping belong in Appendix E. This division follows the advisors'
   earlier request for a readable main body and an essential technical
   appendix.
5. No scientific assertion should be changed from handwriting alone. Items
   that question a theorem, prior, comparison, or numerical design require a
   source check against the fixed Q--DESN and RQR/MTI authorities before text
   changes. A comment asking for clarification is not evidence that the
   underlying result is wrong.

## 3. Status vocabulary

- `SATISFIED_CURRENT`: current `main` already meets the comment's intent; the
  implementation pass verifies and preserves it.
- `PARTIAL`: current `main` improves the reviewed text but does not fully
  resolve the comment.
- `OPEN_EDIT`: a bounded source or structural edit is needed.
- `VERIFY_SCIENCE`: inspect the fixed research source, proof, or numerical
  record before selecting wording.
- `DECISION`: the best disposition depends on a documented author/advisor or
  scope choice.
- `WAITING_REVIEW`: evidence has not been supplied and must not be inferred.

## 4. Chapter 4 itemized plan

Implementation targets are `chapters/04-research-c.tex`, principally labels
`qdesn2026:sec:intro`, `qdesn2026:sec:model`, `qdesn2026:sec:inference`, and
`qdesn2026:sec:forecast`, with supporting definitions in
`appendices/d-qdesn-technical.tex` only when the detail would interrupt the
chapter.

| ID | Review page | Status | Required resolution and acceptance check |
| --- | --- | --- | --- |
| B4-001 | 109/95 | SATISFIED_CURRENT | Preserve the removal of the obsolete manuscript-source notice. The chapter must open with the statistical problem, not its production history. |
| B4-002 | 109/95 | PARTIAL | Define the observed time series before the forecast quantile. Use one convention for (Y_t), observed (y_t), forecast origin, and information set; verify all later indices against it. |
| B4-003 | 109/95 | PARTIAL | State the horizon as steps ahead of a forecast origin and distinguish the origin from the response time. The definition, recursive forecast subsection, and application notation must agree. |
| B4-004 | 110/96 | OPEN_EDIT | Replace repeated general discussion from Chapter 2 with a short contrast: Chapter 2 uses evolving linear states and product synthesis, whereas Chapter 4 uses fixed nonlinear recurrent predictors. Keep only background needed locally. |
| B4-005 | 110/96 | OPEN_EDIT | Cite or define DESN before the qualified phrase “specified deep echo state network.” The first use must identify the fixed reservoir construction rather than assume familiarity. |
| B4-006 | 110/96 | SATISFIED_CURRENT | Preserve the current first-use definition of reservoir states as recurrent states whose internal weights are drawn before regression fitting and held fixed. |
| B4-007 | 110/96 | SATISFIED_CURRENT | Preserve statistically correct prior language: ridge regularization/priors use a common scale; RHS permits coefficient-specific shrinkage with a slab bound. |
| B4-008 | 110--111/96--97 | OPEN_EDIT | Compress AL/exAL background already developed in earlier chapters. Retain only the quantile-location property, the augmentation needed here, the additional exAL shape, and the relevant uncertainty qualification. |
| B4-009 | 110--111/96--97 | SATISFIED_CURRENT | Preserve the direct Q--DESN contribution statement now on current `main`; do not revert to an architecture-first description. |
| B4-010 | 110--112/96--98 | SATISFIED_CURRENT | Preserve the current statement that MQ--DESN couples adjacent slope differences across levels within one regression while independent Q--DESN fits do not. Reconfirm after model-section edits. |
| B4-011 | 111/97 | SATISFIED_CURRENT | Preserve the corrected grammatical construction “stacking reservoirs.” |
| B4-012 | 111/97 | VERIFY_SCIENCE | Verify “penalized quantile sheets” against the Bonas et al. source and use the source's exact term. Do not substitute a plausible name from memory. |
| B4-013 | 112/98 | OPEN_EDIT | Move study-specific simulation and application descriptions to the evidence roadmap or Section 4.5. The introduction should state questions and contributions without narrating results before their design is introduced. |
| B4-014 | 113/99 | OPEN_EDIT | At the model opening, call (Y_t) the time series or stochastic process of interest and distinguish it from observed values (y_t). |
| B4-015 | 113/99 | PARTIAL | Define (mathbf z_t) as the vector of exogenous covariates, not merely variables, and state whether its components are contemporaneously available at fitting/forecast time. |
| B4-016 | 113/99 | VERIFY_SCIENCE | Give the exact scaling that produces (W-bar_d) from the raw recurrent matrix and target spectral radius (rho_d). Check the authoritative source before adding a formula. |
| B4-017 | 113--114/99--100 | OPEN_EDIT | State dimensions for (mathbf W_d), (mathbf W_d^{\rm in}), (mathbf Q_{d-1}), the reduced state, and the bias; verify every matrix product in the recursion. |
| B4-018 | 113/99 | OPEN_EDIT | Define the feature transformation (k) as a function, give its domain/codomain, and identify the transformations actually used. Do not leave “chosen feature transformation” uninterpreted. |
| B4-019 | 114/100 | VERIFY_SCIENCE | Check the leak-rate convention in the authoritative recursion and state correctly how smaller/larger (alpha_d) weights the preceding state. |
| B4-020 | 114/100 | OPEN_EDIT | Distinguish fixed random reservoir quantities, tuning parameters selected with training/development information, and regression parameters inferred from the likelihood. |
| B4-021 | 114/100 | OPEN_EDIT | Move study-specific feature-selection and development-sample qualifications out of the generic model definition unless they are needed to define the estimand. Cross-reference Section 4.5 or Appendix D instead. |
| B4-022 | 114/100 | OPEN_EDIT | Explain exactly which state transformations and direct inputs form (x-tilde_t), then derive its dimension (r) under the stated cases. |
| B4-023 | 115/101 | OPEN_EDIT | Introduce the comparator as (K) independent Q--DESN fits, one at each level, before defining MQ--DESN. Avoid the vague noun “approach.” |
| B4-024 | 115/101 | OPEN_EDIT | Define the observed response vector and the complete parameter collection (theta) before the likelihood; separate regression, likelihood, and prior-scale components. |
| B4-025 | 115--116/101--102 | OPEN_EDIT | Call the product in Eq. 4.5 a composite likelihood, not an “update.” Reserve *update* for the resulting loss-based/generalized posterior operation. |
| B4-026 | 115--116/101--102 | PARTIAL | Define the anchor block and adjacent slope-difference blocks before stating their priors. Explain how they reconstruct (beta_k). |
| B4-027 | 116/102 | OPEN_EDIT | State explicitly that RHS priors are placed on the anchor and slope-difference blocks, with block-specific scales; distinguish intercept ordering from slope coupling. |
| B4-028 | 116/102 | OPEN_EDIT | Use accurate language for the composite likelihood and composite/generalized posterior. State why the product is not a scalar-response joint sampling density and what is nevertheless normalized. |
| B4-029 | 116/102 | SATISFIED_CURRENT | Preserve the current qualification that the same response is reused across levels and the product is not a normalized scalar-response density. |
| B4-030 | 116--117/102--103 | OPEN_EDIT | Introduce the AL/exAL latent representation as a conditional model, define the latent variables and their support, and identify which displayed Gaussian argument is a variance. |
| B4-031 | 117/103 | OPEN_EDIT | Replace generic references to “shape” with the defined parameter (gamma) and use the same symbol in every conditional statement. |
| B4-032 | 117/103 | OPEN_EDIT | Describe tractable blocks through their full conditional distributions and sampling laws, not by saying that parameters “have updates.” |
| B4-033 | 117/103 | VERIFY_SCIENCE | State the proposed scale--shape transition exactly: which variable is integrated out, which conditional is sampled, and why the transition leaves the intended target invariant. Verify against the authority and Appendix D. |
| B4-034 | 117/103 | PARTIAL | Retain and sharpen the diagnostic statement: identify rank-normalized (widehat R), effective sample size, chain comparisons, and crossing diagnostics as checks, not guarantees. |
| B4-035 | 117/103 | PARTIAL | Motivate VB by repeated fitting over long series, forecast origins, or reservoir specifications. State the computational task reduced, not merely that fitting is “fast.” |
| B4-036 | 117/103 | OPEN_EDIT | Define whether VB supplies an approximation, initialization, or reported inference in each study; do not imply uncertainty quality without evidence. |
| B4-037 | 118/104 | OPEN_EDIT | Define forecast origin (o), fitting endpoint (T), horizon (h), and target (Y_{o+h}) in one place; then use that indexing throughout. |
| B4-038 | 118/104 | SATISFIED_CURRENT | Preserve the distinction between a draw-specific conditional-quantile location and the marginal posterior predictive quantile. |
| B4-039 | 118/104 | PARTIAL | Explain how observed history initializes reservoir states and how simulated future responses enter later lags in a recursive forecast. Verify information availability for covariates. |
| B4-040 | 109--118/95--104 | VERIFY_SCIENCE | Recheck all revised definitions, equations, and contributions against the fixed current Q--DESN authority before editing. No comment authorizes a source-version change. |

### Chapter 4 boundary

Bruno's review ends at Section 4.4. Sections 4.5--4.8 may be edited only when
required for consistency with a resolved item above or a later advisor note.
They remain `WAITING_REVIEW`; the eventual response must say “reviewed through
Section 4.4,” not “all Chapter 4 comments implemented.”

## 5. Chapter 5 itemized plan

Implementation targets are `chapters/05-research-d.tex`, with proof,
propriety, profile, and calibration detail in
`appendices/e-mti-technical.tex`. The current introduction already implements
many of Bruno's general requests; those resolutions are protected below.

| ID | Review page | Status | Required resolution and acceptance check |
| --- | --- | --- | --- |
| B5-001 | 137/123 | SATISFIED_CURRENT | Preserve the definition-first opening: fixed content does not determine placement, and a tolerance interval adds a repeated-sampling confidence requirement. |
| B5-002 | 137--140/123--126 | PARTIAL | Keep the exposition linear. Do not interpret simulation or calibration findings before the target, procedure, and study design are defined; retain only a short evidence-status preview. |
| B5-003 | 137/123 | OPEN_EDIT | Add a concise transition from Chapter 4: conditional quantiles are loss-defined distributional functionals, while this chapter studies loss-defined pairs of endpoints under a fixed-content and tolerance objective. Do not imply that the check and residual-product losses have the same target. |
| B5-004 | 137/123 | SATISFIED_CURRENT | Preserve removal of the chapter-source notice and in-preparation manuscript citations from the chapter opening. Attribution remains in acknowledgments/provenance, not as article-production prose. |
| B5-005 | 137--140/123--126 | SATISFIED_CURRENT | Preserve the current three-part contribution statement: identify the MPI target, define the MTI placement family, and construct/evaluate the calibrated tolerance rule. |
| B5-006 | 138/124 | SATISFIED_CURRENT | Preserve the motivation of the Pouplin et al. residual-product criterion through the interval-placement problem and clearly credit the inherited criterion. |
| B5-007 | 138/124 | SATISFIED_CURRENT | The current introduction no longer uses undefined (eta_1,eta_2). Preserve the simpler generic root notation until (a,b) are defined. |
| B5-008 | 138/124 | PARTIAL | When the population score equations first appear, explain that they are first-order conditions for the expected residual-product loss and state what each identifies. |
| B5-009 | 138/124 | SATISFIED_CURRENT | Preserve the current definition of retained mean through (M_c(u)) before using the term in the MPI/MTI contribution statements. |
| B5-010 | 138/124 | SATISFIED_CURRENT | Preserve the replacement of vague “same score” language with explicit MPI/MTI loss and placement-family language. |
| B5-011 | 138/124 | SATISFIED_CURRENT | Preserve the current top-level method sequence before calibration details: target, fixed-target fit, model-based content check, selection, independent evaluation. |
| B5-012 | 138/124 | SATISFIED_CURRENT | Preserve the statement that (delta) defines the estimand and that equal-tailed/shortest rules correspond to distribution-specific values, with target selection kept separate. |
| B5-013 | 138--139/124--125 | SATISFIED_CURRENT | Preserve the rewritten concise tolerance-procedure summary; do not restore the old grid and calibration bookkeeping to the introduction. |
| B5-014 | 139/125 | SATISFIED_CURRENT | Keep candidate-grid details out of the introduction and explain them only after the fixed-target calculation and content check are defined. |
| B5-015 | 139/125 | SATISFIED_CURRENT | Preserve the contribution-led introduction and its explanation of evidentiary value. Do not replace it with a long inventory of chapter contents. |
| B5-016 | 139--140/125--126 | SATISFIED_CURRENT | Preserve the concise evidence-boundary paragraph distinguishing proofs, exact model-based statements, finite-panel simulation evidence, and unevaluated extensions. |
| B5-017 | 140/126 | SATISFIED_CURRENT | Preserve Section 5.2's direct definition of (I_c(u)), retained mean (M_c(u)), and geometric width (W_c(u)), with dimensions/units interpretable. |
| B5-018 | 142/128 | OPEN_EDIT | Remove the meta sentence that announces what Section 5.3 will do. Begin with the interval content, ordered endpoints, and loss. |
| B5-019 | 142/128 | SATISFIED_CURRENT | Preserve the equation label for the piecewise MPI loss and use it in later references. |
| B5-020 | 142/128 | OPEN_EDIT | Replace imperative “Fix” wording where it obscures the setup with a direct assumption such as “Consider content (c\in(0,1)) and ordered endpoints (a<b).” |
| B5-021 | 142/128 | OPEN_EDIT | Explain the two factors as signed distances to the two endpoints; state separately how the (c) and (1-c) weights distinguish misses from retained observations. |
| B5-022 | 142/128 | PARTIAL | Define the empirical estimator through the average loss (or explicitly note that the sum has the same minimizer) and distinguish an unpenalized empirical minimizer from penalized/generalized-posterior calculations later. |
| B5-023 | 142/128 | OPEN_EDIT | Introduce (e(a,b;y)=(y-a)(y-b)) directly and derive the compact check-loss representation without the tutorial-like “Now define” transition. |
| B5-024 | 143/129 | OPEN_EDIT | Move the learning-rate, generalized-Bayes, restricted-regression, and future-qualification discussion until after the population target is established. Keep the loss definition focused. |
| B5-025 | 143--145/129--131 | OPEN_EDIT | Define (X), (x), (F_x), (Q_x), and (mu_x) before Proposition 5.1, or state and prove an unconditional result first and add the conditional version only after the covariate setup. |
| B5-026 | 144/130 | OPEN_EDIT | Number or otherwise give stable labels to the content and retained-mean score equations; later prose and proofs must refer to those labels rather than marks such as “first” and “second.” |
| B5-027 | 144/130 | OPEN_EDIT | Add an exact Appendix E proof pointer immediately after Proposition 5.1 and state the regularity conditions needed to differentiate under the expectation. |
| B5-028 | 144/130 | PARTIAL | Attribute the population-content equation to Pouplin et al. and identify the retained-mean equality as the additional consequence established here. Make that distinction visible in the contribution statement and proof discussion. |
| B5-029 | 144/130 | OPEN_EDIT | Replace undefined “retained core” language with the conditional law of (Y) given (a<Y<b), and define convex-order contraction before using that phrase. |
| B5-030 | 143--144/129--130 | OPEN_EDIT | Define the profiled risk before referring to it, or move the profile-risk argument entirely to Appendix E and leave only the result and proof pointer in the chapter. |
| B5-031 | 145/131 | OPEN_EDIT | Define (F_x), its inverse (Q_x), and the conditioning value (x) before Theorem 5.1; verify that all support and monotonicity conditions are stated on the correct conditional law. |
| B5-032 | 145/131 | OPEN_EDIT | Add a proof pointer for the symmetry implication (u_c(x)=(1-c)/2) and make clear which symmetry center is used. |
| B5-033 | 146/132 | OPEN_EDIT | Define an endpoint/root class and distinguish unrestricted pointwise endpoints from a linear or other restricted regression class. Explain why (X)'s role changes the attainable score equations. |
| B5-034 | 147/133 | OPEN_EDIT | Add the Appendix E proof pointer for Proposition 5.2 and state whether the claim concerns stationary points or global minimizers. |
| B5-035 | 148/134 | OPEN_EDIT | Add the Appendix E proof pointer for Theorem 5.2 and keep its stronger support, density, and moment assumptions visible. |
| B5-036 | 148/134 | OPEN_EDIT | Define the “escaping-root direction” mathematically or move the boundary/unbounded-risk discussion to Appendix E. The chapter should retain only the admissible tilt range and its consequence. |
| B5-037 | 150/136 | OPEN_EDIT | Revise Figure 5.2's title/caption so it is unmistakably a deterministic population calculation, not an estimated finite-sample result. Define every abbreviation and remove the opaque final sentence. |
| B5-038 | 151/137 | OPEN_EDIT | Use “population tilt associated with [target]” or another defined phrase in Figure 5.3 rather than unexplained “recovery tilt”; explain that the Cornish--Fisher values are approximations based on population skewness in this display. |
| B5-039 | 153/139 | OPEN_EDIT | Introduce generalized Bayes before first use, cite an appropriate authoritative source already in or added to the verified bibliography, and distinguish a loss-based posterior from an ordinary likelihood posterior. |
| B5-040 | 153--155/139--141 | OPEN_EDIT | Define the learning rate (omega_R), its role in scaling cumulative loss relative to the prior, and the value used in the reported study. Do not call it a content or tilt parameter. |
| B5-041 | 153/139 | OPEN_EDIT | Move the detailed propriety argument for Gaussian versus heavier-tailed root priors to Appendix E. Retain in the chapter only the prior actually used, the resulting proper target under stated conditions, and a precise caveat. |
| B5-042 | 155/141 | OPEN_EDIT | State explicitly whether the reported endpoints minimize penalized cumulative loss, maximize the generalized posterior density, or summarize posterior draws. Use one correct term throughout. |
| B5-043 | 155/141 | VERIFY_SCIENCE | Verify whether the deterministic profile endpoint is a generalized-posterior mode/M-estimator under independent Gaussian root priors, and state the induced penalty. Do not describe it as a posterior mean or MAP without proof. |
| B5-044 | 155/141 | OPEN_EDIT | Mark (omega_R=1), (lambda=10^{-4}), the prior means, and the objective tolerance as choices of the reported validation study, not universal method defaults. |
| B5-045 | 155--156/141--142 | OPEN_EDIT | Before the content check, define the Dirichlet-process prior (F\sim\mathrm{DP}(aH)), its concentration (a), centering distribution (H), and why a response-distribution model is separate from the loss-based endpoint target. |
| B5-046 | 155--157/141--143 | PARTIAL | State the exact Beta law for (F(I)\mid D_n) for a fixed interval and explain why applying it to data-dependent candidate intervals is a selection device whose tolerance behavior is calibrated empirically. |
| B5-047 | 155--156/141--142 | OPEN_EDIT | Rewrite the tolerance target after defining the random interval (widehat T_n=[L_n,U_n]), the true distribution (F), and (C_F([L,U])=F(U)-F(L)). |
| B5-048 | 156/142 | DECISION | Replace the old “six quantities” paragraph with a hierarchy. Treat (c), (1-alpha), fitted (q), tilt (delta), and eligibility cutoff (gamma) as the five inferential/design quantities; define (omega_R) earlier as a fixed loss scale. Confirm this classification against the implemented procedure before editing. |
| B5-049 | 156/142 | OPEN_EDIT | State in ordered steps how candidate ((q_j,delta_j)) values are fixed, endpoints are fitted, posterior content probability is computed, eligibility is determined, and the shortest eligible interval is selected. |
| B5-050 | 156/142 | OPEN_EDIT | Explain where the DP model comes from and report the actual (a,H) values used. Separate these from the generalized-posterior prior on roots. |
| B5-051 | 156/142 | PARTIAL | Preserve the mathematical selection rule but explain its source and each tie-breaker in prose. Verify that “no eligible interval” is counted as failure in validation. |
| B5-052 | 157/143 | OPEN_EDIT | Identify exactly what calibration selects: a posterior-content cutoff by ((n,c,1-alpha)), with candidate grids, tilt rules, (omega_R), and DP hyperparameters fixed beforehand. |
| B5-053 | 157/143 | VERIFY_SCIENCE | Justify or source the 24,000 assessment samples, eight calibration distributions, and simultaneous one-sided exact binomial lower bound. State the multiplicity adjustment and Monte Carlo error budget explicitly. |
| B5-054 | 157/143 | OPEN_EDIT | Rewrite the two-stage follow-up in chronological order: initial development/assessment, two unresolved settings, prespecified refinement, fresh samples, retained earlier cutoffs, and combined error control. |
| B5-055 | 157/143 | OPEN_EDIT | Explain the DP Beta law's limited role in candidate eligibility and why neither it nor the population MTI theorems establishes a distribution-free tolerance theorem for the selected interval. |
| B5-056 | 158/144 | OPEN_EDIT | Move the shortest-path continuation derivatives to Appendix E unless a one-paragraph consequence is needed to justify the finite grid. The current derivation interrupts the tolerance procedure without affecting its implementation. |
| B5-057 | 159--160/145--146 | OPEN_EDIT | Define a design “cell” as a specified ((n,c,1-alpha)) setting and avoid “row” unless referring to a named table. Explain the full-range feasibility calculation before listing retained settings. |
| B5-058 | 159/145 | SATISFIED_CURRENT | Preserve Young--Mathew and Wilks as the classical comparators with verified references. If Bruno's note names an additional Tony et al. method, identify the exact paper/package before deciding whether it is scientifically comparable. |
| B5-059 | 160/146 | VERIFY_SCIENCE | Trace the sample-size feasibility formula to Wilks/order-statistic theory, derive or cite it, and explain how it limits the two classical comparators. |
| B5-060 | 160/146 | VERIFY_SCIENCE | Recompute or source-check the stated minimum sample sizes and excluded combinations, including the questioned (n=100,c=0.99) statement. Do not change the design from visual inspection alone. |
| B5-061 | 159--160/145--146 | OPEN_EDIT | Define “cell,” “row,” and “feasible” before use and state the complete retained set once, preferably in a compact table. |
| B5-062 | 160/146 | OPEN_EDIT | Explain that calibration concerns the complete interval-selection rule and content-attainment probability, not interval length alone. List all fixed hyperparameters and selection constants. |
| B5-063 | 160/146 | PARTIAL | Keep the primary metric as repeated-sampling content-attainment under known simulation (F), and explain how interval width is compared conditional on an interval being produced. |
| B5-064 | 155--160/141--146 | OPEN_EDIT | Consolidate all reported values—prior precision, learning rate, DP hyperparameters, candidate grids, cutoff menu, replications, error budget, and tie rules—in one reproducible design table or appendix record. |
| B5-065 | 137--160/123--146 | OPEN_EDIT | Complete a reader-path audit after the local fixes: definition, antecedent, contribution, target theorem, fixed-target computation, content check, calibration, independent validation, application, and limitations. Each paragraph must perform one of those functions without repeating an earlier explanation. |

## 6. Appendix E itemized plan

These items are not optional merely because the relevant text is in an
appendix. They support Chapter 5 claims and must use the same notation and
scope.

| ID | Review page | Status | Required resolution and acceptance check |
| --- | --- | --- | --- |
| BE-001 | 201/187 | OPEN_EDIT | Define the convex-order symbol (preceq_{\rm cx}) immediately before Proposition E.1 and state the required finite expectations. |
| BE-002 | 204/190 | OPEN_EDIT | Define an intercept-only endpoint fit before the fractional empirical-balance result and distinguish it from the conditional regression setup in the chapter. |
| BE-003 | 204/190 | OPEN_EDIT | Define the subdifferential (partial\rho_c(e_i)), the choice of (s_i), and the relation (q_i=c-s_i) before the theorem. |
| BE-004 | 204/190 | OPEN_EDIT | Explain that the (q_i) are fractional membership allocations: one inside, zero outside, and only fractional at fitted roots. Avoid introducing them as an unexplained “allocation.” |
| BE-005 | 205/191 | OPEN_EDIT | State the independent priors explicitly, for example (a,b\stackrel{\rm ind}{\sim}N(0,\lambda^{-1})), after verifying that this is the implemented parameterization. |
| BE-006 | 206/192 | OPEN_EDIT | Clarify that, for fixed (m), the minimizing squared half-width is an empirical (s/n) quantile of the observed squared distances ((y_i-m)^2). Distinguish the observations from a random variable. |
| BE-007 | 207/193 | OPEN_EDIT | Define the independent development samples, independent cutoff-assessment samples, and finite cutoff menu before reporting the calibration stages. |
| BE-008 | 207/193 | OPEN_EDIT | Define the simultaneous one-sided exact binomial lower bound, its coverage allocation over laws/settings/cutoffs, and the criterion for accepting a cutoff. |
| BE-009 | 207/193 | OPEN_EDIT | Write follow-up settings as ((n,c)=(50,0.90)) and ((100,0.95)), explicitly identifying both coordinates. |
| BE-010 | 207/193 | OPEN_EDIT | Explain why the total Monte Carlo error probability 0.05 is split across the two stages and how the union bound is applied. |
| BE-011 | 201, 204--207/187, 190--193 | OPEN_EDIT | Align every Chapter 5 proof pointer, theorem name, symbol, and study constant with Appendix E; the chapter should not restate proof algebra that the appendix already supplies. |

## 7. Coverage audit

| Review block | Annotated pages | Normalized items | Coverage |
| --- | ---: | ---: | --- |
| Chapter 4 through Section 4.4 | 10 | 40 | `B4-001`--`B4-040` |
| Chapter 5 main text | 21 | 65 | `B5-001`--`B5-065` |
| Appendix E | 5 | 11 | `BE-001`--`BE-011` |
| **Total** | **36** | **116** | Every non-link annotation object accounted for |

The annotation is handwritten. The normalized wording is therefore a
faithful paraphrase of the requested action, not a claim to reproduce every
handwritten word verbatim. Any ambiguous scientific question is classified as
`VERIFY_SCIENCE` or `DECISION`, not silently converted into a factual command.

## 8. Optimal implementation sequence

### WP-B0 — Freeze sources and construct a response matrix

1. Keep the annotated PDF and rendered inspection pages in ignored local
   storage. Record no private email text or handwriting images in Git.
2. Reconfirm the current Q--DESN and RQR/MTI authority commits, clean states,
   and source paths without modifying their working trees.
3. Add a working response column for each item: current source anchor,
   proposed edit, source evidence, disposition, validation, and commit.
4. Resolve every VERIFY_SCIENCE item before changing the related theorem,
   equation, numerical setting, prior, or citation.

Acceptance: the response matrix contains all 116 identifiers; each scientific
question has an exact source location or an explicit unresolved decision.

### WP-B1 — Rebuild Chapter 4 definitions through Section 4.4

Perform the Chapter 4 work in this order:

1. time-series, forecast-origin, horizon, and information-set notation;
2. contribution/antecedent compression and the Chapter 2 contrast;
3. DESN recursion, dimensions, spectral scaling, leak convention, and feature
   construction;
4. independent Q--DESN versus MQ--DESN target, parameter collection,
   difference blocks, composite likelihood, and priors;
5. conditional augmentation, MCMC transition, diagnostics, and VB role; and
6. recursive forecast construction and conditional-versus-predictive
   quantiles.

Do not edit Sections 4.5--4.8 merely to create a uniform voice. A change there
must be a direct consequence of the revised notation or a separately supplied
comment. After this work package, update Appendix D only where a main-text
definition requires its full technical form.

Acceptance: all B4 items are dispositioned; every displayed matrix product is
dimensionally valid; the chapter introduces each symbol before use; source
claims match the fixed authority; and the response record states that Bruno's
coverage ended at Section 4.4.

### WP-B2 — Reconstruct the Chapter 5 conceptual spine

Preserve the current contribution-led introduction, adding only the Chapter 4
transition and any needed evidence-order refinement. Then establish this
reader sequence:

1. tolerance interval and fixed-content interval class;
2. inherited residual-product criterion and newly identified MPI target;
3. MTI as a fixed-content placement family indexed by retained-mean tilt;
4. population score equations and global identification, with concise proof
   pointers;
5. generalized-Bayes fixed-target endpoint calculation;
6. separate DP response-distribution model and fixed-interval content law;
7. candidate selection and empirically calibrated tolerance action;
8. independent validation, application, and precise limits; and
9. proposed regression/dynamic extensions without inherited calibration
   claims.

This stage resolves definitions and contribution logic before computation or
numerical design is rewritten. It should remove redundant meta-exposition,
not expand the chapter.

Acceptance: a reader can answer, before reaching the validation section, what
is inherited, what is new, what is proved, what is model-based, what is
calibrated, and what remains empirical or proposed.

### WP-B3 — Relocate technical material and repair Appendix E

Move the following out of the main body unless a short consequence is needed:

- detailed generalized-posterior propriety arguments;
- profile-risk and escaping-root derivations;
- shortest-path continuation derivatives;
- subgradient allocation algebra;
- Gaussian-root profile derivation; and
- two-stage calibration bookkeeping and multiplicity calculations.

Appendix E must remain curated. A move is authorized only when it replaces an
existing main-text block or supplies a proof/definition Bruno explicitly
requested; it is not permission to restore previously removed supplement
material. Use stable cross-references from the chapter.

Acceptance: the main chapter contains the definitions, contribution, theorem
statements, method, study design, and principal evidence; Appendix E contains
the technical support needed to verify them without duplicating the chapter.

### WP-B4 — Clarify the fixed-target and calibration procedure

1. Define the generalized posterior, learning rate, Gaussian root prior, and
   exact endpoint summary used.
2. Define the DP prior, concentration, centering law, and Beta content
   probability for a fixed candidate interval.
3. Present the candidate grid and selection rule as a finite prespecified
   decision rule.
4. Define design settings \((n,c,1-\alpha)\), candidate fitted content \(q\),
   tilt \(\delta\), and eligibility cutoff \(\gamma\).
5. Explain development, cutoff assessment, follow-up refinement, and
   independent validation as separate random samples.
6. Verify all constants and feasibility calculations from the research
   records; add one compact design table if it reduces prose and repetition.
7. State clearly that calibration is for the complete selected-interval rule
   on the finite distributional panel, not a distribution-free theorem.

Acceptance: no term such as *cell*, *row*, *feasible*, *cutoff*, *learning
rate*, or *content probability* appears before definition; all numerical
settings are source-backed and reproducible.

### WP-B5 — Contribution, literature, and comparison audit

The contribution statement is defense-critical and must be checked after the
technical edits rather than treated as independent prose.

- Credit Pouplin et al. for the residual-product construction and any
  population-content result established there.
- State precisely which retained-mean characterization, MTI family,
  generalized-posterior calculation, calibrated selection rule, validation,
  and application results are contributed by this project.
- Introduce generalized-Bayes and tolerance-interval antecedents by
  methodological role, not as a citation list.
- Identify the exact method behind Bruno's possible “Tony et al.” comparator
  note before adding or excluding it. Availability of an R package alone does
  not establish comparability.
- Preserve collective attribution unless evidence allocates individual roles.

Acceptance: every contribution has an antecedent, a distinct new object or
result, and an evidence boundary; no novelty or role is inferred from a
repository name.

### WP-B6 — Academic-writing and anti-formulaic-prose gate

Every revised paragraph must follow the verified version 0.2 academic-writing
profile (SHA-256
b9483cf55e108f5615c203dfff6c0940b7ecc5c001aaad679507004b70352513):

1. name the statistical object rather than using generic nouns such as
   *framework*, *approach*, or *method* when a more exact term is available;
2. introduce notation before use and explain why each displayed equation is
   needed;
3. separate data, parameters, latent variables, fixed design quantities,
   priors, likelihood/composite loss, generalized posterior, approximation,
   model-based probability, and repeated-sampling evidence;
4. avoid engineering or machine-learning language unless it names an actual
   Q--DESN component; define such terms statistically;
5. replace promotional or formulaic prose with the assumption, metric,
   information set, comparison, or theorem boundary that supports the claim;
6. retain necessary qualifications next to the claims they limit; and
7. preserve the accurate assistance disclosure. “Anti-AI” means removal of
   generic, promotional, statistically empty prose, not concealment or an AI
   detector score.

Acceptance: a paragraph-by-paragraph review identifies one primary function
for each paragraph—motivate, define, distinguish, derive, specify, report,
interpret, or qualify—and the candidate performs the final scholarly read.

### WP-B7 — Validation and release

Validation is staged so that prose edits cannot hide scientific drift.

1. Before editing, record token sequences for numbers, citations, labels,
   inputs, graphics, and equation environments in the affected files.
2. After each chapter-sized commit, run focused structural/notation scans,
   python3 scripts/validate_manuscript_imports.py with the fixed audit roots,
   and the fast dissertation validator.
3. Build with bash scripts/build.sh from clean generated output while
   preserving the last accepted artifact.
4. Check undefined citations/references, duplicate labels, missing files,
   overfull boxes, fonts, page size, and all new cross-references.
5. Render and inspect every affected Chapter 4, Chapter 5, and Appendix E page,
   not only chapter openings.
6. Compare the item response matrix with the final diff. No item closes on
   prose intent alone; it needs source and compiled evidence.
7. Commit in bounded units: Chapter 4, Chapter 5 conceptual spine, Appendix E
   and computation/calibration, contribution/style reconciliation, and release
   evidence.
8. Fetch and recheck remote divergence before any merge. Merge/push only on
   explicit authorization; do not force-push. Overleaf pull and compilation
   remain a separate user action.

Acceptance: all 116 items are IMPLEMENTED, SATISFIED_CURRENT, or explicitly
deferred with a named reason; all validators pass; the final PDF is inspected;
and the Git history identifies the commit that resolves each item.

## 9. Risks and stop rules

| Risk | Control |
| --- | --- |
| Reverting improvements already made after the 221-page copy | Compare each item with current main; preserve every SATISFIED_CURRENT resolution. |
| Treating Bruno's partial Chapter 4 review as complete approval | Keep Sections 4.5--4.8 explicitly outside the received review scope. |
| Changing a theorem or numerical result from a handwritten question | Resolve VERIFY_SCIENCE from the fixed authority and computations first. |
| Making Chapter 5 longer while trying to clarify it | Relocate proof/computation detail to Appendix E and remove displaced main-text material. |
| Reintroducing a massive appendix | Add only claim-essential support; do not restore superseded supplement content. |
| Conflating ordinary Bayes, generalized Bayes, and the DP content posterior | Define all three targets separately and use distinct notation and prose. |
| Overstating tolerance performance | Tie every claim to the finite prespecified panel and independent validation design. |
| Adding an unsupported comparator | Identify the exact paper, estimand, implementation, and compatible design before inclusion. |
| Publishing private review material | Keep original PDFs and rendered annotations ignored; commit paraphrased action items only. |

Pause only the affected work package if a source result, proof, numerical
constant, or comparator cannot be verified. Continue independent items rather
than replacing missing evidence with a plausible reconstruction.

## 10. Definition of done

The Bruno revision is complete only when:

- all 36 annotated pages and 116 normalized items remain accounted for;
- every current-source resolution is preserved or intentionally superseded
  with documented evidence;
- Chapter 4's time-series, reservoir, composite-target, computation, and
  forecast notation is coherent through Section 4.4;
- Chapter 5 presents a linear definition-to-evidence argument and makes the
  inherited and new contributions unmistakable;
- generalized Bayes, the DP response model, and repeated-sampling tolerance
  calibration are distinct at first use and throughout;
- all theorem/proposition statements have the necessary notation, conditions,
  proof pointers, and exact scope;
- all study constants and feasibility statements are verified;
- Appendix E contains essential technical support without becoming a restored
  full supplement;
- all writing passes the statistical-style gate without promotional,
  engineering, internal-workflow, or formulaic language;
- the build, automated checks, and rendered-page review pass; and
- the response record states honestly that the received Chapter 4 review ends
  at Section 4.4.

## 11. Next action

This intake and planning pass does not authorize manuscript correction. If the
plan is approved, begin with WP-B0 and WP-B1 on the current released baseline.
Do not start by rewriting Chapter 5 globally: first freeze the response matrix
and resolve the scientific-verification items that control notation, theorems,
priors, calibration, and comparisons.
