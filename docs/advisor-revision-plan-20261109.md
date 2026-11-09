# Advisor revision plan: November 2026 committee review

Status: **planning and evidence intake complete; manuscript corrections not
started**. This document controls the next revision cycle. The item-level
record is `docs/advisor-comments-ledger-20261109.md`.

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

## 5. Ordered implementation work packages

### WP0 — Freeze the revision inputs

- Confirm that no newer advisor attachment or Bruno comment file supersedes
  the 9 November intake.
- Fetch Corrected-3 and record a new commit only if the author explicitly says
  a later commit is authoritative; otherwise keep `c0bfccaa...` fixed.
- Record ignored local source paths and original-tree guards.
- Create a revision branch from the synchronized thesis baseline.

Acceptance: exact source commits, attachment hashes, and dirty states are
recorded; no original research checkout has changed.

### WP1 — Reorder Chapters 2 and 3 without rewriting content

- Change body and corresponding appendix input order.
- Audit every chapter/appendix number, forward/back reference, list entry,
  contribution statement, abstract reference, and synthesis reference.
- Build and validate this structural commit separately.

Acceptance: the PDF has the intended order; every reference resolves; no
scientific wording or number changes in this work package.

### WP2 — Rebuild the hydrology chapter from Corrected-3 plus the advisor overlay

1. Make a section/claim/display crosswalk from Corrected-3 to the new Chapter 2.
2. Reconcile the model and notation before touching results.
3. Apply every `C3-*` item in the ledger, including those still partial in the
   new article.
4. Import/adapt the three principal result tables and three principal figures,
   subject to page and redundancy review.
5. Keep only essential technical material in the hydrology appendix.
6. Reconcile numerical claims across the chapter, abstract, introduction,
   synthesis, bibliography, manifests, and provenance ledgers.
7. Run source-hash, label, citation, build, log, and rendered-page checks.

Acceptance: every retained hydrology claim maps to Corrected-3; all advisor
items have evidence; the chapter is readable without the software chapter;
the article source and thesis checkout remain independent.

### WP3 — Shorten and refocus the software chapter

- Apply all `C2-*` items after the reorder.
- State the candidate contribution and package capabilities before technical
  details.
- Remove redundant definitions/equations and the selected redundant example.
- Correct the non-marginal characterization associated with current Equation
  (2.27), then recheck surrounding inference language.
- Rewrite the summary to match the shorter contribution-first chapter.

Acceptance: the chapter demonstrates distinct software/statistical
contributions without repeating Chapter 2 and without assuming extensive R
knowledge.

### WP4 — Integrate Bruno's Chapter 4 comments

- Ingest Bruno's actual annotated file or message before editing.
- Freeze its hash and add itemized entries to the ledger.
- Revise Chapter 4 at its already fixed Q--DESN authority commit unless Bruno's
  notes identify a scientific-source update.

Acceptance: no inferred or second-hand comments; each change maps to Bruno's
actual review evidence.

### WP5 — Rewrite Chapter 1 after Chapters 2–4 stabilize

- Replace the current abstract organizing vocabulary with concrete statistical
  problems and examples.
- Introduce conditional quantiles and fixed-content intervals in standard
  statistical language and explain why each matters.
- describe existing methods and gaps;
- state the dissertation's contributions early, distinguishing antecedents
  from the candidate's collaborative work;
- connect chapters by their statistical questions, not by a generic evidence
  framework;
- remove the evidence-hierarchy block, repeated organization material, and the
  specific opaque phrases identified by Raquel; and
- define every symbol and score when first needed.

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
The program expectation is already satisfied by at least three journal-suitable
research chapters if the first version contains the revised Chapters 2–4, but
the advisors control the scholarly submission strategy.

### WP7 — Global front/back matter and disclosure pass

- Remove the italic chapter-opening manuscript/technical-report notices.
- Preserve manuscript and collaborator attribution in the acknowledgments and
  citations, revising the present acknowledgment so it no longer points to
  notices that have been removed.
- Add an AI-use statement only after the candidate confirms its truthful scope
  and the advisors approve the wording.
- Rewrite the abstract only after the chapter order, contributions, and Chapter
  5 status are settled, as Raquel requested.
- Reconcile the synthesis, contents, lists, and bibliography.

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

## 7. Decisions required before the corresponding work starts

Only three decisions remain material:

1. Confirm the recommended removal of the full Big Tree example from the
   software chapter, replacing it with a concise cross-reference.
2. Describe the factual scope of AI assistance that should be disclosed
   (for example: code, mathematical checking, bibliography work, structural
   editing, and/or prose editing). The repository assistance log can support
   drafting, but the candidate must approve the statement as accurate.
3. Decide whether Chapter 5 belongs in the first revised submission after the
   WP2–WP5 schedule is known. This decision can intentionally remain deferred.

The chapter reorder and use of Corrected-3 are treated as the advised default
for the eventual implementation. If either is not intended, it must be changed
before WP1 or WP2 begins.

## 8. Next action

Wait for explicit authorization to implement. On authorization, first check
for Bruno's promised detailed comments and any newer Corrected-3 commit, then
execute WP0–WP3 in order. Do not begin by rewriting Chapter 1: its contribution
map and chapter references depend on the completed Chapter 2/3 revision.
