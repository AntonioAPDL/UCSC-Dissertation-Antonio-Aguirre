# Reader-first dissertation reorganization and appendix migration plan

**Status:** proposed; advisor-directed planning document; no manuscript
reorganization has been performed under this plan.

**Prepared:** 2026-10-08

**Audited baseline:** Git commit
`0c394122549e903b19edc8014709a6f4318bee26` on `main`, equal to
`origin/main` and clean when this plan was prepared.

## 1. Decision and scope

The dissertation should retain its four-project scientific architecture, but
it should no longer retain the earlier placement rule that put all article and
supplement material inside the research-chapter bodies. The advisors' request
changes that editorial decision. It does not require a new thesis from scratch,
the removal of scientific evidence, or the duplication of the research
repositories inside the dissertation.

The recommended architecture is a **reader-first monograph with long,
recoverable technical appendices**:

1. the main body carries the scientific argument, inferential targets, central
   models, primary results, interpretation, limitations, and cross-project
   synthesis;
2. dissertation appendices carry derivations, proofs, full conditional
   distributions, detailed algorithms, secondary diagnostic evidence, and
   other material needed to verify the argument without interrupting it; and
3. the versioned research repositories remain the authority for code, data,
   fitted objects, complete runs, and computational regeneration.

This plan supersedes only the earlier **no scientific appendix** placement
decision in `docs/chapter-plan.md`, `docs/manuscript-integration-plan.md`,
`docs/STATUS.md`, `README.md`, and the corresponding validation description.
The manuscript-first conversion, four-project chapter structure, evidence
boundaries, imported-source provenance, and external-computation boundary
remain in force.

This is an editorial and structural migration. It must not silently change a
statistical target, theorem, assumption, numerical result, attribution,
publication status, or evidence level.

## 2. Audit diagnosis

### 2.1 Current scale

The current release has 344 PDF pages. Its body and bibliography occupy the
following approximate spans.

| Unit | Source words | Current PDF pages | Principal structural observation |
| --- | ---: | ---: | --- |
| Chapter 1: common framework | 2,561 | 12 | Sound target-first framework; some material is repeated in Chapter 6 and locally in research chapters. |
| Chapter 2: `exdqlm` | 13,843 | 64 | The software contribution is central, but posterior blocks, LDVB derivations, prior updates, and detailed diagnostics interrupt the workflow narrative. |
| Chapter 3: hydrologic application | 9,078 | 45 | The source/horizon contract and findings are central; expanded matrices, full algorithms, parameter summaries, and extra cutoff panels are verification material. |
| Chapter 4: Q--DESN | 16,693 | 97 | The longest chapter. It combines the main method and applications with a complete Gaussian baseline derivation, MCMC/VB algebra, ELBO details, multistep derivations, and extensive sensitivities. |
| Chapter 5: MPI/MTI | 14,217 | 78 | Central target definitions and theorem statements coexist with seven proofs, repeated score derivations, detailed ECM/pseudo-AL updates, and an already identifiable technical-derivation block. |
| Chapter 6: synthesis | 2,376 | 11 | The comparative table and cross-project lessons are useful; some chapter-by-chapter recap duplicates Chapter 1 and research-chapter conclusions. |

The four research chapters occupy about 284 PDF pages. Chapter 4 alone occupies
97 pages and Chapter 5 occupies 78. These lengths are not failures by
themselves, but the location of the technical material makes the principal
argument harder to follow.

### 2.2 Nature of the repetition

The manuscript does not primarily suffer from verbatim paragraph duplication.
A paragraph-level comparison found no widespread near-copy repetition. The
problem is **conceptual and functional repetition**:

- conditional-quantile, AL/exAL, working-likelihood, and generalized-update
  distinctions are reintroduced at several levels;
- MCMC, VB/LDVB, shrinkage, scoring, and calibration concepts recur in the
  common framework and in multiple project chapters;
- local method sections give a central formula, then a complete augmentation,
  posterior block, algorithm, and diagnostic treatment before returning to the
  scientific question;
- Chapter 5 states MPI/MTI objects in the principal development and restates
  closely related definitions in score-derivation and computational-detail
  sections; and
- introductions, chapter discussions, limitations, and the final synthesis
  sometimes repeat the same evidence qualifications rather than assigning one
  clear role to each location.

This diagnosis matters. Moving arbitrary pages to an appendix would shorten
the chapters without fixing the reading path. The implementation must first
assign one authoritative home to each concept and then preserve only the
short local reminder needed to understand the next claim.

### 2.3 Compatibility with program and writing requirements

The UCSC requirements already permit the needed structure: dissertation text,
appendices with continuing Arabic pagination, and the final bibliography. The
bibliography must remain after all appendices. No separate publisher-style
supplement is required.

The repository's academic writing profile also supports this change. Its
structural-editing guidance places long derivations, full conditionals, ELBO
algebra, Laplace details, extended proofs, extra simulations, sensitivity
analyses, and implementation detail in appendices unless one of those items is
central to the immediate argument. It also directs the writer to state a
caveat once and cross-reference it thereafter.

The advisors' recommendation is therefore compatible with both institutional
format and the project's own statistical writing standard. It corrects an
earlier editorial default; it does not contradict the scientific audit.

## 3. Reader contract and placement rules

### 3.1 The body must answer the scientific questions

A reader who does not enter the appendices must still be able to answer, for
each project:

1. What is the scientific or statistical problem?
2. What is the inferential target and information set?
3. What model, loss, or update defines the method?
4. What is genuinely contributed, and what is inherited?
5. How was the method computed and validated at a conceptual level?
6. What are the primary findings, including negative or mixed findings?
7. What assumptions, evidence limits, and unresolved issues constrain the
   conclusion?

The appendix should make every condensed technical step recoverable. It should
not become the only place where the thesis states its target, central model,
principal theorem, main empirical evidence, or limitations.

### 3.2 Unit-level decision rule

Every current section, subsection, proof, algorithm, equation group, figure,
and table should receive one of the following dispositions before it is moved.

| Disposition | Use when | Required treatment |
| --- | --- | --- |
| `BODY-KEEP` | Needed to understand the next argument or a principal result | Retain, edit for flow, and remove redundant reintroductions. |
| `BODY-CONDENSE` | Scientifically central but currently more detailed than the narrative requires | Keep the target, assumptions, key equation or result, interpretation, and appendix pointer. |
| `APPENDIX-MOVE` | Needed for verification or specialist use, but not for the first reading | Move rather than copy; preserve labels where practical and add a clear parent-section cross-reference. |
| `MERGE` | Repeats an object already defined elsewhere | Select one authoritative version, preserve any unique qualification, and record the merge. |
| `EXTERNAL-ONLY` | Code, data, fitted objects, full run output, or operational detail belonging to a research repository | Retain a precise provenance pointer; do not import the object. |
| `OMIT` | Superseded, genuinely duplicative, or submission-only material with no thesis role | Require an explicit rationale and confirm that no claim, assumption, or evidence is lost. |

Additional default rules are:

- state theorem and proposition results in the body; place complete proofs in
  the project appendix unless a short proof is itself essential exposition;
- retain the central model equation and inferential interpretation in the
  body; move augmentations, complete conditionals, block-matrix derivations,
  and numerical-stability algebra;
- summarize an algorithm's purpose, inputs, outputs, and approximation in the
  body; place full pseudocode and update equations in the appendix;
- retain primary figures and tables supporting the chapter's main claims;
  move secondary sensitivities, parameter summaries, additional-origin
  panels, and diagnostic displays, while keeping their substantive conclusion
  in the body;
- state a material caveat where it first affects interpretation, then use a
  cross-reference rather than restating the full caveat; and
- never move a limitation to an appendix merely to make a method look cleaner.

## 4. Recommended target architecture

### 4.1 Main body

The six-chapter sequence remains scientifically coherent and should be
preserved:

1. **Introduction and common framework.** Define the target-first perspective,
   distinguish uncertainty objects and update types, state the contribution
   and evidence map, and establish common terminology without reproducing
   chapter-specific mathematics.
2. **`exdqlm` software and computational workflow.** Present the inherited
   model foundations concisely, then emphasize the software contribution,
   version contract, analysis workflow, primary examples, and limitations.
3. **Source-aware hydrologic correction and synthesis.** Lead with the applied
   problem, source/horizon contract, scientific model differences, validation
   design, principal five-origin evidence, and operational limits.
4. **Bayesian quantile deep echo-state networks.** Present the reservoir-based
   quantile method, single and joint targets, computation at a conceptual
   level, simulations, GloFAS and PriceFM evidence, and qualifications.
5. **Mean-preserving and mean-tilted intervals.** Present interval geometry,
   the target definitions, principal results, TCSP, empirical evidence,
   pharmaceutical illustration, and the carefully bounded proposed
   extensions.
6. **Synthesis, limitations, and future work.** Compare the projects rather
   than summarize them again; focus on what becomes visible only when the four
   contributions are considered together.

### 4.2 Appendices

Five appendices give the cleanest navigation and avoid turning one appendix
into an unstructured repository of leftovers.

#### Appendix A — Shared statistical and computational conventions

Use one authoritative location for full parameterizations and reusable
technical conventions that occur in more than one project:

- AL/exAL parameterization and mixture conventions;
- Normal, inverse-Gaussian/GIG, and state-space notation needed across
  derivations;
- full scoring-rule and finite-grid conventions when the formula is not
  required in the local narrative;
- generic monotone-rearrangement and common diagnostic definitions; and
- a short index mapping each convention to the chapters that use it.

Chapter 1 should retain the inferential meaning of working likelihoods,
ordinary Bayes, generalized Bayes, predictive distributions, and tolerance
claims. Appendix A should contain reusable algebra, not the conceptual
distinctions on which the thesis depends.

#### Appendix B — Technical details for Chapter 2 (`exdqlm`)

**Keep in the body:** software scope and version boundary; concise exDQLM
specification; model-building and fitted-object workflow; package-design
contribution; the principal Sunspots, Turkey, Big Tree, and sparse-regression
evidence; mixed findings; interpretation and limitations.

**Move or condense into Appendix B:** detailed distributional conventions not
already in Appendix A; complete latent representations and posterior target
blocks; nonconjugate VB and backend algebra; LDVB scale/skewness derivations;
regularized-horseshoe update detail; forecast/synthesis formulas beyond the
conceptual procedure; extended diagnostic formulas; and secondary
implementation/API material not needed to understand the software research
claim.

Because this is a software-centered chapter, package architecture and the user
workflow are scientific content and must not be relegated wholesale to an
appendix.

#### Appendix C — Technical details and secondary evidence for Chapter 3

**Keep in the body:** hydrologic motivation; distinct roles of observations,
retrospectives, issued ensembles, and forecast covariates; the concise
source-aware model; why transfer information is introduced; computation and
synthesis summaries; five-origin and horizon design; principal comparisons;
and the deterministic-future-covariate and operational-evidence limits.

**Move or condense into Appendix C:** expanded state and design matrices; full
MCMC and VB algorithms; parameter and source summaries; detailed component
removal tables; additional cutoff panels; secondary sensitivity displays; and
calibration/feasibility mechanics that verify but do not define the main
application claim.

One representative synthesis result should remain in the body. Additional
origins should remain recoverable in the appendix rather than disappear.

#### Appendix D — Technical details and secondary evidence for Chapter 4

**Keep in the body:** Q--DESN motivation and target; reservoir construction at
the level needed to reproduce the feature contract; single-level and joint
quantile model equations; prior structure at a conceptual level; why MCMC and
VB--LD are used; primary simulation findings; the main GloFAS and PriceFM
results; crossing and future-input qualifications; and computational and
empirical limitations.

**Move or condense into Appendix D:** global shrinkage calibration algebra;
the full Gaussian-DESN baseline derivation, completing-the-square calculation,
exact posterior, marginal likelihood, alternative prior calculations, and
initialization details; all MCMC full conditionals; detailed VB--LD, Laplace,
delta-method, and ELBO algebra; stacked joint-design derivations; multistep
forecast recursions and rearrangement mechanics; simulation diagnostics and
secondary sensitivities; and the full latent-path ensemble likelihood and
Laplace--delta path calculation for GloFAS.

The body should retain the conclusion drawn from every moved diagnostic. It
should also explain the Gaussian baseline's role before referring to its full
derivation. This appendix is expected to be long; that is preferable to a
97-page chapter whose principal contribution is difficult to locate.

#### Appendix E — Proofs, computation, and secondary evidence for Chapter 5

**Keep in the body:** distinctions among fixed-content targets; MPI and MTI
definitions; assumptions and statements of the main propositions, theorems,
and corollaries; interpretation of the mean-preserving and mean-tilted paths;
the TCSP action and principal validation evidence; the primary pharmaceutical
analysis; concise statements of proposed regression and dynamic endpoint
extensions; and all limits on tolerance, prediction, and unimplemented work.

**Move or condense into Appendix E:** endpoint-score derivations; complete
proofs; convex-order and interval-path details; restricted-score equations;
Cornish--Fisher derivations; empirical-balance proofs; the direct DP content
law; detailed MTI-ECM calculations; TCSP calibration and feasibility
mechanics; secondary pharmaceutical responses and sensitivities; full
pseudo-AL augmentation and Gaussian-root updates; shrinkage, basis-expansion,
and dynamic-state derivations; and detailed diagnostic specifications.

Chapter 5 already contains a section called “Computational derivation
details”; moving it to Appendix E is a natural migration, but its repeated
definitions must be merged with the earlier development rather than copied.

### 4.3 Bibliography and navigation

The document order should be:

```
front matter
Chapters 1--6
Appendices A--E
final consolidated bibliography
```

Each appendix should begin with a short statement of its purpose, the parent
chapter sections it supports, and the assumptions under which its derivations
apply. Body references should identify useful destinations by topic, not merely
say “see the appendix.” Appendix headings should appear in the table of
contents, and figures/tables should continue to appear correctly in the lists
of figures and tables.

## 5. Canonical-home map for repeated concepts

Before line editing, the following ownership rules should be applied.

| Concept | Authoritative narrative home | Local treatment elsewhere |
| --- | --- | --- |
| Conditional quantile, check loss, and information set | Chapter 1 | One-sentence reminder plus project-specific target. |
| Credible, predictive, confidence, and tolerance distinctions | Chapter 1 | State only the distinction that affects the local claim. |
| Working likelihood versus response model versus generalized update | Chapter 1 | Each chapter declares its actual status; no general tutorial repeated. |
| Full AL/exAL and shared latent-distribution conventions | Appendix A | Retain only the central local density/model equation needed for interpretation. |
| exDQLM foundations and version graph | Chapter 2 | Chapter 3 states only its source-specific modifications and pinned dependency. |
| Reservoir construction and fixed-feature interpretation | Chapter 4 | Chapter 5 mentions deterministic bases only when discussing its proposed extension. |
| Generic meaning of MCMC, VB/LDVB, and approximation | Chapter 1 | Project bodies explain why an approach is used and what was checked; appendices hold updates. |
| Evidence hierarchy | Chapter 1 | Chapters identify their achieved level; Chapter 6 compares consequences. |
| Project-specific negative and mixed findings | Respective research chapter | Chapter 6 synthesizes implications without repeating full result inventories. |
| Provenance and external computation boundary | Chapter 1 and repository documentation | Research chapters give only material version dependencies. |

This map should be enforced at the paragraph level. Cross-references are not a
substitute for a locally intelligible sentence, but a local reminder should not
grow back into a duplicate literature or methods review.

## 6. Implementation workflow

Implementation should occur only after the architecture and placement defaults
are approved. It should be performed in the following order.

### Phase 0 — Freeze and governance

1. Start from a clean, synchronized `main` and record its commit and release
   PDF hash.
2. Create a dedicated restructuring branch.
3. Record that the advisor-directed plan supersedes the no-appendix placement
   rule, while retaining all source/provenance and evidence controls.
4. Do not regenerate the immutable import baseline and do not edit any research
   repository.
5. Preserve the current release as the before-state for content and visual
   comparison.

### Phase 1 — Exhaustive migration map before moving prose

Create a machine-readable migration map covering every section, subsection,
proof, algorithm, labeled equation group, figure, and table. Each record should
include:

- stable unit identifier;
- current file, section, label, and source-provenance locator;
- scientific role and parent claim;
- disposition from Section 3.2;
- proposed destination and ordering;
- dependencies on definitions, equations, displays, and citations;
- reason for the decision;
- evidence/rights sensitivity; and
- author/advisor review status.

Generate a label/reference graph before editing. Search for prose that embeds
hard-coded equation, section, table, figure, or page numbers. No content should
be moved until each dependency is represented in the map.

### Phase 2 — Add the appendix framework

1. Replace the removed demonstration appendix with tracked scientific appendix
   files A--E.
2. Add `\appendix` and the five inputs after Chapter 6 and before the
   bibliography.
3. Establish consistent appendix introductions, section depth, and
   cross-reference language.
4. Build the empty/skeleton structure first to verify numbering, table of
   contents, list entries, pagination, headers/footers, margins, and final
   bibliography placement.

### Phase 3 — Establish shared conventions and remove global repetition

1. Move reusable algebra into Appendix A.
2. Keep the inferential distinctions in Chapter 1 and shorten repeated general
   computation and scoring exposition.
3. Add concise pointers from Chapters 2--5.
4. Defer the final Chapter 1 and Chapter 6 prose polish until all research
   chapters have stable body/appendix boundaries.

### Phase 4 — Pilot and chapter migrations

Use Chapter 3 as the pilot because its expanded matrices, complete algorithms,
parameter summaries, and additional cutoff panels have comparatively clear
body/appendix roles. Confirm that the migration machinery, provenance update,
cross-references, and rendered layout work before applying the pattern to the
larger chapters.

Then migrate Chapters 2, 4, and 5 in that order:

1. move material; do not copy it;
2. preserve stable labels when they remain semantically correct;
3. insert a concise body summary before adding an appendix pointer;
4. merge repeated definitions and preserve unique assumptions or caveats;
5. repair transitions so the body reads continuously when the appendix is
   skipped;
6. update the migration map and revision/provenance ledger;
7. run fast and chapter validation; and
8. inspect the chapter opening, each new transition, primary displays, the
   corresponding appendix entry points, and the chapter ending.

Chapter 4 should receive the most intensive flow review because its main
contribution is currently surrounded by several complete computational
developments. Chapter 5 should receive a theorem/proof dependency review so
that moving proofs does not separate assumptions from statements or hide the
status of proposed extensions.

### Phase 5 — Monograph-level structural edit

After all migrations:

1. revise each research-chapter introduction to give the problem,
   contribution, evidence, and roadmap once;
2. revise each chapter discussion to interpret results rather than repeat the
   introduction;
3. remove repeated common background using the canonical-home map;
4. harmonize transitions from Chapter 2 to 3, 3 to 4, and 4 to 5;
5. shorten Chapter 6's project-by-project recap and strengthen comparative
   synthesis;
6. perform the statistical-literature prose pass using the repository writing
   profile; and
7. confirm that qualifications remain adjacent to the claims they constrain.

### Phase 6 — Release validation and handoff

Run the existing validation tiers and add the appendix-specific checks in
Section 8. Update all documentation that still says technical material lives
only in chapter bodies. Commit milestones in reviewable units. Once a milestone
is complete, validated, and approved, synchronize it through the established
GitHub/Overleaf workflow; do not leave partially moved content on `main`.

## 7. Editorial size guidance

Page counts should be treated as diagnostic ranges, not quotas. A defensible
first target for the narrative body is:

| Unit | Provisional body range |
| --- | ---: |
| Chapter 1 | 10--12 pages |
| Chapter 2 | 32--40 pages |
| Chapter 3 | 28--34 pages |
| Chapter 4 | 45--55 pages |
| Chapter 5 | 40--50 pages |
| Chapter 6 | 8--10 pages |

This would yield an approximately 163--201 page main narrative, followed by
substantial appendices. The total dissertation may remain near its current
length. Success is a coherent body with recoverable detail, not a particular
page reduction. If a central scientific argument requires more space, clarity
takes precedence over the range.

## 8. Validation and acceptance criteria

### 8.1 Automated controls

After each coherent edit:

- run `bash scripts/validate.sh --tier fast`;
- run the chapter tier after each chapter/appendix pair;
- use a fresh release directory and the fixed audit root for final release
  validation;
- fail on undefined citations/references, multiply defined labels, missing
  files, fatal TeX diagnostics, or new overfull boxes;
- verify appendix and bibliography order, continuing Arabic pagination, US
  Letter page size, embedded fonts, and the existing margin/footer envelope;
- compare pre/post inventories of claims, theorem statements, proofs,
  algorithms, figures, tables, citations, and labels against the migration
  map; and
- extend the provenance validator if necessary so appendix destinations are
  first-class dissertation derivatives rather than untracked copies.

The migration may change equation and page numbers. References must be label
based; any hard-coded number must be corrected and audited.

### 8.2 Scientific no-loss audit

For every unit moved or merged, verify:

- the inferential target and assumptions are unchanged;
- theorem/proposition statements still match their proofs;
- the main body retains the conclusion supported by a moved display;
- negative and mixed findings remain visible;
- numerical values, sample sizes, horizons, forecast origins, and version
  qualifications are unchanged unless an independently documented correction
  is made;
- the claim-evidence and display ledgers remain consistent; and
- no unimplemented method is promoted from proposed to established.

### 8.3 Two reader tests

The final structure must pass both tests:

1. **Body-only test:** a statistically literate reader can skip Appendices
   A--E and still follow every chapter's question, method, primary evidence,
   interpretation, and limitations without encountering a missing logical
   step.
2. **Recovery test:** a specialist can follow each appendix pointer and recover
   the derivation, proof, algorithm, diagnostic, or secondary result needed to
   audit the corresponding body statement.

### 8.4 Visual review

Render and inspect at minimum:

- the final Chapter 6 page and first page of Appendix A;
- the first and last page of every appendix;
- representative proof, algorithm, wide equation, figure, and table pages;
- every page containing a newly moved or reflowed primary display;
- table of contents, list of figures, list of tables, appendix transitions,
  and the first and last bibliography pages; and
- any page with an underfull/overfull or float-placement diagnostic.

Automated compilation is not evidence that the reading path or display
placement is satisfactory.

## 9. Provenance and documentation changes

The restructure must remain compatible with the two-layer provenance model:
immutable imported-source baselines plus editable dissertation derivatives.
Do not regenerate source imports merely because their derivative content moved
from a chapter to an appendix.

Recommended durable records are:

- `docs/appendix-migration-map.json` — the unit-level disposition and
  destination map;
- the existing `docs/revision-ledger.json` — updated derivative hashes and
  revision identifiers;
- the existing claim, display, bibliography, and source records — updated only
  where location or disposition changes;
- `docs/VALIDATION.md` — actual commands, artifact hashes, log results, and
  rendered-page inspection; and
- `docs/STATUS.md` — current stage, completed chapter/appendix pairs, unresolved
  scientific or administrative issues, and next decision.

After implementation, update the stale no-appendix statements in `README.md`,
`docs/chapter-plan.md`, `docs/manuscript-integration-plan.md`, and
`docs/VALIDATION.md`. Retain historical facts as dated history where useful,
but do not leave contradictory current instructions.

## 10. Risks and controls

| Risk | Control |
| --- | --- |
| Shorter body but missing logic | Apply the seven-question body test and require a summary before each appendix pointer. |
| Accidental loss during moves | Complete the migration map first; move instead of copy; reconcile pre/post inventories. |
| Appendix becomes an unstructured dump | Use five named appendices, parent-section links, purpose statements, and parallel ordering with the chapters. |
| Technical duplication survives in both places | Assign canonical homes and use `MERGE`, not duplicated body and appendix versions. |
| Proof separated from required assumptions | Retain assumptions in the body statement and repeat only the minimal local setup at the proof destination. |
| Central evidence is hidden | Keep claim-defining displays in the body; move only secondary or diagnostic evidence and retain its conclusion. |
| Cross-references and numbering break | Preserve semantic labels, build after small moves, and audit hard-coded references. |
| Provenance validator treats new files as untracked copies | Extend destination tracking and revision-ledger coverage before release. |
| Page reduction becomes the objective | Treat length ranges as diagnostics; review for comprehension and scientific completeness. |
| Overleaf receives a half-migrated manuscript | Merge/push only complete, buildable, inspected milestones. |

## 11. Remaining work beyond reorganization

The appendix migration will improve the dissertation but will not resolve
separate scientific, authorship, rights, or administrative issues. The final
program of work must also include:

1. advisor confirmation that the software-centered `exdqlm` chapter counts as
   an acceptable independent research unit;
2. conservative treatment of the unresolved exact TCSP scan recursion and
   action-matched finite-sample proof;
3. continued exclusion of unsupported empirical claims for the unimplemented
   MTI regression/dynamic extensions;
4. final candidate/coauthor contribution confirmation and material-specific
   reuse/publisher review;
5. final title, committee/dean fields, conferral date, ORCID,
   acknowledgments, and publication-status information;
6. a human scholarly read for emphasis, transitions, notation, and statistical
   phrasing after the structural edit; and
7. an independently inspected Overleaf build and final filing review.

Those tracks should be recorded separately so an improvement in manuscript
structure is not mistaken for resolution of a scientific or administrative
gap.

## 12. Recommended approval defaults

Implementation can begin cleanly if the following defaults are approved:

1. retain the four research chapters and adopt Appendices A--E as specified;
2. keep theorem/proposition statements in the body and move full proofs to the
   project appendix;
3. retain primary claim-defining displays in the body and move secondary
   diagnostic/sensitivity displays;
4. treat the page ranges as guidance rather than limits;
5. keep concise proposed MTI extensions in Chapter 5 and move their full
   computational derivations to Appendix E;
6. delete no scientific content without a documented `OMIT` decision and a
   no-loss check; and
7. keep code, data, fitted objects, and full computation external, while using
   the existing exact provenance links.

After approval, the first implementation deliverable should be the complete
migration map and appendix skeleton—not immediate large-scale prose cutting.
That gate makes the restructuring reversible, reviewable, and substantially
less likely to lose assumptions, evidence, or attribution.
