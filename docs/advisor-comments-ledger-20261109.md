# Advisor comments and proposed-resolution ledger: 9 November 2026

This ledger paraphrases every item in the advisor review into a proposed
solution and a verifiable acceptance test. The original attachment and
reviewed thesis PDF are stored locally under the ignored
`audit-inputs/advisor-review-20261109/` directory. They are not on GitHub.
Email bodies and private message metadata are not reproduced here.

No item in this ledger has been implemented in the dissertation. The source
status describes only whether the new Corrected-3 hydrology manuscript already
contains a satisfactory or partial source-level response.

Status vocabulary:

- `OPEN`: dissertation change required;
- `SOURCE_RESOLVED`: Corrected-3 contains a strong resolution, still to be
  adapted and verified in the dissertation;
- `SOURCE_PARTIAL`: Corrected-3 improves the issue but does not fully satisfy
  the advisor request;
- `DECISION`: candidate/advisor choice required;
- `WAITING`: required advisor evidence has not yet arrived.

## General comments

| ID | Advisor requirement | Status | Recommended resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| G-01 | Present hydrology before software; make hydrology independent and remove repeated exposition. | OPEN | Compile the hydrology source before the software source, reorder their technical appendices, and make software refer back to the statistical model rather than redefining it. Keep physical filenames stable during the first pass to avoid provenance churn. | Intended PDF order; complete cross-reference audit; zero repeated distribution/model blocks without a documented purpose |
| G-02 | State novelty, advantages, and reader value before criticism and future work in every chapter. | OPEN | Give each research chapter a problem–gap–contribution opening, then present evidence, and place limitations after the supported advantages. Preserve important negative findings without leading with them. | Opening-paragraph audit against contribution dossiers; advantages and evidence precede limitations |
| G-03 | Remove chapter-opening technical-report/manuscript notices and retain attribution elsewhere. | OPEN | Delete the italic notices; move manuscript titles, collaborators, and appropriate citations to acknowledgments and bibliography; retain antecedent credit in the chapter where scientifically needed. | Zero compiled chapter-opening notices; complete acknowledgment/citation map |
| G-04 | Explain whether and how AI was used. | DECISION | Draft one factual acknowledgment from the assistance log, covering the actual categories used; do not narrow it to “coding only” if structural editing, prose, bibliography, mathematical checking, or validation were also assisted. Obtain candidate approval and advisor/institutional review. | Candidate-approved wording consistent with the assistance log and applicable policy |

## Chapter 1

| ID | Advisor requirement | Status | Recommended resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| C1-01 | Rewrite in standard statistical language and remove opaque organizing jargon. | OPEN | Replace the current conceptual framework with a problem–literature–gap–contribution structure. Remove “target-first,” “evidentiary boundaries,” “evidence-matched claim,” and “update mechanisms” unless a precise standard definition is indispensable. | Terminology scan plus paragraph-level statistical-style review |
| C1-02 | Motivate the statistical problems and explain why the contributions matter. | OPEN | Begin with concrete conditional-quantile/forecasting and fixed-content-interval examples, then explain what existing methods provide and what remains unresolved. | A reader can identify the motivating problem, gap, and consequence before technical notation |
| C1-03 | Replace the broad research question with specific objectives. | OPEN | State four concise objectives: hydrologic correction/synthesis, reusable dynamic-quantile computation, nonlinear-feature quantile regression, and mean-tilted interval construction; connect each to a chapter and contribution. | Four objective statements agree with the final chapter content |
| C1-04 | Write for a first/second-year statistics Ph.D. reader. | OPEN | Define specialized methods at first use, assume regression/probability knowledge only, and test each section for unexplained project-specific terms. | First-use definition audit and reader checklist |
| C1-05 | Specify whether `u` is real. | OPEN | State `u in R` when defining check loss/quantiles and retain the domain in any later generalized use. | Symbol-definition check |
| C1-06 | Explain how current Equation (1.2), a single quantile, and multiple quantiles connect to the thesis. | OPEN | Explain that Chapters 2–3 fit conditional quantiles separately and may synthesize a predictive distribution, while Chapter 4 also considers a multi-quantile formulation; distinguish separate fits from a joint/composite construction. | Equation-to-chapter crosswalk; no conflation of separate and joint fits |
| C1-07 | Connect fixed-content intervals to preceding concepts; explain placement and define `D` in current Equation (1.4). | OPEN | Introduce intervals as a different inferential target: probability content alone does not determine which interval is chosen. Define `D` as the relevant distribution and use a simple asymmetric-distribution example to motivate location/length tradeoffs. | Defined symbol, explicit transition, and example checked against Chapter 5 |
| C1-08 | State software-chapter novelty and distinguish the candidate's work from Raquel Barata's. | OPEN | Use the contribution dossier: credit Yan et al. for exAL and Barata et al. for exDQLM/original computation/transfer foundations; state the later integrated software workflow, LDVB, APIs, static shrinkage support, compiled computation, diagnostics, tests, and reproducibility contribution only to the extent established by evidence. | Antecedent matrix and confirmed candidate-role statement |
| C1-09 | Replace the abstract “different update” description of Chapter 5 and define all terms in current Equation (1.5). | OPEN | Describe the loss-based generalized posterior and interval action in ordinary statistical terms; define the loss, learning rate, data, parameter/action, and normalizing expression before showing the equation. | Complete first-use notation audit; consistency with Chapter 5 |
| C1-10 | Do not use “reservoir” without statistical explanation. | OPEN | At first use describe fixed echo-state/deep-reservoir states as predetermined nonlinear time-series features; use “reservoir” only afterward as the established method name. | First-use definition and terminology scan |
| C1-11 | Define or replace “endpoint states.” | OPEN | Say that the proposed dynamic MTI extension models time-varying latent coefficients determining the lower and upper interval endpoints, then introduce any state notation. | Definition agrees with the extension manuscript |
| C1-12 | Replace the sentence about the “status of future inputs.” | OPEN | State whether future covariates are observed, externally supplied, forecast, or integrated over; explain that conditioning on supplied paths differs from propagating their uncertainty. | Concrete input-status statement for Chapters 2 and 4 |
| C1-13 | Define CRPS and explain its importance at first mention. | OPEN | Give the standard proper-score definition or expectation form, state that smaller values are better, and explain that it assesses the full predictive distribution rather than one quantile. | Definition, interpretation, and consistent sign convention |
| C1-14 | Replace the “frozen procedure / distribution-free theorem” wording. | OPEN | Say directly that simulation estimates performance for the prespecified procedure and studied data-generating distributions; it does not prove coverage for every distribution. | Standard statistical wording consistent with Chapter 5 evidence |
| C1-15 | Remove the identified evidence-hierarchy block. | OPEN | Delete the numbered hierarchy and place short, project-specific evidence qualifications next to the corresponding contribution. | Structural diff and smooth surrounding transition |
| C1-16 | Move contributions earlier and remove repetition. | OPEN | Place the four-project contribution map immediately after problems and literature gaps; mention each contribution once in substance and use only short navigation references later. | Duplicate-idea audit and revised outline |
| C1-17 | Remove or rewrite the dense pseudo-operational/hindcast sentence. | OPEN | State plainly that the hydrology evidence comprises five retrospective forecast origins and supplied covariate summaries, not a continuous operational evaluation. | Source-consistent scope statement |
| C1-18 | Remove the paragraph immediately before the current organization section. | OPEN | Delete it and preserve only any unique factual statement by moving that statement to the relevant contribution paragraph. | No lost unique claim; clean transition |
| C1-19 | Remove the redundant organization section unless needed. | OPEN | Prefer one short closing roadmap paragraph after the contribution map; do not retain a second chapter-by-chapter summary. | No repeated contribution/organization material |

## Current Chapter 2 / proposed Chapter 3: software

| ID | Advisor requirement | Status | Recommended resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| C2-01 | Reduce three real-data examples plus a simulation. | DECISION | Recommended default: remove the full Big Tree software analysis because it overlaps most with the preceding hydrology chapter. Retain a short package-capability cross-reference; keep Lake Huron, Sunspots, and the static sparse simulation for distinct functions. | Candidate/advisor confirmation; shortened chapter with no capability gap |
| C2-02 | Emphasize package capabilities and static exAL with Nishimura–Suchard priors; include model specifications. | OPEN | Promote the static AL/exAL model and shrinkage priors to a named methods subsection before the example, with response model, prior, inferential methods, and intended use. | Model/prior fully defined; contribution map references it |
| C2-03 | Refocus the opening after reordering on features, provenance, and importance. | OPEN | Start from the need for usable computation for the model in Chapter 2; list the package's statistically distinct capabilities and identify inherited versus later work. | Contribution-first opening and backward reference to hydrology |
| C2-04 | Remove undefined `q(gamma)q(sigma|gamma)` from the introduction. | OPEN | Remove it from the opening; introduce a factorization only in the computation subsection after all random quantities and conditioning are defined. | Zero undefined opening formula |
| C2-05 | Explain S3 interfaces or use plain language. | OPEN | Say that fitted model objects support standard summary, plotting, prediction, and diagnostic functions; optionally define R's S3 dispatch in one sentence later. | Readable without R internals |
| C2-06 | Correct anomalous paragraph spacing. | OPEN | Normalize LaTeX environment/paragraph commands to the dissertation style and inspect the rendered page. | Consistent baseline spacing in PDF |
| C2-07 | Replace version trivia with developer roles and substantive differences. | OPEN | Retain only versions needed for provenance; state the statistical/computational changes and documented authorship roles, while keeping the hydrology analysis pinned to 1.1.0. | Version table/paragraph tied to scientific consequences and contribution evidence |
| C2-08 | Remove or revise distributional conventions after reordering. | OPEN | Delete the standalone repeated conventions section; refer to Chapter 2 and define only software-specific parameterization differences locally. | No redundant definitions; every remaining convention is necessary |
| C2-09 | Introduce exAL notation before use. | OPEN | Add one local reminder defining quantile location, scale, and skewness before the first software signature that uses the notation. | First-use notation order passes |
| C2-10 | Remove or shorten repeated equations in model/prior subsections. | OPEN | Keep only equations needed to understand software inputs or a genuinely new computational method; replace repeated hydrology-model derivations with precise references. | Equation crosswalk documents every deletion/retention |
| C2-11 | Emphasize `exdqlmLDVB` as a new contribution. | OPEN | State what the routine computes, how it differs from the inherited ISVB/MCMC methods, why joint scale–skewness approximation matters, and what evidence supports its performance; use confirmed role language. | Source-backed contribution paragraph and method comparison |
| C2-12 | Correct the “marginal” description of current Equation (2.27) and following indentation. | OPEN | Identify the displayed density/factor by its actual conditioning and integrated variables; do not call it marginal unless all relevant variables are integrated out. Fix the display environment. | Mathematical review plus rendered check |
| C2-13 | Rewrite the chapter summary. | OPEN | Summarize the distinct software/computational contribution, retained examples, evidence, and limitations without repeating the introduction. | Summary-to-body and contribution-dossier consistency |

## Current Chapter 3 / proposed Chapter 2: hydrology

“Chapter 3” in Raquel's comments means the present hydrology chapter. After the
recommended reorder it will be reader-facing Chapter 2. Corrected-3 is the
scientific authority; Corrected-2 may supply only nonsuperseded exposition.

| ID | Advisor requirement | Corrected-3 status | Recommended resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| C3-01 | Define “product family” with a concrete example. | SOURCE_PARTIAL | At first indexed use, define a family as one external forecasting system supplying a retrospective product and issued ensemble; identify GloFAS and NWS/NWM as the two examples. | Definition precedes `j` indexing and is reused consistently |
| C3-02 | Use normal-sized component equations and address seven equations with five labels. | SOURCE_PARTIAL | Use normal text size and one readable line/block per component. Label each equation that is referenced independently; deliberately leave purely definitional unreferenced lines unnumbered and explain that choice in the equation crosswalk. | Rendered readability; complete label/reference map |
| C3-03 | State plainly that the lead-specific covariate vector is available and define forecast-member notation. | SOURCE_PARTIAL | State that `x_{T+k}` is the covariate vector supplied to the model for target time `T+k`; define `y_T^{j,i}(k)` as member `i` from family `j`, issued at origin `T`, for lead `k`. | First-use symbol audit |
| C3-04 | Explain the purpose of the stacked/compact form. | SOURCE_RESOLVED | Introduce it as a computational rewrite that combines state blocks and active observation channels for filtering/VB; explicitly say it adds no new scientific component. | Motivation immediately precedes stacked notation |
| C3-05 | Use normal font size for compact equations. | SOURCE_RESOLVED | Adopt Corrected-3's ordinary-size layout and split displays if page width requires it rather than shrinking type. | Rendered equation pages at body size |
| C3-06 | Treat scale and skewness as scalars. | SOURCE_RESOLVED | Use `sigma^s` and `gamma^s` in ordinary math italic; reserve boldface for vectors/matrices. | Notation scan |
| C3-07 | Define `c` and `epsilon` at first use and distinguish earlier symbols. | SOURCE_RESOLVED | State that `c>0` scales the prior mean/reference covariance and `epsilon>0` determines its relative prior weight; note that these are local covariance-prior symbols. | First-use definitions and cross-chapter symbol review |
| C3-08 | Clarify Laplace–Delta parameter blocks, transformation, moment approximation, and “stability.” | SOURCE_PARTIAL | Define the unconstrained coordinates explicitly (including the positive-scale and bounded-skewness transformations), identify the remaining variational factors, show how second-order Delta moments enter updates, and replace “stable” with a measurable numerical claim or remove it. | Source/equation audit; no unsupported stability adjective |
| C3-09 | Explain computation times clearly and compare new VB with MCMC. | SOURCE_RESOLVED | Use Corrected-3: approximately two hours is a recorded representative combined VB fit/forecast time under named conditions; several weeks is an expectation, not measured MCMC timing; no matched full-model MCMC comparison was performed. | Timing provenance and clear measured/estimated distinction |
| C3-10 | Remove the defensive operational-deployment sentence. | SOURCE_RESOLVED | Delete that sentence. Retain the scientifically relevant facts—five origins, archive constraints, and supplied future covariates—in the evaluation limitations. | Zero occurrence and preserved substantive boundary |
| C3-11 | Define `R` as the number of posterior predictive draws. | SOURCE_RESOLVED | Define it in the first sentence containing `Y_{ell,t}^{(r)}`. | First-use definition |
| C3-12 | Make time indexing explicit in isotonic regression. | SOURCE_PARTIAL | Prefer decision variables `m_{ell,t}` in the fixed-time optimization, or state explicitly that `m_ell` is optimized separately for each fixed `t`; use one convention throughout. | Equation and prose agree at every occurrence |
| C3-13 | State that lower CRPS means better predictive performance. | SOURCE_RESOLVED | Use the standard “proper, negatively oriented score; smaller values are better” wording once at first use. | Consistent direction in text/tables/captions |
| C3-14 | Use consistent draw/rank indices. | SOURCE_RESOLVED | Follow Corrected-3's predictive draws `r=1,...,R`; introduce a separate ordered-rank index only where CRPS requires it and explain the distinction. | Notation scan and manual equation review |

## Bruno's sequencing and pending review

| ID | Advisor requirement | Status | Recommended resolution | Acceptance evidence |
| --- | --- | --- | --- | --- |
| B-01 | Revise Chapters 2 and 3 first. | OPEN | Complete the reorder, hydrology reconciliation, and software reduction before rewriting the introduction. | Work-package/commit order |
| B-02 | Incorporate Chapter 4 comments when detailed notes arrive. | WAITING | Download the actual annotation, store it ignored with a hash, and extend this ledger item by item before editing Chapter 4. | Exact attachment/message evidence and expanded ledger |
| B-03 | Chapter 5 has good ideas but needs substantial narrative refinement. | OPEN | Rebuild its exposition around the interval problem, antecedent criterion, mean-preserving characterization, tilt family, calibrated procedure, empirical evidence, and clearly marked proposed extensions; remove internal development language. | Chapter-level problem–contribution–evidence review |
| B-04 | Reassess whether all work fits the schedule. | OPEN | Estimate remaining work only after Chapters 2–4; prioritize defensible contribution statements and readable chapters over preserving all material. | Written schedule/quality gate |
| B-05 | Consider submitting first without Chapter 5 and adding it later. | DECISION | Decide with the advisors after the workload estimate; if omitted, remove all dangling abstract/introduction/synthesis references for that release and restore them coherently in the later version. | Explicit release decision and reference audit |

## User-directed contribution and style controls

These controls implement the candidate's instruction that the contribution
case is central to the defense and that the prose must read as a statistical
dissertation.

| ID | Required control | Recommended resolution | Acceptance evidence |
| --- | --- | --- | --- |
| P-01 | Establish contributions in relation to prior literature. | Build one antecedent/contribution matrix per project from the fixed sources listed in the revision plan; distinguish inherited, adapted, extended, and newly developed elements. | Every contribution sentence has a source and antecedent classification |
| P-02 | Make the candidate's role clear without inventing credit. | Separate project contribution from personal task allocation; use author/package records plus candidate/coauthor confirmation for conceptual, theoretical, computational, empirical, and writing roles. | Completed role record or explicitly collective wording |
| P-03 | Give contributions early and prominently. | Put a concise dissertation contribution map early in Chapter 1 and a project contribution paragraph near each chapter opening; use Chapter 6 for synthesis, not a third repetition. | Location and duplication audit |
| P-04 | Give special care to current Chapter 3/proposed Chapter 2. | Use Corrected-3 as authority, compare Corrected-2 line by line for useful nonsuperseded exposition, and apply every `C3-*` resolution before results are finalized. | Source crosswalk, claim ledger, and rendered chapter review |
| P-05 | Use thesis-standard statistical prose. | Apply the statistical-style rubric in the revision plan paragraph by paragraph; prefer inferential targets, assumptions, estimators/posteriors, predictive distributions, and study designs over workflow language. | Compiled-text scan plus manual style review |
| P-06 | Avoid artificial-intelligence and engineering framing. | Remove promotional/internal terms; retain Q--DESN, echo-state-network, software, and computational terms only when scientifically necessary and define them statistically. | Context-reviewed terminology report, not a blind deletion count |
| P-07 | Preserve qualifications without underselling. | Present contribution and supporting result first, followed by the exact study or theorem boundary; do not begin contribution sections with defensive caveats. | Claim-order and tone review |
| P-08 | Keep the thesis coherent after revision. | Reconcile chapter order, terminology, notation, contributions, abstract, acknowledgments, synthesis, appendices, citations, displays, and provenance in one final global pass. | Release validation matrix and rendered inspection |

## Completion rule

An item may move to complete only when all four conditions hold:

1. the corresponding source or dissertation change is present in the diff;
2. any affected scientific or contribution claim matches fixed evidence;
3. relevant automated and rendered checks pass; and
4. the ledger names the commit or release containing the evidence.

Items may not be closed solely because Corrected-3 contains improved prose;
the dissertation adaptation and its cross-chapter consequences must also be
verified.
