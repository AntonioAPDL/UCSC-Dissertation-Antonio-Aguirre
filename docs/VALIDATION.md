# Validation record

Performed 2026-09-15 in a Linux container. This is technical verification of
this starter, not a verified Overleaf run or institutional approval.

## Actual build

- A fresh copy containing source files only was compiled with
  `bash scripts/build.sh`, which invokes pdfLaTeX/BibTeX through latexmk.
- pdfTeX 3.141592653-2.6-1.40.25, TeX Live 2023/Debian;
  LaTeX2e 2023-11-01 patch 1; latexmk 4.83 (2024-01-31).
- Exit 0. Output: 20 pages. No undefined citations/references, duplicate
  labels/destinations, overfull or underfull boxes in the final LaTeX log.
- One documented package warning remains: caption does not recognize this
  legacy class and uses standard defaults. The project explicitly sets its
  caption size/alignment; the actual rendered captions were checked.
- Initial build defects (legacy setspace current-size hook and natbib's
  expected newblock definition) were repaired in the preamble. Original
  vendor class/size files remain byte-identical to the pinned upstream.

## Actual PDF checks

- Every page is US Letter (612 x 792 PDF points), portrait.
- Title and blank second page are counted i/ii with no visible numbers.
  Contents start iii; front matter ends viii; chapter 1 starts Arabic 1 on
  PDF page 9. Appendix A is Arabic 10-11; final bibliography is Arabic 12.
- All 18 visible page numbers are centred at x = 306 PDF points. Minimum
  lower edge clearance is 0.910 inches, exceeding 0.75 inches.
- Layout settings: left 1.50, right 1.25, top 1.30, bottom 1.35 inches.
  The vertical allowance was added after measured glyph bounds reached
  beyond the minimum-margin envelope. Final extracted text bounds stay
  within left >=1.5 and other margins >=1.25 inches (0.6-point tolerance).
  Figure and table placement were also visually inspected.
- Body size is 12 TeX points (about 11.96 PDF points). The double-spaced
  baseline is 23.99748 TeX points; the median measured PDF baseline is
  23.908 PDF points across 29 samples. TeX points and
  PDF points use slightly different inch conversions.
- Seven fonts are embedded Type 1 fonts. Ordinary footnote/caption/table
  text remains 12 TeX points; mathematical scripts and note marks scale
  normally. No bitmap Type 3 fonts were found.
- Text is extractable. There are 28 PDF outline entries; Roman/Arabic page
  labels and working internal link targets are present. Link destinations
  were structurally checked, not every external website opened from the PDF.
- Demonstrated: equation A.1, theorem/proof A.1, prose algorithm A.1,
  figure A.1, table A.1, footnote, two real citations and appendix references.
  The short proof was kept together after the first layout review.
- Every starter page was rendered. Contact sheets and individual front
  matter, body, mathematical/float and bibliography pages were inspected.
  A clean-directory build has identical text and rasterized pages to the
  inspected final PDF; its PDF is the delivered preview.
- The requirements report was generated from its Markdown using Pandoc's
  parsed document and ReportLab. Its 12 pages were rendered and inspected,
  including the comparative tables, timeline and source register. Its layout
  is a report layout, not the dissertation layout.

## Limits and future checks

No Overleaf account linking, remote GitHub creation, synchronization cycle,
or actual user-machine IDE permissions were tested. Landscape pages and
special facing-caption full-page figures are unused and untested. No PDF/A,
PDF/UA or tagged-accessibility compliance is asserted. Real names/titles,
long committee lists, imported article macros, complex tables/figures and
substantive chapter content will need renewed checks after introduction.
Metadata and approval remain unresolved; the substantive abstract, chapters,
acknowledgments and contributions have not been written.

Machine-readable results and retained final logs are in `docs/validation/`.
Preview SHA-256: `27497309dd35d101331403125a97ae3bab144ab2706f2f7df4c636d5bb0b779e`.

## Muscat four-project scaffold revalidation

Performed 2026-09-15 after the author supplied the identity mapping and
four-project architecture:

- `bash scripts/build.sh` completed successfully under pdfTeX
  3.14159265-2.6-1.40.19 (TeX Live 2018).
- Output is 22 US Letter pages, 98,529 bytes, SHA-256
  `d8cac07847f10e1cd9ac0800a8f155e7127a3de4d9ec3cec25c572723b62062a`.
- The final log has no undefined citations/references, duplicate-label report,
  overfull/underfull boxes, or font warnings. The known legacy-class caption
  warning remains.
- All seven PDF fonts are embedded Type 1 fonts; text extraction finds the
  official long name and all six chapter titles.
- The title page, both table-of-contents pages, and both MTI-placeholder pages
  were rendered and visually inspected. The official long name fits the title
  page, the four research chapters and synthesis appear in the intended order,
  and no clipping or collision was observed.

This revalidation covers metadata and empty chapter scaffolding only. It does
not validate substantive chapter prose, imported source assets, or the final
university record spelling.

## Muscat manuscript-first conversion revalidation

Performed 2026-09-15 after local conversion of all four research chapters:

- The documented build script completed successfully under pdfTeX
  3.14159265-2.6-1.40.19 (TeX Live 2018). After the final chapter-local
  navigation wording was cleaned up, two additional pdfLaTeX passes stabilized
  pagination and cross-references.
- Final output is 367 US Letter pages, 19,926,717 bytes, SHA-256
  821793008fcb183c59ad9cc42e837c4aac75934ffdd0066b1f3e513dd8878a8e.
  Research Chapters 2--5 begin on PDF pages 39, 106, 154, and 256.
- The final log has zero undefined citations, undefined references, duplicate
  labels, changed-label notices, oversized floats, overfull boxes, pdfTeX
  warnings, or missing-file errors. Forty-one underfull-box diagnostics remain
  from conservative line breaking in imported prose, tables, and bibliography;
  they do not indicate clipping. The known legacy-class caption warning and two
  automatic !h to !ht float-placement adjustments remain.
- All 35 PDF fonts are embedded; no Type 3 fonts occur. PDF metadata contains
  the unresolved working title and the official long author name
  Jose Antonio Aguirre Perez de Leon.
- The manuscript-import validator passed against the retained audit root. It
  checked four chapter manifests, nine source documents, 96 top-level section
  dispositions, 102 destination records and immutable Git blobs, 54 imported
  TeX files, 434 unique labels, and 124 cited keys. Dependency, file-type,
  local-only rights, absolute-path, and secret scans also passed.
- Chapter openings and representative prose, equation, theorem/proof,
  algorithm, table, figure, integrated-support, and extension-transition pages
  were rasterized and visually sampled across all four chapters. The sampled
  pages showed no clipping or collisions. Dense tables and selected long
  QDESN derivations use provisional compact typesetting and still require a
  final human readability review.
- A case-insensitive scan of Chapters 2--5 finds no stale appendix or
  supplement navigation. Source supporting material now appears as ordinary
  chapter sections.

This validation proves a self-contained technical conversion and local build,
not scientific acceptance, full computational reproduction, contribution-role
allocation, direct-reuse permission, committee approval, accessibility
compliance, or filing readiness. The research repositories remain external and
no source computation was rerun.

## 2026-09-16 editorial-provenance validation

Before scientific editing, the import workflow was separated into an immutable
baseline and editable dissertation derivatives. The following checks passed
under Python 3.11:

- lifecycle-invariant unit tests;
- `scripts/validate_research_audit.py` for eight sources and 32 evidence
  records;
- check-only importer verification of the five manuscript source snapshots;
- `scripts/validate_manuscript_imports.py --audit-root ...`, including all 102
  immutable source blobs, the four schema-2 import manifests, baseline/current
  revision-ledger linkage, 434 unique labels, and 124 cited keys; and
- `git diff --check` through the fast validation tier.

This validation establishes workflow safety and provenance continuity. It does
not yet certify revised chapter prose or an Overleaf build.

## 2026-09-16 scholarly-inventory validation

The read-only post-import audit completed before chapter editing. The fast
validation tier passed with the retained fixed-commit audit root and reported:

- 29 prioritized scientific, editorial, attribution, and presentation issues;
- explicit dispositions for all 95 labeled displays (46 KEEP, 30 MERGE,
  18 TEXT-SUMMARY, and 1 OMIT);
- 11 bibliography reconciliation groups, including three records that need
  factual metadata correction rather than key-only deduplication; and
- continued passage of the research-audit and manuscript-import validators,
  including all 102 immutable source blobs, 434 unique labels, and 124 cited
  bibliography keys.

The audit is a revision specification, not a certification of the imported
science. Candidate-specific coauthor roles, material-specific reuse approval,
the stronger TCSP result, administrative metadata, and an independently
inspected Overleaf build remain unresolved. The chapter pass must retain
collective attribution and narrow unsupported claims rather than fill those
gaps by inference.

## 2026-09-16 global-integration validation

After canonicalizing the 11 bibliography groups, the chapter validation tier
passed against the retained audit root. It rechecked all 102 immutable source
blobs and resolved all 118 cited keys. The final pdfLaTeX pass produced a
367-page US Letter PDF of 19,926,260 bytes with no undefined citation or
reference, duplicate-label, missing-file, or overfull-box diagnostic. The log
contains 42 underfull-box notices, the known legacy-class caption warning, and
two automatic `!h`-to-`!ht` float adjustments. The PDF is untagged and retains
the unresolved working title.

The generated bibliography was inspected for the three factual corrections:
Emily Tallman, the Nishimura--Suchard 2023 record, and Yunwen Yang, Huixia Judy
Wang, and Xuming He appear under their canonical entries. PDF SHA-256:
`3f096e7b8555f27c0ee7c83eb9fbce46b5d533ad7107b3f3b73f45dd1567f39a`.
