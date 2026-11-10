# Final readability polish — 2026-11-10

## Scope and standard

This pass reviewed the abstract, acknowledgments, all six chapters, and the
active appendices against the project academic-writing profile. The standard
was precise statistical prose: direct identification of the inferential
target, explicit qualification of empirical evidence, restrained contribution
claims, and terminology consistent with the statistical literature. The pass
did not change source authorities, research results, models, estimands, or the
scope of the advisor response records.

## Revisions

- The abstract now distinguishes models, uncertainty statements, and
  validation criteria without generic framing. It is self-contained and 347
  words.
- The introduction states the four contributions directly and distinguishes
  predictive, posterior, and repeated-sampling evidence.
- Chapter 2 states the 28-day hydrologic result without implying uniform
  dominance across origins, horizons, scores, or scales.
- Chapter 3 replaces product-style descriptions of the software with
  statistical descriptions of fitted objects, inferential methods, and the
  scope of the reported comparisons. Its longest empirical paragraph was
  divided for readability.
- Chapter 4 describes MCMC, variational approximation, recurrent features,
  quantile ordering, and the two applications without engineering or
  promotional language. The PriceFM comparison remains explicitly limited to
  matched average quantile loss.
- Chapter 5 separates mathematical, model-conditional, simulation, and
  application evidence and states the primary comparator set directly.
- Chapter 6 now concludes with the validation criterion appropriate to each
  inferential target rather than a generic framework claim.
- Appendix E describes the tolerance study as finite-panel empirical support,
  not proof of a distribution-free theorem.
- The acknowledgments retain the required, bounded disclosure of AI-assisted
  debugging and language checks. No AI terminology appears in the scientific
  exposition.

## Invariants checked

Citation keys, labels, graphic and input dependencies, and numerical results
are unchanged. One table reference was added in Chapter 3 to connect the prose
to the displayed benchmark. No new scientific claim, bibliography entry,
figure, table, or research-source dependency was introduced.

The final phrase scan found no stock promotional expressions, engineering or
machine-learning framing, drafting markers, or internal workflow language in
the scientific text. Terms such as “framework” remain only where they name an
established statistical construction or a source title.

## Validation

Fast and release validation passed. The accepted local artifact is
`build/release-20261110T084508Z/main.pdf`: 186 US-Letter pages, 4,148,801
bytes, PDF 1.7, SHA-256
`2526bcedfbd154f815217fa188d66eda0110516e5f2cabf3e6d1ea57e3f896aa`.
The release rechecked the frozen research sources. Its log has 12 underfull and
zero overfull boxes, with no unresolved citation, reference, duplicate-label,
missing-file, rerun, or fatal diagnostic. All 32 fonts are embedded and no
Type 3 font occurs. The PDF is searchable.

Physical pages 9, 12, 14, 38, 71, 99, 102, 133, and 140 were rendered and
inspected. They cover the abstract, disclosure, contribution framing, revised
chapter conclusions, empirical summaries, and final synthesis. No clipping,
collision, unreadable content, or abnormal page break was found.

This is a local editorial checkpoint. It does not represent committee approval,
an accessibility-conformant filing PDF, an independent Overleaf compilation,
or a push or merge to `main`.
