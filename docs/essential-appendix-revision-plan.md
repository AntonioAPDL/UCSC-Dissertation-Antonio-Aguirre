# Final controlling plan for essential appendix revision

**Plan version:** 2.1 (implemented controlling revision)

**Plan state:** approved and implemented on 2026-10-28; Phases 0--8 and all
sixteen defaults passed their gates, while push, merge, and Overleaf
synchronization remain separately gated

**Prepared:** 2026-10-28

**Repository baseline:** `37b9da0fdb16168dff07efdc9454886f8467f6cd`
(`main`, equal to `origin/main` when audited)

**Accepted baseline PDF:** `build/release-20261028T044714Z/main.pdf`

**PDF SHA-256:**
`49b0bc25f5c4b46c474379d3b7f33bfbfd01a3a28cb77660db63a4a8c5f0e409`

**Authority and relationship to earlier plans:** this file is the only current
plan for the appendix-compression stage. It does not reopen the completed
reader-first restructuring, current-source refresh, or final-reader revision.
It preserves their four-project architecture, body-only contract, source
freeze, and scientific qualifications. It supersedes only their earlier
presumption that all specialist material moved into the appendices should
remain active in the compiled dissertation. The historical
`appendix-migration-map.json` remains immutable evidence of that move.

After approval, an architectural, scientific, source-version, display-family,
or Git/Overleaf departure from this plan requires a dated decision in
`docs/research-decisions.md`. Ordinary editorial choices governed by the
approved essentiality map do not require a new master plan.

## 1. Decision and purpose

The appendix section should be revised from an article-supplement archive into
a selective dissertation technical record. The body should remain readable on
its own. The appendices should retain the proofs, model definitions,
nonstandard calculations, and claim-changing sensitivity evidence that a
statistical reader needs to verify the dissertation's argument. Full table
decks, repeated standard algebra, software-level controls, source-audit
details, and alternative calculations that do not affect a thesis claim should
not remain in the compiled document.

The recommended architecture does **not** combine all technical material into
one thematic appendix. Appendix A should remain a compact cross-project
concordance, and Appendices B--E should remain paired with Chapters 2--5. This
preserves a one-step path from a chapter claim to its technical support and
avoids mixing incompatible likelihood scales, inferential targets, and
notation. The present problem is excessive depth within Appendices D and E,
not the existence of five appendix chapters.

This is the audit and implementation specification. Authorization changes its
state, not its evidentiary boundary: appendix edits must still pass the stated
phase gates, and no research repository may be changed.

### 1.1 Executive decision

The optimal revision is **selective compression within the existing five
appendices**, coupled to precise body links and a no-loss record. It is not a
new thesis architecture and not a second manuscript import. The current
chapters remain the narrative authority. The appendices retain only the
technical material required to prove, reproduce conceptually, or properly
qualify that narrative.

The implementation must satisfy both reader contracts inherited from the
approved reader-first plan:

1. **Body-only contract:** a statistically literate reader can identify each
   project's question, target, model or loss, contribution, principal
   evidence, interpretation, and limitations without opening an appendix.
2. **Technical-recovery contract:** a specialist can follow a precise link to
   the assumptions, proof, nonstandard derivation, algorithm, or
   claim-changing sensitivity evidence needed to audit the body statement.

The advisor's new concern changes the recovery contract from “retain the
complete article supplement” to “retain the complete support needed for the
dissertation claim.” Code, data, full outputs, development diagnostics, and
the superseded article-supplement layer remain recoverable through the fixed
research snapshots and Git history rather than through the compiled PDF.

### 1.2 Alternatives considered

| Alternative | Assessment | Decision |
| --- | --- | --- |
| Keep the 204-page appendix layer | Preserves everything but fails the stated reader and advisor constraint; generic links make the record difficult to use. | Reject |
| Eliminate scientific appendices | Produces a shorter document but loses complete proofs, nonstandard posterior calculations, and specialist recovery. | Reject |
| Move all detail back into Chapters 2--5 | Recreates the interruption that the reader-first restructuring corrected. | Reject |
| Create one thematic appendix for proofs, algorithms, and evidence | Shortens navigation only superficially and risks conflating incompatible scales, targets, and notation across projects. | Reject |
| Publish an external supplement only | Weakens dissertation self-containment and makes central proofs or qualifications depend on another artifact. | Reject |
| Retain five chapter-paired selective appendices | Preserves scientific traceability, project-specific notation, and one-step navigation while permitting substantial reduction. | **Adopt** |

This choice is optimal because it changes only the layer that is causing the
problem, preserves the successful chapter architecture, and can be validated
against the accepted PDF and fixed source records without research
recomputation.

### 1.3 Nonnegotiable scientific invariants

Compression must not silently change:

- an inferential target, conditioning set, likelihood interpretation, loss,
  learning rate, or interval type;
- a theorem statement, assumption, proof obligation, or guarantee;
- a numerical result, data split, forecast origin, horizon, or source role;
- a contribution, attribution, publication status, or reuse status;
- a positive, negative, mixed, or null empirical conclusion; or
- the boundary between implemented evidence and proposed work.

If an apparent error is discovered, stop that unit and handle it as a separate
scientific correction against the authoritative source. Do not hide it inside
an editorial condensation.

## 2. Evidence audited

The audit used the active compiler graph and the accepted release artifact,
not only source-file length. It examined:

- `main.tex`, Chapters 1--5, and Appendices A--E;
- the table of contents and label data generated for the accepted PDF;
- every body reference to an appendix label;
- the reader-first migration map and implementation record;
- the current source and revision ledgers;
- the current status, validation, workflow, and academic-writing
  instructions; and
- the complete academic style profile shared by the Q--DESN and RQR sources.

The audit did not rerun simulations, refit models, or modify any research
checkout. Those operations are unnecessary for deciding whether an already
reported appendix unit is essential to the dissertation argument.

### 2.1 Measured baseline

The accepted PDF has 414 physical US-Letter pages:

| Reading layer | Numbered pages | Pages |
| --- | ---: | ---: |
| Front matter | Roman pagination | 24 |
| Chapters 1--6 | 1--174 | 174 |
| Appendices A--E | 175--378 | 204 |
| Bibliography | 379--390 | 12 |

Appendices occupy 49.3% of the physical PDF and are 30 pages longer than the
six-chapter body. Their distribution is highly uneven:

| Appendix | Present pages | Principal contents |
| --- | ---: | --- |
| A. Cross-chapter conventions | 4 | Target, scale, score, and uncertainty distinctions |
| B. exDQLM details | 14 | Posterior blocks, LDVB, shrinkage, forecasting and synthesis |
| C. Hydrologic details | 9 | Four long algorithms, parameter summaries, four forecast panels |
| D. Q--DESN details | 111 | Full posterior/VB development, extensive empirical supplement, Gaussian note |
| E. MPI/MTI details | 66 | Proofs, computation, calibration, application sensitivities, proposed extensions |

Appendices D and E contribute 177 pages: 86.8% of all appendix pages and
42.8% of the whole PDF. A uniform percentage reduction would therefore be
poorly targeted.

The compiled appendices contain at least 39 numbered tables, 21 figures, ten
algorithm blocks, and eight theorem-like results with proofs. Appendix D alone
contains 26 tables and 15 figures. Appendix E contains 13 tables, four figures,
and all eight formal proof blocks. Several source-level counts are lower
because long TeX table fragments are included from separate files.

The source concentration is consistent with the PDF measurement:

| Source | Lines | Major structural content |
| --- | ---: | --- |
| `a-shared-conventions.tex` | 104 | Six short sections |
| `b-exdqlm-technical.tex` | 566 | 30 displayed equation groups and one algorithm |
| `c-hydrology-technical.tex` | 274 | Four long algorithms and two multi-panel figures |
| `d-qdesn-technical.tex` | 3,373 | 116 displayed equation groups in the source, four algorithms, and extensive included display fragments |
| `e-mti-technical.tex` | 1,685 | Eight theorem-like results and proofs, one algorithm, and extensive included validation/application tables |

The current fast validation baseline passes before any manuscript change:

- ten unit tests;
- eight audited research sources and 30 evidence records;
- 29 editorial issues, 102 display records, and 11 bibliography groups;
- 102 immutable imported records and 115 imported TeX files;
- 83 active TeX files, including seven compiler-resolved macro inputs;
- 482 unique active labels and six historical migration records; and
- 47 active graphic/visual records with accessibility-ledger coverage.

These counts are controls, not targets that must remain numerically constant.
After compression, every difference must be explained by the essentiality map.

### 2.2 Reference diagnosis

The body-to-appendix reference graph is much coarser than the appendix depth:

| Appendix | Labels defined | Direct body references | Distinct labels reached from body |
| --- | ---: | ---: | ---: |
| B | 43 | 5 | 1, the appendix chapter label |
| C | 9 | 8 | 5, including two algorithms and two figures |
| D | 178 | 24 | 1, the appendix chapter label |
| E | 49 | 13 | 1, the appendix chapter label |

Thus, a reader is repeatedly sent to a 111-page or 66-page appendix without a
precise destination. The remedy is not merely to shorten the appendices. The
body bridges must point to retained, reader-facing sections for the exact
derivation, proof, protocol, or sensitivity result being invoked.

### 2.3 Principal diagnosis

The current appendices are scientifically rich, but they preserve the scale
and organization of several article supplements. Four patterns account for
most of the excess:

1. **Complete empirical table decks.** Appendix D devotes numbered pages
   243--299 to supplementary simulation, PriceFM, and GloFAS material.
   Appendix E devotes pages 343--355 to two distribution-level validation
   tables even though Chapter 5 already reports the decision-relevant range
   summaries.
2. **Repeated computational variants.** Single- and multi-quantile MCMC/VB
   blocks repeat standard latent-variable and shrinkage updates. The Gaussian
   Q--DESN note separately repeats conjugate regression algebra, alternative
   priors, implementation advice, and validation checklists.
3. **Article- or audit-facing organization.** Headings such as “Supplementary
   Simulation and Application Tables,” “Omitted Variants and Why They Are Not
   Main Derivations,” “Implementation Notes,” and “Reproducibility and
   Validation Limits” describe document production rather than statistical
   content.
4. **Generic body bridges.** The main chapters often say only that “Appendix
   D/E gives” the material. This hides which part is essential and encourages
   the appendix to operate as an undifferentiated repository.

The audit did **not** find that the appendices are long because the body and
appendix contain large verbatim prose duplicates. The excess is primarily
semantic overlap, exhaustive variants, and complete supporting evidence—not
literal copy-and-paste repetition. Compression therefore requires scholarly
selection and consolidation, not a mechanical duplicate-line deletion.

### 2.4 Audit of the previous appendix plan

The first essential-appendix plan established the correct high-level answer:
retain five project-linked appendices, protect central proofs and negative
evidence, reduce Appendices D and E most heavily, replace generic pointers by
specific links, and keep deactivated assets recoverable. It also correctly
treated the proposed page range as a diagnostic rather than permission to cut
scientific content.

The deeper comparison with the implemented reader-first plan, the
current-source refresh, the final-reader revision, and the active validators
identified seven gaps that this version closes:

1. **Plan authority was implicit.** The earlier draft did not state precisely
   which historical decisions it superseded. Version 2 changes only active
   appendix inclusion, not chapter architecture, source authority, or the
   historical migration record.
2. **Display decisions were too discretionary.** Phrases such as “keep either
   the table or figure” would force the implementing agent to make late
   scientific-placement choices. Section 5.6 now gives the recommended exact
   retained display set and exception process.
3. **Theorem deduplication was overgeneralized.** Not every supporting result
   belongs in the body. Section 5.5 now distinguishes principal body
   statements with appendix proofs from supporting results whose complete
   statement and proof remain in Appendix E.
4. **Current validators would reject deactivated `KEEP` displays.** The
   display ledger records historical/source inclusion, while the accessibility
   ledger currently requires exact equality with active graphics. Section 8
   defines a backward-compatible current-inclusion layer rather than rewriting
   historical decisions or simply deleting ledger records.
5. **Historical migration markers were not protected explicitly.** The
   structure validator requires each migration marker and a body reference to
   the appendix chapter label. These invariants are now part of the file and
   validation contract.
6. **The file impact and rollback boundaries were incomplete.** Version 2
   identifies every expected manuscript, record, validator, test, and status
   file and names files that should remain unchanged.
7. **The work order began with mapping before validator support for the new
   state existed.** The revised sequence freezes the baseline, adds the small
   schema/validator capability, creates and approves the map, and only then
   edits TeX.

### 2.5 Decisions inherited unchanged

The following completed decisions remain authoritative:

- four research chapters in the current order;
- current audited source commits and the 2026-10-26 source-refresh record;
- manuscript-first reuse rather than rewriting chapters from zero;
- external code/data/computation boundary;
- development-informed qualifications in Chapters 3 and 4;
- current profiled-MTI method and its finite-panel calibration boundary;
- proposed, unimplemented status of MTI regression/dynamic extensions;
- exact candidate/coauthor and reuse uncertainties;
- consolidated bibliography after the appendices; and
- untagged baseline PDF status and separate accessibility filing work.

This stage does not rescan GitHub, refresh research repositories, rerun a
simulation, change the package version graph, or revisit project selection.

## 3. Essentiality rule

Every current appendix unit should receive one of four internal editorial
dispositions. These terms belong in the audit record, not in the dissertation
prose.

| Disposition | Test | Result in the compiled thesis |
| --- | --- | --- |
| `RETAIN` | Necessary to establish a central original result, define a nonstandard target, or support a main claim | Kept, with reader-facing editing |
| `CONDENSE` | Necessary idea, but repeated, standard, or more detailed than the claim requires | Rewritten as one authoritative treatment |
| `SUMMARIZE` | Evidence changes interpretation, but a full table/figure family is unnecessary | One compact table, figure, or paragraph |
| `DEACTIVATE` | Archival, software-level, superseded, standard, or not linked to a dissertation claim | Excluded from the compiler graph; recoverable from Git/source records |

A unit is essential only if at least one of these questions has a documented
“yes” answer:

1. Would omitting it leave a central theorem, proposition, model, or
   inferential target unsupported?
2. Is it a nonstandard derivation needed to distinguish likelihood-based
   inference, variational approximation, generalized updating, prediction, or
   tolerance calibration?
3. Does it supply a design fact or sensitivity result that materially narrows
   a claim in the chapter?
4. Does a reader need it to understand exactly what was estimated, compared,
   or held fixed?
5. Is it the only dissertation-level record of a negative or mixed result that
   prevents an overstated conclusion?

The following are not sufficient by themselves:

- presence in an article supplement;
- availability of a table or figure;
- usefulness to a software maintainer;
- existence of an alternative derivation;
- reproducibility at the level of every command, file, seed, or convergence
  trace; or
- completeness relative to every research-repository output.

The thesis remains reproducibly connected to the exact source snapshots,
manifests, and research repositories. It does not need to compile every
research artifact to preserve that connection.

## 4. Recommended scale and architecture

Pagination is a diagnostic rather than the selection rule. Applying the
essentiality rule gives the following realistic envelope:

| Appendix | Present | Planned range | Editorial role after revision |
| --- | ---: | ---: | --- |
| A | 4 | 2--3 | Compact target and terminology concordance |
| B | 14 | 8--10 | exDQLM posterior and nonconjugate-inference record |
| C | 9 | 4--5 | Hydrologic MCMC/VB structure and only claim-bearing support |
| D | 111 | 38--46 | Q--DESN/MQ--DESN posterior core plus selective sensitivities |
| E | 66 | 30--38 | Central proofs, profiled computation, calibration, selective application support |
| **Total** | **204** | **82--102** | Selective technical record |

The projected complete dissertation is approximately 292--312 pages if the
body and bibliography remain stable. The implementation should not pad or cut
material merely to hit these numbers. A retained unit outside the range needs
a claim-specific justification in the disposition map.

## 5. Appendix-by-appendix disposition plan

### 5.1 Appendix A: statistical targets and conventions

Appendix A is already concise and has a legitimate cross-project function.
It prevents false equivalence among likelihoods, synthesized predictive
distributions, loss-defined intervals, and tolerance procedures.

| Current unit | Decision | Planned treatment |
| --- | --- | --- |
| Targets and update mechanisms | `RETAIN` | Keep the likelihood/generalized-update distinction and the separation of content, tilt, and learning rate. |
| AL and exAL latent-variable scales | `CONDENSE` | Keep only the scale conversion that prevents formulas from being transferred incorrectly across chapters. |
| Multiple quantiles and predictive distributions | `RETAIN` | Keep the distinction among separate fits, synthesis, stacked composite likelihood, and a joint predictive distribution. |
| Scores and empirical comparisons | `RETAIN` | Keep the CRPS/aCRPS/check-loss/tolerance distinction in compact form. |
| Uncertainty language | `RETAIN` | Keep the credible/predictive/tolerance terminology boundary. |
| Where the complete details reside | `DEACTIVATE` | The introduction and chapter bridges should provide this navigation; a directory-like appendix section is redundant. |

Rename the appendix to **Statistical targets and conventions**. It should read
as statistical exposition, not as a map of the dissertation's file structure.

### 5.2 Appendix B: exDQLM posterior and variational calculations

The exDQLM appendix is moderate in size. Its revision should concentrate the
original numerical/statistical content and remove package-maintainer detail.

| Current unit | Decision | Planned treatment |
| --- | --- | --- |
| Nonconjugate VB and computational details | `CONDENSE` | Retain the transformed nonconjugate block and the structured scale--skewness idea. Remove backend-option names, thread controls, package-test commentary, and obsolete kernel inventory. |
| Dynamic DQLM/exDQLM posterior targets | `CONDENSE` | Give one common state-space target and state the AL/exAL difference once. Do not repeat the chapter's model exposition. |
| Transfer-function augmentation | `RETAIN` | Keep the augmented state/evolution block because it connects the scientific lag mechanism to inference. |
| Static AL/exAL regression | `CONDENSE` | Keep only what is needed for the sparse static example and the distinction from the dynamic model. |
| LDVB scale--skewness implementation | `RETAIN` | Preserve the factorization, required mixed moments, Gaussian pseudo-observation, latent-factor updates, structured (q(\gamma)q(\sigma\mid\gamma)) calculation, and approximation boundary. |
| Earlier Laplace--delta variant | `SUMMARIZE` | One comparison paragraph and, if needed, one transformed objective. Do not reproduce a second full computational path. |
| Nishimura--Suchard shrinkage | `CONDENSE` | Retain the effective prior precision and compact MCMC/VB update summary. Cite standard auxiliary-scale results rather than repeating every entropy term. |
| Forecasting and diagnostics | `CONDENSE` | The body already defines the important scores. Keep only posterior-predictive generation and the distinction between fitted-quantile and predictive-distribution summaries. |
| Posterior-predictive synthesis algorithm | `RETAIN` | Keep one compact algorithm because it establishes that synthesis is post hoc rather than a joint multi-quantile posterior. |

The body should link to three specific sections: posterior target, LDVB
calculation, and predictive synthesis. Code-level option names are appropriate
in Chapter 2's software discussion when scientifically relevant, but they do
not belong in the technical appendix merely as implementation inventory.

### 5.3 Appendix C: hydrologic posterior computation

Appendix C currently repeats filtering/smoothing recursions inside four long
algorithm boxes and then adds material that is only weakly connected to the
chapter's claims.

| Current unit | Decision | Planned treatment |
| --- | --- | --- |
| MCMC algorithm | `RETAIN` | Replace the two nested blocks by one source-indexed sampler outline. State latent, shape, scale, and state-path updates; cite the standard FFBS recursion instead of reproducing every filtering line. |
| Variational algorithm | `RETAIN` | Give the factorization and one block-update table or compact algorithm. Do not repeat the MCMC notation and the complete standard smoother. |
| Source-specific exAL parameter summaries | `SUMMARIZE` | Retain one sentence only if it is needed to prevent interpreting likelihood parameters as synthesis weights. The numerical ranges are not a central result. |
| Four cutoff-specific synthesis panels | `DEACTIVATE` | The body already reports all five origins in score tables and shows one representative synthesis. The additional panels are illustrative rather than claim-bearing. |

If advisor preference favors one visual robustness check, a single compact
four-panel figure may be retained instead of deactivation, but it should not
be the default. The Chapter 3 sentences that directly cite the present two
figures must be rewritten either way.

### 5.4 Appendix D: Q--DESN and MQ--DESN technical support

Appendix D needs the largest intervention. Its present 111 pages divide into
three different functions:

- model/computation, pages 202--242 (41 pages);
- empirical supplement, pages 243--299 (57 pages); and
- Gaussian baseline note, pages 300--312 (13 pages).

The revised appendix should have four reader-facing sections: (i) posterior
specification, (ii) single- and multi-quantile computation, (iii) forecasting
and empirical support, and (iv) Gaussian baseline and initialization.

#### Model and computation

| Current unit | Decision | Planned treatment |
| --- | --- | --- |
| Distributional conventions | `CONDENSE` | Define only exAL branch constants, the GIG convention, and branchwise regularity needed by later calculations. Use Appendix A for global conceptual distinctions. |
| DESN feature map and fixed design | `CONDENSE` | Chapter 4 already states the reservoir recursion. Retain the conditioning statement, feature dimension, and fixed-design boundary in at most one page. |
| AL/exAL augmentation | `RETAIN` | Keep one authoritative hierarchy and one generic posterior factorization. |
| Ridge and regularized-horseshoe priors | `RETAIN` | Preserve the product-prior distinction and finite-slab effective variance because scale-dependent normalizing factors affect posterior updates. |
| Global-scale reference calibration | `CONDENSE` | Retain the final calibration rule and assumptions used in the studies; remove the extended Gaussian/AL/exAL sequence when it does not change the applied rule. |
| MCMC full conditionals | `CONDENSE` | Keep the coefficient block, nonconjugate scale--shape block, and one sampler outline. Consolidate standard GIG, truncated-normal, and inverse-gamma updates in a table or refer to the common augmented target. |
| Single-level VB and ELBO | `RETAIN` | Keep the variational family, coefficient/latent updates, structured scale--shape factor, and stopping definition. Remove generic entropy bookkeeping and repeated standard identities. |
| Earlier Laplace--delta calculation | `SUMMARIZE` | Retain only enough to explain the approximation compared in the chapter or source article. |
| MQ--DESN composite target and adjacent-difference prior | `RETAIN` | These are central methodological contributions. Preserve the target, prior precision structure, ordered-intercept treatment, and crossing definition. |
| MQ--DESN block updates | `CONDENSE` | State only blocks that differ from the single-level method; do not reproduce the complete single-level derivation for every quantile. |
| Forecast summaries, monotone projection, and scores | `CONDENSE` | Retain the conditional-quantile versus posterior-predictive distinction, isotonic projection, and oracle-score calculation not already fully defined in Chapter 4. |
| Reservoir selection and initialization | `SUMMARIZE` | One final-specification table and a clear leakage/development boundary. Remove search narration and duplicate initialization diagnostics. |

This revision should reduce the model/computation portion from 41 pages to
approximately 20--24 pages while retaining every nonstandard inferential
block.

#### Simulation and application evidence

| Current unit | Decision | Planned treatment |
| --- | --- | --- |
| Single-quantile generating design | `CONDENSE` | Keep one complete DGP specification or table sufficient to interpret the main comparisons. |
| Three primary family-specific metric tables | `DEACTIVATE` | Chapter 4 already gives the principal check-loss evidence. Preserve a compact cross-family summary only if a main claim cannot be checked without it. |
| Fit-path recovery and VB figure/table families | `SUMMARIZE` | Retain one consolidated recovery diagnostic if it materially distinguishes forecast score from latent-path recovery. |
| 500-target sensitivity | `SUMMARIZE` | Keep one compact comparison stating whether and where the primary ranking changes; do not repeat full Gaussian/Laplace/mixture tables and paired figures. |
| Empirical quantile frequencies | `RETAIN` | Keep one compact figure or table because calibration qualifies the score-based claims. Do not retain both. |
| Multiquantile protocol and complete score tables | `CONDENSE` | Keep the common design and one principal table combining oracle score, crossing rate, and the winner/runner-up qualification. |
| Secondary realized-response, VB, contrast, and path-recovery tables | `SUMMARIZE` | One targeted sensitivity table or paragraph. Retain the fact that all winner/runner-up intervals overlap and that independent models lead in most score mechanisms. |
| PriceFM fold design | `CONDENSE` | Keep dates/sample structure only if not fully stated in Chapter 4. |
| PriceFM regional and historical comparisons | `SUMMARIZE` | Retain one compact regional display or table because the aggregate result is mixed. Do not keep both the historical and current full comparisons. |
| GloFAS design and weighted likelihood | `RETAIN` | Preserve observed/latent quantities, selected final specification, horizon weights, and latent future-path approximation. |
| Three GloFAS prior tables | `CONDENSE` | Merge into one final-specification table limited to hyperparameters needed to interpret the comparison. |
| Full seven-family GloFAS forecast figure | `SUMMARIZE` | The body already shows representative forecasts and the full score table. Retain only if it adds a claim not visible there. |
| Reference-only, discrepancy-only, and combined component figures | `DEACTIVATE` | These are useful exploratory diagnostics but not necessary to support the issued-ensemble conclusion. |
| Convergence table and figure | `SUMMARIZE` | State the stopping rule and achieved values in prose or one small table; do not retain both. |
| GloFAS empirical frequencies | `RETAIN` | Keep either the table or the figure because severe undercoverage is a central limitation; the figure is likely the more readable choice. |

Negative and mixed findings are protected: the 500-target sensitivity, the
score-versus-crossing distinction, overlap of the multiquantile score
intervals, GloFAS undercoverage, the particularly poor upper-quantile
frequency for MQ--DESN exAL, and PriceFM's mixed aggregate/fold results must
remain in either the body or one retained supporting display.

The empirical portion should fall from 57 pages to approximately 14--18.

#### Gaussian baseline

| Current unit | Decision | Planned treatment |
| --- | --- | --- |
| Scope and mean-versus-quantile distinction | `RETAIN` | Keep the scientific interpretation and computational role. |
| Conjugate scaled-ridge model and posterior | `CONDENSE` | State the model, posterior parameters, predictive law, and direct sampler without reprinting the full joint-density expansion and square completion. |
| Log marginal likelihood | `DEACTIVATE` | Exclude unless Chapter 4 uses it for an actual comparison or selection decision. |
| Quantile initialization | `RETAIN` | Preserve the intercept shift, scale initialization, and uncertainty warning because these connect the baseline to Q--DESN computation. |
| Alternative unscaled/RHS variants | `DEACTIVATE` | They are not the reported exact baseline and add no thesis claim. |
| Implementation notes | `DEACTIVATE` | Cholesky and matrix-inversion advice belongs in software documentation unless a numerical issue changes a reported result. |
| Dimension, conjugacy, numerical, and initialization checklists | `DEACTIVATE` | These are development checks. Retain any scientifically consequential failure as prose, not as a checklist. |

This section should become approximately 3--4 pages.

### 5.5 Appendix E: MPI/MTI proofs, calibration, and extensions

Appendix E contains central original theory and should not be compressed by
dropping proofs indiscriminately. Its current 66 pages divide into theory and
computation (27 pages), validation (19), application support (13), and proposed
extensions (7). The revision should prioritize complete proofs of original
claims over exhaustive empirical tables.

#### Theory and computation

| Current unit | Decision | Planned treatment |
| --- | --- | --- |
| Fixed-content interval targets | `CONDENSE` | Chapter 5 already compares ET, MPI, and shortest intervals. Retain only definitions needed by the proofs. |
| MPI first-order equations | `CONDENSE` | State the score equations once and move directly to proof material not in the chapter. |
| Quantile-window identification proof | `RETAIN` | Central support for the MPI target. Refer to the theorem statement in Chapter 5 rather than restating extended motivation. |
| Mean-preserving contraction proof | `RETAIN` | This is a substantive consequence cited in the body. |
| Interval-path and tail-sensitivity analysis | `CONDENSE` | Preserve nesting assumptions, the support-gap counterexample, affine equivariance, and the restricted-regression qualification; remove repeated target exposition. |
| Fixed-content MTI proposition proof | `RETAIN` | Keep the short score proof. |
| Profile-radius lemma and global-identification proof | `RETAIN` | These are central original theoretical support and should remain complete. |
| Boundary/admissible-tilt cases | `CONDENSE` | Preserve finite-root existence and unbounded-risk qualifications in one coherent result. |
| Cornish--Fisher derivation | `CONDENSE` | Retain the first-order formula, assumptions, and failure boundary needed for the main figure/table; remove repeated plug-in workflow commentary. |
| Fractional empirical-balance proof | `RETAIN` | Central finite-sample score identity. Keep the DKW statement with its limited interpretation. |
| Loss-geometry figure | `DEACTIVATE` | The algebra and chapter exposition are sufficient. |
| Width-regularized comparison | `CONDENSE` | Keep one page establishing that RQR-W changes both content and placement. This is a scientific antecedent distinction, not optional background. |
| Alternative ECM calculation | `DEACTIVATE` from this section | The reported computation uses the convex profile. The general extension section already explains ECM; one representation is enough. |
| Convex midpoint profile and proof | `RETAIN` | This supports the actual reported calculation and objective-gap check. |
| Direct DP content law | `CONDENSE` | State the Beta law and its interpretation; cite standard DP conjugacy instead of retaining a separate proposition and proof. |

Principal theorem and proposition statements already needed for a body-only
reading should have one authoritative location in Chapter 5. Appendix E should
use headings such as “Proof of Theorem 5.x” rather than repeat those formal
statements. Supporting results that the body only summarizes--for example the
profile-radius lemma, convex-order contraction, convex midpoint profile, or a
technical empirical-balance theorem--may retain both statement and proof in
Appendix E. The theorem/proof graph must record which of these two patterns
applies. This avoids competing formal versions without forcing every technical
lemma into the reading chapter.

#### Calibration evidence

| Current unit | Decision | Planned treatment |
| --- | --- | --- |
| Simulation panel and feasible cells | `RETAIN` | Keep distributions, paired design, feasible ((n,c)) cells, and the independent calibration/validation boundary. |
| Cutoff development and multiplicity allocation | `RETAIN` | This is required to interpret the empirical tolerance claim. Condense to the actual fixed rule and error allocation. |
| Distribution-level content table (6 pages) | `DEACTIVATE` | Chapter 5 reports the across-distribution ranges and uncertainty assessment. Retain the exact data in the source repository/provenance record. |
| Distribution-level width table (7 pages) | `DEACTIVATE` | The body width figure and summary give the reader-facing result. |
| Population shortest-interval figure | `DEACTIVATE` | It is a benchmark aid already represented in the body width figure. |
| Selected cutoff/policy table | `RETAIN` | Compact and directly documents the calibrated rule. |
| Scan-reference table | `CONDENSE` | Merge retained counts/buffers with the policy table if legible. |
| Full-range feasibility thresholds | `RETAIN` | Small, and necessary to distinguish structural infeasibility from method failure. |

The revised validation section must continue to say that the evidence is for a
prespecified finite simulation panel, not a distribution-free MTI tolerance
theorem.

#### Pharmaceutical application and proposed extensions

| Current unit | Decision | Planned treatment |
| --- | --- | --- |
| Data definition and integrity limitations | `RETAIN` | Keep unresolved physical units, inconsistent summary relationships, ties, dependence, and batch-selection limitations. |
| Response-diagnostic table | `CONDENSE` | Keep only variables needed to justify the selected primary response and the RSD sensitivity. |
| Representative-split construction | `SUMMARIZE` | One paragraph is sufficient unless the rule is challenged in the body. |
| RSD table and figure | `SUMMARIZE` | Keep one, preferably the figure, because it illustrates asymmetric placement and the one-sided quality-control caveat. |
| Paired-comparison tables | `DEACTIVATE` | The primary chapter table and retained sensitivity summary are sufficient. |
| Partition-sensitivity tables and figure | `RETAIN` selectively | Keep one compact figure or merged table showing that partition choice materially changes held-out content. |
| Campaign-sharing table | `SUMMARIZE` | Preserve the non-independence limitation and key result in prose unless it changes the selected interpretation. |
| Numerical-diagnostics table | `DEACTIVATE` | State the objective-gap success and independent recalculation in prose. |
| Regression/dynamic targets and root labels | `RETAIN` | Necessary to define the proposed extension and label invariance. |
| Pseudo-AL augmentation and Gaussian root updates | `RETAIN` | Nonstandard computation; keep compact derivation and clarify that it augments a loss, not a response likelihood. |
| ECM, shrinkage, basis, and dynamic updates | `CONDENSE` | One computational path for each proposed model class, with explicit theory-only status. |
| Diagnostic checklist | `CONDENSE` | Replace the checklist with a short paragraph stating what future validation would need. |

The application support should fall to about 4--5 pages, and the proposed
extension section to about 3--4 pages. The revised appendix must preserve that
the extensions have no matched implementation, simulation study, or
application.

### 5.6 Recommended exact display outcome

The following is the default display set for the appendix-compression map.
It resolves the discretionary “table or figure” choices in the first plan.
An exception is permitted only when the map identifies the body claim that
would otherwise become unverifiable and records author/advisor approval.

#### Appendix C

- Retain no additional cutoff forecast figure. The five-origin score tables
  and representative main-text synthesis already provide the necessary
  empirical evidence.
- Replace the current four algorithm boxes by two compact algorithms: one
  integrated MCMC outline and one variational outline. Standard FFBS/FFBSm
  recursions should be cited and described, not reproduced as separate long
  boxes.

#### Appendix D

Retain, after condensation where indicated:

1. `qdesn2026:tab:supp-reservoir-selection` -- final fixed reservoir
   specifications and design diagnostics, substantially shortened;
2. `qdesn2026:tab:simulation-dgp` -- the complete single-quantile generating
   design;
3. `qdesn2026:fig:independent-eval500-forecast_check` -- the 500-target
   check-loss sensitivity that qualifies the primary 300-target result;
4. `qdesn2026:fig:supp-independent-quantile-calibration` -- empirical
   quantile frequencies; do not also retain the numerical duplicate table;
5. `qdesn2026:tab:joint-qdesn-pure-desn-v2-recursive-policy` -- the targeted
   averaged-predictor versus trajectory-specific forecast sensitivity;
6. `qdesn2026:fig:supp-pricefm-r98-region-comparison` -- regional
   heterogeneity behind the mixed PriceFM aggregate result;
7. `qdesn2026:tab:supp-glofas-search3-specifications` -- final selected
   historical specifications, shortened to parameters needed for
   interpretation; and
8. `qdesn2026:fig:supp-glofas-part4-calibration` -- the clearest retained
   evidence of issued-window undercoverage.

Deactivate from the compiled thesis the remaining Appendix D display family,
including duplicate numerical counterparts, component-only GloFAS forecast
figures, full-family display, convergence figure/table pair, complete
family-specific simulation table decks, initialization illustration, and
historical PriceFM duplicate comparison. Preserve their source assets and
baseline locations.

The main Chapter 4 score figures and tables remain untouched. Values copied
into condensed tables must be exact selections from existing verified cells;
no new derived comparison or arithmetic summary is allowed without a small,
recorded verification script or an independent manual cross-check.

#### Appendix E

Retain, after condensation where indicated:

1. `rqr2026:tab:supp-mti-profile-policy` -- selected calibrated MTI cutoffs and
   assessment bounds;
2. `rqr2026:tab:supp-scan-reference` -- retained-count/content buffers, merged
   with the policy table only if the combined table remains legible;
3. `rqr2026:tab:supp-full-range-thresholds` -- the small feasibility table;
4. `rqr2026:fig:supp-pharma-rsd` -- asymmetric placement and the one-sided
   quality-control caveat; and
5. `rqr2026:fig:supp-pharma-partition-sensitivity` -- the application result
   that most directly demonstrates partition dependence.

Deactivate from the compiled thesis the two 13-page distribution-level
validation tables, loss-geometry figure, population-shortest benchmark figure,
RSD numerical duplicate table, paired-comparison table deck, campaign table,
response-diagnostic table, and numerical-diagnostics table. Preserve their
claim-changing conclusions in the body or concise appendix prose exactly as
specified in Section 5.5.

#### Appendices A and B

No figure or table decision is required. Appendix B retains one compact
posterior-predictive synthesis algorithm. Its computational formulas are
selected by inferential necessity, not display count.

### 5.7 Protected conclusion register

Before any display is deactivated, the essentiality map must assign a final
visible location to each of these conclusions:

- hydrologic performance varies across the five forecast origins and the
  28-day and common 8-day comparisons answer different questions;
- LDVB is an approximation, and MCMC remains the reference when posterior
  tails or interval accuracy are central;
- the Q--DESN 500-target sensitivity preserves the principal pattern but does
  not create an untouched confirmation experiment;
- MQ--DESN reduces crossings more consistently than it improves score;
- every multiquantile winner/runner-up marginal interval overlaps in the
  reported study;
- the GloFAS descriptive score leader remains undercovered, and MQ--DESN exAL
  has particularly poor upper-quantile empirical frequency;
- Q--DESN does not dominate PriceFM in aggregate and varies by region/fold;
- calibrated MTI evidence applies to the fixed eight-distribution panel and is
  not a distribution-free theorem;
- MTI width is not uniformly smaller than Young--Mathew, especially near the
  sample-range boundary;
- the pharmaceutical splits overlap, partition choice matters, and the
  physical interpretation of the derived response remains unresolved; and
- proposed endpoint regression and dynamic models have no matched
  implementation, simulation, or application.

No display deactivation is complete until this register passes a body and
appendix text search plus human review.

## 6. Main-text reference revision

The appendix edit and body-reference edit must be one atomic scholarly change.
The body should never describe what was cut. It should state what support is
available and point directly to it.

### 6.1 Planned stable section labels

The implementation should preserve all five appendix chapter labels and add a
small stable reader-facing label set:

| Appendix | Planned destinations |
| --- | --- |
| B | `app:exdqlm-posterior`, `app:exdqlm-ldvb`, `app:exdqlm-synthesis` |
| C | `app:hydrology-mcmc`, `app:hydrology-vb` |
| D | `app:qdesn-posterior`, `app:qdesn-computation`, `app:qdesn-simulation-support`, `app:qdesn-glofas-support`, `app:qdesn-pricefm-support`, `app:qdesn-gaussian-baseline` |
| E | `app:mti-proofs`, `app:mti-profile-computation`, `app:mti-calibration`, `app:mti-application-sensitivity`, `app:mti-extensions` |

Final names may follow existing namespaces, but they must describe statistical
content rather than migration or supplement status.

### 6.2 Required bridge pass

| Body locations | Required final routing |
| --- | --- |
| Chapter 1 roadmap | Describe appendices as optional proof/computation/support and stop promising a complete article-level record. |
| Chapter 2 overview and model discussion | Appendix B chapter label for the overview; posterior target for model blocks. |
| Chapter 2 computation (current lines near 475 and 493) | LDVB section, with a separate synthesis link only where synthesis is discussed. Remove promises of backend inventories that will no longer be present. |
| Chapter 2 discussion | Link only to the specific unresolved approximation or synthesis calculation, not to “posterior and package-specific details” generally. |
| Chapter 3 MCMC discussion | Consolidated MCMC section; replace direct reference to the separate FFBS box with a standard-method citation or the consolidated algorithm. |
| Chapter 3 VB/computation discussion | Consolidated variational section. |
| Chapter 3 final evidence discussion | Remove direct promises of the four cutoff panels; the body score tables already carry the five-origin evidence. |
| Chapter 4 model/prior links (current lines near 231--354) | Posterior specification, prior, and model-constant sections. |
| Chapter 4 MCMC/VB links (near 380) | Computation section. |
| Chapter 4 forecasting/scoring links (near 403--474) | Computation/forecast subsection or simulation support, according to whether the sentence invokes a formula or an empirical check. |
| Chapter 4 simulation links (near 528--655) | Simulation-support section; 500-target, calibration, and recursive-policy claims should point to their retained display or subsection. |
| Chapter 4 GloFAS links (near 689--756) | GloFAS-support section. Remove the promise of a full-family figure when the body table already supplies the comparison. |
| Chapter 4 PriceFM links (near 850--862) | PriceFM-support section and retained regional figure. |
| Chapter 5 theory links (near 298--409) | Proof section and, where appropriate, the specific proof heading for the body theorem/proposition. |
| Chapter 5 computation links (near 599--629) | Profile-computation section. |
| Chapter 5 calibration links (near 711 and 904) | Calibrated-policy/feasibility subsection. Rewrite the current promise of complete distribution-level tables because those tables will be inactive. |
| Chapter 5 application links (near 1005--1013) | Application-sensitivity section and retained partition/RSD figures. |
| Chapter 5 proposed-method links (near 1059--1073) | Extensions section. |

The chapter-opening attribution notes may retain the appendix chapter label,
but “complete,” “preserved,” and similar archive promises must be replaced by
an exact description of the selective support. All other generic references
should become topical links.

Every final appendix reference must pass two tests: the cited section exists,
and the first paragraph or display at that destination answers the question
raised by the body sentence.

The historical migration validator currently checks that each source chapter
still contains the corresponding appendix chapter label. Preserve at least one
truthful chapter-level bridge for every historical migration record while
adding the narrower links. Do not satisfy the validator with an invisible or
semantically empty label mention.

## 7. Reader-facing language policy

The compiled thesis should not discuss editorial deletion, migration, files,
ledgers, internal repositories, or what a supplement used to contain. Such
facts remain in this plan and the disposition map.

Examples of required conversion:

| Current style | Reader-facing style |
| --- | --- |
| “This appendix preserves the current article's detailed...” | “This appendix gives the posterior calculations and sensitivity analyses used in Chapter 4.” |
| “Supplementary Simulation and Application Tables” | “Simulation sensitivity and application diagnostics” |
| “The full intervals remain recorded in the fixed source materials...” | State the interpretable parameter result, or omit the sentence. |
| “Omitted Variants and Why They Are Not Main Derivations” | No compiled counterpart unless a variant affects interpretation. |
| “Implementation Notes” | “Numerical calculation,” only when statistically consequential. |
| “package tests,” “scripts,” or “file records” | A statistical validation statement, or a data/code-availability record outside the argument. |
| “internal retained-count reference” | “scan-calibrated retained-count reference” |
| “main article” or “supplement” | “Chapter 4/5,” a named study, or the statistical object itself. |

Engineering terms remain acceptable when they name the scientific object
(for example, a fixed reservoir feature map or a numerical stopping rule).
They should not organize the prose around software maintenance. Statistical
verbs should lead: define, condition, estimate, approximate, identify,
calibrate, compare, and qualify.

## 8. Reproducibility and provenance controls

Compression must not erase recoverability.

### 8.1 Historical records that remain immutable

- Do not rewrite `appendix-migration-map.json`; it records how technical units
  entered the appendices. Preserve every `% migration-id:` marker required by
  `validate_structure.py`.
- Do not alter immutable import-source or baseline destination hashes in
  `docs/imports/*.json`.
- Do not change the audited research commits, source-refresh record, rights
  status, or contribution status.
- Do not delete the accepted baseline PDF or treat a later ordinary build as
  its replacement.

### 8.2 New essentiality map

Before TeX changes, create `docs/appendix-essentiality-map.json`. This is a
follow-on inclusion record, not a replacement migration history. Its top-level
fields should include:

- `schema_version`, `plan_id`, and approval record;
- baseline thesis commit, branch, appendix source hashes, PDF path/hash/pages,
  and validation counts;
- links to the historical migration map, display ledger, accessibility ledger,
  claim ledger, revision ledger, and source-refresh record; and
- a `records` array.

Each record should cover a section/subsection, theorem/proof unit, algorithm,
labeled equation group, or display family and contain:

- stable `APPX-ESS-*` identifier and parent appendix/chapter;
- source path plus heading or semantic-label anchor;
- baseline line/page span and normalized source-span SHA-256;
- historical migration IDs, display IDs, claim IDs, labels, citations, and
  active file dependencies;
- current body references and the claim/question each reference asks;
- disposition: `RETAIN`, `CONDENSE`, `SUMMARIZE`, or `DEACTIVATE`;
- exact rationale under the essentiality rule;
- target path, planned heading/label, replacement display/text, and required
  body bridge;
- protected conclusion/assumption IDs;
- recovery pointer: baseline PDF pages, source snapshot/path, and Git commit;
- risk class and reviewer;
- status: `PROPOSED`, `APPROVED`, `IMPLEMENTED`, or `VERIFIED`;
- implementation commit, final hash, and validation evidence after execution.

The map validator must fail on uncovered active appendix units, duplicated IDs
or targets, a `DEACTIVATE` record without recovery/no-loss rationale, an active
body reference to an inactive label, missing protected conclusions, or an
implemented record whose final hash/location does not match the source.

### 8.3 Display and accessibility record semantics

`display-ledger.json` records the prior scholarly/source disposition. A
display that was correctly `KEEP` under the current-source refresh may become
inactive under the later essentiality decision. Do not falsify the historical
decision by changing `KEEP` to `OMIT` without context.

Use a backward-compatible current-inclusion field or a join to the
essentiality map. Update `validate_editorial_audit.py` so a historical `KEEP`
display may be absent only when an approved, implemented essentiality record
marks it inactive and supplies a recovery pointer and replacement/no-loss
location. Unmapped `KEEP` displays must still be active.

Extend `accessibility-ledger.json` with an explicit active/inactive thesis
state, or preserve inactive records in a documented history collection.
Update `validate_structure.py` so every active graphic has exactly one active
accessibility record and every inactive retained record points to an approved
essentiality decision. Do not simply delete descriptions to make the active
graph comparison pass.

### 8.4 Derivative and asset controls

- Update `revision-ledger.json` with a new revision ID and final hashes for
  every edited chapter/appendix derivative.
- Deactivate nonessential `\input`, `\includegraphics`, table, and figure
  calls. Do not initially delete their tracked assets or source fragments.
- Keep the thesis build self-contained. No appendix source should read from a
  sibling research checkout.
- Do not rerun expensive simulations. Numerical values may be consolidated
  only from current verified tables/results. A new arithmetic summary requires
  a small auditable calculation and independent cross-check.
- Keep material-specific reuse and contribution status unchanged. Shortening
  an appendix does not establish publication permission or authorship roles.

### 8.5 No-loss reconciliation

Raw before/after counts are useful diagnostics but not acceptance criteria.
Theorem counts may fall because duplicate formal statements become proof-only
headings; display counts should fall by design; citations used solely by
inactive material may leave the compiled bibliography. Every difference must
nevertheless be classified in the essentiality map.

The final reconciliation must cover targets, formal statements, proofs,
algorithms, equations, numerical design constants, displays, citations,
negative/mixed results, limitations, and implemented/proposed status. A count
may change; an unaccounted scientific role may not.

## 9. Implementation sequence

### Gate P0: explicit approval

Approval covers the architecture, exact default display set, essentiality
grammar, source freeze, validator-first sequence, protected conclusion
register, diagnostic page envelope, and no-deletion asset policy. It does not
authorize a scientific correction, source refresh, rights assertion,
destructive Git operation, push/merge, or Overleaf synchronization unless
those actions are separately requested.

### Phase 0: synchronize and freeze

- Coordinate any Overleaf editing under `docs/WORKFLOW.md`; preserve comments
  and pending source changes.
- Fetch and verify that clean `main` equals `origin/main`; stop on divergence
  or uncommitted thesis work that overlaps the plan.
- Create a focused review branch such as
  `editorial/essential-appendices-20261028`.
- Record commit, source hashes, accepted PDF hash/page map, TeX version,
  validator counts, and active compiler graph.
- Reconfirm that the current source-refresh commits remain available without
  fetching or modifying original research working trees.

**Gate A:** exact reproducible baseline, clean branch, and no research-source
change.

### Phase 1: schema and validator support only

- Add the essentiality-map schema/validator by extending the smallest suitable
  existing validator; avoid a new framework unless separation is clearly
  simpler.
- Add backward-compatible current-inclusion handling for display and
  accessibility records.
- Add tests for an approved inactive `KEEP` display, an unapproved missing
  `KEEP` display, stale active accessibility record, body reference to an
  inactive label, missing recovery pointer, missing protected conclusion, and
  preserved historical migration marker.
- Run the current fast validation and confirm the accepted TeX/PDF content is
  unchanged.

**Gate B:** tooling/tests only, all current validators pass, no TeX source or
active compiler input changed.

### Phase 2: complete essentiality and reference map

- Generate the full structural inventory from the active graph and accepted
  `.toc`/`.aux` evidence.
- Populate every disposition, exact default display decision, body bridge,
  protected conclusion, recovery pointer, risk class, and target label.
- Build theorem/proof, label/reference, display, citation, and file-dependency
  graphs.
- Produce a concise review packet from the map rather than a second narrative
  plan.

**Gate C:** 100% active appendix-unit/display coverage; every deactivation has
recovery and no-loss rationale; high-risk theory/posterior decisions reviewed;
no TeX prose movement.

### Phase 3: Appendix C pilot

- Consolidate the MCMC and VB algorithms.
- Deactivate the two extra-cutoff figures and replace their body promise with
  the five-origin result already visible in Chapter 3.
- Preserve source/horizon, latent-scale, predictive-band, and approximation
  distinctions.
- Update essentiality, display, accessibility, and revision records.
- Build and inspect Chapter 3, Appendix C, and both neighboring transitions.

Appendix C is the optimal pilot because it tests algorithm consolidation,
figure deactivation, direct-label repair, and ledger joins with limited
algebraic risk.

**Gate D:** body-only and recovery tests pass; inactive-display validators
prove the new state; no claim or five-origin conclusion is lost.

### Phase 4: Appendices A and B

- Condense Appendix A to a statistical concordance and remove the directory
  section.
- Consolidate Appendix B around posterior target, LDVB, and synthesis.
- Preserve the software contribution, transfer-function mechanism, structured
  scale--shape approximation, MCMC reference boundary, and static shrinkage
  example.
- Repair Chapters 1 and 2 links atomically.

**Gate E:** every shared convention remains compatible; Chapter 2 still reads
as statistical software research; package-maintainer detail is absent from the
appendix unless scientifically consequential.

### Phase 5: reconstruct Appendix D

- Establish the six planned stable destination labels, including separate
  GloFAS and PriceFM support.
- Consolidate posterior and computational derivations before changing the
  empirical support.
- Apply the exact eight-display default in Section 5.6.
- Reduce the Gaussian note to exact posterior, predictive law, direct sampler,
  and Q--DESN initialization.
- Repair all 24 Chapter 4 generic bridges in the same commit series.

Use reviewable commits for: (1) posterior/model core, (2) computation and
Gaussian baseline, (3) simulation/application support, and (4) body
links/language/records. The branch may contain intermediate commits, but no
partial Appendix D state may reach `main`.

**Gate F:** target/parameterization checks pass; fixed-feature, future-input,
development-selection, composite-likelihood, rearrangement, and approximation
boundaries remain explicit; all protected Chapter 4 conclusions remain
visible.

### Phase 6: reconstruct Appendix E

- Complete the theorem/proof graph before editing formal material.
- Convert duplicate principal formal statements to proof headings linked to
  Chapter 5, while retaining full supporting result statements in Appendix E.
- Preserve the original proof content and assumptions before tightening prose.
- Apply the exact five-display default in Section 5.6.
- Retain the calibrated-policy evidence and all empirical/theoretical limits.
- Compact the proposed extensions without suggesting implementation.
- Repair all 13 Chapter 5 generic bridges.

Use reviewable commits for: (1) theory/proofs, (2) profile computation,
(3) calibration/application support, and (4) proposed extensions plus body
links/language/records.

**Gate G:** theorem/proof graph complete; no guarantee strengthened; no
proposed method appears implemented; tolerance, posterior content, prediction,
and generalized endpoint uncertainty remain distinct.

### Phase 7: global scholarly pass

- Read Chapters 1--6 continuously without opening an appendix; every argument
  must remain coherent.
- Follow every appendix link from the body; every destination must be specific
  and sufficient.
- Read Appendices A--E independently for notation, headings, and transitions.
- Remove article-supplement, migration, and internal-workflow language from
  the compiled text.
- Confirm that all claims retain assumptions, design boundaries, negative
  findings, and approximation qualifications.

**Gate H:** end-to-end body-only, recovery, statistical-style, and protected-
conclusion tests pass.

### Phase 8: release validation and handoff

- Build from a new empty timestamped output directory using
  `scripts/build.sh`.
- Run structure, manuscript, editorial, lifecycle, provenance, and release
  validators applicable to the current repository.
- Update `VALIDATION.md`, `STATUS.md`, the essentiality map, revision ledger,
  and any affected display/accessibility records.
- Inspect the full diff and compiler graph.
- Commit by appendix-sized scholarly units. Push/merge only after the local
  release candidate passes and only under the repository's explicit GitHub /
  Overleaf handoff procedure.

**Gate I:** clean timestamped release, reconciled records, systematic rendered
review, and no open blocking diagnostic. A push, merge, or Overleaf handoff is
a later explicit lifecycle action, not implied by plan approval.

## 10. Expected file impact

Listing a file does not authorize an edit. It defines the expected scope so an
implementation that touches materially more can be stopped and reviewed.

### 10.1 Manuscript files

| File/group | Expected change |
| --- | --- |
| `appendices/a-shared-conventions.tex` | Condense and retitle; preserve chapter label. |
| `appendices/b-exdqlm-technical.tex` | Reorganize around posterior, LDVB, and synthesis; preserve migration marker. |
| `appendices/c-hydrology-technical.tex` | Consolidate algorithms and deactivate additional cutoff figures; preserve migration markers. |
| `appendices/d-qdesn-technical.tex` | Major selective reconstruction and exact display-set implementation; preserve migration markers. |
| `appendices/e-mti-technical.tex` | Proof graph, computation, validation, application, and extension compression; preserve migration markers. |
| `chapters/01-introduction.tex` | Update appendix roadmap only. |
| `chapters/02-research-a.tex` | Replace generic appendix promises with topical links and match condensed support. |
| `chapters/03-research-b.tex` | Consolidated algorithm links and removal of inactive-panel promises. |
| `chapters/04-research-c.tex` | Route 24 generic links and preserve all claim qualifications. |
| `chapters/05-research-d.tex` | Route 13 generic links and establish authoritative principal formal statements. |

No change is expected in `chapters/06-synthesis.tex`, `metadata.tex`,
`notation.tex`, `preamble.tex`, or `main.tex` unless a concrete build or
navigation defect is demonstrated. Appendix order and bibliography placement
are already correct.

### 10.2 Records, validators, and tests

| File/group | Expected change |
| --- | --- |
| `docs/appendix-essentiality-map.json` | New authoritative current-inclusion/no-loss map after approval. |
| `docs/appendix-migration-map.json` | Read-only historical record; no content change. |
| `docs/display-ledger.json` | Backward-compatible current-inclusion linkage only; preserve historical disposition. |
| `docs/accessibility-ledger.json` | Preserve inactive records/history while enforcing exact active-graphic coverage. |
| `docs/revision-ledger.json` | New revision ID and final hashes for edited derivatives. |
| `docs/claim-evidence.json` | Location link only if a claim currently points to a deactivated display; no evidence-level change. |
| `docs/research-decisions.md` | Approval and any later material exception. |
| `docs/STATUS.md`, `docs/VALIDATION.md`, `docs/ASSISTANCE-LOG.md` | Phase state, final evidence, and assistance disclosure. |
| `scripts/validate_editorial_audit.py` | Join historical display disposition to approved current inclusion. |
| `scripts/validate_structure.py` | Essentiality and active/inactive accessibility invariants. |
| existing test files or one focused new test module | Positive/negative cases in Phase 1. |

`source-manifest.json`, `docs/imports/*.json`, the source-refresh record, and
research audit files should remain unchanged unless a validator requires a
non-semantic link to the new current-inclusion map. Immutable hashes and source
commits must not change.

### 10.3 Assets and generated output

- Do not delete tracked figure/table assets during this revision.
- Do not move assets merely because their compiler calls become inactive.
- Do not commit `build/`, `main.pdf`, auxiliary files, or raster review output.
- If a condensed table is created, derive it from existing tracked table cells,
  place it with the responsible chapter assets, record its provenance, and
  verify every copied value.
- The existing font-safe PriceFM derivative remains the active source if its
  regional figure is retained.

## 11. Validation and acceptance criteria

### 11.1 Scientific preservation

- Every principal Chapter 5 theorem/proposition has a mapped proof or explicit
  citation; every retained supporting result has a complete local statement
  and proof.
- The Q--DESN single-level and MQ posterior targets remain fully specified.
- The likelihood versus generalized-update distinction survives every edit.
- Approximate VB draws are not described as exact posterior draws.
- Separate quantile fits, stacked composite inference, synthesis, and a joint
  predictive distribution remain distinct.
- Calibration evidence is not upgraded to a distribution-free theorem.
- Negative and mixed findings listed in this plan remain visible.
- Proposed MTI extensions remain explicitly unimplemented and unvalidated.
- The protected conclusion register has no missing or weaker final location.
- All changed numerical summaries match the current verified source cells.

### 11.2 Reader navigation

- No body sentence points only to a large appendix when a narrower section is
  available.
- No retained appendix display is orphaned; each has an interpretive purpose
  and a nearby or body-level citation.
- No appendix begins with document-engineering language.
- Headings use sentence case and name statistical content.
- A reader can finish the body without needing derivations, but can recover
  every central derivation in one step.

### 11.3 Technical checks

- Zero undefined or multiply defined labels/citations.
- Zero missing active inputs and zero absolute server paths.
- No overfull boxes, oversized floats, clipped displays, or unexpected blank
  pages.
- All active fonts embedded and no Type 3/Type 0 regression.
- All active visuals represented in the display/accessibility records.
- Every immutable imported blob still passes the existing source audit.
- The compiler `.fls` confirms that deactivated assets are not build
  dependencies.
- Every historical migration marker remains present and every historical
  migration record retains a truthful body-level appendix bridge.
- Every implemented essentiality record matches its final source hash,
  location, active state, and recovery pointer.

Run, at minimum:

```bash
bash scripts/validate.sh --tier fast
bash scripts/validate.sh --tier chapter
bash scripts/validate.sh --tier release --audit-root "ACTUAL_IGNORED_AUDIT_ROOT"
git diff --check
```

The release command must use the already recorded ignored audit root; do not
invent a path or refresh the source clones. Log, PDF, font, page-size, label,
citation, and dependency checks must use the new timestamped release artifact.

### 11.4 Rendered review

Rasterize and inspect:

- the body-to-appendix transition;
- every appendix opening and ending;
- every retained algorithm, theorem/proof boundary, multi-page table, and
  figure;
- pages before and after each large deactivated display family;
- the Appendix D/E transition and appendix-to-bibliography transition; and
- a spread sampled at least every ten appendix pages.

### 11.5 Size outcome

The expected appendix range is 82--102 pages, implying an approximate
292--312-page full document if the body and bibliography remain stable. This
is a warning envelope, not a release gate. Exceeding it is not an automatic
failure, and falling below it is not evidence of quality. Each retained unit
outside the envelope needs an essentiality justification; each deactivated
unit needs a no-loss/recovery record. A reduction achieved by shrinking type,
compressing spacing, or creating unreadably dense tables is a failure even if
the numerical target is met.

### 11.6 Milestone review packet

At Gates D--G, generate a concise packet from the essentiality map rather than
write another plan. It should contain:

- baseline and milestone commits;
- before/after appendix outline and page count;
- disposition counts and all high-risk records;
- theorem/proof, algorithm, display, citation, label, and dependency
  reconciliation;
- protected conclusions and their final visible locations;
- body-link inventory and recovery-test result;
- validation commands/artifacts; and
- rendered pages inspected plus unresolved decisions.

Review proceeds in two passes: read the parent chapter without the appendix,
then follow every technical link needed to audit it.

## 12. Risks, stop conditions, and safeguards

| Risk | Safeguard |
| --- | --- |
| A useful qualification disappears with a table family | Record claim-changing findings before deactivation and verify them in body/retained summary |
| A proof and theorem statement drift apart | Principal body results use proof headings that reference them; supporting appendix results retain complete local statements |
| Label deletion breaks body prose | Update appendix and body link in the same commit; run reference validation after each phase |
| Compression makes an appendix denser rather than clearer | Use fewer displays and shorter derivations, not smaller type or reduced spacing |
| Historical source provenance is lost | Preserve baseline commit, import manifests, migration map, source hashes, and inactive assets initially |
| Article wording survives as internal thesis prose | Run the language scan and complete a dedicated object-level prose pass |
| Overleaf diverges from GitHub | Treat push, Overleaf pull, compile, and rendered inspection as separate verified states |

Stop the affected phase when:

- `main` or Overleaf contains unreviewed divergence;
- a source hash or audited research commit differs from the freeze;
- a proposed condensation changes a target, formula, theorem scope, numerical
  result, attribution, or evidence strength;
- the only visible location of a material limitation would disappear;
- a theorem/proof dependency cannot be reconciled confidently;
- a retained result depends on a display proposed for deactivation and no
  exact prose/replacement location exists;
- an appendix becomes shorter only through typography or unreadable density;
- a validator can pass only by deleting history or weakening a safety rule;
- build or rendered evidence contradicts the planned layout; or
- implementation would require research recomputation or a source-repository
  change not separately authorized.

Rollback uses focused commit reversal on the review branch. Do not reset,
clean, stash, regenerate source imports, or delete assets to restore a passing
state.

## 13. Recommended approval defaults

If this plan is approved, the recommended defaults are:

1. retain five chapter-linked appendices;
2. use the 82--102 page range as a diagnostic envelope, not a quota;
3. preserve all central original proofs;
4. keep one authoritative computational path per reported method;
5. retain one claim-changing sensitivity display rather than a full display
   family;
6. deactivate the 13 pages of distribution-level MTI validation tables while
   retaining the calibrated-policy and feasibility summaries;
7. reduce the Q--DESN Gaussian note to exact posterior and initialization;
8. deactivate rather than delete unused assets during the first accepted
   revision;
9. update all body links to specific appendix sections; and
10. use only object-level statistical prose in the compiled thesis;
11. use the exact Appendix C/D/E display set in Section 5.6 unless a recorded
    claim-specific exception is approved;
12. preserve the historical migration map, migration markers, import hashes,
    display decisions, and inactive accessibility descriptions;
13. add validator support for the new current-inclusion state before changing
    TeX;
14. use Appendix C as the pilot before the high-risk D/E revisions;
15. keep the current audited research-source freeze and perform no research
    recomputation; and
16. keep push, merge, and Overleaf synchronization outside the authority of
    plan approval unless separately requested.

The author confirmed these defaults without an exception. Implementation
therefore began with schema, validator, and test support, followed by the
complete essentiality map; no appendix was shortened before those gates.

The unambiguous authorization phrase for a later turn is:

> Approve the sixteen defaults in the final controlling essential-appendix
> plan. Implement Phases 0--8 subject to every gate, but do not push, merge, or
> synchronize with Overleaf unless I separately authorize that lifecycle
> action.

That authorization was supplied on 2026-10-28. The completed implementation,
release evidence, and exact page outcome are recorded in
`appendix-essentiality-review.md`, `VALIDATION.md`, and `STATUS.md`.
