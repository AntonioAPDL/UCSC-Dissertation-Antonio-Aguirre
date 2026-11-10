# Final author-style revision

Date: 2026-11-10  
Manuscript commit: `d076051b4ba1e4dee391aad882cb9fb4453352e9`  
Baseline: `b0f688e`

## Scope

This revision implements the author's final terminology and prose decisions
across the abstract, acknowledgments, six chapters, five active appendices, and
two connected tables. It preserves the statistical models, estimands,
assumptions, numerical results, proofs, citations, figures, and source
authorities. The main changes are:

- contribution statements use first-person plural or direct object-centered
  prose rather than referring to the candidate in the third person;
- the abstract gives a concise account of the MCMC and variational procedures
  for dynamic and static AL/exAL regression without a method-ranking claim
  unsupported by a single common comparison;
- the five-origin hydrology design is tied to the cost of repeated dynamic
  fitting, data processing, storage, and post-processing;
- Q--DESN and MQ--DESN are distinguished from earlier bootstrap aggregation,
  residual-quantile regression, and post-fit calibration, and MQ--DESN is
  described through its generalized Bayes posterior and adjacent-coefficient
  regularization without claiming explicit noncrossing constraints;
- the exAL background includes only the coefficient-coverage comparison
  supported by Yan, Zheng, and Kottas, with the strongest qualification at the
  0.05 quantile;
- proposed Q--DESN and MTI extensions are presented as future work, without
  repository or source-audit commentary in the dissertation;
- the MTI chapter and Appendix E use distributional and generalized-Bayes
  terminology consistently and state the mathematical, model-based, and
  repeated-sampling claims directly;
- unnecessary defensive qualifications and process-oriented sentences were
  removed, while qualifications needed to distinguish inferential targets,
  empirical findings, and proved claims were retained.

The acknowledgments retain the required bounded disclosure: AI-assisted tools
were used for selected code debugging and editorial checks of grammar,
readability, organization, and consistency, not for full code implementation,
method formulation, proof derivation, bibliography searches, independent
analysis, or generation of results.

## Consistency controls

The revision ledger, appendix essentiality map, and display ledger were updated
to the current derivatives. Source and extracted-PDF scans found no remaining
targeted promotional phrases, generic drafting tropes, third-person
self-attribution, source-version commentary, obsolete composite-posterior
terminology, or use of *law* where *distribution* is intended. The only
reader-facing reference to AI-assisted tools is the approved disclosure in the
acknowledgments. Statistical uses of *benchmark* were retained.

The abstract contains 323 words under the same source-word convention used for
earlier compliance checks and remains below the 350-word indexing
recommendation.

## Validation

The complete release gate passed with:

```bash
bash scripts/validate.sh --tier release \
  --audit-root /tmp/bruno-complete-audit.xDFvN4
```

The gate passed all 20 tests and the research-audit, editorial-audit, Bruno
revision, author-comment, manuscript-import, and structure controls. It
rechecked 120 immutable source blobs, 108 cited keys, 192 active labels, and 15
active visual records.

The accepted local artifact is
`build/release-20261110T102200Z/main.pdf`:

- 186 US-Letter pages;
- 4,146,465 bytes, PDF 1.7;
- SHA-256
  `89855c527c712777cdc92dd0671a41d7076c275e5af57150ecd09c836cd81e1b`;
- searchable, unencrypted, and untagged;
- 32 embedded fonts and no Type 3 fonts;
- 11 underfull and zero overfull boxes;
- no unresolved citation, reference, duplicate-label, rerun, missing-file, or
  fatal diagnostic.

Physical PDF pages 9, 72, 101, 102, 130, 140, 152, 155, and 165 were rendered
from the accepted release and inspected. These cover the abstract, Q--DESN and
MTI openings, synthesis, and the revised appendix openings. No clipping,
collision, unreadable content, malformed glyph, or abnormal page break was
found.

This record validates the local source and artifact. It does not constitute
committee approval, an independent Overleaf compilation, or an
accessibility-conformant filing PDF.
