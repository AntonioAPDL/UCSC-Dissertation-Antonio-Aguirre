# Chapter 5 polish: changes for author review

Date: 2026-11-12. Baseline main:
`a56b66e256245436f5a93af65efa16ca35bba0cd`.

## What changed

This revision polishes the completed MTI–ECM/MTI–Gibbs migration. It changes
exposition and display placement, not the scientific results, fitting methods,
priors, algorithmic updates, or source authority. No scientific job was
launched, stopped, or retuned. The complete itemized response and before/after
text are in `docs/ch05-postmigration-polish-20261112.json`.

The main contribution sequence is now explicit: original residual-product
criterion, characterized mean-preserving population interval, retained-mean
tilt family, generalized-posterior computation, and evaluated tolerance action.
The text credits the original RQR procedure and population-content analysis.
It names MPI as the population functional characterized here, not as a
wholesale renaming of the original procedure. The description uses penalized
empirical minimization rather than attributing an unsupported Lagrangian
algorithm to Pouplin et al. (2024).

The numerical interpretation now identifies the comparator and property:
MTI–ECM gives smaller mean width than Young–Mathew in 39/72 comparisons
(54.2%), including 36/54 asymmetric-distribution cases (66.7%). The largest
reduction is 30.6% under strongly skewed lognormal sampling. All 39 narrower
comparisons also have greater empirical content attainment. The chapter keeps
the three settings in which Young–Mathew is narrower in every distribution,
the actual iteration-cap evidence, and the pharmaceutical comparison in which
MTI–ECM is wider than Young–Mathew.

## Exact review locations

Numbers in this table refer to the newly compiled release. The JSON companion
provides current source lines and before/after text for every edited passage.
Stable labels, rather than historic printed pages, identify mathematical and
display objects.

For a quick review of the accepted PDF, start with physical pages 102
(introduction), 107 and 110 (propositions), 113 (computation bridge), 122
(width findings), 124 (compact table), 127–128 (discussion), 135 (synthesis),
166–168 (proofs and balance), and 176 (moved table). The revised synthesis
sentence is now on printed page 123 rather than the old page 124. The
acknowledgment change is on physical page 12. The unchanged abstract and
Chapter 1 passages are on physical pages 10 and 17.

| Review | Dissertation location | What to inspect |
|---|---|---|
| R01 | Chapter 5 introduction | Original RQR purpose, MPI naming, interior-tilt identification, and the connected contribution sequence. |
| R02 | Population-characterization discussion | Integrated attribution, the retained-mean interpretation, and the sentence connecting unequal tail probabilities with balanced first moments. |
| R03 | Propositions 5.1–5.3 | Two former theorems are now propositions. Statements, proofs, assumptions, and internal labels are preserved. |
| R04 | Generalized-posterior computation | Standard check-loss optimality citation and a shorter empirical-balance bridge. The full derivation remains in Appendix E. |
| R05 | Tolerance procedure and simulation setup | Corrected cutoff-calibration sentence. Pointwise calibration bounds remain distinct from simultaneous independent-validation bounds. |
| R06 | Simulation results and Figures 5.3–5.4 | Added percentages, the lognormal width effect, greater attainment in narrower comparisons, and preserved unfavorable sample-range settings. |
| R07 | New Table 5.2 and retained Figure 5.5 | Pharmaceutical table compacted to median width and held-out content, each with empirical partition ranges. No values changed. |
| R08 | Chapter 5 discussion | More direct account of target, computation, and supported asymmetric-distribution advantage. Requested numerical-optimality disclaimer removed here, while numerical controls remain in methods and Appendix E. |
| R09 | Appendix E population/empirical results | Proposition proof headings and citation for the standard check-loss subgradient technique. The MTI-specific balance derivation remains. |
| R10 | Appendix E, new Table E.2 | Former main Table 5.2 moved intact beside calibration details. Figure 5.3 stays in the main chapter. |
| R11 | Chapter 6, fixed-content interval synthesis | Former printed-page-124 sentence now reports 39/72 (54.2%), 36/54 (66.7%), and the strongest skewed-lognormal reduction. |
| R12 | Acknowledgments | Short, factual assistance disclosure aligned with the assistance log, with author responsibility retained. |
| R13 | Abstract, fourth-project paragraph | Reviewed and retained unchanged: its target/computation/evaluation summary remains accurate. |
| R14 | Chapter 1, MTI contribution paragraph | Reviewed and retained unchanged: attribution, computation, and empirical scope agree with Chapter 5. |
| R15 | Chapter 5 and Appendix E throughout | Selective sentence and paragraph connections. Prose semicolon joins were recast where appropriate without changing mathematical parameter punctuation. |

The pharmaceutical table omits repeated split/return counts and endpoint/tail
columns already represented in Figure 5.5. Its caption records the 1,000
overlapping 100/87 partitions and identifies the ranges as empirical
partition quantiles rather than posterior credible intervals. Every scientific
figure is byte-identical to the baseline.

## Important accuracy decisions

- The two author-owned theorem names become propositions, but the standard
  implicit-function theorem keeps its conventional name.
- Population uniqueness is asserted for interior admissible tilts under the
  stated conditions. Boundary behavior remains in the mathematical account.
- The stale phrase “simultaneous calibration bounds” was corrected. The
  adverse calibration minima, 0.9460 and 0.9382, remain. The actual independent
  simultaneous-validation statement remains as well.
- The assistance sentence is concise but not restricted to grammar, because
  the factual record includes code/document checking, literature verification,
  and manuscript editing. The institutional disclosure-policy question remains
  open; this revision does not assert institutional approval.
- No empirical Gibbs agreement or speed ratio is reported without completed
  evidence. No universal advantage over frequentist tolerance methods is claimed.

## Provenance and validation

The prior migration record, including its source hashes, release proof, and
publication receipt, remains byte-identical. The new record explicitly links
each edited artifact's original and current hashes. The migration validator
accepts only source-locked current-derivative overrides and rejects unknown
paths, duplicate overrides, changed baselines, or stale current hashes.

`scripts/reconcile_ch05_polish.py` refreshes only the new editorial record and
connected derivative/display/appendix ledgers. Its default is check-only. It
does not change manuscript text, scientific assets, or prior release records.

Seventeen new polish tests and six new migration-override tests supplement the
existing 48 tests. The new checks reproduce matched counts, verify percentages
and compact table values, preserve 14 frozen scientific assets, and reject
mutations of proposition placement, calibration wording, table location, and
provenance. The full fast gate passed all 71 tests and rechecked 132 immutable
import-source blobs plus the existing additional source controls.

The final release artifact, rendered-page inspection, and actual Git promotion
are recorded in the JSON companion and the dated status/validation entries.
The accepted local proof is `build/release-20261112T053327Z/main.pdf`,
189 pages, SHA-256
`dbe16ce5173c12886203fbd982e461e606620d6a96fbc849a9d15a48488b5fa7`.
The dissertation's GitHub push does not itself update Overleaf: use its
deliberate **Pull from GitHub**, preserving newer advisor edits, then compile.
No independent Overleaf compilation is claimed.

## Verified Git integration

Implementation commit: `f7c3125e7733bdf91de10f30ed3fb60df03f4a6c`.
Two-parent main integration: `783d5ef613e5721ff54b96b24e0a240ebc2185d0`.
Its tree equals the tested editorial tree. The merged source-aware gate
passed all 71 tests. GitHub main and both task branches were pushed and
freshly read back successfully. This later documentation receipt changes
no manuscript or scientific asset. No token was required for the existing
SSH transport.
