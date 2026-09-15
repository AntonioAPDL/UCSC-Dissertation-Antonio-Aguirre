# Template provenance and changes

Community template, not an official UCSC approval. Audited 2026-09-15.

Upstream: https://github.com/adamnovak/ucscthesis
Pinned commit: 38a711c243bd78f1ace969f4dacb15e9c52c39de (2020-12-05).
Class header: v3.2-ucsc-4, 2017-03-29. LPPL 1.3c or later.

The root class and three `.clo` files are byte-for-byte upstream copies.
The upstream license and available sample files are retained in
`vendor/ucscthesis/`. Its log message about a modified class is upstream text;
it does not mean this project changed the vendored class.

Project adaptations are separate, readily replaceable files:

- `preamble.tex` overrides the legacy 1.37 spacing factor with `setspace`
  double spacing; initializes its legacy current-size hook and the command
  expected by natbib; fixes ordinary-page left margins; centres page numbers on
  the physical sheet; keeps footnotes and captions at 12 pt; adds modern
  hyperlinks, mathematics, and author-year references.
- `frontmatter/title.tex` adapts the upstream title-page layout with explicit
  role placeholders, an unconfirmed committee block and no signed approval.
  It removes the hardcoded Chair suffix. This adapted file is under LPPL
  1.3c or later, with the upstream attribution retained here and in its header.
- `main.tex` explicitly orders appendices before the final bibliography and
  handles Roman/Arabic numbering. The blank copyright leaf is counted as ii.
- Times-compatible `mathptmx` is used for portability in the tested TeX Live
  installation. It is mature rather than a claim of latest math typography;
  any later switch to `newtx` requires font, symbol and layout verification.

Do not edit the vendored class for routine changes. No external repository,
symlink, dataset or shell escape is needed to compile. No new license is
imposed here on the author's future dissertation content.
