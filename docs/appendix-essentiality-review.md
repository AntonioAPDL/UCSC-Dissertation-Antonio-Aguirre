# Essential-appendix review and implementation record

**State:** implemented and release validated

**Baseline thesis commit:** `37b9da0fdb16168dff07efdc9454886f8467f6cd`

**Accepted PDF:** 414 pages, with 204 appendix pages

**Accepted PDF SHA-256:**
`49b0bc25f5c4b46c474379d3b7f33bfbfd01a3a28cb77660db63a4a8c5f0e409`

## Coverage

`appendix-essentiality-map.json` assigns one record to every inventoried
appendix unit:

| Unit type | Records |
| --- | ---: |
| Section, subsection, or subsubsection | 115 |
| Algorithm | 8 |
| Labeled equation group | 149 |
| Theorem or proposition with proof obligation | 8 |
| Appendix display | 60 |
| **Total** | **340** |

The map contains 48 baseline body bridges: two in the introduction, five in
Chapter 2, four in Chapter 3, 24 in Chapter 4, and 13 in Chapter 5. Forty are
retargeted to topical destinations, seven remain truthful chapter-level
bridges, and the final Chapter 3 promise of additional cutoff panels is
replaced by the five-origin evidence already in the body.

## Appendix decisions

| Appendix | Mapped units | Principal action |
| --- | ---: | --- |
| A | 6 | Retain a compact statistical concordance; remove directory prose. |
| B | 43 | Preserve posterior, LDVB, transfer-function, shrinkage, and synthesis support while removing package-maintainer inventory. |
| C | 9 | Consolidate four algorithm blocks to one MCMC and one variational outline; deactivate two additional cutoff figures. |
| D | 221 | Preserve nonstandard posterior/composite-target calculations and exactly eight supporting displays; remove duplicate result decks and development checks from the compiled graph. |
| E | 61 | Preserve the central proof graph and exactly five supporting displays; replace complete validation/application decks with calibrated, claim-bearing support. |

The 60 appendix display decisions contain 13 retained displays and 47
deactivations from the compiled graph. Historical `KEEP` decisions remain
unchanged in `display-ledger.json`; the essentiality map is the later inclusion
authority.

## Formal-result graph

Three principal results have their authoritative statements in Chapter 5 and
proof-only destinations in Appendix E:

| Appendix label | Authoritative body statement |
| --- | --- |
| `rqr2026:thm:supp-quantile-window` | `rqr2026:thm:quantile-window` |
| `rqr2026:prop:supp-mean-tilt` | `rqr2026:prop:mean-tilt` |
| `rqr2026:thm:supp-profiled-risk` | `rqr2026:thm:profiled-mean-tilt` |

The mean-preserving contraction, profile-radius lemma, fractional empirical
balance theorem, and convex midpoint profile remain complete supporting
statement-and-proof units in Appendix E. The direct DP content law is reduced
to its Beta law and interpretation because standard DP conjugacy supplies the
proof.

## Exact appendix display outcome

Appendix C retains no additional forecast figure. Appendix D retains:

1. `qdesn2026:tab:supp-reservoir-selection`;
2. `qdesn2026:tab:simulation-dgp`;
3. `qdesn2026:fig:independent-eval500-forecast_check`;
4. `qdesn2026:fig:supp-independent-quantile-calibration`;
5. `qdesn2026:tab:joint-qdesn-pure-desn-v2-recursive-policy`;
6. `qdesn2026:fig:supp-pricefm-r98-region-comparison`;
7. `qdesn2026:tab:supp-glofas-search3-specifications`; and
8. `qdesn2026:fig:supp-glofas-part4-calibration`.

Appendix E retains:

1. `rqr2026:tab:supp-mti-profile-policy`;
2. `rqr2026:tab:supp-scan-reference`;
3. `rqr2026:tab:supp-full-range-thresholds`;
4. `rqr2026:fig:supp-pharma-rsd`; and
5. `rqr2026:fig:supp-pharma-partition-sensitivity`.

## No-loss controls

All eleven protected conclusions have a responsible map record and a visible
location. The fixed research commits, baseline PDF, appendix source hashes,
migration markers, import records, rights states, and inactive assets remain
recoverable. The implementation did not change a target, likelihood
interpretation, theorem scope, numerical result, attribution, or evidence
strength.

## Gate C result

The fast validation gate passes with 18 tests, 340 mapped units, six preserved
migration records, 102 historical display records, and 47 active visual
records. The map is complete enough to begin the Appendix C pilot. No
appendix, chapter, display, citation, or compiler dependency has changed at
this checkpoint.

## Final implementation result

All 340 records are now `IMPLEMENTED`. Their dispositions are 104 `RETAIN`,
161 `CONDENSE`, 16 `SUMMARIZE`, and 59 `DEACTIVATE`; 167 units remain active
in the compiled graph, and all 173 inactive units have an exact no-loss and
recovery record. The appendix sequence occupies 52 numbered pages rather than
the 204-page baseline:

| Appendix | Final numbered pages | Final count |
| --- | --- | ---: |
| A | 175--178 | 4 |
| B | 179--184 | 6 |
| C | 185--187 | 3 |
| D | 188--208 | 21 |
| E | 209--226 | 18 |
| **Total** | **175--226** | **52** |

The 82--102-page planning envelope was explicitly diagnostic rather than a
quota. The unit-level review supported a shorter result because most of the
additional pages belonged to complete display families, repeated algebra, or
parallel computational variants whose claim-bearing content was retained in a
single location. The 52-page outcome therefore reflects the approved
essentiality decisions, not tighter typography or the deletion of an
unresolved scientific dependency.

Appendix D contains exactly the eight displays listed above, and Appendix E
contains exactly the five listed above. The formal-result graph was
implemented as specified: three body-authoritative results have proof-only
appendix destinations, four supporting results retain their complete
statement-and-proof units, and the direct Dirichlet-process content law is
presented as an exact Beta result with interpretation rather than a duplicate
proof.

The end-to-end release gate passed against all 102 immutable imported Git
blobs. The final PDF has 261 pages, 43 active TeX files, 257 unique active
labels, 30 active visual records, no blocking citation or reference
diagnostics, no overfull boxes, and no Type 3 fonts. Rendered review covered
appendix boundaries, retained evidence classes, the Appendix E ending, and
the bibliography transition. The exact artifact, hash, and review pages are
recorded in `VALIDATION.md`.
