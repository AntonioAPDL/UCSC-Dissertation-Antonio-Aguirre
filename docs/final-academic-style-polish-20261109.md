# Final academic-style polish: 9 November 2026

Status: **implemented, release validated, merged, and pushed**

Baseline: `main` at
`696d57458a697373e124ae788a6b4776ec047760`, with the 184-page advisor
revision already validated and released.

## 1. Governing writing standard

This pass follows `AGENTS.md` and the two byte-identical version 0.2 writing
profiles:

- `Article-Q-DESN---Version-2/Academic_Writing_Style_Profile_v0.2.md`; and
- `RQR-GIBBS/STYLE_PROFILE.md`.

Both files have SHA-256
`b9483cf55e108f5615c203dfff6c0940b7ecc5c001aaad679507004b70352513`.
They require prose that is precise, restrained, mathematically clear,
statistically mature, explanatory, and non-promotional. The operative rule is
to replace generic fluency with statistical specificity, not to make the text
merely smoother.

The pass therefore applies the following controls:

1. begin from the statistical problem or inferential target rather than an
   algorithm or software feature;
2. distinguish data, parameters, latent states, working likelihoods,
   generalized updates, posterior targets, approximations, predictive
   quantities, and repeated-sampling claims;
3. introduce notation before use and retain equation interpretation;
4. restrict empirical statements to their simulation design, forecast origin,
   information set, comparator, and metric;
5. use exact statistical nouns rather than vague terms such as *framework*,
   *pipeline*, *robust*, *powerful*, or *flexible* when a more precise object is
   available;
6. remove product-style software narration, empty transitions, repetitive
   sentence openings, and self-conscious paper-about-paper prose where they do
   not serve navigation;
7. preserve necessary terminology such as reservoir state, recurrent feature,
   software, variational approximation, and forecast system when it names an
   actual object; and
8. retain the accurate AI-assistance disclosure. Detector scores and attempts
   to conceal documented assistance are outside the writing standard.

## 2. Protected scientific content

This is an editorial pass, not a new research integration. It must not change
the four-project architecture, source authorities, contribution allocation,
inferential targets, likelihoods, losses, priors, equations, propositions,
proofs, algorithms, numerical values, study designs, figures, tables,
bibliography, or qualifications unless a concrete error is found. Corrected-3
remains the hydrology authority. The fixed Q--DESN, exdqlm, RQR, and
MTI-EXTENSIONS source identities remain unchanged. Bruno Sansó's detailed
Chapter 4 annotation is still unavailable and may not be inferred.

## 3. Audit by dissertation unit

### Front matter

The abstract follows the required problem--construction--evidence--qualified
conclusion sequence. Each result is tied to a named design and metric. The
acknowledgments use evidence-bounded collaborative attribution and an accurate,
proportionate AI-assistance statement. No substantive rewrite is indicated.

### Chapter 1: introduction

The opening begins with conditional-distribution and fixed-content-interval
problems, not with an algorithm. Four objectives and their antecedents appear
early, specialized terms are defined, and the interval and forecast targets
are distinguished. The chapter implements Raquel Prado's structural and
terminological comments. No generic evidence hierarchy or repeated full
roadmap remains. Only a final consistency read is required.

### Software chapter (reader-facing Chapter 3)

The chapter correctly credits the exAL and exDQLM foundations and identifies
the later integrated software contribution. Its model, posterior target,
approximations, diagnostics, and examples are statistically distinct. The
remaining weakness is localized article/tutorial prose: several example
openings describe what functions are called rather than the statistical
question, one paragraph uses future tense, and several sentences repeat *we*
as the procedural subject. These passages should be converted to object-first
descriptions while preserving the function names needed to document package
capabilities. Empirical verbs such as *demonstrate* should be replaced by the
reported capability or comparison.

### Hydrology chapter (reader-facing Chapter 2)

The chapter is contribution-first, source-specific, and explicit about
forecast origins, covariate availability, working-likelihood assumptions,
score direction, undercoverage, and the absence of a matched MCMC comparison.
Its claims follow Corrected-3 and Raquel Prado's itemized comments. Two uses of
*outperforms* can be stated more precisely as smaller CRPS under the named
comparison.

### Chapter 4: Q--DESN

The chapter distinguishes fixed recurrent predictors from unknown regression
parameters; defines single-level and composite multiquantile targets; and
qualifies reservoir selection, crossing, recursive forecasts, and application
information sets. The contribution is situated relative to prior quantile
reservoir, calibrated-DESN, DQLM, and QVP work. The opening can name Q--DESN
directly rather than begin with *This chapter develops*. The application discussion should
state the score comparison rather than use a leaderboard-style *outperform*.
No broader Chapter 4 rewrite is justified without Bruno Sansó's detailed
annotation.

### Chapter 5: MTI

The revised narrative now separates population identification, generalized
updating, model-based content probability, calibrated selection, independent
repeated-sampling validation, and proposed extensions. This directly addresses
Bruno Sansó's general concern about clarity. One transition announces the
section rather than the score equations. It should be corrected without weakening
the work-in-progress qualifications or expanding the appendix.

### Chapter 6: synthesis

The synthesis compares the four inferential targets rather than repeating
chapter abstracts. Findings, limitations, and future work are design-specific.
Two uses of *demonstrates* in the software summary can be replaced by the
specific operation or comparison. No structural change is indicated.

### Technical appendices

Each active appendix begins with orientation and retains only material needed
to interpret a main-text claim. The appendices distinguish standard from
nonstandard calculations and do not recreate full supplements. Established
technical terms and proof language are appropriate. A final scan for accidental
duplication and compiled layout is sufficient.

## 4. Controlled intervention

The manuscript edit will:

1. revise the software-example openings and selected procedural sentences into
   statistical, object-first prose;
2. replace vague empirical verbs with the named capability, metric, or
   comparison;
3. revise the Q--DESN opening and MTI score transition locally;
4. remove an internal transition comment that has no source-maintenance value;
5. scan the complete compiled text for drafting language, stock AI phrasing,
   promotional terminology, repeated text, and unsupported claims; and
6. compile and inspect all affected pages before release.

## 5. Acceptance gates

The pass closes only if:

- no equation, numerical result, citation, label, table, figure, source
  identity, attribution, or scientific qualification changes unintentionally;
- Raquel Prado's accepted chapter order, contribution emphasis, definitions,
  and reduction of repetition remain intact;
- Bruno Sansó's Chapter 5 narrative concern remains addressed and the absent
  detailed Chapter 4 annotation remains explicitly waiting;
- the fast and release validation tiers pass against the fixed audit sources;
- the TeX log has no unresolved references, citations, duplicate labels,
  overfull boxes, missing files, or fatal errors;
- affected pages pass rendered inspection; and
- the extracted PDF contains no drafting instructions, tool names, internal
  workflow language, generic promotional claims, or accidental duplicate
  prose. The approved disclosure is the only intentional reference to
  AI-assisted work.

## 6. Git and handoff policy

Audit documentation, manuscript edits, and release evidence will be committed
separately. The branch may be fast-forwarded into `main` and pushed only after
all gates pass and the remote is rechecked for divergence. No force push or
automatic Overleaf synchronization is permitted. Overleaf must pull and
compile the verified GitHub `main` as a separate handoff.

## 7. Implementation and validation record

The controlled manuscript revision is commit `8f39c1a`. Chapter 3 now presents
the Lake Huron, Sunspots, and sparse-regression examples as statistical
analyses rather than command sequences while retaining the package interfaces
needed for reproducibility. Chapters 2 and 4 state comparative findings through
CRPS or grid aCRPS rather than the unqualified verb *outperforms*. Chapter 4
opens with the Q--DESN model itself and gives an evidence-bounded interpretation
of the single-quantile study. Chapter 5 moves directly from the residual-product
loss to its population score equations, and Chapter 6 names the operations in
the software example instead of using a generic empirical verb. The internal
Chapter 4 transition comment was removed. No appendix required a prose change.

The numerical-token sequence and the citation, cross-reference, label, input,
and figure-token sequences are unchanged in every edited chapter. The fast and
release tiers passed all 19 tests. Release validation rechecked 120 immutable
source blobs, 102 import records, 18 current-source projections, 108 cited
keys, 189 active labels, and all active structure and accessibility records.
The accepted ignored artifact is
`build/release-20261109T230953Z/main.pdf`: 183 US-Letter pages, 4,136,754
bytes, PDF 1.7, SHA-256
`5cc16fe050e59b733e86d9d57051e0645cdce63b2320464cfe6a814e890e7599`.
The final log contains 12 underfull-box notices, no overfull boxes, and no
blocking citation, reference, duplicate-label, missing-file, or fatal
diagnostic. All fonts are embedded and no Type 3 font occurs. The PDF is
searchable, unencrypted, and untagged.

Physical pages 34, 57, 63, 66, 71, 86, 98, 103, and 134 were rendered and
inspected. They cover each altered hydrology, software, Q--DESN, MTI, and
synthesis passage. The shortened software-example heading now fits on one
line; inspection found no clipping, collision, malformed glyph, abnormal
margin, or unreadable material. Extracted-text scans found no drafting marker,
tool name, internal workflow language, or generic promotional phrase. The only
AI-assistance reference is the approved disclosure. The term *state-of-the-art*
occurs only inside the title of a cited ERA5-Land publication; *framework* and
*workflow* occur only in named statistical or bibliographic contexts.

All received Raquel Prado items and Bruno Sansó's sequencing and Chapter 5
narrative comments remain implemented. Bruno Sansó's promised detailed
Chapter 4 annotation has not been received, so item `B-02` remains `WAITING`
and is not represented as addressed. This pass does not change that evidence
boundary.

The editorial branch was fast-forwarded into `main` without a merge commit or
history rewrite. Release-bearing commit
`3cb7e978923032329897e410f64108c48ec5ccca` was pushed to GitHub and matched
the remote branch identifier before this closeout record was written.
