# Current research-source refresh audit

Status: **integration, release validation, and rendered review passed**

Audit and projection date: 2026-10-26

Controlling machine records: `../source-manifest.json`,
`claim-evidence.json`, and `source-refresh-20261026.json`

Reproducible projection: `../scripts/refresh_current_research.py`

## Purpose and decision

This audit determines whether the dissertation still represents the current
authoritative manuscript lines for Q--DESN, mean-tilted intervals, and the
`exdqlm` software article. It compares the prior dissertation pins with the
current remote default branches, identifies changes that alter scientific
claims or reported evidence, and projects only the current manuscript prose and
display dependencies needed by the thesis.

The refresh does not turn the dissertation into a second research repository.
Code, data, fitted objects, caches, simulations, source histories, and complete
output archives remain external. Original research working trees were not
fetched, checked out, built, or modified. All inspection and extraction used
isolated Git clones, and the public records contain commits and hashes rather
than machine-local paths.

The reader-first architecture remains appropriate:

- current article main texts are the spines of Chapters 4 and 5;
- current derivations, algorithms, proofs, and supporting diagnostics are in
  Appendices D and E;
- the unchanged MTI extension manuscript follows the current tolerance
  article, but it is not allowed to override the latter's updated procedure;
- Chapter 2 retains its established dissertation organization while adopting
  the numerical and figure changes from the current `exdqlm` article; and
- only final active main displays and claim-relevant appendix displays are
  copied. The Q--DESN presentation-override chain is resolved to its final
  macro values so superseded review assets are not imported.

## Source comparison

| Source | Prior thesis pin | Current audited pin | Result |
| --- | --- | --- | --- |
| Q--DESN article | `757522db0f85815244370ec92a194de132268883` | `483e6edbec72ec76e48f2259e943e674b76e5041` | Material scientific and presentation update |
| RQR/MTI tolerance article | `73887b9c86ef767aa1567c660718667945630aef` | `4223c6a3a44f376255bacdca91db71cdf4f3afde` | Material method, validation, and application update |
| MTI regression/dynamic extensions | `f345d946aa5a81b94795838bec58d874a0fdd0c9` | same | Unchanged; documentation now lags the tolerance article |
| `exdqlm` software article | `d5534e97db8414fd875022261d4c530eae4676e4` | `98cec593d11bf32715a690ae168086f16160e7f0` | Material version and rerun update |
| `exdqlm` package | `e51045a4324901cced27ca2aaa22569afbc8e0e6` | same | Unchanged 1.1.2 support authority |
| Environmetrics article | `1272bfc10442a28add5a4c74ff641e9b9a8e9666` | same | Unchanged |
| San Lorenzo reproducibility source | `a8797b804271b46c62bd04dab7dba6b84a10ab7d` | same | Unchanged |
| Environmetrics corrections source | `b1ceeb610d20f8287e4ca44e146c9cfdbcda1ee6` | same | Unchanged |

The exact SHA-256 values of the current main documents, supplements, generated
derivatives, and copied dependencies are recorded in
`source-refresh-20261026.json`. The original import manifests in
`docs/imports/` remain immutable records of the first conversion; the revision
ledger and current refresh record describe the editable derivatives.

## Q--DESN findings and integration

The current article is titled *Bayesian Quantile Regression with Deep Echo
State Network Features*. It distinguishes single-level Q--DESN from MQ--DESN,
the multiquantile model. The latter reuses the same observed response across
quantile-level factors. Its likelihood is therefore described as composite,
not as a normalized joint likelihood for a scalar response.

The current simulation contract differs from the earlier thesis snapshot. The
primary single-level evaluation contains 300 forecast targets, with 500 targets
used as a sensitivity analysis. The older 1000-target framing is no longer the
article result line. In the multiquantile study, MQ--DESN reduces crossing but
does not yield a uniform score improvement. Independent fits have the lowest
mean oracle score in six of eight mechanisms, and the reported uncertainty
intervals for the best and second-best methods overlap in every mechanism.

The current GloFAS Search III application evaluates 28 issued horizons at one
origin, 25 December 2022. Q--DESN AL is the descriptive score leader relative
to the raw issued ensemble, but its nominal 90% interval covers 21 of 28
horizons; MQ--AL covers 22 of 28. The design conditions on realized future
PRISM and ERA5 weather. It is therefore a bounded retrospective forecast-
correction experiment, not an operational multi-origin claim.

The current PriceFM comparison contains 38 regions and three folds, or 114
matched cases. Q--DESN has the lower average quantile loss in 54 cases and
PriceFM in 60; the aggregate difference is small and favors PriceFM. The result
is heterogeneous across regions and folds. The thesis preserves this mixed
finding instead of using dominance language.

One upstream inconsistency remains: the Q--DESN abstract contains a PriceFM
placeholder even though the results section reports the matched comparison.
The dissertation replaces only that placeholder with the supported result and
records the adaptation in the claim ledger. The upstream abstract should still
be repaired. The Q--DESN supplement also records an internal `exdqlm` baseline
at version 1.1.1; that study-specific statement is preserved and is not silently
changed to the separate software article's 1.1.2 rerun.

## Profiled MTI findings and integration

The current RQR manuscript no longer uses the prior TCSP construction as its
primary proposed tolerance method. It profiles fitted content and tilt over a
prespecified grid, computes fixed-target endpoints through a convex midpoint
profile of the penalized MTI criterion, screens candidates by a direct
Dirichlet-process posterior content probability, and reports the shortest
eligible interval.

Calibration and validation are separated. Cutoffs are chosen using development
and assessment samples and then evaluated on independent validation samples.
Across 72 distribution-level validation cells, MTI attainment ranges from
95.1% to 99.3%. None of the simultaneous validation intervals has an upper
endpoint below 0.95. MTI has smaller mean width than Young--Mathew in 40 of 72
cells and in six of nine designs for each asymmetric distribution. These are
empirical results for the fixed eight-distribution panel, not a
distribution-free theorem.

The pharmaceutical illustration still uses 187 product-23 batches and 1000
paired splits with 100 training and 87 held-out observations, but the current
article reports materially stronger limitations and sensitivity checks. The
recorded data contain measurement-definition anomalies and an unresolved
physical unit; paired splits overlap; production campaign, API grouping,
recorded order, dependence, and ties may matter. Held-out content is descriptive
and is not a nominal tolerance validation. These limitations remain in the
chapter and appendix.

MTI-EXTENSIONS is unchanged. Its introduction and README still refer to the
older companion tolerance procedure. The dissertation treats the current RQR
main branch as authority for tolerance inference and uses MTI-EXTENSIONS only
for generalized-Bayes regression, basis, and dynamic endpoint proposals after
content and tilt have been specified. The extension proposals still have no
snapshot-matched implementation or empirical validation.

## `exdqlm` findings and integration

The current software article reports its final rerun under public CRAN
`exdqlm` 1.1.2. The implementation description adds a platform-stable
covariance square root for the fast dynamic MCMC state-simulation path. The
flat replication interface remains `code.R`; its reported reference run takes
about 40 minutes and was not rerun during this document refresh.

Chapter 2 now contains the current runtimes, stochastic summaries, benchmark
scores, and all nine rerun article figures. The substantive interpretation
remains mixed: the examples demonstrate the workflow and computational
tradeoffs rather than uniform model or inference superiority. The Environmetrics
application remains attached to its recorded 1.1.0 snapshot and is not
retroactively relabeled as a 1.1.2 analysis.

## Reproducible projection and checks

Given an audit root containing clones named `qdesn`, `rqr`,
`mti-extensions`, `exdqlm-article`, and `environmetrics`, the projection is:

```bash
python3.11 scripts/refresh_current_research.py --audit-root "$AUDIT_ROOT"
python3.11 scripts/refresh_current_research.py --audit-root "$AUDIT_ROOT" --apply
python3.11 scripts/update_current_research_records.py
```

The first command is read-only. Application is hash guarded: it accepts only
the approved pre-refresh derivatives or an exact recorded refresh. The script
records source blobs, destination hashes, editorial resolutions, copied assets,
and exclusions. It does not execute a scientific workflow.

The release gate is:

```bash
bash scripts/validate.sh --tier release --audit-root "$AUDIT_ROOT"
```

That gate covers unit tests, research-audit consistency, immutable baseline
imports, the editable-derivative ledger, active inputs, citations, labels,
appendix bridges, visual descriptions, a clean TeX build, blocking log
diagnostics, and PDF geometry/font checks.

The final gate passed against the immutable audit clones. It rechecked all 102
baseline source blobs and produced
`build/release-20261027T005737Z/main.pdf`: 439 US-Letter pages, PDF 1.7,
20,511,580 bytes, SHA-256
`92e4c36c451ecfceca2e0674e7d904f40f9b63e863f5799ba4b310dc262391d1`.
The final log contains 30 underfull line-breaking notices and zero overfull
boxes, oversized floats, unresolved citations or references, duplicate labels,
unstable-label notices, PDF-inclusion warnings, or fatal errors. All 52 PDF
font records are embedded and no Type 3 font remains.

Rendered inspection covered the title/front matter, the Chapter 4 and 5
openings, principal GloFAS evidence, Appendix D and E openings, the converted
multi-page Q--DESN score tables and their continuation headers, both MTI
partition-sensitivity tables, the PriceFM source/outline-derivative pair, and
the final bibliography page. No visible clipping, collision, margin breach, or
illegible table was found. The current PriceFM PDF's embedded Type 3 text was
replaced in the active thesis graph by a recorded Ghostscript vector-outline
derivative; the immutable copied source is retained, and the page size, plotted
data, labels, caption, and scientific claim are unchanged.

## Remaining decisions and limits

- The working commits are current default-branch authorities as of the audit
  date, not immutable final-submission releases. A final source freeze is still
  required.
- Candidate-specific conceptual, theoretical, computational, empirical, and
  writing roles remain to be confirmed with the candidate and coauthors.
- Material-specific reuse permission remains unverified. Repository access and
  a successful GitHub or Overleaf handoff do not establish publication rights.
- The Q--DESN upstream abstract and the MTI-EXTENSIONS companion-procedure
  wording should be repaired in their source repositories; the dissertation
  adaptations do not modify those repositories.
- The thesis build is reproducible from the copied prose and displays, but the
  complete scientific computations remain governed by the external research
  repositories.
