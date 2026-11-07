# QDESN authority refresh: implementation record

## Scope and authority

This revision replaces the live Chapter 4 QDESN authority with
`AntonioAPDL/Bayesian-Quantile-Regression-withDeep-Echo-State-Network-Features---Thesis`
at commit `aa613b056b054edd9347eeb4739bd4bce0c92818`. The former
`Article-Q-DESN---Version-2` repository remains historical and computational
provenance under `SRC-QDESN-LEGACY`; it is not used to fill current numerical
gaps. Chapter 3 and its assets are explicitly outside scope.

The new source was inspected in a fresh isolated clone. Its main article and
supplement compiled independently under the server's TeX Live 2018
installation after the required pdfLaTeX and BibTeX passes, with no unresolved
citations or references. The source contains all manuscript tables, macros,
figures, and bibliography-style dependencies referenced by those documents.

## Scientific diagnosis

The current source changes the streamflow application at the target level,
not merely at the result-table level. The implemented dissertation projection
therefore updates the target, computation, experiment, results, and
interpretation together:

- every issued GloFAS member has unit likelihood weight;
- 28 latent future-reference factors and 1,428 issued-member factors enter the
  forecast-window target;
- the future-reference likelihood defines a normalized sequential response
  distribution, with no replacement Gaussian path prior;
- regression updating retains reference--discrepancy covariance;
- the local Gaussian--Delta path update retains response--design covariance;
- reported forecasts are marginal response quantiles of the retained path
  factor, without an added response-noise term or post-hoc crossing correction;
- all six fitted models improve on raw GloFAS, all four quantile models improve
  on both Gaussian baselines, and Q--DESN under AL has the lowest grid aCRPS;
- the PriceFM analysis selects among Q--DESN and MQ--DESN under AL and exAL for
  each region, then holds that choice fixed across three 2025 test folds.

The former coverage claims and the former PriceFM win-count comparison are not
carried forward because they belong to the superseded target and experiment.

## Dissertation changes

- `chapters/04-research-c.tex` now states the current GloFAS target,
  latent-path approximation, seven-model score comparison, and selected-DESN
  PriceFM design and results.
- `appendices/d-qdesn-technical.tex` now records the source counts, update
  shapes, covariance terms, stopping rules, PriceFM fold boundaries, and
  compact claim-relevant simulation evidence.
- The abstract and Chapter 6 synthesis now use the current bounded empirical
  conclusions.
- One current GloFAS figure was imported byte-for-byte. Existing simulation
  figures retained by the source were hash-verified rather than copied again.
- Current values and paths are centralized in
  `tables/ch04-qdesn/current_source_aliases_20261106.tex`.
- `source-manifest.json`, `docs/claim-evidence.json`, and
  `docs/imports/ch04-qdesn.json` distinguish current authority from legacy
  provenance.

No code, data, fitted objects, caches, simulation archives, source histories,
or external build dependencies were imported.

## Unchanged-source verification

Fresh isolated clones confirm that the other requested authorities remain at
the commits already used by the dissertation:

| Source | Commit | Verification |
| --- | --- | --- |
| `RQR-GIBBS` | `4223c6a3a44f376255bacdca91db71cdf4f3afde` | main and supplement hashes unchanged |
| `MTI-EXTENSIONS` | `f345d946aa5a81b94795838bec58d874a0fdd0c9` | main and supplement hashes unchanged |
| `exdqlm---Article` | `98cec593d11bf32715a690ae168086f16160e7f0` | JSS manuscript hash unchanged |
| `exdqlm` package | `e51045a4324901cced27ca2aaa22569afbc8e0e6` | current package head unchanged |

These comparisons are deliberate no-ops: no Chapter 2 or Chapter 5 prose or
assets changed without a source discrepancy.

## Frozen Chapter 3 guard

The following baseline Git objects must remain unchanged through the final
merge:

- `chapters/03-research-b.tex`:
  `85ed8219597648edd34e7aa8e6884243aef017a9`
- `appendices/c-hydrology-technical.tex`:
  `9529faec7cb6828ec41c688c2c45ae0821d63c06`
- `figures/ch03-environ` tree:
  `4ab337bd505ab7054406a2fa5225036038aa83ae`
- `tables/ch03-environ` tree:
  `35cfaaa56ce9cbad1adcf9d1c6439c4cb1bea25b`

## Reproduction and acceptance

The source and destination hashes are recorded in
`docs/source-refresh-20261106.json` and `docs/imports/ch04-qdesn.json`.
The accepted local artifact is
`build/release-20261107T042021Z/main.pdf`: 253 US-Letter pages, 16,235,653
bytes, PDF 1.7, SHA-256
`920f729693533463e1852f76f574232006a78cf64034236ca11ce4294c60ed4c`.
All 18 tests and the research, editorial, import, and structure validators
pass; the release gate rechecked 108 immutable source blobs, including all six
current-projection records. The final log has 25 underfull-box notices, zero
overfull boxes, and zero blocking citation, reference, label, file, or fatal
diagnostics. Every font is embedded and no Type 3 font occurs.

Extracted-text searches found none of the superseded GloFAS calibration or
PriceFM comparison claims in the active PDF. Physical pages 137, 139, 142,
220, and 222 were rasterized and inspected. They cover the current GloFAS
target and results, the issued-forecast display, the PriceFM results table,
and the Appendix D target and moment details; no clipping, collision, duplicate
caption, malformed glyph, or unreadable display was found. The PDF remains
untagged, as before.

The source and destination hashes are recorded in
`docs/source-refresh-20261106.json` and `docs/imports/ch04-qdesn.json`.
GitHub and Overleaf synchronization remain separate events; a GitHub push does
not establish an Overleaf compile.
