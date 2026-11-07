# Essential-appendix review and implementation record

**State:** implemented and locally validated

**Pre-curation thesis commit:**
`6906f9e6bfa20bc2ffc40cbb3575558c0ef16307`

**Pre-curation PDF:** 253 pages, with 52 numbered appendix pages

**Pre-curation PDF SHA-256:**
`920f729693533463e1852f76f574232006a78cf64034236ca11ce4294c60ed4c`

**Curated PDF:** 227 pages, with 26 numbered appendix pages

**Curated PDF SHA-256:**
`505d326622ae657615cde95e42e7387b7732737d1f9be3ba120cb506ebe42c66`

## Outcome

The five-appendix architecture is retained because each appendix serves a
distinct research chapter or cross-chapter purpose. The revision reduces the
appendix sequence by half without changing the principal inferential targets,
theorem scope, reported numerical results, attribution, or evidence strength.
The reduction comes from consolidating repeated calculations, replacing
parallel display families with concise qualifications, and keeping standard
derivations in their cited sources.

| Appendix | Before | After | Reader-facing role |
| --- | ---: | ---: | --- |
| A | 4 pages | 2 pages | Cross-chapter distinctions among targets, latent scales, multiple-quantile constructions, and uncertainty statements. |
| B | 6 pages | 3 pages | exDQLM posterior target, transfer-function and shrinkage blocks, structured LDVB approximation, and post-fit synthesis. |
| C | 3 pages | 2 pages | Source-indexed MCMC, Laplace--delta approximation boundary, and interpretation of source-specific likelihood parameters. |
| D | 21 pages | 9 pages | Q--DESN posterior/composite target, nonstandard computation, claim-changing simulation qualifications, PriceFM fold design, and GloFAS path approximation. |
| E | 18 pages | 10 pages | MPI/MTI proof graph, profile computation, finite-panel calibration, feasibility, and proposed endpoint computations. |
| **Total** | **52 pages** | **26 pages** | |

The complete dissertation is 227 pages rather than 253. No smaller type,
reduced line spacing, or margin change was used to obtain the reduction.

## Inclusion record

`appendix-essentiality-map.json` now contains 341 unit records:

| Unit type | Records |
| --- | ---: |
| Section, subsection, or subsubsection | 115 |
| Algorithm | 8 |
| Labeled equation group | 149 |
| Theorem or proposition with proof obligation | 8 |
| Appendix display | 61 |
| **Total** | **341** |

The final dispositions are 96 `RETAIN`, 161 `CONDENSE`, 17 `SUMMARIZE`, and
67 `DEACTIVATE`. There are 128 active mapped units and 213 inactive historical
units. Each inactive unit retains a source path, baseline commit, page range,
and no-loss location. The validator now rejects a `DEACTIVATE` decision that
remains active.

## Retained appendix displays

Only three appendix displays remain:

1. `qdesn2026:tab:supp-sensitivity-summary`, a four-row consolidation of the
   single-quantile, recursive-predictor, multiquantile-score, and ordering
   qualifications;
2. `qdesn2026:tab:supp-pricefm-fold-design`, the exact PriceFM validation and
   test boundaries; and
3. `rqr2026:tab:supp-mti-profile-policy`, the calibrated finite-panel MTI
   policy.

Appendices A--C contain no figure or table, Appendix D contains the two tables
above, and Appendix E contains the policy table. No appendix figure remains.
Claim-bearing conclusions formerly carried by longer display families are
stated in the corresponding research chapter or in the compact Q--DESN table.

## Formal-result graph

Chapter 5 retains the authoritative statements of the principal population
results, with their proofs in Appendix E. The appendix also retains complete
statements and proofs for mean-preserving contraction, the profile-radius
lemma, exact fractional empirical balance, and the convex midpoint profile.
Standard Dirichlet-process conjugacy is represented by its exact Beta law and
its interpretation rather than by a duplicated proof.

## Body links and prose

Chapter bridges now point to the relevant appendix section rather than to an
undifferentiated technical archive. The Q--DESN chapter distinguishes sections
within Appendix D, and the MTI chapter distinguishes proof, computation,
calibration, and extension sections. Removed labels are not cited by the active
manuscript. The compiled dissertation contains no drafting markers,
collaboration-tool names, artificial-intelligence terminology, or production
instructions.

Software and implementation terminology remains only where it is part of the
statistical software contribution, a stated numerical method, or a documented
limitation. The research prose otherwise uses statistical targets,
assumptions, computations, and empirical findings directly.

## Implementation commits

The scholarly changes are separated by appendix:

- Appendix A and its Chapter 1 bridge: `d1a03494c8bab944f4933274cf8d18d3abec63a1`;
- Appendix B and its Chapter 2 bridges: `c7d8e19da4bd92cdd574fb083714ff2b28b1e885`;
- Appendix C: `2595a74356993dc70c32f74e2809dec31cfa5bc5`;
- Appendix D and its Chapter 4 bridges: `b1332ddda22a7bec913de320de0b686527b015f9`; and
- Appendix E and its Chapter 5 bridges: `c472f67e91cb2094c46217447cd2b7bad5494d59`.

## Validation

The fast gate passes 19 tests and all research, editorial, manuscript-import,
and structure validators. The active graph contains 37 TeX files, 216 unique
labels, six migration records, and 24 graphic or visual records, all covered by
the accessibility ledger. The final TeX log has 24 underfull-box notices, no
overfull boxes, and no blocking citation, reference, label, file, or fatal
diagnostic. All 24 reported fonts are embedded and no Type 3 font occurs.

Rendered inspection covered every appendix opening and ending, the retained
Q--DESN and PriceFM tables, representative proof and equation pages, and the
appendix-to-bibliography transition. No clipped text, collision, stranded
heading, one-line spill page, unreadable table, or malformed glyph was found.

The validation establishes a self-contained local dissertation build. It does
not rerun research simulations, establish material-specific reuse permission,
produce a tagged accessibility-conformant filing PDF, or verify an Overleaf
pull and compile.
