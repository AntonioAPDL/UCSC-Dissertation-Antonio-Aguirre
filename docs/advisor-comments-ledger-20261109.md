# Advisor comments and proposed-resolution ledger: 9 November 2026

This ledger paraphrases every item in the advisor review into a proposed
solution and a verifiable acceptance test. The original attachment and
reviewed thesis PDF are stored locally under the ignored
`audit-inputs/advisor-review-20261109/` directory. They are not on GitHub.
Email bodies and private message metadata are not reproduced here.

The first advisor-revision execution design is
`docs/advisor-revision-plan-20261109.md`. It records the completed Raquel-led
revision and its hydrology source/asset/appendix blueprint. The final
controlling specification for Bruno's later detailed review is
`docs/bruno-revision-integration-plan-20261109.md`. It resolves source questions
that the provisional intake left open, maps every affected dissertation file,
sets body/appendix compactness controls, defines the 116-row response record,
and supplies bounded commit and validation gates. This ledger remains the
advisor-level status record; neither plan silently closes an item.

The first advisor-revision program was implemented and validated before
Bruno's detailed annotation arrived. That new evidence is now frozen and
itemized in `docs/bruno-revision-integration-plan-20261109.md`; its manuscript
changes have not yet been implemented. The `IMPLEMENTED` status records
dissertation changes rather than merely improved wording in a source article.
Exact completed work-package commits are listed below, while the new Bruno
items retain planning statuses until their own validation passes.

Status vocabulary:

- `IMPLEMENTED`: the resolution is present in the dissertation and has passed
  the applicable source, structural, build, and rendered checks;
- `RECEIVED_PARTIAL / PLANNED`: the evidence arrived but covers only the named
  scope and has not yet been applied;
- `REOPENED / PLANNED`: an earlier general resolution remains useful, but the
  detailed review creates new unresolved work; and
- `WAITING`: required advisor evidence has not yet arrived.

## General comments

| ID | Advisor requirement | Status | Implemented resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| G-01 | Present hydrology before software; make hydrology independent and remove repeated exposition. | IMPLEMENTED | Compile the hydrology source before the software source, reorder their technical appendices, and make software refer back to the statistical model rather than redefining it. Keep physical filenames stable during the first pass to avoid provenance churn. | Intended PDF order; complete cross-reference audit; zero repeated distribution/model blocks without a documented purpose |
| G-02 | State novelty, advantages, and reader value before criticism and future work in every chapter. | IMPLEMENTED | Give each research chapter a problem–gap–contribution opening, then present evidence, and place limitations after the supported advantages. Preserve important negative findings without leading with them. | Opening-paragraph audit against contribution dossiers; advantages and evidence precede limitations |
| G-03 | Remove chapter-opening technical-report/manuscript notices and retain attribution elsewhere. | IMPLEMENTED | Delete the italic notices; move manuscript titles, collaborators, and appropriate citations to acknowledgments and bibliography; retain antecedent credit in the chapter where scientifically needed. | Zero compiled chapter-opening notices; complete acknowledgment/citation map |
| G-04 | Explain whether and how AI was used. | IMPLEMENTED | State the candidate-confirmed boundary: limited selected-code debugging and editorial review of organization, grammar, clarity, consistency, and readability; no statistical-method development, mathematical/proof derivation, scientific-literature identification/evaluation, independent implementation of the research analyses, or result generation. State the author's verification and responsibility directly. | Disclosure in acknowledgments agrees with the candidate's statement and the assistance log |

## Chapter 1

| ID | Advisor requirement | Status | Implemented resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| C1-01 | Rewrite in standard statistical language and remove opaque organizing jargon. | IMPLEMENTED | Replace the current conceptual framework with a problem–literature–gap–contribution structure. Remove “target-first,” “evidentiary boundaries,” “evidence-matched claim,” and “update mechanisms” unless a precise standard definition is indispensable. | Terminology scan plus paragraph-level statistical-style review |
| C1-02 | Motivate the statistical problems and explain why the contributions matter. | IMPLEMENTED | Begin with concrete conditional-quantile/forecasting and fixed-content-interval examples, then explain what existing methods provide and what remains unresolved. | A reader can identify the motivating problem, gap, and consequence before technical notation |
| C1-03 | Replace the broad research question with specific objectives. | IMPLEMENTED | State four concise objectives: hydrologic correction/synthesis, reusable dynamic-quantile computation, nonlinear-feature quantile regression, and mean-tilted interval construction; connect each to a chapter and contribution. | Four objective statements agree with the final chapter content |
| C1-04 | Write for a first/second-year statistics Ph.D. reader. | IMPLEMENTED | Define specialized methods at first use, assume regression/probability knowledge only, and test each section for unexplained project-specific terms. | First-use definition audit and reader checklist |
| C1-05 | Specify whether `u` is real. | IMPLEMENTED | State `u in R` when defining check loss/quantiles and retain the domain in any later generalized use. | Symbol-definition check |
| C1-06 | Explain how current Equation (1.2), a single quantile, and multiple quantiles connect to the thesis. | IMPLEMENTED | Explain that Chapters 2–3 fit conditional quantiles separately and may synthesize a predictive distribution, while Chapter 4 also considers a multi-quantile formulation; distinguish separate fits from a joint/composite construction. | Equation-to-chapter crosswalk; no conflation of separate and joint fits |
| C1-07 | Connect fixed-content intervals to preceding concepts; explain placement and define `D` in current Equation (1.4). | IMPLEMENTED | Introduce intervals as a different inferential target: probability content alone does not determine which interval is chosen. Define `D` as the relevant distribution and use a simple asymmetric-distribution example to motivate location/length tradeoffs. | Defined symbol, explicit transition, and example checked against Chapter 5 |
| C1-08 | State software-chapter novelty and distinguish the candidate's work from Raquel Barata's. | IMPLEMENTED | Use the contribution dossier: credit Yan et al. for exAL and Barata et al. for exDQLM/original computation/transfer foundations; state the later integrated software workflow, LDVB, APIs, static shrinkage support, compiled computation, diagnostics, tests, and reproducibility contribution only to the extent established by evidence. | Antecedent matrix and confirmed candidate-role statement |
| C1-09 | Replace the abstract “different update” description of Chapter 5 and define all terms in current Equation (1.5). | IMPLEMENTED | Describe the loss-based generalized posterior and interval action in ordinary statistical terms; define the loss, learning rate, data, parameter/action, and normalizing expression before showing the equation. | Complete first-use notation audit; consistency with Chapter 5 |
| C1-10 | Do not use “reservoir” without statistical explanation. | IMPLEMENTED | At first use describe fixed echo-state/deep-reservoir states as predetermined nonlinear time-series features; use “reservoir” only afterward as the established method name. | First-use definition and terminology scan |
| C1-11 | Define or replace “endpoint states.” | IMPLEMENTED | Say that the proposed dynamic MTI extension models time-varying latent coefficients determining the lower and upper interval endpoints, then introduce any state notation. | Definition agrees with the extension manuscript |
| C1-12 | Replace the sentence about the “status of future inputs.” | IMPLEMENTED | State whether future covariates are observed, externally supplied, forecast, or integrated over; explain that conditioning on supplied paths differs from propagating their uncertainty. | Concrete input-status statement for Chapters 2 and 4 |
| C1-13 | Define CRPS and explain its importance at first mention. | IMPLEMENTED | Give the standard proper-score definition or expectation form, state that smaller values are better, and explain that it assesses the full predictive distribution rather than one quantile. | Definition, interpretation, and consistent sign convention |
| C1-14 | Replace the “frozen procedure / distribution-free theorem” wording. | IMPLEMENTED | Say directly that simulation estimates performance for the prespecified procedure and studied data-generating distributions; it does not prove coverage for every distribution. | Standard statistical wording consistent with Chapter 5 evidence |
| C1-15 | Remove the identified evidence-hierarchy block. | IMPLEMENTED | Delete the numbered hierarchy and place short, project-specific evidence qualifications next to the corresponding contribution. | Structural diff and smooth surrounding transition |
| C1-16 | Move contributions earlier and remove repetition. | IMPLEMENTED | Place the four-project contribution map immediately after problems and literature gaps; mention each contribution once in substance and use only short navigation references later. | Duplicate-idea audit and revised outline |
| C1-17 | Remove or rewrite the dense pseudo-operational/hindcast sentence. | IMPLEMENTED | State plainly that the hydrology evidence comprises five retrospective forecast origins and supplied covariate summaries, not a continuous operational evaluation. | Source-consistent scope statement |
| C1-18 | Remove the paragraph immediately before the current organization section. | IMPLEMENTED | Delete it and preserve only any unique factual statement by moving that statement to the relevant contribution paragraph. | No lost unique claim; clean transition |
| C1-19 | Remove the redundant organization section unless needed. | IMPLEMENTED | Prefer one short closing roadmap paragraph after the contribution map; do not retain a second chapter-by-chapter summary. | No repeated contribution/organization material |

## Current Chapter 2 / proposed Chapter 3: software

| ID | Advisor requirement | Status | Implemented resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| C2-01 | Reduce three real-data examples plus a simulation. | IMPLEMENTED | Remove the full Big Tree software analysis because it overlaps with the preceding hydrology chapter. Retain a short capability cross-reference and keep Lake Huron, Sunspots, and the static sparse simulation for distinct evidentiary roles. | Shortened chapter has no duplicated Big Tree analysis or capability gap |
| C2-02 | Emphasize package capabilities and static exAL with Nishimura–Suchard priors; include model specifications. | IMPLEMENTED | Promote the static AL/exAL model and shrinkage priors to a named methods subsection before the example, with response model, prior, inferential methods, and intended use. | Model/prior fully defined; contribution map references it |
| C2-03 | Refocus the opening after reordering on features, provenance, and importance. | IMPLEMENTED | Start from the need for usable computation for the model in Chapter 2; list the package's statistically distinct capabilities and identify inherited versus later work. | Contribution-first opening and backward reference to hydrology |
| C2-04 | Remove undefined `q(gamma)q(sigma|gamma)` from the introduction. | IMPLEMENTED | Remove it from the opening; introduce a factorization only in the computation subsection after all random quantities and conditioning are defined. | Zero undefined opening formula |
| C2-05 | Explain S3 interfaces or use plain language. | IMPLEMENTED | Say that fitted model objects support standard summary, plotting, prediction, and diagnostic functions; optionally define R's S3 dispatch in one sentence later. | Readable without R internals |
| C2-06 | Correct anomalous paragraph spacing. | IMPLEMENTED | Normalize LaTeX environment/paragraph commands to the dissertation style and inspect the rendered page. | Consistent baseline spacing in PDF |
| C2-07 | Replace version trivia with developer roles and substantive differences. | IMPLEMENTED | Retain only versions needed for provenance; state the statistical/computational changes and documented authorship roles, while keeping the hydrology analysis pinned to 1.1.0. | Version table/paragraph tied to scientific consequences and contribution evidence |
| C2-08 | Remove or revise distributional conventions after reordering. | IMPLEMENTED | Delete the standalone repeated conventions section; refer to Chapter 2 and define only software-specific parameterization differences locally. | No redundant definitions; every remaining convention is necessary |
| C2-09 | Introduce exAL notation before use. | IMPLEMENTED | Add one local reminder defining quantile location, scale, and skewness before the first software signature that uses the notation. | First-use notation order passes |
| C2-10 | Remove or shorten repeated equations in model/prior subsections. | IMPLEMENTED | Keep only equations needed to understand software inputs or a genuinely new computational method; replace repeated hydrology-model derivations with precise references. | Equation crosswalk documents every deletion/retention |
| C2-11 | Emphasize `exdqlmLDVB` as a new contribution. | IMPLEMENTED | State what the routine computes, how it differs from the inherited ISVB/MCMC methods, why joint scale–skewness approximation matters, and what evidence supports its performance; use confirmed role language. | Source-backed contribution paragraph and method comparison |
| C2-12 | Correct the “marginal” description of current Equation (2.27) and following indentation. | IMPLEMENTED | Identify the displayed density/factor by its actual conditioning and integrated variables; do not call it marginal unless all relevant variables are integrated out. Fix the display environment. | Mathematical review plus rendered check |
| C2-13 | Rewrite the chapter summary. | IMPLEMENTED | Summarize the distinct software/computational contribution, retained examples, evidence, and limitations without repeating the introduction. | Summary-to-body and contribution-dossier consistency |

## Current Chapter 3 / proposed Chapter 2: hydrology

“Chapter 3” in Raquel's comments means the present hydrology chapter. After the
recommended reorder it will be reader-facing Chapter 2. Corrected-3 is the
scientific authority; Corrected-2 may supply only nonsuperseded exposition.

| ID | Advisor requirement | Status | Implemented resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| C3-01 | Define “product family” with a concrete example. | IMPLEMENTED | At first indexed use, define a family as one external forecasting system supplying a retrospective product and issued ensemble; identify GloFAS and NWS/NWM as the two examples. | Definition precedes `j` indexing and is reused consistently |
| C3-02 | Use normal-sized component equations and address seven equations with five labels. | IMPLEMENTED | Use normal text size and one readable line/block per component. Label each equation that is referenced independently; deliberately leave purely definitional unreferenced lines unnumbered and explain that choice in the equation crosswalk. | Rendered readability; complete label/reference map |
| C3-03 | State plainly that the lead-specific covariate vector is available and define forecast-member notation. | IMPLEMENTED | State that `x_{T+k}` is the covariate vector supplied to the model for target time `T+k`; define `y_T^{j,i}(k)` as member `i` from family `j`, issued at origin `T`, for lead `k`. | First-use symbol audit |
| C3-04 | Explain the purpose of the stacked/compact form. | IMPLEMENTED | Introduce it as a computational rewrite that combines state blocks and active observation channels for filtering/VB; explicitly say it adds no new scientific component. | Motivation immediately precedes stacked notation |
| C3-05 | Use normal font size for compact equations. | IMPLEMENTED | Adopt Corrected-3's ordinary-size layout and split displays if page width requires it rather than shrinking type. | Rendered equation pages at body size |
| C3-06 | Treat scale and skewness as scalars. | IMPLEMENTED | Use `sigma^s` and `gamma^s` in ordinary math italic; reserve boldface for vectors/matrices. | Notation scan |
| C3-07 | Define `c` and `epsilon` at first use and distinguish earlier symbols. | IMPLEMENTED | State that `c>0` scales the prior mean/reference covariance and `epsilon>0` determines its relative prior weight; note that these are local covariance-prior symbols. | First-use definitions and cross-chapter symbol review |
| C3-08 | Clarify Laplace–Delta parameter blocks, transformation, moment approximation, and “stability.” | IMPLEMENTED | Define the unconstrained coordinates explicitly (including the positive-scale and bounded-skewness transformations), identify the remaining variational factors, show how second-order Delta moments enter updates, and replace “stable” with a measurable numerical claim or remove it. | Source/equation audit; no unsupported stability adjective |
| C3-09 | Explain computation times clearly and compare new VB with MCMC. | IMPLEMENTED | Use Corrected-3: approximately two hours is a recorded representative combined VB fit/forecast time under named conditions; several weeks is an expectation, not measured MCMC timing; no matched full-model MCMC comparison was performed. | Timing provenance and clear measured/estimated distinction |
| C3-10 | Remove the defensive operational-deployment sentence. | IMPLEMENTED | Delete that sentence. Retain the scientifically relevant facts—five origins, archive constraints, and supplied future covariates—in the evaluation limitations. | Zero occurrence and preserved substantive boundary |
| C3-11 | Define `R` as the number of posterior predictive draws. | IMPLEMENTED | Define it in the first sentence containing `Y_{ell,t}^{(r)}`. | First-use definition |
| C3-12 | Make time indexing explicit in isotonic regression. | IMPLEMENTED | Prefer decision variables `m_{ell,t}` in the fixed-time optimization, or state explicitly that `m_ell` is optimized separately for each fixed `t`; use one convention throughout. | Equation and prose agree at every occurrence |
| C3-13 | State that lower CRPS means better predictive performance. | IMPLEMENTED | Use the standard “proper, negatively oriented score; smaller values are better” wording once at first use. | Consistent direction in text/tables/captions |
| C3-14 | Use consistent draw/rank indices. | IMPLEMENTED | Follow Corrected-3's predictive draws `r=1,...,R`; introduce a separate ordered-rank index only where CRPS requires it and explain the distinction. | Notation scan and manual equation review |

## Bruno's sequencing and pending review

| ID | Advisor requirement | Status | Implemented resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| B-01 | Revise Chapters 2 and 3 first. | IMPLEMENTED | Complete the reorder, hydrology reconciliation, and software reduction before rewriting the introduction. | Work-package/commit order |
| B-02 | Incorporate Chapter 4 comments when detailed notes arrive. | RECEIVED_PARTIAL / PLANNED | Bruno's annotated PDF arrived on 9 November. It is frozen locally with SHA-256 `4824065866f8a60c547339e1349b2adeca23a4b459badece319d7395e183d035`; the Chapter 4 review covers Sections 4.1--4.4 only. The 40 normalized Chapter 4 items are `B4-001`--`B4-040` in `bruno-revision-integration-plan-20261109.md`. | Ten annotated Chapter 4 pages accounted for; manuscript corrections not yet implemented; Sections 4.5--4.8 remain outside the received review |
| B-03 | Chapter 5 has good ideas but needs substantial narrative refinement. | REOPENED / PLANNED | The earlier global rewrite remains useful and satisfies several opening-level comments, but Bruno's detailed review adds 65 Chapter 5 and 11 Appendix E items. Preserve already-satisfied prose and implement the unresolved definition, theorem, generalized-Bayes, calibration, validation, and appendix corrections item by item. | Twenty-six annotated Chapter 5/Appendix E pages accounted for in `B5-001`--`B5-065` and `BE-001`--`BE-011`; manuscript corrections not yet implemented |
| B-04 | Reassess whether all work fits the schedule. | IMPLEMENTED | Revise the contribution-bearing units first, remove redundant material, and retain only work that can pass the scientific and readability gates in the complete release. | Work-package sequence and chapter-sized commits document the completed quality gate |
| B-05 | Consider submitting first without Chapter 5 and adding it later. | IMPLEMENTED | Use the candidate-approved complete release: retain the substantially revised Chapter 5 and reconcile every abstract, introduction, synthesis, appendix, and cross-reference dependency. | Full four-project build and reference audit pass |

## User-directed contribution and style controls

These controls implement the candidate's instruction that the contribution
case is central to the defense and that the prose must read as a statistical
dissertation.

| ID | Required control | Status | Implemented resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| P-01 | Establish contributions in relation to prior literature. | IMPLEMENTED | Use the fixed-source antecedent/contribution matrices to distinguish inherited, adapted, extended, and newly developed elements. | Contribution statements and citations reviewed against the fixed sources |
| P-02 | Make the candidate's role clear without inventing credit. | IMPLEMENTED | State project contributions collectively where the manuscript records do not allocate individual tasks; retain only documented first-author, corresponding-author, package-author, creator, and maintainer roles. | Acknowledgments and Chapter 1 contain evidence-bounded role language |
| P-03 | Give contributions early and prominently. | IMPLEMENTED | Place the four-project contribution map near the beginning of Chapter 1 and a concise contribution statement near each research-chapter opening. | Location and duplication review passed |
| P-04 | Give special care to current Chapter 3/proposed Chapter 2. | IMPLEMENTED | Use Corrected-3 as the hydrology authority and use Corrected-2 only for nonsuperseded context; apply every `C3-*` resolution to the chapter and appendix. | Source crosswalk, claim ledger, build, and rendered chapter review passed |
| P-05 | Use thesis-standard statistical prose. | IMPLEMENTED | Prefer inferential targets, assumptions, posterior quantities, predictive distributions, and study designs to internal process language. | Compiled-text scan and paragraph-level style review passed |
| P-06 | Avoid artificial-intelligence and engineering framing. | IMPLEMENTED | Remove promotional and internal terminology; retain echo-state-network, reservoir, software, and computational terms only where technically required and define them statistically. | Contextual terminology review passed; no blind deletion rule was used |
| P-07 | Preserve qualifications without underselling. | IMPLEMENTED | State each contribution and its supporting result before the precise theorem or study boundary. | Claim-order and tone review passed |
| P-08 | Keep the thesis coherent after revision. | IMPLEMENTED | Reconcile chapter order, terminology, contributions, abstract, acknowledgments, synthesis, appendices, citations, displays, and provenance. | Fast and chapter validation, clean build, and rendered inspection passed |
| P-09 | Make the AI disclosure accurate, proportionate, and nondefensive. | IMPLEMENTED | State limited debugging and editorial support together with the substantive exclusions and author verification. | Disclosure reconciled with the assistance log and candidate-supplied boundary |
| P-10 | Apply the supplied academic-writing profile and anti-formulaic-prose controls to every correction. | IMPLEMENTED | Preserve sound source prose, replace generic phrasing with statistical specificity, verify equations and claims against fixed sources, and context-review sentence rhythm and terminology. | Manual paragraph review and compiled-text review passed; no detector score was used |

## Implementation record

| Scope | Commit(s) | Principal evidence |
| --- | --- | --- |
| Chapter order and appendix order (`G-01`) | `6f7543e` | Hydrology precedes software in the compiled contents and appendices follow the same order |
| Corrected-3 hydrology reconciliation (`C3-01`--`C3-14`, `P-04`) | `a840a78`, `3d3c346`, `7b0a7e7` | Pinned source imports, revised chapter and appendix, numerical-claim review, clean build, and rendered equation/display inspection |
| Software reduction and contribution revision (`C2-01`--`C2-13`) | `d9cebb7` | Big Tree duplication removed; static model added; retained examples have distinct roles; clean build and rendered review |
| Q--DESN global revision (`G-02`, `P-05`--`P-07`) | `a532e3b` | Contribution and terminology revision against the current authority; Bruno's later detailed Chapter 4 review is received through Section 4.4 and remains planned under `B4-001`--`B4-040` |
| Introduction (`C1-01`--`C1-19`) | `9174f32` | Four objectives and contribution map, first-use definitions, one roadmap, clean build, and inspection of all introduction pages |
| MTI narrative and release decision (`B-03`--`B-05`) | `63ccfe6` | Complete four-project release, contribution-led Chapter 5, two peripheral displays omitted, clean build, and rendered review |
| Abstract, attribution, disclosure, synthesis, and global style (`G-02`--`G-04`, `P-01`--`P-10`) | `d2e56b9` | Correct chapter order, collective attribution where roles are unassigned, candidate-confirmed disclosure, standard statistical synthesis, terminology scan, and clean 184-page build |

## Coverage audit

| Review source block | Source item count | Ledger coverage |
| --- | ---: | --- |
| Raquel general comments | 4 | `G-01`–`G-04` |
| Chapter 1 overview/structural comments | 4 | `C1-01`–`C1-04` |
| Chapter 1 numbered comments | 15 | `C1-05`–`C1-19` |
| Software chapter overview comments | 2 | `C2-01`–`C2-02` |
| Software chapter numbered comments | 11 | `C2-03`–`C2-13` |
| Hydrology chapter numbered comments | 14 | `C3-01`–`C3-14` |
| Bruno email sequencing/submission points | 5 | `B-01`–`B-05` |
| Bruno annotated Chapter 4 review through Section 4.4 | 40 | `B4-001`–`B4-040` in `bruno-revision-integration-plan-20261109.md` |
| Bruno annotated Chapter 5 and Appendix E review | 76 | `B5-001`–`B5-065`; `BE-001`–`BE-011` in `bruno-revision-integration-plan-20261109.md` |
| Candidate contribution/style/disclosure controls | 10 | `P-01`–`P-10` |

All 50 items in Raquel's attachment and all five actionable points in Bruno's
earlier email have a ledger entry and prior implementation record. Bruno's new
annotated PDF is now accounted for separately: 40 Chapter 4 items, 65 Chapter
5 items, and 11 Appendix E items, for 116 normalized actions across all 36
annotated pages. The detailed plan distinguishes items already satisfied by
current `main` from open edits, scientific-verification questions, decisions,
and the unreviewed remainder of Chapter 4. These new items are planned, not yet
implemented. The ten candidate controls extend the review; they do not replace
any advisor item.

## Completion rule

An item may move to complete only when all five conditions hold:

1. the corresponding source or dissertation change is present in the diff;
2. any affected scientific or contribution claim matches fixed evidence;
3. relevant automated and rendered checks pass; and
4. any changed prose passes the contextual academic-writing and
   anti-formulaic-prose review in Plan Section 4.13; and
5. the ledger names the commit or release containing the evidence.

Items may not be closed solely because Corrected-3 contains improved prose;
the dissertation adaptation and its cross-chapter consequences must also be
verified.
