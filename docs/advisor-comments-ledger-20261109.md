# Advisor comments ledger: 9 November 2026

This ledger paraphrases the advisor review into verifiable work items. The
original attachment and reviewed thesis PDF are stored locally under the
ignored `audit-inputs/advisor-review-20261109/` directory. Email bodies and
private message metadata are not reproduced here.

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

| ID | Paraphrased requirement | Status | Planned evidence |
| --- | --- | --- | --- |
| G-01 | Present the hydrology chapter before the software chapter; make hydrology independent and remove repeated distributional exposition from software. | OPEN | WP1 structural commit, reference audit, rebuilt PDF |
| G-02 | State novelty, advantages, and reader value before qualifications and future work in every research chapter. | OPEN | chapter-opening contribution audit and paragraph-level review |
| G-03 | Remove chapter-opening notices that say material was adapted from a technical report/manuscript; retain appropriate attribution in acknowledgments/citations. | OPEN | zero compiled matches for the notices; revised acknowledgment |
| G-04 | Add a truthful acknowledgment statement explaining any AI use. | DECISION | candidate-approved scope and wording; advisor/institution check |

## Chapter 1

| ID | Paraphrased requirement | Status | Planned evidence |
| --- | --- | --- | --- |
| C1-01 | Rewrite the chapter in standard statistical language; remove opaque organizing jargon. | OPEN | full Chapter 1 rewrite and terminology scan |
| C1-02 | Motivate the statistical problems and explain the significance of the contributions. | OPEN | problem/gap/contribution opening reviewed against chapters |
| C1-03 | Replace the overly broad research question with specific research objectives. | OPEN | explicit objective statements with chapter links |
| C1-04 | Write for a first/second-year statistics Ph.D. reader. | OPEN | independent audience checklist and definition audit |
| C1-05 | State that `u` is real where introduced. | OPEN | symbol-definition check |
| C1-06 | Explain how current Equation (1.2), single quantiles, and multiple-quantile work connect to the projects. | OPEN | revised transition and chapter map |
| C1-07 | Connect fixed-content intervals to the preceding material, explain why placement matters, and define `D` in current Equation (1.4). | OPEN | revised example and notation check |
| C1-08 | State the software chapter's novelty and distinguish the candidate's work from Raquel Barata's antecedent work. | OPEN | evidence-backed contribution paragraph |
| C1-09 | Replace the abstract statement that Chapter 5 uses a different “update”; define the actual statistical construction and all terms in current Equation (1.5). | OPEN | rewritten MTI motivation with definitions |
| C1-10 | Do not use “reservoir” before defining its statistical meaning. | OPEN | terminology/definition scan |
| C1-11 | Define or replace “endpoint states.” | OPEN | revised MTI description |
| C1-12 | Replace the sentence about the status of future inputs with a concrete statistical statement. | OPEN | revised forecasting-input paragraph |
| C1-13 | Define CRPS and explain why it is used at first mention. | OPEN | score definition and role |
| C1-14 | Replace the “frozen procedure / distribution-free theorem” wording with a direct distinction between empirical and proved claims. | OPEN | standard statistical wording |
| C1-15 | Remove the evidence-hierarchy block identified in the review. | OPEN | diff and continuity review |
| C1-16 | Move contributions earlier and remove repetition. | OPEN | new outline and duplicate-idea audit |
| C1-17 | Remove or rewrite the dense pseudo-operational/hindcast sentence. | OPEN | reader-facing hydrology scope statement |
| C1-18 | Remove the paragraph immediately before the present organization section. | OPEN | structural diff |
| C1-19 | Remove the redundant dissertation-organization section unless a concise navigation paragraph is demonstrably needed. | OPEN | final Chapter 1 outline |

## Current Chapter 2 / proposed Chapter 3: software

| ID | Paraphrased requirement | Status | Planned evidence |
| --- | --- | --- | --- |
| C2-01 | Reduce the example load; three real-data analyses plus a simulation are too much. | DECISION | recommended removal of full Big Tree example |
| C2-02 | Emphasize package capabilities and the static exAL model with Nishimura--Suchard priors; include its model specification. | OPEN | revised contribution map and static-model section |
| C2-03 | After reordering, focus the opening on software features, provenance, and importance, referring back to hydrology. | OPEN | revised opening and cross-reference |
| C2-04 | Remove the undefined `q(gamma) q(sigma | gamma)` formula from the opening. | OPEN | zero opening occurrence; later defined factorization only if needed |
| C2-05 | Explain S3 interfaces in plain language or use a nontechnical description. | OPEN | first-use definition and reader audit |
| C2-06 | Correct the anomalous paragraph spacing around the R discussion. | OPEN | rendered-page inspection |
| C2-07 | Replace detailed version trivia with who developed scientifically relevant versions and what differs. | OPEN | provenance-backed version paragraph |
| C2-08 | Remove or substantially revise distributional conventions after the reorder. | OPEN | duplication audit against new Chapter 2 |
| C2-09 | Ensure exAL notation is introduced before use. | OPEN | notation-order validator/manual review |
| C2-10 | Remove or shorten repeated equations at the end of the current model/prior subsections. | OPEN | equation crosswalk and page review |
| C2-11 | Make the candidate's `exdqlmLDVB` development explicit and explain its importance. | OPEN | evidence-backed contribution statement |
| C2-12 | Correct the “marginal” characterization of current Equation (2.27) and the following indentation. | OPEN | mathematical review and rendered check |
| C2-13 | Rewrite the chapter summary after the structural reductions. | OPEN | summary-to-body consistency check |

## Current Chapter 3 / proposed Chapter 2: hydrology

| ID | Paraphrased requirement | Corrected-3 status | Planned dissertation evidence |
| --- | --- | --- | --- |
| C3-01 | Define “product family” with a concrete example near first use. | SOURCE_PARTIAL | define GloFAS and NWS as concrete families at first indexed use |
| C3-02 | Use normal-sized component equations and address why seven equations have only five labels. | SOURCE_PARTIAL | ordinary-size display; label/reference decision documented for all seven lines |
| C3-03 | State plainly that the lead-specific covariate vector is assumed available and define forecast-member notation. | SOURCE_PARTIAL | first-use sentence and symbol audit |
| C3-04 | Explain why the model is rewritten in stacked/compact form before presenting it. | SOURCE_RESOLVED | adapt the prior-specification/computation motivation |
| C3-05 | Use normal font size for the compact equations. | SOURCE_RESOLVED | rendered equation pages |
| C3-06 | Treat source-specific scale and skewness as scalars, not bold vectors. | SOURCE_RESOLVED | notation scan |
| C3-07 | Define `c` and `epsilon` at first use: covariance scale and prior weight, distinct from earlier symbols. | SOURCE_RESOLVED | first-use definition and cross-chapter notation check |
| C3-08 | Define the Laplace--Delta parameter blocks in model terms, explain transformations and moment approximation, and justify any stability language. | SOURCE_PARTIAL | explicit transformed coordinates or removal of unsupported wording |
| C3-09 | Explain computation times in words, identify the new VB method, and distinguish estimate/measurement and MCMC comparison. | SOURCE_RESOLVED | source-consistent runtime paragraph and qualification check |
| C3-10 | Remove the defensive operational-deployment disclaimer. | SOURCE_RESOLVED | zero occurrence; retain only scientifically necessary scope limits |
| C3-11 | Define `R` as the number of posterior predictive draws. | SOURCE_RESOLVED | first-use definition |
| C3-12 | Make the time index explicit throughout the isotonic-regression optimization. | SOURCE_PARTIAL | use time-indexed decision variables or explain the fixed-time convention |
| C3-13 | State directly that lower CRPS is better. | SOURCE_RESOLVED | score definition at first use |
| C3-14 | Use one consistent draw/rank index and total (`r`, `R`) in synthesis notation. | SOURCE_RESOLVED | notation scan and equation review |

## Bruno's sequencing and pending review

| ID | Paraphrased requirement | Status | Planned evidence |
| --- | --- | --- | --- |
| B-01 | Revise Chapters 2 and 3 first. | OPEN | WP1–WP3 before other prose revision |
| B-02 | Incorporate Chapter 4 comments when the detailed notes arrive. | WAITING | hash and itemize the actual notes before editing |
| B-03 | Chapter 5 has strong ideas but requires substantial narrative clarification even if presented as work in progress. | OPEN | Chapter 5 narrative audit after WP2–WP5 |
| B-04 | Reassess whether the available time supports all revisions. | OPEN | explicit schedule/quality gate after Chapter 4 |
| B-05 | Consider a first submission without Chapter 5, followed by a second version about a week later. | DECISION | candidate/advisor submission decision after workload estimate |

## Completion rule

An item may move to complete only when all four conditions hold:

1. the corresponding source or dissertation change is present in the diff;
2. any affected scientific claim matches the fixed authoritative source;
3. the relevant automated and rendered checks pass; and
4. the ledger names the commit or release containing the evidence.

Items may not be closed solely because Corrected-3 contains improved prose;
the dissertation adaptation and its cross-chapter consequences must also be
verified.
