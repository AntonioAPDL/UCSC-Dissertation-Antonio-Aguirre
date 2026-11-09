# FINAL controlling advisor-revision plan: November 2026 committee review

Status: **the first advisor revision was implemented and released; Bruno's
later detailed review is received, itemized, and not yet implemented**. This
document was the controlling execution plan for the first revision and now
also records how the completed work is to be continued. The item-level source of truth is
`docs/advisor-comments-ledger-20261109.md`; the original advisor files remain
ignored local evidence.

The controlling supplement for the new evidence is
`docs/bruno-revision-integration-plan-20261109.md`. It accounts for all 36
annotated pages and 116 normalized actions, distinguishes comments already
satisfied by current `main` from unresolved work, and records that Bruno's
Chapter 4 review ends at Section 4.4. Where this historical plan says that the
annotation had not arrived, the new supplement supersedes that statement.

### Implementation closeout and continuation state

The prospective language in Sections 0--8 records the frozen baseline and the
decisions under which the work was executed. It is retained for auditability;
statements there that the corrections had not started or had not been pushed
describe the planning date, not the current repository state.

| Work package | Current disposition | Principal commit or evidence |
| --- | --- | --- |
| WP0: evidence freeze | Complete | `71eda89`--`1e2d849`; advisor PDFs remain ignored and hash-identified |
| WP0A: contribution dossiers | Complete | `73e69e9` |
| WP1: chapter and appendix order | Complete | `6f7543e` |
| WP2: Corrected-3 hydrology conversion | Complete | `a840a78`, `3d3c346`, `7b0a7e7` |
| WP3: software reduction | Complete | `d9cebb7` |
| WP4: Bruno Chapter 4 annotation | Received through Section 4.4; planned | Ten annotated pages; `B4-001`--`B4-040` in the Bruno supplement; no new manuscript correction yet |
| WP5: introduction | Complete | `9174f32` |
| WP6: Chapter 5 decision and first revision | Detailed review reopened bounded work | Prior revision `63ccfe6` remains useful; 65 Chapter 5 and 11 Appendix E actions are planned in the Bruno supplement |
| WP7: abstract, attribution, disclosure, and synthesis | Complete | `d2e56b9` |
| WP8: validation and GitHub handoff | Complete | `8da8e45`, `c02299e` |

The current accepted release contains 183 US-Letter pages and passed the
19-test release gate against fixed audit clones. Before this intake, local
`main` and `origin/main` were equal at
`11984bfb89b1df1ca882bf7759b605719df4cd0d`. Bruno's later message and
annotated PDF are new evidence relative to that release; no claim is made that
the current manuscript implements them.

Two actions remain deliberately separate from the completed manuscript work:

1. Execute the received Bruno review only after the itemized plan is approved.
   The ignored file, hash, coverage boundary, 116 action items, source checks,
   work-package order, and acceptance gates are now recorded in the supplement.
2. Pull GitHub `main` into Overleaf, compile there, and compare page count and
   blocking diagnostics. A successful GitHub push is not evidence that this
   independent handoff occurred.

This planning branch is the current stopping boundary. The evidence is frozen
and the response plan is complete, but no Chapter 4, Chapter 5, or Appendix E
prose has been changed in response to the new annotation.

**Mandatory writing notice:** no manuscript work package may begin or close
without the source-fidelity, academic-writing, anti-formulaic-prose, and
candidate-review gates in Section 4.13. Surface fluency is never sufficient.

## 0. Executive diagnosis and final recommendation

The dissertation does not primarily need a sentence-by-sentence copy edit.
Four coupled issues explain most of the advisors' concerns:

1. the hydrology chapter still reflects the superseded Corrected-2 article,
   while Corrected-3 changes the structure, comparisons, numerical evidence,
   calibration discussion, limitations, and contribution statement;
2. presenting the software before the hydrologic problem forces the thesis to
   introduce methods through implementation and then repeat them in the
   application;
3. the project contributions are present but distributed across late,
   repetitive, or overly qualified prose, and personal contribution must be
   separated from collaborative project novelty; and
4. chapter order, appendices, displays, claims, citations, and provenance are
   recorded in several connected files, so editing only the visible TeX would
   leave a scientifically inconsistent dissertation.

The final recommendation is therefore a **source-led, contribution-first,
reader-facing revision**, executed in bounded work packages:

1. freeze advisor and scientific-source evidence and prepare contribution
   dossiers;
2. reorder hydrology before software in a structural-only commit;
3. rebuild the hydrology chapter from Corrected-3, retaining older prose only
   when it is both scientifically current and clearer;
4. reduce the software chapter after the hydrology chapter is self-contained;
5. incorporate Bruno's actual Chapter 4 comments when they arrive;
6. rewrite the introduction only after Chapters 2--4 are stable;
7. make an explicit first-release decision about Chapter 5; and
8. reconcile the abstract, synthesis, acknowledgments, bibliography,
   appendices, displays, provenance, and release validation.

This sequence is preferable to patching advisor comments in current page
order. It prevents repeated rewrites of Chapter 1, avoids importing a journal
article wholesale, and makes every scientific claim traceable to a fixed
source. It also preserves the useful existing thesis material rather than
starting from zero.

## 1. Objective and boundary

The next revision should make the dissertation easier for a statistician to
read, state the candidate's contributions earlier and more directly, and use
the current hydrologic article as the scientific authority. The work is not a
fresh rewrite of all four projects and is not a wholesale copy of a research
repository. Existing sound article prose, equations, results, and displays
should be reused after dissertation-level adaptation.

This planning pass performed only the following actions:

- verified the 9 November 2026 advisor email thread and the candidate's reply;
- stored the two review attachments in the ignored local `audit-inputs/`
  area, with hashes and restricted permissions;
- synchronized the thesis checkout with `origin/main` by fast-forward-only
  pull and froze the reviewed thesis commit;
- created a clean, separate audit clone of the new hydrologic source;
- compared that source with the thesis and the former Corrected-2 authority;
- normalized the advisor comments into a traceable ledger; and
- designed the implementation, validation, and decision gates below.

No chapter, appendix, abstract, acknowledgment, bibliography, display,
manifest, or compiled dissertation was changed in this pass. No research
computation was rerun. Nothing was pushed, merged, or synchronized with
Overleaf.

### 1.1 Storage and synchronization state

The advisor inputs and the planning records deliberately have different
storage boundaries:

- the two original advisor PDFs and their extracted text are private local
  inputs under the ignored `audit-inputs/advisor-review-20261109/` directory;
- this plan, the correction ledger, the status entry, and the assistance-log
  entry are committed only on local branch
  `editorial/advisor-revision-audit-20261109`; the final plan before the
  academic-writing addendum is `35d67bc...`; the addendum is recorded at the
  current documentation-only branch tip;
- GitHub `main`, local `main`, and `origin/main` remain equal at
  `07b8f0d0...`; and
- the planning branch does not exist on the remote.

Accordingly, revision work can proceed locally without importing the advisor
PDFs into Git. The safest implementation branch should be created from the
final local planning-branch tip so the ledger travels with the edits. Only
reviewed thesis source and public documentation should later be merged and
pushed; the ignored advisor files must remain local. As of the final 9
November recheck, Gmail contains Raquel's attachment message and Bruno's
sequencing message, but no newer detailed Chapter 4/5 annotation.

## 2. Frozen evidence and exact baselines

| Evidence | Frozen identity | Role |
| --- | --- | --- |
| Dissertation source | `07b8f0d0f2ee6362dc3c8030fbc2152e122f0216` on `main`, equal to `origin/main` after `git pull --ff-only` | Source baseline to revise |
| Raquel's comment document | `audit-inputs/advisor-review-20261109/thesis_comments.pdf`; SHA-256 `529de844bc6a74302ae0b50f4d4c5d2d5169db809aaa2b2ce0451dc21a9502dd` | Exact advisor action source; ignored and local only |
| Thesis PDF reviewed by Raquel | `audit-inputs/advisor-review-20261109/UCSC_Dissertation___Antonio_Aguirre.pdf`; SHA-256 `7145eae7fa840801d8526155327ae2ab81aafaebb002d8496eea6faa5fb6eaa9`; 221 pages | Exact commented baseline; ignored and local only |
| Former hydrologic authority | `AntonioAPDL/Evironmetrics---REVISED-DOC-Corrected-2` at `1272bfc10442a28add5a4c74ff641e9b9a8e9666` | Historical source presently recorded by the dissertation |
| New hydrologic authority | `AntonioAPDL/Evironmetrics----Corrected-3` at `c0bfccaa7cec698c016626ee30187f18a56d495c` on clean `main` | Scientific source for the revised hydrology chapter |
| New article release record | 31 pages; 10 submitted tables, 7 figures, and 2 algorithms; source hashes in `docs/presentation_revision_release.json` of the source repository | Validation and asset-selection evidence |
| Advisor correspondence | Raquel's review, Bruno's sequencing/schedule advice, and the candidate's reply, all dated 9 November 2026 | Workflow evidence; full email text is not copied into the public repository |

The attached 221-page thesis has the same page count and source family as the
recorded committee release, but it is not byte-identical and mathematical
glyphs extract differently. The attached PDF, not a locally reconstructed
copy, is therefore the review baseline.

The Corrected-3 audit clone was read only. Its default `python3` check fails on
muscat because that executable is Python 3.6.8; `python3.11` is the compatible
interpreter. The compact-table check passes under Python 3.11. The predictive
figure check reaches R rendering but cannot render PNGs in this headless shell
because R defaults to the unavailable Xlib device, even though Cairo support
is present. This is an environment-specific validation gap, not evidence of a
scientific or source-tree failure. The source repository remains clean.

## 3. Assessment of the candidate's email reply

The reply was appropriate. It acknowledged the feedback, accepted the advised
sequence (Chapters 2 and 3, then Chapter 4 after Bruno's notes, then Chapter 1,
then Chapter 5), did not promise an unrealistic Wednesday completion, and
alerted the advisors that the hydrologic article had been restructured.

No corrective follow-up email is needed now. The next useful update should be
sent only after one of these events:

1. Bruno's detailed Chapter 4/5 comments arrive;
2. Chapters 2 and 3 have a reviewable revision and the remaining schedule can
   be estimated; or
3. a decision is required about omitting Chapter 5 from the first submission.

That update should identify Corrected-3 as the hydrologic source and state the
chosen Chapter 5 submission strategy. The journal rejection itself does not
need to be narrated in the dissertation; it matters here because it changes
the authoritative manuscript, not because it is a scientific result.

## 4. Controlling editorial and scientific decisions

### 4.1 Source hierarchy

When evidence conflicts, use this order:

1. Corrected-3 at the fixed commit above for hydrologic model statements,
   numerical results, display content, qualifications, and appendix details;
2. Raquel's comments for exposition, order, definitions, emphasis, and the
   committee-facing level of detail;
3. the existing dissertation for cross-project terminology, thesis formatting,
   labels, citations, and material already integrated from other projects;
4. the older Corrected-2 source only for provenance or material intentionally
   retained and explicitly shown not to be superseded.

The new article does not automatically overwrite the thesis. Each scientific
claim and asset must be mapped. Conversely, unresolved wording in the old
chapter must not survive merely because it was already adapted once.

### 4.2 Chapter order

The recommended visible order is:

1. Introduction;
2. hydrologic correction and predictive synthesis;
3. statistical computation and the `exdqlm` software;
4. Q--DESN;
5. mean-tilted intervals, subject to the submission gate below;
6. synthesis and conclusions.

This order makes the statistical problem and methodological contribution
precede the software implementation. It also permits the new Chapter 3 to
refer back to the model and distributions instead of defining them twice.
The corresponding technical appendices should appear in the same reader order.

During implementation, change the compiler input order first and keep the
physical filenames stable unless a later, purely mechanical rename has a clear
maintenance benefit. This minimizes provenance churn in import manifests and
revision ledgers. Labels and cross-references, not filenames, must express the
new reader-facing numbering.

### 4.3 Hydrology source conversion

The current hydrology chapter is a 508-line derivative of an 825-line
Corrected-2 manuscript, plus a 58-line curated technical appendix. Corrected-3
has a 398-line main article and a 370-line integrated appendix. Its main source
is not a minor edit: relative to the former article root it has 195 inserted
and 622 deleted lines, a new problem-first structure, compact evidence tables,
new external comparisons and calibration evidence, and sharper limitations.

The optimal approach is therefore **source-led reconciliation**, not local
sentence patching and not blind replacement:

- use the six main article sections as the chapter spine;
- adapt journal navigation and boilerplate to dissertation prose;
- retain the article's three explicit contributions near the opening;
- retain the source-aware model, full-distribution quantile synthesis, and
  joint scale--skewness VB development as distinct contributions;
- use the current comparison claims, including the five-origin, horizon,
  transformed-scale, discharge-scale, calibration, and approximation limits;
- import only claim-bearing main assets and essential appendix material;
- keep code, data, fitted objects, generators, and research computation in the
  external repository; and
- update the source/import/claim/display records only after the chapter agrees
  with the fixed source commit.

Corrected-3 already resolves many of Raquel's Chapter 3 concerns: ordinary
equation sizing, scalar scale/skewness notation, definitions of `c` and
`epsilon`, the purpose of stacked notation, predictive-draw notation, and a
plain statement that smaller CRPS is better. It only partially resolves the
product-family example, the labeling of all seven displayed component
equations, the transformed scale/skewness coordinates in the Laplace--Delta
description, and the time index inside the isotonic-regression optimization.
Those partial items remain open in the ledger.

### 4.4 Asset policy for the hydrology chapter

The current article's main-body evidence is the starting default:

- tables: aggregate external/Bayesian comparison, pooled quantile loss, and
  calibration;
- figures: historical river-flow context, representative predictive synthesis,
  and quantile reliability.

Appendix candidates are the origin-level score table, compact component
comparison, origin-level quantile loss, exact-score sensitivity,
discharge-scale scores, origin coverage, covariate-effect table, two compact
remaining-origin forecast figures, and the minimal computation required to
interpret the VB claims.

This is a selection list, not an instruction to import all 17 article assets.
Each appendix candidate must pass three tests: it supports a claim retained in
the thesis, it is not already summarized adequately in the body, and a
committee reader would lose material understanding without it. Repository-only
items in the article's publication manifest remain external by default. This
preserves the dissertation's prior appendix-curation objective.

### 4.5 Software chapter reduction

After the hydrology chapter is independent, rewrite the software chapter as a
software and computation contribution, not a second methods chapter. It should:

- identify the original package/method foundations and the candidate's
  documented additions without inventing task allocations;
- emphasize `exdqlmLDVB`, prediction, diagnostics, synthesis, transfer-function
  support, and static exAL regression with Nishimura--Suchard priors;
- define software interfaces in ordinary language before using R-specific
  terms;
- remove redundant distribution and state-space derivations now established
  by Chapter 2;
- replace version trivia with the scientifically relevant differences and
  contribution provenance; and
- keep a small set of examples that demonstrate distinct capabilities.

The recommended default is to remove the full Big Tree software example and
replace it with a short cross-reference to the hydrologic chapter and the
external package vignette. It is the example with the greatest overlap after
the reorder. Lake Huron preserves multi-quantile prediction/synthesis,
Sunspots preserves the DQLM/exDQLM computation comparison, and the static
simulation preserves the otherwise hidden shrinkage-prior contribution. This
choice should be confirmed before implementation.

### 4.6 Contribution audit and presentation standard

The dissertation's contribution case is a primary scholarly requirement, not
an ornamental front-matter paragraph. It must be reconstructed from the
authoritative manuscripts, prior versions, directly relevant repositories,
and central antecedent literature before Chapter 1 is rewritten.

The audit is bounded to evidence that can change a contribution claim:

| Project | Current authority | Prior/related evidence to compare | Antecedent boundary that must remain explicit |
| --- | --- | --- | --- |
| Hydrology | Corrected-3 `c0bfccaa...` | Corrected-2 `1272bfc...`, publication-package/revision records, San Lorenzo reproducibility source, `exdqlm` 1.1.0 role | exAL and exDQLM foundations are inherited; the project contribution is source-aware correction/synthesis, full-distribution synthesis, model-specific VB development, and the bounded hydrologic evaluation |
| `exdqlm` | JSS article `98cec593...`; package support `e51045a...` | earlier article/package version records and the hydrology dependency graph | Yan et al. supply exAL/static foundations; Barata et al. supply exDQLM, original MCMC/ISVB, and transfer foundations |
| Q--DESN | thesis authority `aa613b05...` | legacy Version-2 only for lineage and superseded-claim checks | ESN/DESN feature construction and quantile-regression antecedents must be credited; the project contribution concerns the Bayesian quantile formulations, computation, and evaluated applications |
| MTI | RQR `4223c6a...`; extensions `f345d946...` | earlier tolerance-procedure language only to identify superseded claims | residual-product, generalized-Bayes, and tolerance-interval antecedents must be separated from the mean-preserving characterization, tilt family, calibrated procedure, and proposed extensions |

Do not audit the many unrelated or exploratory worktrees merely because they
exist. Inspect an older branch or related repository only when an authority
file, manuscript, response document, or central claim identifies it as needed
to establish lineage, authorship, or a scientific difference.

For each project, prepare a contribution dossier with six fields:

1. **Statistical problem and literature gap.** What inferential or
   computational problem was not adequately addressed by the cited literature?
2. **Inherited foundation.** Which models, distributions, algorithms, or
   criteria were already available, and who developed them?
3. **Distinct project contribution.** What model, computational method,
   inferential construction, software capability, or empirical design is added?
4. **Candidate-specific evidence.** What do author lists, package metadata,
   Git history, contribution statements, response documents, and confirmed
   collaborator records establish about Antonio de Leon's role?
5. **Evidence supporting the contribution.** Is support mathematical,
   computational, simulation-based, or empirical, and under what design?
6. **Boundary.** What is not proved, not evaluated, inherited, proposed, or
   still work in progress?

Three different statements must then be written without duplication:

- a concise dissertation-level contribution map early in Chapter 1;
- a precise project-level contribution paragraph near the beginning of each
  research chapter; and
- a candidate/collaborator attribution statement in the acknowledgments.

Project-level contributions may be stated firmly when the manuscript supports
them. Candidate-specific task allocation must not be inferred from first or
corresponding authorship alone. The current records establish that Antonio de
Leon is first author on all four project lines, corresponding author on the
hydrology article, and a package author for `exdqlm`; detailed conceptual,
theoretical, computational, empirical, and writing allocations remain to be
confirmed. Until confirmed, use collective project language rather than weak
or vague prose, and do not replace missing evidence with excessive caveats.

For the current Chapter 3 / proposed Chapter 2 hydrology project, the
contribution paragraph should be organized around the three claims already
stated in Corrected-3:

1. a shared dynamic quantile process with source-specific discrepancies for
   gauge observations, retrospective products, and issued ensembles with
   different horizons;
2. synthesis of full predictive distributions from separate quantile fits,
   including their tails, into a nondecreasing marginal quantile function; and
3. a Laplace--Delta variational method with joint non-conjugate scale and
   skewness updates for the extended DQLM.

The five-origin San Lorenzo analysis is evidence for these developments under
the stated products, horizons, and evaluation design; it is not itself a
universal methodological claim. Corrected-3 should provide the main prose and
current numerical evidence, while Corrected-2 is used only to recover useful
exposition that is scientifically consistent and not superseded.

### 4.7 Thesis-language and statistical-style standard

All revised prose must use conventional statistical terminology and a
committee-facing thesis voice. Apply these controls paragraph by paragraph:

- state the statistical object, assumptions, inferential target, method, and
  evidence directly;
- replace internal workflow words such as “pipeline,” “authority chain,”
  “evidence boundary,” “target-first,” “frozen procedure,” and “deployment”
  when a standard statistical statement conveys the meaning;
- avoid promotional artificial-intelligence or engineering framing;
- retain software, algorithm, neural-network, echo-state-network, and
  computational terminology only where it names an actual method or research
  contribution, and define it statistically;
- do not use repository, branch, manifest, implementation, or validation-log
  language in reader-facing prose unless reproducibility genuinely requires
  it;
- prefer “method,” “model,” “estimator,” “posterior approximation,”
  “predictive distribution,” “simulation design,” and “empirical comparison”
  over vague system language;
- state advantages before limitations without overstating novelty or evidence;
  and
- preserve negative and mixed findings when they qualify the contribution.

The final style audit must scan the compiled dissertation, not only the TeX
source, and manually review every flagged occurrence in context. Necessary
terms in the `exdqlm` software chapter and Q--DESN methodology are not removed
mechanically.

### 4.8 AI-assistance disclosure: candidate statement and accuracy control

The candidate has supplied the intended substantive boundary:

- AI-assisted tools were used for selected code debugging, not for autonomous
  or complete implementation of the scientific code or research analyses;
- they were not used to formulate the statistical methodology or to derive
  mathematical results or proofs;
- they were not used to identify, select, or evaluate the scientific
  literature; and
- writing assistance was intended to improve grammar, clarity, and
  readability rather than replace the candidate's scientific authorship.

The final acknowledgment must also agree with the repository assistance log.
That log records document organization, source/provenance auditing, citation
and bibliography consistency checks, editorial restructuring, LaTeX/build
tooling, and validation. These activities do not amount to scientific
literature search, proof derivation, generation of research results, or
independent implementation of the statistical analyses, but they are broader
than grammar correction alone. Omitting them while saying “only debugging and
grammar” would create an avoidable discrepancy.

Use the following distinctions when finalizing the statement:

| Excluded scientific use | Permitted supporting use that should not be confused with it |
| --- | --- |
| identifying, selecting, or evaluating scientific literature | checking citation keys, bibliography consistency, and formatting for sources already selected by the author/project manuscripts |
| originating mathematical arguments or deriving proofs | checking notation, transcription, cross-references, and consistency against authoritative source manuscripts |
| independently designing or implementing the statistical methods and analyses | limited debugging plus dissertation import, build, validation, and provenance tooling |
| authoring the scientific contributions or interpretations | editorial suggestions concerning organization, grammar, clarity, consistency, and readability, all subject to author review |

Recommended acknowledgment wording for later author/advisor review:

> AI-assisted tools were used in a limited supporting role to help debug
> selected code and to review the organization, grammar, clarity, consistency,
> and readability of the dissertation. They were not used to formulate the
> statistical methodology, derive mathematical results or proofs, identify or
> evaluate the scientific literature, independently implement the research
> analyses, or generate the reported results. The author reviewed and verified
> all code changes, references, mathematical statements, analyses,
> interpretations, and final text and takes responsibility for the content of
> the dissertation.

This wording is a planning draft, not implemented front matter. Before it is
inserted, the candidate should confirm that “reviewed and verified all” is
factually accurate and ask the advisors whether they prefer a shorter form.
The disclosure should be direct and proportionate, without discussing the
perceived reliability of AI systems or sounding defensive.

### 4.9 Exact hydrology reconciliation blueprint

Corrected-3 supplies the scientific spine, not a block of text to paste. The
following crosswalk fixes what each source section should become in the
reader-facing dissertation.

| Corrected-3 unit | Thesis destination and purpose | Required adaptation | Advisor/quality controls |
| --- | --- | --- | --- |
| Introduction | New Chapter 2 opening | Preserve the river-flow problem, literature gap, and three contributions; remove journal navigation and article-status language; distinguish collective project contributions from the candidate's confirmed role. | `G-02`, `G-03`, `P-01`--`P-04` |
| Forecasting setting and data | Problem, products, observations, and covariates | Define a product family concretely; state time support, horizons, forecast-member notation, transformations, and the status of supplied future covariates. Move catalogs and extraction details to citations or the external reproducibility source. | `C3-01`, `C3-03`, `C1-12` |
| Bayesian correction and predictive synthesis | Core statistical method | Retain the exAL target, seven component relations, source-specific discrepancies, prior/discounting summary, VB-LD idea, and distributional synthesis. Use ordinary-size equations, label only independently referenced relations, define all symbols on first use, and distinguish conditional, posterior predictive, and synthesized quantiles. | `C3-02`--`C3-08`, `C3-11`, `C3-12`, `C3-14` |
| Application specification and evaluation | Reproducible empirical design | Retain model components, quantile grid, five fixed origins, 28-day/common-eight-day comparisons, external baselines, calibration, and scoring definitions. State that smaller CRPS is better and keep transformed- and discharge-scale results distinct. | `C3-09`, `C3-10`, `C3-13`, `P-07` |
| Results | Main evidence | Lead with supported findings, then heterogeneity and failures. Preserve the non-uniform origin/horizon results; do not turn a pooled comparison into a universal superiority claim. | `G-02`, `P-04`, `P-07` |
| Discussion and conclusions | Scope, limitations, and implications | State what the model and evaluation establish, then limitations: five origins, archive constraints, supplied covariate paths, conditional residual independence, unquantified VB approximation error, and no matched full-model MCMC benchmark. | `C3-09`, `C3-10`, `P-07` |
| Integrated article appendices | Curated hydrology technical appendix | Retain only definitions, computational details, or secondary evidence required to verify a claim in the chapter. Do not reproduce the article appendix wholesale. | Appendix essentiality rule below |

The main body should initially retain Corrected-3's six principal displays,
because each answers a distinct committee-facing question:

| Source asset | Default thesis disposition | Reason |
| --- | --- | --- |
| `main_aggregate.tex` | Retain and restyle | Establishes pooled full-distribution performance against Bayesian variants and external references. |
| `main_quantile_loss.tex` | Retain and restyle | Shows that lower-tail/central and upper-tail behavior differ across AL and exAL rather than supporting one uniform winner. |
| `main_calibration.tex` | Retain and restyle | Prevents a score-only argument and makes undercoverage visible. |
| `site_context_usgs.png` | Retain existing byte-identical thesis copy | Defines the response record and hydrologic scale. |
| `predictive_synthesis_2022_12_25.pdf` | Import the current vector figure | Makes the distributional-synthesis output interpretable at one representative origin. |
| `no_refit_quantile_reliability.png` | Import | Provides quantile-level calibration evidence not duplicated by the aggregate score table. |

The hydrology appendix should target **four to six pages and must not exceed
eight pages without a written claim-based exception**. Its default empirical
content is limited to three compact tables:

1. `si_origin_crps.tex`, because pooled means conceal material origin and
   horizon heterogeneity;
2. `si_component_comparison.tex`, because the chapter makes a structural
   contribution and must show what is lost when major components are removed;
   and
3. `si_discharge_score.tex`, because the main scores use transformed discharge
   and the original-scale comparison materially qualifies the eight-day
   conclusion.

By default, omit the appendix quantile-loss table (duplicated by the pooled
main table), exact-score sensitivity table (rankings can be summarized in one
sentence if retained as a claim), origin-coverage table (aggregate calibration
and the reliability figure already establish the limitation), the coefficient
table (unless a covariate-interpretation claim survives), historical-input
figures, and four additional origin plots. The external article repository
preserves these materials. A display may be restored only if a retained thesis
claim cannot be evaluated without it.

The technical appendix should contain a compact version of only the following:

- stacked state/selectors needed to interpret the actual filtering problem;
- the forecast-window covariance prior when cited by the empirical
  specification;
- numerical predictive-synthesis conventions that affect intervals or scores;
- the unconstrained scale/skewness parameterization, Laplace--Delta moment
  approximation, and a concise VB update algorithm supporting the third
  contribution; and
- enough EMOS definition to identify the comparator, preferably in prose or a
  short formula rather than a full optimization derivation.

Remove the current source-indexed MCMC algorithms and parameter-summary blocks
from the hydrology appendix unless a final Chapter 2 claim explicitly uses
them. Corrected-3 does not report a matched full-model MCMC comparison; keeping
an extended MCMC appendix would suggest evidence that the current study does
not provide. Standard seasonal-rotation algebra, data-source catalogs, repeated
exAL derivations, and exhaustive coordinate updates should also remain in the
external source or be cross-referenced to the single thesis location where
they are genuinely needed. Superseded migration and display records must be
marked as such rather than erased.

### 4.10 Numerical and inferential claim controls for hydrology

The revised chapter, introduction, abstract, and synthesis must agree on the
following bounded statements from Corrected-3:

- exAL-M-T1 has pooled transformed-scale CRPSS of 0.68601 over 28 days and
  0.58967 over the common eight-day horizon relative to seasonal climatology;
  rounded percentage statements must be generated from these recorded values;
- its central 95% predictive intervals cover 123/140 cases over 28 days and
  29/40 over eight days (87.9% and 72.5% after rounding), so a favorable CRPS
  does not imply nominal calibration;
- on the discharge scale, exAL-M-T1 is best among the listed 28-day methods,
  while raw NWS has the lowest aggregate eight-day CRPS; the transformed-scale
  and discharge-scale conclusions must not be conflated;
- origin-level results are heterogeneous: GloFAS EMOS is best at the May 2022
  28-day origin, and raw NWS is best at two eight-day winter origins; and
- approximately two hours is a recorded representative combined VB
  fit/forecast time under named conditions, whereas “several weeks” is an
  expectation for MCMC, not a measured matched benchmark. Predictive evidence
  does not validate the VB posterior approximation itself.

Before drafting results, create a machine-readable crosswalk with one record
per retained claim: thesis location, source file/label, source commit, exact
value or qualitative boundary, transformation/horizon/origin, and destination
display. A number should not be copied independently into multiple files;
each occurrence must point to the same claim record.

### 4.11 Contribution dossiers and thesis-level presentation

The contribution audit must produce four evidence dossiers by updating the
existing research-audit records, not by adding an unrelated planning system.
Each dossier must separate three levels:

1. **antecedent literature**: what was already known or available;
2. **collaborative project contribution**: what the manuscript and fixed
   evidence establish; and
3. **candidate-specific role**: what author records and explicit
   candidate/coauthor confirmation support.

The provisional project-level formulations to test against the evidence are:

- **Hydrology:** source-aware dynamic quantile correction for gauge,
  retrospective, and issued-ensemble products; full-distribution synthesis
  across separate quantile fits; and joint scale--skewness Laplace--Delta VB,
  evaluated in the bounded five-origin San Lorenzo study.
- **`exdqlm`:** an integrated statistical-computing interface for established
  exAL/exDQLM foundations, including the documented LDVB development,
  prediction, diagnostics, synthesis, transfer-function support, and static
  shrinkage regression. The exact candidate role in design, implementation,
  testing, examples, and writing must be confirmed rather than inferred.
- **Q--DESN:** Bayesian single- and multi-quantile regression built on fixed
  deep echo-state features, with AL/exAL formulations, model-specific
  computation, crossing assessment, and bounded simulation/application
  evidence. ESN/DESN feature construction and quantile-regression antecedents
  must remain explicit.
- **MTI:** characterization of the mean-preserving interval within a
  retained-mean tilt family and a calibrated profiled tolerance procedure,
  with proved, simulated, empirical, and proposed-extension claims clearly
  separated. Work-in-progress extensions must not be presented as established
  results.

Implementation outputs are: an updated contribution matrix in
`docs/research-audit.md`, an updated source-to-chapter map in
`docs/chapter-plan.md`, any private role-confirmation notes under ignored
`audit-inputs/`, one concise contribution map early in Chapter 1, one precise
paragraph near each research-chapter opening, and one collaborator/assistance
statement in the acknowledgments. Chapter 6 should synthesize relationships
and limitations rather than repeat all four contribution paragraphs.

### 4.12 Exact file and dependency map

The eventual revision must treat the following as one connected change set.
“Review” does not mean every file must change; it means the file must be
checked and either updated or explicitly recorded as unaffected.

| Change class | Files/records to review | Required outcome |
| --- | --- | --- |
| Chapter order | `main.tex`; appendix input order | Hydrology then software; hydrology technical appendix then software appendix; physical filenames and stable labels retained during the first pass. |
| Thesis framing | `chapters/01-introduction.tex`, `chapters/06-synthesis.tex`, `frontmatter/abstract.tex` | Contributions, chapter numbers, numerical claims, and statistical terminology agree with the revised chapters and Chapter 5 release decision. |
| Research chapters | `chapters/03-research-b.tex` (new visible Chapter 2), `chapters/02-research-a.tex` (new visible Chapter 3), then Chapters 4 and 5 as gated | Source-led hydrology conversion, software reduction, and advisor-specific revisions without uncontrolled rewriting of sound material. |
| Appendices | `appendices/a-shared-conventions.tex`, `appendices/c-hydrology-technical.tex`, `appendices/b-exdqlm-technical.tex`; later D/E only if their chapters change | One necessary location per derivation/detail; short body bridges; no superseded MCMC implication or duplicated distribution theory. |
| Attribution/disclosure | `frontmatter/acknowledgments.tex`, `docs/ASSISTANCE-LOG.md` | Remove dependence on chapter-opening notices; accurately credit collaborators and state proportionate AI-assisted support. |
| Notation/citations | `notation.tex`, `references.bib`, `docs/bibliography-map.json` | First-use definitions, consistent symbols, and DOI/title-based deduplication of Corrected-3 references using the thesis namespace rather than blind BibTeX concatenation. |
| Hydrology assets | `figures/ch03-environ/`, `tables/ch03-environ/` | Import only approved assets; retain byte-identical copies where hashes match; deactivate superseded assets without losing provenance. |
| Source authority | `source-manifest.json`, `docs/source-register.json`, `docs/source-snapshots.json`, ignored `source-manifest.local.json` | Replace Corrected-2 as current hydrology authority with Corrected-3 at `c0bfccaa...`; retain Corrected-2 as historical lineage only. |
| Claim/import provenance | `docs/claim-evidence.json`, `docs/imports/ch03-environ.json`, `docs/revision-ledger.json` | Every retained prose/display item maps to the correct source commit and current thesis derivative; obsolete records receive an explicit disposition. |
| Display/appendix control | `docs/display-ledger.json`, `docs/accessibility-ledger.json`, `docs/appendix-essentiality-map.json`, `docs/appendix-essentiality-review.md`, `docs/appendix-migration-map.json`, `docs/editorial-issues.json`, `docs/editorial-review.md` | Active labels and graphics match the compiler graph; removed items are marked inactive/superseded with recovery evidence; every retained appendix unit has a claim-based justification. |
| Academic-writing control | Verified version-0.2 style profiles; `docs/editorial-issues.json`; `docs/editorial-review.md`; compiled PDF text | Every edited unit passes the Section 4.13 four-pass gate; contextual flags are adjudicated rather than mechanically replaced; disclosure and necessary statistical terminology remain intact. |
| Status and validation | `docs/STATUS.md`, `docs/VALIDATION.md`, this plan and correction ledger | Record source identities, decisions, completed work packages, test results, rendered review, remaining advisor items, and release identity. |

The old `ch03-environ` directory and manifest identifiers may remain as stable
internal identifiers even after the chapter becomes reader-facing Chapter 2.
Renaming them during a scientific revision would create unnecessary hash and
provenance churn. Reader-visible numbering must come from compiler order and
labels, not storage names.

### 4.13 Binding academic-writing and anti-formulaic-prose gate

Every future manuscript correction is governed by the repository-supplied
*Academic Writing Style Profile for AI-Assisted Statistical Writing*, version
0.2. The verified copies at
`SRC-QDESN-LEGACY:Academic_Writing_Style_Profile_v0.2.md` and
`SRC-RQR:STYLE_PROFILE.md` are byte-identical (SHA-256
`b9483cf55e108f5615c203dfff6c0940b7ecc5c001aaad679507004b70352513`).
The current Q--DESN authority repository does not itself contain that profile;
the verified profile is therefore a cross-project writing standard, not a
scientific source for Q--DESN claims.

The precedence order is: scientific correctness and fixed evidence; explicit
advisor requirements; thesis-specific terminology and contribution controls;
then the style profile. The profile is not a phrase template. No sentence or
paragraph structure should be copied from its exemplars, and a stylistic edit
may not change a claim, equation, citation, interpretation, or evidence
boundary.

For this plan, “anti-AI writing check” means a check against generic,
promotional, formulaic, or statistically empty prose. It is **not** an attempt
to defeat an AI detector, conceal assistance, or remove the accurate disclosure
in Section 4.8. Automated AI-authorship scores are not an acceptance criterion:
they are unreliable for mathematical and technical writing. Acceptance depends
on source-grounded meaning, paragraph-level human review, and the candidate's
approval of the final prose.

#### Required academic-writing contract

Every revised paragraph must have one identifiable primary function:
motivate, define, distinguish, derive, specify, report, interpret, qualify, or
connect. It must also satisfy the relevant controls below.

| Prose function | Required content |
| --- | --- |
| Motivation/gap | Name the statistical or scientific problem, what existing work provides, and the precise unresolved inferential, modeling, or computational object. |
| Contribution | Name the model, inferential construction, computational method, software capability, theorem, or empirical design; credit antecedents; avoid novelty adjectives. |
| Model/mathematics | Define data, conditioning information, target, parameters, latent quantities, dimensions/support, likelihood or loss, and priors before use; introduce and interpret every important display. |
| Computation | State the exact target before MCMC/VB/Laplace--Delta; distinguish equivalent augmentation from approximation; name factorization, convergence evidence, and uncertainty limitations. |
| Simulation/application | State the goal, data or DGP, preprocessing/information set, competitors, metric, horizon/split, and limitation before interpreting performance. |
| Results | Tie each claim to the exact design and metric; separate score, calibration, sharpness, parameter uncertainty, predictive uncertainty, and approximation accuracy. |
| Discussion | State the supported contribution first, then design-specific evidence, exact limitations, and technically concrete future work. |
| Appendix/caption | Orient the reader to the body claim or equation supported; avoid derivation dumps, file-history narration, and captions that merely name the display. |

The default voice is precise, restrained, mathematically clear, statistically
mature, explanatory, and non-promotional. First person is permitted for genuine
modeling, inferential, and evaluative choices. It should not be removed merely
to sound formal. Existing article prose should be preserved when it already
meets these standards; editing must not homogenize four projects into one
repetitive synthetic voice.

#### Patterns that require contextual review

The following are flags, not mechanical deletion rules:

- broad openings about a “data-driven world,” rapid data growth, modern
  challenges, or the power of machine learning;
- unsupported modifiers such as *novel*, *robust*, *powerful*, *flexible*,
  *scalable*, *comprehensive*, *seamless*, *crucial*, or *state-of-the-art*;
- vague verbs such as *leverage*, *harness*, *enhance*, *facilitate*,
  *underscore*, or *demonstrate* without a named mechanism or evidence;
- generic nouns such as *framework*, *pipeline*, *architecture*, *system*, or
  *workflow* where model, likelihood, prior, estimator, approximation,
  algorithm, software interface, or evaluation protocol is more exact;
- stock transitions such as “building on these insights,” “to this end,” “in
  light of these considerations,” and “taken together” when they do not state
  the logical connection;
- formulaic “not only ... but also ...,” repeated three-part slogans,
  excessive roadmap prose, consecutive sentences beginning with “we,” or a
  repeated sentence rhythm;
- self-conscious topic sentences about “this paper,” “this work,” “this
  chapter,” or “this supplement” when the statistical object can be the
  subject;
- citation chains that do not explain what prior work provides and what gap
  remains;
- generic equation introductions, product-style algorithm descriptions,
  leaderboard simulation language, application overclaims, or limitations
  that could apply to any study; and
- fluent sentences that omit an assumption, conditioning set, approximation,
  comparator, metric, uncertainty statement, or study boundary.

Legitimate field terms are retained when they name the scientific object:
artificial intelligence in the disclosure, machine learning in a genuine
literature classification, deep echo-state network, reservoir, software,
algorithm, architecture of an actual neural model, and computational scaling.
Each must be used precisely rather than promotionally.

#### Four-pass acceptance procedure for every edited unit

1. **Pre-edit audit:** record the paragraph/section purpose, controlling
   advisor item, scientific source, claim boundary, and reason an edit is
   needed. Structural and scientific problems are resolved before copyediting.
2. **Controlled revision:** preserve the author's sound article prose and
   change only what is required for accuracy, integration, duplication,
   notation, thesis voice, or the advisor comment. Do not invent citations,
   results, roles, or interpretation.
3. **Source and language audit:** compare every changed claim/equation with its
   fixed source; run a contextual phrase scan for the patterns above; and
   inspect every hit manually. The scan produces candidates, never automatic
   replacements or proof of AI authorship.
4. **Reader and voice review:** read each changed paragraph in context and the
   compiled section aloud or with equivalent close review. Confirm that the
   paragraph performs one logical function, sentence lengths/functions are not
   mechanically repetitive, transitions state real relationships, and the
   result still sounds like the surrounding statistical work. The candidate
   must approve contribution, interpretation, and disclosure wording.

Use the existing `docs/editorial-issues.json` and `docs/editorial-review.md` to
record the pre-edit and post-edit style disposition; do not create a separate
unconnected style framework. Each work-package review packet must list: files
and sections reviewed, flagged phrases with contextual dispositions, claims or
equations rechecked, changes rejected because they weakened specificity, and
remaining author/advisor decisions. A work package cannot close on grammar or
fluency alone.

## 5. Ordered implementation work packages

### WP0 — Freeze the revision inputs

- Confirm at the start of implementation that no later advisor attachment
  supersedes Bruno's detailed 9 November annotated review.
- Verify the version and hash of the two writing-style profiles and record any
  later author-supplied replacement before prose editing begins.
- Fetch Corrected-3 and record a new commit only if the author explicitly says
  a later commit is authoritative; otherwise keep `c0bfccaa...` fixed.
- Record ignored local source paths and original-tree guards.
- Recheck `origin/main` for divergence, then create the revision branch from
  the final planning-branch tip so the controlling plan and ledger are present.
- Capture before-state hashes for all active hydrology prose, assets, and
  public provenance records. Do not fetch, checkout, clean, or build inside an
  original research working tree.

Acceptance: exact source commits, attachment hashes, and dirty states are
recorded; the revision branch contains no unexplained pre-existing edits; no
original research checkout has changed.

### WP0A — Build the contribution dossiers before drafting

- Read the contribution, novelty, discussion, acknowledgment, and limitation
  sections of every current authority listed in Section 4.6.
- Compare the current authorities with only the named prior versions and
  directly relevant antecedents.
- Reconcile the existing research audit, source manifest, claim ledger,
  package metadata, and revision history.
- Prepare one source-cited antecedent/contribution/evidence matrix per project.
- Present the candidate-specific role fields for confirmation rather than
  filling them by inference.
- Draft a one-paragraph contribution statement for each project and a concise
  dissertation-level synthesis, but do not insert them into the thesis until
  the scientific wording has been reviewed.
- Update the existing `docs/research-audit.md` and `docs/chapter-plan.md`; keep
  unconfirmed personal role details in ignored local records until approved.

Acceptance: every contribution phrase identifies its evidence, inherited
foundation, support level, and limitation; no contribution rests only on a
repository name, commit date, or author order.

### WP1 — Reorder Chapters 2 and 3 without rewriting content

- Change body and corresponding appendix input order.
- Audit every chapter/appendix number, forward/back reference, list entry,
  contribution statement, abstract reference, and synthesis reference.
- Build and validate this structural commit separately.
- Keep `chapters/02-research-a.tex`, `chapters/03-research-b.tex`, existing
  labels, and `ch02`/`ch03` provenance identifiers unchanged in this work
  package. Compiler order, not filename renaming, establishes visible chapter
  numbers.

Acceptance: the PDF has the intended order; every reference resolves; no
scientific wording or number changes in this work package.

### WP2 — Rebuild the hydrology chapter from Corrected-3 plus the advisor overlay

1. Make a section/claim/display crosswalk from Corrected-3 to the new Chapter 2.
2. Compare Corrected-3 with Corrected-2 paragraph by paragraph. Retain older
   exposition only when it improves thesis readability, agrees with the new
   scientific authority, and is not superseded by a current result or limit.
3. Reconcile the model and notation before touching results.
4. Establish the three-part contribution statement in Section 4.6 against the
   antecedent map and candidate-role evidence.
5. Apply every `C3-*` item in the ledger, including those still partial in the
   new article.
6. Import/adapt the three principal result tables and three principal figures
   in Section 4.9; retain existing bytes when the source and thesis hashes
   already agree.
7. Rebuild the hydrology appendix to the four-to-six-page target in Section
   4.9. Use the three-table default and restore an omitted item only through a
   written claim-based exception.
8. Reconcile numerical claims across the chapter, abstract, introduction,
   synthesis, bibliography, manifests, and provenance ledgers.
9. Run source-hash, label, citation, build, log, and rendered-page checks.

Execute this as three reviewable commits rather than one opaque replacement:

- **WP2A — model and narrative:** chapter spine, notation, contributions,
  advisor equation/symbol corrections, evaluation design, and claim wording;
- **WP2B — evidence and appendix:** selected figures/tables, result text,
  compact technical appendix, captions, accessibility text, and body bridges;
  and
- **WP2C — scientific records:** bibliography, source/import/claim/display/
  appendix ledgers, source hashes, status, and validation evidence.

Acceptance: every retained hydrology claim maps to Corrected-3; all advisor
items `C3-01`--`C3-14` have implementation and rendered evidence; the chapter
is readable without the software chapter; the appendix stays within its
approved scope; the article source and thesis checkout remain independent.

### WP3 — Shorten and refocus the software chapter

- Apply all `C2-*` items after the reorder.
- State the candidate contribution and package capabilities before technical
  details.
- Remove redundant definitions/equations and the selected redundant example.
- Correct the non-marginal characterization associated with current Equation
  (2.27), then recheck surrounding inference language.
- Rewrite the summary to match the shorter contribution-first chapter.
- Unless the candidate rejects the recommended default before this work
  package begins, remove the detailed Big Tree analysis, retain a concise
  capability/provenance cross-reference, and update every affected display,
  accessibility, import, revision, appendix, and editorial record. Do not
  delete its source lineage.

Acceptance: the chapter demonstrates distinct software/statistical
contributions without repeating Chapter 2 and without assuming extensive R
knowledge.

### WP4 — Integrate Bruno's Chapter 4 comments

**Current addendum:** the annotated review has now arrived and covers Chapter
4 only through Section 4.4, together with detailed Chapter 5 and Appendix E
comments. The evidence identity, 116 itemized actions, revised execution order,
and validation gates are in
`docs/bruno-revision-integration-plan-20261109.md`. The prospective bullets
below are retained as the historical intake rule.

- Ingest Bruno's actual annotated file or message before editing.
- Freeze its hash and add itemized entries to the ledger.
- Revise Chapter 4 at its already fixed Q--DESN authority commit unless Bruno's
  notes identify a scientific-source update.

Acceptance: no inferred or second-hand comments; each change maps to Bruno's
actual review evidence.

### WP5 — Rewrite Chapter 1 after Chapters 2–4 stabilize

- Use this fixed outline: (1) motivating statistical problems and concrete
  examples; (2) relevant methods and unresolved gaps; (3) four research
  objectives and the approved contribution map; (4) only the shared
  statistical background required to read the chapters; and (5) one short
  relationship/roadmap paragraph.
- Introduce conditional quantiles and fixed-content intervals in standard
  statistical language and explain why each matters.
- State the dissertation's contributions early, distinguishing antecedents
  from collaborative project contributions and from the candidate's confirmed
  personal role.
- Define check loss, separate versus joint quantile fits, predictive
  synthesis, CRPS, interval placement, generalized updating, fixed echo-state
  features, and future-covariate conditioning only to the depth needed for the
  reader to understand the four objectives.
- Remove the evidence-hierarchy block, repeated organization material, the
  paragraph before the current organization section, and the opaque/internal
  phrases identified by Raquel.
- Define every symbol and score when first needed and reconcile every
  chapter-level claim with the final chapter text rather than an older plan.

Audience test: a first- or second-year statistics Ph.D. student should be able
to state the four problems and contributions after one reading.

### WP6 — Decide and, if retained, revise Chapter 5

After WP2–WP5, estimate the remaining work against the actual submission date.
Choose one of two explicit releases:

- **complete release:** include a substantially rewritten Chapter 5 with a
  clear work-in-progress boundary; or
- **staged release:** omit Chapter 5 from the first advisor submission and add
  it in the agreed second version.

Do not leave the present chapter in place merely to preserve chapter count.
A staged copy without Chapter 5 would be an advisor-review strategy, not a
claim about final program or filing requirements. The advisors and candidate
must decide the scholarly submission strategy explicitly.

### WP7 — Global front/back matter and disclosure pass

- Remove the italic chapter-opening manuscript/technical-report notices.
- Preserve manuscript and collaborator attribution in the acknowledgments and
  citations, revising the present acknowledgment so it no longer points to
  notices that have been removed.
- Reconcile the proposed AI-use statement in Section 4.8 with the assistance
  log, obtain the candidate's factual confirmation, and use the concise
  advisor-approved wording. Do not claim “coding/grammar only” while omitting
  documented organizational, editorial, citation-consistency, or validation
  support.
- Rewrite the abstract only after the chapter order, contributions, and Chapter
  5 status are settled, as Raquel requested.
- Reconcile the synthesis, contents, lists, and bibliography.
- Replace Chapter 6's “target-first” framing and any remaining project-internal
  workflow language with a direct statistical synthesis: common questions,
  distinct inferential targets, supported findings, limitations, and future
  work. Do not repeat the full contribution map.

### WP8 — Release validation and handoff

- Run fast and full repository validators under Python 3.11.
- Build in a fresh generated-output directory.
- check citations, references, labels, fonts, margins, pagination, and log
  warnings;
- inspect every changed chapter opening, equation cluster, table, figure,
  appendix bridge, acknowledgment, abstract, and transition page;
- scan extracted text for drafting notes, repository paths, internal workflow
  language, and unsupported AI/engineering terminology;
- review the full diff and provenance updates;
- commit by work package; and
- push/merge only after the author explicitly authorizes the completed
  manuscript release and the remote has been rechecked for divergence.

Overleaf remains a separate verification environment: preserve Overleaf edits,
pull the finalized GitHub `main`, compile there, and compare page count and
blocking diagnostics.

The minimum local validation sequence is:

```bash
python3.11 scripts/validate_research_audit.py
python3.11 scripts/validate_editorial_audit.py
python3.11 scripts/validate_structure.py
bash scripts/validate.sh --tier fast
bash scripts/validate.sh --tier chapter --audit-root /PATH/TO/IMMUTABLE/AUDIT-CLONES
bash scripts/validate.sh --tier release --audit-root /PATH/TO/IMMUTABLE/AUDIT-CLONES
```

The ignored local audit root must contain the fixed commits recorded in
`source-manifest.json`. The release gate also requires PDF text extraction,
font inspection, page rasterization, and manual review of every changed chapter
opening, contribution paragraph, dense equation page, table, figure, appendix
opening, transition, abstract, acknowledgment, and synthesis page. Automated
success alone is not sufficient.

The extracted-text review must also apply Section 4.13. It should report
contextual hits for stock or promotional wording, consecutive repetitive
sentence openings, self-referential topic sentences, and vague performance
claims. Each hit is marked `REVISE`, `RETAIN_SCIENTIFIC_TERM`, or
`FALSE_POSITIVE` with a short reason. No detector score substitutes for this
review.

The planned commit sequence is: evidence/contribution records; structural
reorder; WP2A; WP2B; WP2C; software reduction; Chapter 4 comments; Chapter 1;
Chapter 5 decision/revision; global front/back matter; final validation. A
failed package is corrected before the next begins. No force push, reset,
clean, automatic stash, or merge of unrelated work is permitted. A coherent
advisor release, rather than an intermediate broken state, is the unit eligible
for merging to `main` and Overleaf handoff.

### Work-package coverage of the correction ledger

| Work package | Controlling ledger items |
| --- | --- |
| WP0/WP0A | `P-01`, `P-02`, `P-04`, `P-10`; evidence and writing-profile prerequisites for all items |
| WP1 | `G-01`, `B-01`, `P-08` |
| WP2A--WP2C | `C3-01`--`C3-14`, `G-02`, `P-03`--`P-08`, `P-10` |
| WP3 | `C2-01`--`C2-13`, `G-02`, `P-03`, `P-05`--`P-08`, `P-10` |
| WP4 | `B-02` plus the itemized ledger created from Bruno's actual annotations |
| WP5 | `C1-01`--`C1-19`, `G-02`, `P-01`--`P-08`, `P-10` |
| WP6 | `B-03`--`B-05`, `P-10`, and all Chapter 5 items later extracted from Bruno's review |
| WP7 | `G-03`, `G-04`, `P-03`, `P-05`--`P-10` |
| WP8 | Completion evidence for every non-deferred item |

## 6. Validation matrix

| Risk | Required check |
| --- | --- |
| Wrong scientific source | Source-manifest commit and every imported blob hash match Corrected-3 |
| Stale numerical claim | Claim ledger agrees across Chapter 2, abstract, Chapter 1, Chapter 6, tables, and captions |
| Reorder damage | Zero unresolved/duplicate labels; all chapter and appendix references inspected |
| Over-imported article | Every retained display/technical block has a thesis claim and reader-need justification |
| Contribution ambiguity | Antecedents and collaborative project contributions are explicit; no undocumented individual role is invented |
| Approximation overclaim | VB/MCMC, parameter/predictive interval, calibration, and five-origin limits remain distinct |
| Private/internal leakage | No email body, absolute server path, token, ignored attachment, or workflow note is tracked or compiled |
| Formatting regression | Fresh build, log audit, font/margin/page checks, and rendered inspection pass |
| Source-tree damage | Thesis and research checkouts have expected clean/controlled dirty states |
| Appendix expansion | Four-to-six-page hydrology target; written claim-based justification before exceeding eight pages |
| Citation duplication | Corrected-3 references reconciled by title/DOI and existing thesis key; no blind BibTeX concatenation |
| Formulaic or over-smoothed prose | Section 4.13 four-pass review; every flagged phrase adjudicated in context; no generic fluency replaces assumptions, evidence, or authorial voice |
| Style overcorrection | Scientifically necessary AI/ML/software/engineering terms retained and defined; sound article prose not rewritten merely for surface variation |
| Incomplete advisor evidence | No Chapter 4/5 revision attributed to Bruno until his actual comments are frozen and itemized |
| Remote/Overleaf divergence | Fetch and compare before merge; no force push; Overleaf pull and compile verified as a separate handoff |

### 6.1 Stop conditions and recovery rules

Pause only the affected work package, preserving completed commits, if any of
the following occurs:

- a newer advisor file or explicitly authoritative research commit arrives;
- a retained number, figure, or model statement cannot be reconciled with the
  fixed source;
- a personal contribution statement lacks documentary evidence or explicit
  candidate/coauthor confirmation;
- a private or permission-restricted source would have to be published;
- the active TeX graph, source-blob validation, or release build fails after
  the change cannot be isolated locally;
- `origin/main` diverges before the planned merge; or
- an Overleaf edit would be overwritten by the proposed synchronization.

Recovery is additive: revert or correct the smallest work-package commit,
update the ledger, and rerun its acceptance checks. Do not reset, clean, hide
changes in a stash, rewrite an original research checkout, or compensate for a
scientific mismatch by weakening provenance records.

### 6.2 Reader and scientific acceptance tests

In addition to automated validation, the revision must pass six manual tests:

1. **one-reading test:** a first- or second-year statistics Ph.D. reader can
   state each chapter's problem, contribution, evidence, and principal limit;
2. **contribution test:** each novelty statement identifies its antecedent and
   does not rely on author order to assign individual credit;
3. **hydrology test:** a reader can explain the three methodological
   contributions, the five-origin design, the transformed/discharge-scale
   difference, and why score and calibration conclusions differ;
4. **independence test:** visible Chapter 2 is readable before the software
   chapter and the software chapter does not redefine the full model; and
5. **professional-document test:** no drafting notes, repository operations,
   internal production vocabulary, defensive AI language, or unexplained
   software/engineering jargon appears in the compiled thesis; and
6. **specificity and voice test:** every changed paragraph names the relevant
   statistical object, assumption, metric, evidence, or logical relation; no
   paragraph is merely smoother, formulaic, or interchangeable with a generic
   methods paper, and legitimate variation among the four project voices is
   preserved.

## 7. Decisions required before the corresponding work starts

Four decisions or factual confirmations remain material:

1. Confirm the recommended removal of the full Big Tree example from the
   software chapter, replacing it with a concise cross-reference.
2. Confirm the proposed disclosure wording in Section 4.8, especially that all
   assisted changes, references, mathematical statements, analyses,
   interpretations, and final text were personally reviewed and verified. The
   scientific exclusions and intended limited role have now been supplied;
   only factual reconciliation and final wording remain.
3. Decide whether Chapter 5 belongs in the first revised submission after the
   WP2–WP5 schedule is known. This decision can intentionally remain deferred.
4. Confirm the candidate-specific conceptual, theoretical, computational,
   empirical, and writing roles for each collaborative project, preferably
   against coauthor or project records. Until then, project contributions may
   be stated firmly but personal task allocation must remain collective.

The chapter reorder and use of Corrected-3 are treated as the advised default
for the eventual implementation. If either is not intended, it must be changed
before WP1 or WP2 begins.

## 8. Definition of done

The revision is complete only when all of the following are true:

- every one of the 65 current controlled items (50 Raquel items, five Bruno
  email items, and ten candidate controls) is marked implemented, explicitly
  deferred by decision, or waiting on named evidence, with a commit/release
  reference;
- Bruno's received annotation retains its 116-item count and complete
  36-page coverage audit through implementation;
- Corrected-3 is the current hydrology authority everywhere, while Corrected-2
  remains only as documented historical lineage;
- all retained chapter, display, appendix, and numerical claims have current
  source records and all superseded items have explicit recoverable
  dispositions;
- the four contribution dossiers and approved personal/collaborator
  attribution agree with Chapter 1, chapter openings, acknowledgments, and
  Chapter 6;
- the hydrology appendix satisfies the approved scope and page gate;
- fast, chapter, and release validation pass against immutable audit clones;
- the changed PDF pages and full extracted text pass manual scientific,
  stylistic, anti-formulaic-prose, voice, and layout review under Section 4.13;
- the final disclosure is factually confirmed and agrees with the assistance
  log; and
- the reviewed release is merged and pushed without divergence only after
  authorization, then pulled and compiled independently in Overleaf.

## 9. Next action

Do not repeat WP0--WP8 or rewrite the released chapters speculatively. Bruno's
new evidence has now been read, stored in the ignored advisor-input directory,
hash-identified, compared with current `main`, and normalized into the 116-item
supplement. No manuscript correction has been made.

If that supplement is approved, the next work begins with WP-B0 and WP-B1 in
`docs/bruno-revision-integration-plan-20261109.md`: verify the fixed scientific
sources, construct the response matrix, and resolve Chapter 4 definitions
through Section 4.4. Chapter 5 follows only after its conceptual and technical
dependencies are checked. Commit by coherent correction unit; run fast,
chapter, and release validation; inspect every affected page; and merge/push
without force only after explicit authorization. The Overleaf pull and compile
remain a separate handoff.

Independently, the currently released `main` may still be pulled and compiled
in Overleaf. If Overleaf reports a difference, preserve its edits and build log
before reconciling; do not use a force pull or overwrite an uninspected
Overleaf change.
