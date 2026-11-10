# FINAL controlling plan for Bruno Sansó's revision and advisor integration

Status: **implementation complete and locally release-validated; not pushed or merged**

Version: 9 November 2026, final planning revision

This document is the controlling execution specification for the detailed
Bruno Sansó review that arrived after the first advisor-revision release. It
supersedes the provisional implementation sequence previously recorded in this
file while preserving its complete 116-item comment inventory. It supplements
`docs/advisor-revision-plan-20261109.md`; it does not replace Raquel Prado's
ledger or reopen revisions that remain correct. It compares Bruno's comments
with the current dissertation rather than the older review copy alone, resolves
the scientific questions that can be settled from the fixed research
authorities, and specifies the exact implementation, validation, and release
path for every remaining point.

This is a planning artifact. No chapter, appendix, bibliography, figure,
table, manifest, or compiled dissertation artifact is changed by this plan.

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
| Current accepted dissertation artifact | 183 US-Letter pages; SHA-256 `5cc16fe050e59b733e86d9d57051e0645cdce63b2320464cfe6a814e890e7599` |
| Current Q--DESN authority | `AntonioAPDL/Bayesian-Quantile-Regression-withDeep-Echo-State-Network-Features---Thesis`, `main` at `aa613b056b054edd9347eeb4739bd4bce0c92818` |
| Current MTI foundation authority | `AntonioAPDL/RQR-GIBBS`, `main` at `4223c6a3a44f376255bacdca91db71cdf4f3afde` |
| Current MTI extensions authority | `AntonioAPDL/MTI-EXTENSIONS`, `main` at `f345d946aa5a81b94795838bec58d874a0fdd0c9` |
| Remote-tip check | all three research authority tips and thesis `origin/main` matched the recorded commits on 9 November 2026; no scientific source refresh is required for this revision |
| Binding writing profile | version 0.2, SHA-256 `b9483cf55e108f5615c203dfff6c0940b7ecc5c001aaad679507004b70352513` |
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

### 2.1 Measured current state

The current dissertation is already much shorter and more coherent than the
221-page copy Bruno annotated. The implementation must therefore work from
current `main`, not reconstruct the reviewed copy.

| Unit | Current size | Planning consequence |
| --- | ---: | --- |
| Chapter 4 | 944 lines; 5,477 words | Edit the 2,099-word opening-through-forecast block first; later evidence sections change only when notation or cross-references require it. |
| Appendix D | 336 lines; 1,567 words | The model/computation block through line 183 contains about 706 words; add only definitions or derivations required to keep Chapter 4 readable. |
| Chapter 5 | 954 lines; 5,821 words | The opening-through-validation block contains about 4,400 words and is the principal narrative target. Added definitions must be offset by removal of meta-exposition, repeated caveats, or displaced algebra. |
| Appendix E | 357 lines; 1,466 words | The appendix is already a compressed derivative of a much longer supplement. Preserve its proof graph and allow only bounded additions needed by the comments. |
| Current PDF | 183 pages | Page growth is not a measure of quality; unexplained growth is a review failure and must be justified in the response matrix. |

Two public records require reconciliation during implementation even if their
scientific content is unaffected. The top-level state note in
`source-manifest.json` still says that Bruno's detailed annotation is
unavailable, and `source-manifest.local.json` contains older temporary audit
paths rather than the clean fixed-source clones used for this final planning
audit. These are documentation defects, not manuscript defects. Correct them
in the preflight commit without changing any source authority.

### 2.2 Scientific questions resolved during the final audit

The provisional plan correctly refused to infer mathematical or numerical
answers from handwriting. The fixed authorities now resolve every such item
except the identity and comparability of the possible additional comparator.

| Question | Fixed evidence | Binding planning resolution |
| --- | --- | --- |
| Bonas terminology (`B4-012`) | Q--DESN `main.tex`, lines 180--182 at `aa613b0...`, uses *penalized quantile sheets*. | Preserve the source term with its citation; clarify its role if needed but do not rename it from memory. |
| Recurrent-matrix scaling (`B4-016`) | Q--DESN `main.tex`, lines 277--281. | State \(\bar W_d=\rho_d W_d/\rho(W_d)\), conditional on nonzero raw spectral radius, and define \(\rho(W)\). |
| Leak convention (`B4-019`) | Q--DESN `main.tex`, lines 291--312. | The recursion weights the old state by \(1-\alpha_d\); smaller \(\alpha_d\) retains more of it. Preserve this convention. |
| Collapsed scale--shape transition (`B4-033`) | Q--DESN supplement, lines 246--278. | Integrate scale from the shape transition, sample shape from the collapsed density, and immediately redraw scale from its GIG conditional before another block. Describe this as a target-preserving partially collapsed transition, not a generic “update.” |
| Deterministic MTI endpoint summary (`B5-042`--`B5-043`) | RQR `main.tex`, lines 662--684, and the convex profile in the supplement. | Report the endpoints as the minimizer of penalized cumulative loss, equivalently the mode of the stated loss-based generalized posterior under the fixed Gaussian root prior. Do not call them posterior means or ordinary-likelihood MAP estimates. |
| Direct DP content law (`B5-045`--`B5-050`) | RQR supplement, lines 1147--1186. | Use \(F\sim\mathrm{DP}(a,H)\), with reported \(a=1\) and \(H=N(0,4^2)\), and the exact fixed-interval Beta law. Keep it separate from the root prior and generalized posterior. |
| Calibration budget (`B5-053`--`B5-054`) | RQR supplement, lines 1242--1267. | Record 32 development samples, 24,000 independent assessments per distribution, 26 initial cutoffs, 105 follow-up cutoffs for each unresolved setting, and the two-part union-bound allocation of total Monte Carlo error 0.05. |
| Full-range feasibility (`B5-059`--`B5-060`) | RQR supplement, lines 1357--1397. | Use \(1-n(1-c)c^{n-1}-c^n\); an independent calculation reproduces minimum \(n=(46,93,473)\) at confidence 0.95 for \(c=(0.90,0.95,0.99)\). Thus \((100,0.99)\) is excluded and the \(c=0.99\) study begins at \(n=500\). |
| Additional comparator (`B5-058`) | The handwriting may read “Tony et al.”; neither the fixed RQR manuscript nor its supplement establishes a matching method. | Do not add a comparator or citation. Identify an exact paper, estimand, implementation, and compatible design only if Bruno or the candidate clarifies the note. This does not block the other work. |

The public remote tips still equal the fixed commits above. A latest-version
refresh would add risk without adding evidence and is therefore outside this
revision. If any tip changes before implementation, record the new tip but
continue from the fixed authority unless the candidate explicitly authorizes a
scientific source refresh.

### 2.3 Audit of the provisional plan

The provisional plan had four important strengths: complete annotation
coverage, preservation of already-correct current prose, a firm boundary at
Chapter 4 Section 4.4, and a correct separation between generalized Bayes, the
DP response model, and repeated-sampling tolerance evidence. These controls
remain binding.

The final audit identified six gaps and resolves them here:

1. Several `VERIFY_SCIENCE` items were left open even though the fixed
   authorities contain exact answers. Section 2.2 freezes those answers.
2. The provisional work packages did not identify all downstream dissertation
   files. Section 8 now gives a file-and-label dependency map for Chapter 1,
   the abstract, synthesis, notation, provenance, and validation records.
3. It did not impose a compactness control. The measured baseline in Section
   2.1 and the change budgets in Section 8 prevent clarification from restoring
   the old chapter or appendix length.
4. It proposed a response matrix but did not define its schema. WP-B0 now
   requires one row for every item, with source, destination, rationale,
   evidence, validation, and commit fields.
5. It grouped Chapter 5 conceptually but did not make theorem, computation,
   content-model, calibration, and validation dependencies transactional. The
   revised sequence does so and requires a build after each bounded unit.
6. It did not explicitly address stale public/local source-state records. The
   preflight package now corrects those records before prose editing.

### 2.4 Alternatives considered and final decision

| Alternative | Assessment | Decision |
| --- | --- | --- |
| Apply Bruno's markings directly to the 221-page PDF text | Would discard the stronger 183-page rewrite and could restore deleted repetition. | Reject. Use each mark as evidence, then resolve it against current source. |
| Replace Chapters 4 and 5 wholesale with current article files | Would reintroduce journal roadmaps, online-supplement language, duplicated material, and a source organization not optimized for a dissertation. | Reject. Use the articles as scientific authorities, not drop-in chapters. |
| Globally rewrite both chapters for uniform voice | Creates unnecessary scientific drift and erases project-specific prose that is already sound. | Reject. Use bounded structural and paragraph edits. |
| Expand Chapter 5 until every technical question is answered in the body | Conflicts with the advisors' readability request and the compact appendix decision. | Reject. Keep definitions, theorem statements, method, and principal evidence in the body; put verification algebra in Appendix E. |
| Remove Chapter 5 from the working thesis immediately | Bruno offered this as a schedule contingency, not a judgment that the project lacks merit. The complete current thesis already contains a substantially improved chapter. | Do not remove by default. Retain and revise it; create an omission-ready release only if the advisors later request one explicitly. |
| Source-pinned staged revision with response-matrix control | Preserves current improvements, resolves comments against exact evidence, limits scientific drift, and yields reviewable commits. | **Adopt.** |

The final design therefore uses one governing rule: **change only what a
comment, a direct consistency dependency, or fixed scientific evidence
requires, and verify each change before widening the scope.**

## 3. Status vocabulary

- `SATISFIED_CURRENT`: current `main` already meets the comment's intent; the
  implementation pass verifies and preserves it.
- `PARTIAL`: current `main` improves the reviewed text but does not fully
  resolve the comment.
- `OPEN_EDIT`: a bounded source or structural edit is needed.
- `SOURCE_RESOLVED_EDIT`: the fixed authority settles the scientific question,
  but the corresponding dissertation edit has not been made.
- `CONTROL_GATE`: no local prose change is implied; the item remains a required
  source, scope, or validation check.
- `EXTERNAL_DECISION`: only an identified advisor/candidate choice can settle
  the point; it must not be guessed.
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
| B4-012 | 111/97 | SATISFIED_CURRENT | The exact authority uses “penalized quantile sheets,” and current `main` reproduces that term with the Bonas et al. citation. Preserve it; add only a concise role description if the surrounding comparison still needs clarification. |
| B4-013 | 112/98 | OPEN_EDIT | Move study-specific simulation and application descriptions to the evidence roadmap or Section 4.5. The introduction should state questions and contributions without narrating results before their design is introduced. |
| B4-014 | 113/99 | OPEN_EDIT | At the model opening, call (Y_t) the time series or stochastic process of interest and distinguish it from observed values (y_t). |
| B4-015 | 113/99 | PARTIAL | Define (mathbf z_t) as the vector of exogenous covariates, not merely variables, and state whether its components are contemporaneously available at fitting/forecast time. |
| B4-016 | 113/99 | SOURCE_RESOLVED_EDIT | Add the authority's exact scaling \(\bar W_d=\rho_d W_d/\rho(W_d)\), conditional on nonzero raw radius, and define \(\rho(W)\) as the largest absolute eigenvalue. |
| B4-017 | 113--114/99--100 | OPEN_EDIT | State dimensions for (mathbf W_d), (mathbf W_d^{\rm in}), (mathbf Q_{d-1}), the reduced state, and the bias; verify every matrix product in the recursion. |
| B4-018 | 113/99 | OPEN_EDIT | Define the feature transformation (k) as a function, give its domain/codomain, and identify the transformations actually used. Do not leave “chosen feature transformation” uninterpreted. |
| B4-019 | 114/100 | SATISFIED_CURRENT | Current `main` and the authority agree: the previous state has weight \(1-\alpha_d\), so a smaller leak rate retains more of it. Preserve this statement and verify it after any recursion edit. |
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
| B4-033 | 117/103 | SOURCE_RESOLVED_EDIT | State the verified partially collapsed transition: integrate scale out of the shape step, sample shape from the collapsed density, and immediately redraw scale from its GIG conditional before another block. Cross-reference the exact Appendix D kernel. |
| B4-034 | 117/103 | PARTIAL | Retain and sharpen the diagnostic statement: identify rank-normalized (widehat R), effective sample size, chain comparisons, and crossing diagnostics as checks, not guarantees. |
| B4-035 | 117/103 | PARTIAL | Motivate VB by repeated fitting over long series, forecast origins, or reservoir specifications. State the computational task reduced, not merely that fitting is “fast.” |
| B4-036 | 117/103 | OPEN_EDIT | Define whether VB supplies an approximation, initialization, or reported inference in each study; do not imply uncertainty quality without evidence. |
| B4-037 | 118/104 | OPEN_EDIT | Define forecast origin (o), fitting endpoint (T), horizon (h), and target (Y_{o+h}) in one place; then use that indexing throughout. |
| B4-038 | 118/104 | SATISFIED_CURRENT | Preserve the distinction between a draw-specific conditional-quantile location and the marginal posterior predictive quantile. |
| B4-039 | 118/104 | PARTIAL | Explain how observed history initializes reservoir states and how simulated future responses enter later lags in a recursive forecast. Verify information availability for covariates. |
| B4-040 | 109--118/95--104 | CONTROL_GATE | Recheck every revised definition, equation, and contribution against Q--DESN commit `aa613b0...`. The remote tip currently matches; no comment authorizes a source-version change. |

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
| B5-021 | 142/128 | SATISFIED_CURRENT | Current lines 144--149 explain the two endpoint-distance factors and distinguish inside weight \(1-c\) from miss weight \(c\). Preserve this explanation while making the adjacent transition less tutorial-like. |
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
| B5-043 | 155/141 | SOURCE_RESOLVED_EDIT | The deterministic profile minimizes cumulative MTI loss plus the independent Gaussian-root quadratic penalty, equivalently giving the mode of the stated loss-based generalized posterior. State this relationship once; do not call the result a posterior mean or an ordinary-likelihood MAP estimate. |
| B5-044 | 155/141 | OPEN_EDIT | Mark (omega_R=1), (lambda=10^{-4}), the prior means, and the objective tolerance as choices of the reported validation study, not universal method defaults. |
| B5-045 | 155--156/141--142 | OPEN_EDIT | Before the content check, define the Dirichlet-process prior (F\sim\mathrm{DP}(aH)), its concentration (a), centering distribution (H), and why a response-distribution model is separate from the loss-based endpoint target. |
| B5-046 | 155--157/141--143 | PARTIAL | State the exact Beta law for (F(I)\mid D_n) for a fixed interval and explain why applying it to data-dependent candidate intervals is a selection device whose tolerance behavior is calibrated empirically. |
| B5-047 | 155--156/141--142 | OPEN_EDIT | Rewrite the tolerance target after defining the random interval (widehat T_n=[L_n,U_n]), the true distribution (F), and (C_F([L,U])=F(U)-F(L)). |
| B5-048 | 156/142 | SOURCE_RESOLVED_EDIT | Replace the flat “six quantities” list with a role hierarchy: the tolerance requirement is \((c,1-\alpha)\); candidate targets are \((q,\delta)\); \(\omega_R\) is the fixed loss scale; and \(\gamma\) is the calibrated eligibility cutoff. Do not force a misleading count when the distinction among roles is the point. |
| B5-049 | 156/142 | SATISFIED_CURRENT | Current `main` already states the four-stage order: construct candidates, fit endpoints, compute DP content probabilities, and select the shortest eligible interval. Preserve it and add only the missing source/tie-rule details. |
| B5-050 | 156/142 | OPEN_EDIT | Explain where the DP model comes from and report the actual (a,H) values used. Separate these from the generalized-posterior prior on roots. |
| B5-051 | 156/142 | PARTIAL | Preserve the mathematical selection rule but explain its source and each tie-breaker in prose. Verify that “no eligible interval” is counted as failure in validation. |
| B5-052 | 157/143 | OPEN_EDIT | Identify exactly what calibration selects: a posterior-content cutoff by ((n,c,1-alpha)), with candidate grids, tilt rules, (omega_R), and DP hyperparameters fixed beforehand. |
| B5-053 | 157/143 | SOURCE_RESOLVED_EDIT | Use the fixed calibration record: 32 development samples, 24,000 fresh assessments per distribution, eight laws, 26 initial cutoffs, and the stated one-sided exact-binomial multiplicity allocation. Keep full bookkeeping in Appendix E and a concise consequence in the chapter. |
| B5-054 | 157/143 | OPEN_EDIT | Rewrite the two-stage follow-up in chronological order: initial development/assessment, two unresolved settings, prespecified refinement, fresh samples, retained earlier cutoffs, and combined error control. |
| B5-055 | 157/143 | SATISFIED_CURRENT | Current lines 587--596 distinguish the DP model-based law, population MTI theory, and empirical tolerance validation. Preserve this boundary and make it consistent with the expanded DP definition. |
| B5-056 | 158/144 | SATISFIED_CURRENT | The current 183-page release already removes the shortest-path continuation derivatives from Chapter 5. Do not restore them from the article or reviewed copy; retain only the finite-grid consequence if needed. |
| B5-057 | 159--160/145--146 | OPEN_EDIT | Define a design “cell” as a specified ((n,c,1-alpha)) setting and avoid “row” unless referring to a named table. Explain the full-range feasibility calculation before listing retained settings. |
| B5-058 | 159/145 | SATISFIED_CURRENT | Preserve Young--Mathew and Wilks as the classical comparators with verified references. If Bruno's note names an additional Tony et al. method, identify the exact paper/package before deciding whether it is scientifically comparable. |
| B5-059 | 160/146 | SOURCE_RESOLVED_EDIT | Retain the verified full-range formula \(1-n(1-c)c^{n-1}-c^n\), connect it to two-sided order-statistic tolerance feasibility, and explain that it constrains the classical sample-bounded comparators rather than proving an MTI boundary. |
| B5-060 | 160/146 | SATISFIED_CURRENT | The authority and an independent calculation agree on minimum sample sizes 46, 93, and 473 at 0.95 confidence for contents 0.90, 0.95, and 0.99. Preserve exclusion of \((100,0.99)\) and the first \(c=0.99\) design at \(n=500\). |
| B5-061 | 159--160/145--146 | OPEN_EDIT | Define “cell,” “row,” and “feasible” before use and state the complete retained set once, preferably in a compact table. |
| B5-062 | 160/146 | OPEN_EDIT | Explain that calibration concerns the complete interval-selection rule and content-attainment probability, not interval length alone. List all fixed hyperparameters and selection constants. |
| B5-063 | 160/146 | SATISFIED_CURRENT | Current lines 654--666 identify content attainment under known simulation \(F\) as primary, count nonproduction as nonattainment, and define within-distribution width comparisons. Preserve these choices and terminology. |
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

The final current-state classification is:

| Block | Satisfied current | Partial | Open edit | Source-resolved edit | Control gate | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Chapter 4 | 10 | 7 | 20 | 2 | 1 | 40 |
| Chapter 5 | 22 | 6 | 33 | 4 | 0 | 65 |
| Appendix E | 0 | 0 | 11 | 0 | 0 | 11 |
| **Total** | **32** | **13** | **64** | **6** | **1** | **116** |

`SATISFIED_CURRENT` does not mean “ignore.” Those 32 items are preservation
tests against regression. `SOURCE_RESOLVED_EDIT` means the scientific decision
is settled but the dissertation edit is still open. The remaining 64 open and
13 partial items define the substantive implementation workload.

The annotation is handwritten. The normalized wording is therefore a
faithful paraphrase of the requested action, not a claim to reproduce every
handwritten word verbatim. Source-resolvable questions are settled in Section
2.2; the unidentified comparator remains an `EXTERNAL_DECISION` rather than
being silently converted into a factual command.

## 8. Exact implementation targets and controls

### 8.1 File and dependency map

“Review” below means that the file must be checked and recorded as changed or
unaffected. It does not authorize unrelated rewriting.

| Revision object | Primary destination | Direct dependencies and required outcome |
| --- | --- | --- |
| Chapter 4 forecast object and notation | `chapters/04-research-c.tex`, labels `qdesn2026:sec:intro`, `qdesn2026:sec:model`, and `qdesn2026:sec:forecast` | One convention for stochastic response, observation, fitting endpoint, forecast origin, horizon, information set, covariate availability, and recursive path. |
| Chapter 4 reservoir construction | `qdesn2026:subsec:desn-features` | Exact spectral scaling, leak convention, matrix dimensions, input lags, feature transformation, direct-input choice, and separation of fixed draws, tuned settings, and inferred parameters. |
| Chapter 4 multiquantile target | `qdesn2026:subsec:joint-qdesn` | Independent fits introduced first; complete parameter blocks; composite likelihood and normalized composite/generalized posterior described accurately; anchor/difference priors and intercept ordering separated. |
| Chapter 4 computation | `qdesn2026:sec:inference`; `appendices/d-qdesn-technical.tex`, labels `app:qdesn-posterior` and `app:qdesn-computation` | Latent supports and Gaussian variance defined; full conditionals distinguished from numerical transitions; collapsed shape transition and VB role stated exactly. |
| Chapter 4 later evidence | `qdesn2026:sec:simulation` through `qdesn2026:sec:discussion` | No discretionary rewrite. Change only notation, definitions, or cross-references propagated from Sections 4.1--4.4. Preserve the statement that Bruno did not review these sections. |
| Chapter 5 introduction and targets | `chapters/05-research-d.tex`, labels `rqr2026:sec:introduction`, `rqr2026:sec:interval-functionals`, and `rqr2026:sec:mpi-loss` | Preserve the contribution-led opening; add the Chapter 4 transition; remove meta/tutorial wording; define conditional objects and endpoint class before results. |
| Chapter 5 theory | labels `rqr2026:prop:population-characterization`, `rqr2026:thm:quantile-window`, `rqr2026:prop:mean-tilt`, and `rqr2026:thm:profiled-mean-tilt` | Conditions, inherited/new distinction, stable score-equation labels, theorem scope, and exact Appendix E proof pointers. |
| Chapter 5 computation and content model | `rqr2026:sec:static-theory-statements`; `app:mti-profile-computation` | Generalized posterior, learning rate, Gaussian root prior, deterministic endpoint summary, DP response model, fixed-interval Beta law, and their non-equivalence. |
| Chapter 5 tolerance rule and validation | `rqr2026:sec:mti-tolerance`, `rqr2026:sec:evaluation`; `app:mti-calibration` | Role hierarchy for \((c,1-\alpha,q,\delta,\omega_R,\gamma)\), candidate rule, tie/nonproduction rule, calibration chronology, multiplicity allocation, feasible settings, comparators, primary metric, and limitations. |
| Chapter 5 application and proposed extensions | `rqr2026:sec:pharma-application`, `mti:sec:extensions`, `rqr2026:sec:discussion` | Review only for terminology, target/evidence consistency, and cross-references; do not imply implementation or tolerance calibration for proposed extensions. |
| Appendix E proof graph | `appendices/e-mti-technical.tex`, labels `app:mti-proofs`, `app:mti-profile-computation`, `app:mti-calibration`, and `app:mti-extensions` | Define notation before each supporting result, retain one authoritative theorem statement, keep proof algebra out of the chapter, and avoid restoring deactivated supplement material. |
| Thesis-wide contribution framing | `chapters/01-introduction.tex`, `frontmatter/abstract.tex`, `chapters/06-synthesis.tex` | Reconcile only changed contribution, target, computation, and evidence language after Chapters 4--5 stabilize. Preserve correct results and chapter order. |
| Attribution and assistance statement | `frontmatter/acknowledgments.tex`, `docs/ASSISTANCE-LOG.md` | Verify consistency; change only if a contribution/assistance statement becomes factually incomplete. Do not weaken or conceal the approved disclosure. |
| Notation and bibliography | `notation.tex`, `references.bib`, `docs/bibliography-map.json` | Add or alter only genuinely recurring notation or verified references. The ambiguous comparator creates no bibliography entry without identification. |
| Public provenance and state | `source-manifest.json`, `docs/imports/ch04-qdesn.json`, `docs/imports/ch05-mti.json`, `docs/claim-evidence.json`, `docs/revision-ledger.json`, `docs/display-ledger.json`, `docs/appendix-essentiality-map.json` | Remove the stale “annotation unavailable” state, preserve fixed commits, and update only records affected by actual manuscript changes. |
| Private machine state | ignored `source-manifest.local.json`, `audit-inputs/` | Record fixed audit-clone paths and review hashes without publishing paths, email, or handwriting. |
| Project handoff | `docs/advisor-comments-ledger-20261109.md`, `docs/STATUS.md`, `docs/VALIDATION.md`, this plan | Record item dispositions, commits, checks, artifact identity, and the honest Section 4.4 review boundary. |

### 8.2 Scientific and editorial invariants

The following remain unchanged unless a fixed source proves a current statement
wrong and the response matrix records the correction:

- all reported numerical results, sample definitions, forecast horizons,
  simulation distributions, replications, metrics, and application outcomes;
- all theorem claims and assumptions outside the exact item being repaired;
- all citation keys, labels, file inputs, and active assets not required by the
  correction;
- the author-designated source commits and the historical/source-lineage
  boundary;
- collective attribution where the source records do not allocate individual
  tasks; and
- the distinction among a likelihood or composite likelihood, a loss-based
  generalized posterior, a response-distribution posterior, a variational
  approximation, and repeated-sampling evidence.

No new simulation, fit, proof claim, data transformation, figure, or result is
needed to implement Bruno's comments. If an edit appears to require one, stop
that item and determine whether the existing source already answers the
question. The revision is editorial and expository except for correcting a
verified mathematical statement.

### 8.3 Compactness and appendix controls

The current size is the reference, not a quota to fill.

- The 2,099-word affected Chapter 4 block should remain approximately
  size-neutral. Growth beyond five percent requires an item-level explanation
  and corresponding removal of redundant introduction or study-specific prose.
- The 4,400-word Chapter 5 opening-through-validation block should be no longer
  after revision. Added definitions and proof pointers should be offset by
  removing meta-exposition, repeated qualifications, or displaced derivations.
- Appendix E should normally remain at or below about 1,800 words. Exceeding
  that planning target requires a claim-essential proof or calibration record
  that cannot be expressed through a stable cross-reference.
- Do not add a new figure. At most one compact design/parameter table may be
  added if it replaces more prose than it introduces and does not duplicate the
  existing calibrated-policy table.
- Do not restore the shortest-path continuation derivation, distribution-level
  validation tables, deactivated application diagnostics, or other removed
  supplement material merely because it remains in the article repository.

These controls are review triggers, not permission to omit assumptions or
proof support. Scientific completeness takes precedence, but every exception
must be explicit.

### 8.4 Response-matrix contract

Before manuscript editing, create a machine-readable or tabular response
record with exactly one row for each `B4-*`, `B5-*`, and `BE-*` identifier.
Each row must contain:

1. advisor-review page and paraphrased issue;
2. current thesis file, stable label, and pre-edit line anchor;
3. fixed source ID, commit, file, and locator, or `not source-dependent`;
4. disposition: preserve, edit, move, clarify, verify-only, defer, or
   out-of-scope;
5. proposed reader-facing resolution and why it is preferable to the rejected
   alternatives;
6. changed files and cross-chapter dependencies;
7. focused validation and rendered-page check;
8. final status and commit; and
9. any unresolved advisor/candidate decision.

An item cannot close merely because its source article is clearer. The thesis
source and compiled result must contain and validate the resolution.

## 9. Final implementation sequence

### WP-B0 — Freeze sources and construct a response matrix

1. Begin from a clean branch created from the then-current `origin/main` after
   checking divergence. Do not assume that the planning branch or an open
   Overleaf session contains later work.
2. Keep the annotated PDF and rendered inspection pages in ignored local
   storage. Record no private email text or handwriting images in Git.
3. Recreate clean, disposable audit clones at `aa613b0...`, `4223c6a...`, and
   `f345d94...` with `scripts/prepare_research_audit_clones.sh`; do not fetch,
   checkout, reset, clean, build, or edit original research working trees.
4. Record the actual clone paths only in ignored `source-manifest.local.json`.
   Correct the stale public statement that Bruno's annotation is unavailable,
   while preserving the fixed authority commits.
5. Create the response matrix defined in Section 8.4 with all 116 identifiers
   and preload the source resolutions from Section 2.2.
6. Freeze pre-edit sequences for numbers, citations, labels, `\input` and
   `\includegraphics` paths, equation environments, active displays, and file
   hashes in every affected source.
7. Record the 183-page accepted artifact and its hash as the comparison
   baseline; preserve it before any clean build.

Acceptance: the implementation branch has a known parent; the three authority
commits are immutable and independently readable; the private/public path
boundary is correct; the response matrix contains exactly 116 unique IDs; and
every source-resolvable question has an exact commit/file/locator.

### WP-B1 — Repair Chapter 4 definitions through Section 4.4

Perform the Chapter 4 work in this order:

1. time-series, forecast-origin, horizon, and information-set notation;
2. contribution/antecedent compression and the Chapter 2 contrast;
3. DESN recursion, dimensions, spectral scaling, leak convention, and feature
   construction, including the authority's covariate-lag and direct-input
   distinction;
4. independent Q--DESN versus MQ--DESN target, parameter collection,
   difference blocks, composite likelihood, and priors;
5. conditional augmentation, MCMC transition, diagnostics, and VB role; and
6. recursive forecast construction and conditional-versus-predictive
   quantiles.

Implement these as five local transactions—notation/introduction, reservoir,
multiquantile model, computation, and forecast construction. After each
transaction, check symbol first use, matrix dimensions, citation/label tokens,
and current-source agreement before continuing. Preserve the current direct
contribution paragraph and source-verified Bonas terminology.

Do not edit Sections 4.5--4.8 merely to create a uniform voice. A change there
must be a direct consequence of the revised notation or a separately supplied
comment. After this work package, update Appendix D only where a main-text
definition requires its full technical form.

Acceptance: all `B4-001`--`B4-040` items are dispositioned; every displayed
matrix product is dimensionally valid; the raw/scaled recurrent matrices and
all fixed/tuned/inferred quantities are distinct; the forecast indices work for
the first and later horizons; source claims match `aa613b0...`; a focused build
passes; and the response record states that Bruno's coverage ended at Section
4.4. Commit this package before Chapter 5 work.

### WP-B2 — Reconstruct the Chapter 5 conceptual spine

Before editing prose, make a paragraph-function map of current Chapter 5 using
the permitted functions motivate, define, distinguish, derive, specify,
report, interpret, qualify, and connect. Mark repetition and every paragraph
that interprets an object not yet defined. Preserve the current
contribution-led introduction, adding only the Chapter 4 transition and any
needed evidence-order refinement. Then establish this reader sequence:

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
numerical design is rewritten. Delete the meta opening of Section 5.3,
tutorial transitions such as “Now define,” repeated future qualifications, and
any result preview that precedes its design. Do not copy the article roadmap or
restore article-only derivations. Preserve the evidence-boundary paragraph and
the three-part contribution statement unless a source-backed correction is
needed.

Acceptance: a reader can answer, before reaching the validation section, what
is inherited, what is new, what is proved, what is model-based, what is
calibrated, and what remains empirical or proposed. Every paragraph has one
primary function, all objects are defined before interpretation, and the main
body has not grown.

### WP-B3 — Relocate technical material and repair Appendix E

Resolve the theorem/proof graph and Appendix E together. Move or keep the
following outside the main body unless a short consequence is needed:

- detailed generalized-posterior propriety arguments;
- profile-risk and escaping-root derivations;
- shortest-path continuation derivatives, which are already absent from the
  current chapter and must not be restored;
- subgradient allocation algebra;
- Gaussian-root profile derivation; and
- two-stage calibration bookkeeping and multiplicity calculations.

For the main text, define \(X\), \(x\), \(F_x\), \(Q_x\), \(\mu_x\), the
endpoint class, the population risk, and the relevant conditions before the
first proposition. Give stable labels to the content and retained-mean score
equations. For each proposition/theorem, state whether it concerns stationary
points or global minimizers and place an immediate proof pointer.

For Appendix E, define convex order before Proposition E.1; define the
intercept-only problem, subdifferential, subgradient choice, and fractional
allocations before the empirical-balance theorem; and state the independent
Gaussian root prior before the convex profile. Use one authoritative formal
statement: main results stay in Chapter 5, while Appendix E headings identify
their proofs. Supporting lemmas may retain statements in the appendix.

Appendix E must remain curated. A move is authorized only when it replaces an
existing main-text block or supplies a proof/definition Bruno explicitly
requested; it is not permission to restore previously removed supplement
material. Use stable cross-references from the chapter.

Acceptance: `B5-018`--`B5-038` and `BE-001`--`BE-006` have evidence-backed
dispositions; theorem assumptions and proof pointers are complete; the main
chapter contains definitions, contribution, theorem statements, method, study
design, and principal evidence; Appendix E supplies verification without
duplicating the chapter; no deactivated supplement unit returns; and the
Appendix E compactness trigger in Section 8.3 is respected.

### WP-B4 — Clarify the fixed-target and calibration procedure

1. Define the generalized posterior, learning rate, Gaussian root prior, and
   exact endpoint summary used. State that the reported deterministic profile
   minimizes penalized loss and is the generalized-posterior mode under that
   specification.
2. Define the DP prior, concentration, centering law, and Beta content
   probability for a fixed candidate interval, using \(a=1\) and
   \(H=N(0,4^2)\) for the reported study.
3. Present the candidate grid and selection rule as a finite prespecified
   decision rule, including tie breaking and nonproduction.
4. Organize the quantities by role: tolerance requirement \((c,1-\alpha)\),
   candidate target \((q,\delta)\), fixed loss scale \(\omega_R\), and
   calibrated eligibility cutoff \(\gamma\).
5. Explain development, cutoff assessment, follow-up refinement, and
   independent validation as separate random samples.
6. Use the verified calibration budget and union-bound allocation in Section
   2.2; explain why the follow-up preserves the seven earlier cutoffs.
7. Derive or cite the verified full-range order-statistic probability and list
   the nine retained \((n,c)\) settings once. State that the resulting boundary
   constrains the classical sample-bounded comparators, not MTI.
8. Add one compact design table only if it replaces scattered prose and can
   include priors, learning rate, DP hyperparameters, candidate rule,
   calibration budget, validation replications, and tie/nonproduction rules
   without duplicating the policy table.
9. State clearly that calibration is for the complete selected-interval rule
   on the finite distributional panel, not a distribution-free theorem.

Acceptance: no term such as *cell*, *row*, *feasible*, *cutoff*, *learning
rate*, or *content probability* appears before definition; all numerical
settings are source-backed and reproducible; `B5-039`--`B5-065` and
`BE-007`--`BE-011` are dispositioned; the primary metric remains
content-attainment under known simulation \(F\); and the calibration, DP model,
and population theorems are not conflated.

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
- Leave Bruno's possible “Tony et al.” comparator out unless the exact source
  is identified. Availability of an R package alone does not establish
  comparability.
- Preserve collective attribution unless evidence allocates individual roles.

After the chapter statements stabilize, reconcile their exact content in
Chapter 1, the abstract, and Chapter 6. This is a consistency pass, not a new
global rewrite. Check acknowledgments for factual agreement, but do not repeat
full contribution statements there. Check every numerical summary in the
abstract and synthesis against the unchanged chapter evidence.

Acceptance: every contribution has an antecedent, a distinct new object or
result, and an evidence boundary; no novelty or role is inferred from a
repository name; Chapter 1, the abstract, Chapter 6, and acknowledgments do not
contradict the revised chapters; and the ambiguous comparator is recorded as
unresolved rather than silently added or ignored.

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
interpret, qualify, or connect. Also perform the following contextual scans,
then adjudicate every hit manually: promotional modifiers; stock transitions;
generic *framework/approach/pipeline/architecture* nouns; engineering or
machine-learning claims; internal workflow language; self-referential
paper-about-paper openings; repeated caveats; and unsupported
*demonstrates/outperforms/robust/scalable* language. Automated authorship or
“AI detector” scores are not evidence. The candidate performs the final
scholarly read.

### WP-B7 — Validation and release

Validation is staged so that prose edits cannot hide scientific drift.

1. Before editing, record token sequences for numbers, citations, labels,
   inputs, graphics, and equation environments in the affected files.
2. After each bounded commit, run focused structural/notation scans,
   `python3 scripts/validate_manuscript_imports.py --audit-root AUDIT_ROOT`,
   and `bash scripts/validate.sh --tier fast --audit-root AUDIT_ROOT`.
3. Build with bash scripts/build.sh from clean generated output while
   preserving the last accepted artifact.
4. Check undefined citations/references, duplicate labels, missing files,
   overfull boxes, fonts, page size, and all new cross-references.
5. Render and inspect every affected Chapter 4, Chapter 5, and Appendix E page,
   not only chapter openings.
6. Compare the item response matrix with the final diff. No item closes on
   prose intent alone; it needs source and compiled evidence.
7. Run `bash scripts/validate.sh --tier chapter --audit-root AUDIT_ROOT` after
   each chapter is complete, then run the release tier from fresh generated
   output after all cross-chapter dependencies stabilize.
8. Commit in the bounded units listed in Section 9.1. Never combine unresolved
   scientific work with release evidence merely to obtain a clean tree.
9. Fetch and recheck remote divergence before any merge. Merge/push only on
   explicit authorization; do not force-push. Overleaf pull and compilation
   remain a separate user action.

Acceptance: all 116 items are IMPLEMENTED, SATISFIED_CURRENT, or explicitly
deferred with a named reason; all validators pass; the final PDF is inspected;
and the Git history identifies the commit that resolves each item.

### 9.1 Commit and review architecture

| Commit unit | Authorized scope | Required checkpoint |
| --- | --- | --- |
| C0: controls and preflight | Response matrix, stale state records, fixed clone/path records, frozen token baseline | Clean diff; exactly 116 IDs; source tips/commits recorded; no `.tex` change |
| C1: Chapter 4 | Chapter 4 Sections 4.1--4.4 and only necessary Appendix D/cross-reference propagation | All B4 items dispositioned; fast and chapter gates; rendered affected pages |
| C2: Chapter 5 theory | Conceptual spine, MPI/MTI definitions, theorem statements, proof graph, corresponding Appendix E proofs | B5-001--B5-038 and BE-001--BE-006 dispositioned; compactness check; chapter gate |
| C3: Chapter 5 procedure | Generalized Bayes, profile, DP content model, calibration, feasibility, validation, corresponding Appendix E record | B5-039--B5-065 and BE-007--BE-011 dispositioned; constants/source audit; chapter gate |
| C4: dissertation reconciliation | Contributions, Chapter 1, abstract, synthesis, acknowledgments check, notation/citations/provenance | Cross-chapter claims and numbers agree; style gate; no unrelated rewrite |
| C5: release evidence | Status, ledger, validation record, final response matrix and accepted artifact identity | Release gate, complete rendered inspection, clean diff and history |

Each commit must be independently reviewable and revertible. Do not amend a
published commit or force-push. If `main` changes during implementation, stop
before merge, fetch, compare histories, and integrate deliberately on the
editorial branch.

### 9.2 Work-package coverage

| Item block | Primary work package | Secondary gate |
| --- | --- | --- |
| `B4-001`--`B4-040` | WP-B1 | WP-B5--WP-B7 |
| `B5-001`--`B5-017` | WP-B2 | WP-B5--WP-B7 |
| `B5-018`--`B5-038` | WP-B2/WP-B3 | WP-B5--WP-B7 |
| `BE-001`--`BE-006` | WP-B3 | WP-B6--WP-B7 |
| `B5-039`--`B5-065` | WP-B4 | WP-B5--WP-B7 |
| `BE-007`--`BE-011` | WP-B4 | WP-B6--WP-B7 |

This table covers every item once at the primary implementation level. Style,
source, build, and response-matrix gates apply to every block.

## 10. Risks and stop rules

| Risk | Control |
| --- | --- |
| Reverting improvements already made after the 221-page copy | Compare each item with current main; preserve every SATISFIED_CURRENT resolution. |
| Treating Bruno's partial Chapter 4 review as complete approval | Keep Sections 4.5--4.8 explicitly outside the received review scope. |
| Changing a theorem or numerical result from a handwritten question | Use the source resolutions in Section 2.2 and cite the fixed locator in the response matrix before editing. |
| Making Chapter 5 longer while trying to clarify it | Relocate proof/computation detail to Appendix E and remove displaced main-text material. |
| Reintroducing a massive appendix | Add only claim-essential support; do not restore superseded supplement content. |
| Conflating ordinary Bayes, generalized Bayes, and the DP content posterior | Define all three targets separately and use distinct notation and prose. |
| Overstating tolerance performance | Tie every claim to the finite prespecified panel and independent validation design. |
| Adding an unsupported comparator | Identify the exact paper, estimand, implementation, and compatible design before inclusion. |
| Blindly replacing thesis prose with article prose | Import no section wholesale; apply source passages only through the item matrix and dissertation dependency map. |
| Silent source drift after planning | Record changed remote tips but retain the fixed commits unless the candidate authorizes a separate scientific refresh. |
| Cross-chapter inconsistency after local edits | Reconcile Chapter 1, abstract, synthesis, acknowledgments, notation, citations, and provenance only after Chapters 4--5 pass their own gates. |
| Treating a clean build as scientific validation | Require source, item, structural, and rendered evidence in addition to compilation. |
| Mixing an Overleaf edit with the Git revision | Preserve Overleaf work before synchronization; no push or pull is part of manuscript implementation without a deliberate handoff. |
| Publishing private review material | Keep original PDFs and rendered annotations ignored; commit paraphrased action items only. |

Pause only the affected work package if a source result, proof, numerical
constant, comparator, or attribution cannot be verified. Continue independent
items rather than replacing missing evidence with a plausible reconstruction.
Also stop before merge if the response matrix is incomplete, a frozen numeric
token changes without a source explanation, the chapter/appendix compactness
trigger is exceeded without justification, the build loses a reference, or
the remote branch has diverged.

## 11. Definition of done

The Bruno revision is complete only when:

- all 36 annotated pages and 116 normalized items remain accounted for;
- every item names its final thesis location, source evidence or
  `not source-dependent`, validation evidence, and commit;
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
- no current numerical result, citation, label, input, figure, or table changes
  without an item-level explanation;
- Chapter 1, abstract, synthesis, acknowledgments, notation, bibliography, and
  provenance records agree with the final Chapters 4--5;
- all writing passes the statistical-style gate without promotional,
  engineering, internal-workflow, or formulaic language;
- fast, chapter, and release validators pass against fixed audit clones; the
  build log, fonts, page size, references, labels, cross-references, and every
  affected rendered page are reviewed;
- the accepted artifact, branch, commit, page count, byte count, and SHA-256
  are recorded; and
- the response record states honestly that the received Chapter 4 review ends
  at Section 4.4.

## 12. Implementation closeout and handoff boundary

The candidate subsequently authorized the complete implementation. Work
proceeded through the bounded C0--C5 sequence without a scientific source
refresh or new research computation. Chapter 4 and Appendix D are fixed in
commit `1af9387`; their evidence records are fixed in `f53104b`. Chapter 5,
Appendix E, and the cross-dissertation contribution reconciliation are fixed in
commit `967dcaa60f6ab217c6138d8086e3bc9e426b2620`.

All 116 response items have final dispositions. Eighty-three are implemented
and validated, 32 were already satisfied and were revalidated, and `B5-058` is
deferred until the possible additional comparator can be identified from an
exact source. The deferral is nonblocking because the two reported comparators
are source-verified and no scientific claim depends on the unidentified note.

Fast, chapter, and release gates pass against all 120 immutable source blobs.
The accepted artifact is
`build/release-20261110T004025Z/main.pdf`, SHA-256
`379e6436ef1f27d77d1e183eae9a89c4b4d54585f014a10c83933d7c1c60661e`.
The release has 184 US-Letter pages, all fonts embedded, no Type 3 fonts, zero
overfull boxes, and no unresolved references, citations, labels, files, or
fatal diagnostics. The changed reader-facing regions were inspected page by
page.

Implementation authorization did not include automatic publication. No push,
merge into `main`, Overleaf synchronization, or advisor communication is part
of this closeout. Those operations require a separate deliberate handoff.
