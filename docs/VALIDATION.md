# Validation record

## 2026-10-28 Fall 2026 filing-metadata release

The Fall 2026 date and dean update was validated from a fresh timestamped
release directory. Because the earlier temporary audit-root record no longer
contained usable repositories, the release used fresh temporary no-checkout
clones of the five explicitly authorized source repositories and removed them
after validation. No original research working tree was fetched, checked out,
or changed. The gate passed all 18 tests, rechecked all 102 immutable imported
Git blobs, resolved all 116 cited keys, and retained the validated graph of 43
active TeX files, 257 active labels, six migration records, and 30 active
visual records.

The accepted ignored artifact is
`build/release-20261028T193327Z/main.pdf`: 254 US-Letter pages, 16,491,675
bytes, PDF 1.7, SHA-256
`b46b49ed32b6d5f70e4caf44695cf1181b0e0f952dfdf6d3e088f3f57db91672`.
The final log has 25 underfull-box notices, zero overfull boxes, and zero
blocking citation, reference, label, file, or fatal diagnostics. All 32 font
rows are embedded and no Type 3 font occurs. The PDF remains untagged.

The title page was extracted and rasterized at 150 dpi. Direct inspection
confirmed `December 2026`, Donald Smith, the exact two-line title `Interim Vice
Provost and Dean of Graduate Studies`, the official candidate name, and the
four-member committee block. Text, rules, spacing, margins, and the draft
notice are legible without clipping or collision. The exact dissertation title
remains an explicit placeholder, and the page does not assert dissertation
approval. The blank copyright leaf remains an allowed author choice.

Private email contents, student identifiers, addresses, signatures, and
administrative attachments were not added to the repository. This release
validates the local source and rendering; it does not supply the missing title,
committee approval/signatures, reuse/contribution acknowledgments, a
candidate-specific MyUCSC degree-field comparison, an Overleaf build, or an
accessible tagged filing PDF.

## 2026-10-28 approved-committee metadata release

The Dissertation Reading Committee metadata update was validated from a fresh
timestamped release directory against the retained current-source audit
clones. The gate passed all 18 tests, rechecked all 102 immutable imported Git
blobs, resolved all 116 cited keys, and retained the validated graph of 43
active TeX files, 257 active labels, six migration records, and 30 active
visual records.

The accepted ignored artifact is
`build/release-20261028T192313Z/main.pdf`: 254 US-Letter pages, 16,491,666
bytes, PDF 1.7, SHA-256
`00b19e103360973e89ab490fdc7dae7849c6078fe0c9c269d50332f55cbeb2cf`.
The final log has 25 underfull-box notices, zero overfull boxes, and zero
blocking citation, reference, label, file, or fatal diagnostics. The PDF
remains searchable, unencrypted, and untagged.

The title page was extracted and rasterized at 150 dpi. Direct inspection
confirmed the official long candidate name and the committee block: Raquel
Prado, Chair; Bruno Sansó; Paul Parker; and Athanasios Kottas. The accent,
signature rules, margins, line spacing, and unresolved-field notice are
legible, with no clipping or collision. The page identifies an approved
Dissertation Reading Committee but does not assert that the dissertation has
been approved. The title, conferral date, dean fields, and signatures remain
explicit placeholders.

The private administrative messages and nomination attachment used to verify
the committee were not copied into the repository. This release records only
the approved names, role, approval dates, and the boundary between committee
appointment and dissertation approval.

## 2026-10-28 final comprehensive polish release

The final dissertation polish was validated from a new timestamped output
directory with the release tier and the retained five-clone current-source
audit root. The public record omits that machine-local path. The gate passed
18 unit tests; reconciled eight research sources, 30 claim-evidence records,
29 historical editorial issues, 102 display decisions, and 11 bibliography
groups; checked four chapter manifests, nine source documents, and 96 section
dispositions; and rechecked all 102 imported records against their immutable
Git blobs. It resolved all 116 cited keys and covered 43 active TeX files, 257
unique active labels, six migration records, and 30 active visual records.

The accepted ignored artifact is
`build/release-20261028T190946Z/main.pdf`: 254 US-Letter pages, 16,491,650
bytes, PDF 1.7, SHA-256
`28898586b38c3db7ccc4c16d88fd846bdb0578aef0f3fe0fa9bb5d679e1300e7`.
The title metadata retains the unresolved placeholder and the official author
field remains `Jose Antonio Aguirre Perez de Leon`. The PDF is searchable,
unencrypted, and untagged.

The final log has zero unresolved citations or references, multiply defined or
unstable labels, missing files, overfull boxes, fatal errors, or emergency
stops. It contains 25 underfull-box notices and the documented legacy-class
caption warning. All 32 reported font rows are embedded and no Type 3 font is
present.

The research chapters begin on physical pages 36, 80, 118, and 145; Chapter 6
begins on physical page 180. Appendices A--E begin on physical pages 192, 196,
202, 205, and 226 and occupy numbered pages 169--220, exactly 52 pages. The
bibliography begins on physical page 244 and ends on page 254. Twenty-one
release pages covering the title/front matter, every chapter opening and
ending, the revised Chapter 3 exAL display, every appendix opening, the
bibliography opening, and the last page were rasterized. Their pixels match
the corresponding chapter-tier review images exactly. Direct inspection and
PDF word-coordinate checks found no clipping, collision, missing glyph,
stranded heading, margin violation, or unreadable display.

This release validates the bounded organizational and prose revision. It does
not establish filing readiness, material-specific reuse permission, granular
candidate/coauthor roles, an accessible tagged PDF, or a successful Overleaf
pull and build. No research repository was changed and no research
computation was rerun.

## 2026-10-28 essential-appendix release

The approved essential-appendix revision was validated from a fresh,
timestamped output directory with:

```text
bash scripts/validate.sh --tier release --audit-root /PATH/TO/IMMUTABLE/AUDIT-CHECKOUTS
```

The public record omits the disposable machine-local audit path. Two intact
local Git histories and three disposable no-checkout verification clones
supplied the fixed historical objects without modifying any research working
tree. The gate passed 18 unit tests; reconciled eight sources, 30 evidence
records, 29 prioritized editorial issues, 102 historical display decisions,
and 11 bibliography groups; and rechecked all 102 imported records against
their immutable source Git blobs. Structure validation covered 43 active TeX
files, including two compiler-resolved macro inputs, 257 unique active labels,
six migration records, 30 active graphic or visual records, and all 116 cited
keys.

The accepted ignored artifact is
`build/release-20261028T064248Z/main.pdf`: 261 US-Letter pages, PDF 1.7,
16,502,013 bytes, SHA-256
`19ffa613857ba95d95e905e6c7782abb0d35321f434ee449ee8f94cf9ff14e1f`.
The final log has no unresolved citations or references, duplicate or unstable
labels, missing files, overfull boxes, fatal errors, or emergency stops.
Twenty-five underfull-box notices remain as benign line-breaking diagnostics.
All 32 reported font rows are embedded and no Type 3 font occurs. The PDF is
searchable but untagged.

The final appendix sequence occupies numbered pages 175--226: Appendix A,
175--178; Appendix B, 179--184; Appendix C, 185--187; Appendix D, 188--208;
and Appendix E, 209--226. This is 52 appendix pages, down from 204 in the
accepted 414-page baseline. The full dissertation is 153 pages shorter; 152
of those pages come from the selective appendix revision and one from final
bibliography reflow. No smaller type, margin reduction, or content-obscuring
layout was used.

Rendered review sampled physical PDF pages 199, 209, 212, 220, 231, 233, 243,
250, and 251. These cover the Appendix A, C, D, and E openings; a retained
Q--DESN specification table; a retained calibration figure; the calibrated
MTI policy table; the end of the proposed-extension discussion; and the
bibliography transition. Earlier chapter-gate inspections also covered the
Appendix B opening, Appendix C algorithms, all retained Appendix D and E
display classes, and the relevant chapter bridges. The sampled pages show no
clipping, collision, margin breach, illegible table, stranded continuation,
or malformed appendix transition. A PDF text scan found none of the internal
revision phrases prohibited by the plan in the reader-facing document.

This release validates the selected technical record and its provenance. It
does not assert a tagged-accessibility result, material-specific reuse
permission, committee approval, filing readiness, a research recomputation,
or an independently inspected Overleaf build. Push, merge, and Overleaf pull
remain separate handoffs.

## 2026-10-26 current-source refresh release

The manuscript-first current-source refresh was validated from a fresh
timestamped output directory with:

```text
bash scripts/validate.sh --tier release --audit-root /PATH/TO/IMMUTABLE/AUDIT-CLONES
```

The public record omits the machine-local audit path. The gate passed 10 unit
tests; reconciled eight sources, 30 claim records, 29 editorial issues, 102
active displays, and 11 bibliography groups; rechecked all 102 immutable
baseline Git blobs; resolved 83 active TeX files, 490 unique active labels, six
appendix migrations, 47 active visuals, and all 121 cited keys; and confirmed
that no authentication secret or absolute local source path entered the public
projection.

The accepted ignored build artifact is
`build/release-20261027T005737Z/main.pdf`: 439 US-Letter pages, PDF 1.7,
20,511,580 bytes, SHA-256
`92e4c36c451ecfceca2e0674e7d904f40f9b63e863f5799ba4b310dc262391d1`.
Its final log has zero unresolved citations or references, duplicate or
unstable labels, missing files, PDF-version inclusion warnings, oversized
floats, overfull boxes, fatal errors, or emergency stops. Thirty underfull-box
notices remain as benign line-breaking diagnostics. All 52 font records are
embedded; no Type 3 font remains. The PDF is searchable but untagged.

The clean build initially exposed tall Q--DESN appendix tables, crowded MTI
sensitivity headers, and a Type 3 DejaVuSans font inside the current PriceFM
regional-comparison PDF. The refresh script now converts only those tall
tables to page-breaking `longtable` displays, retains their complete captions
on the first page and short continuation headers thereafter, adjusts table
padding and header line breaks without changing values, and creates a recorded
Ghostscript `NoOutputFonts` rendering derivative of the PriceFM figure. The
immutable copied source asset remains available. Source and derivative have the
same 468 by 518.4 point page and were visually compared; plotted data, labels,
caption, and claim are unchanged.

Rendered review covered the title/front matter; Chapter 4 and 5 openings; the
principal GloFAS figure; Appendix D and E openings; first and continuation pages
of the multiquantile score, recursive-policy, variational, and recovery tables;
both MTI partition-sensitivity tables; the PriceFM source/derivative pair; and
the final bibliography page. The sampled pages showed no clipping, collision,
margin breach, stranded continuation caption, or illegible evidence display.

This validation establishes current-source integration and local rendering,
not computational reruns, coauthor or publisher reuse permission, committee
approval, filing readiness, a tagged-accessibility claim, or an independently
inspected Overleaf build. The working title and administrative metadata remain
unresolved. GitHub push and Overleaf pull are separate handoffs.

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

## 2026-09-16 Chapter 2 milestone validation

The Chapter 2 milestone passed the chapter validation tier against the retained
audit root. The final build is 362 US Letter pages and 19,507,649 bytes, with
no undefined citation or reference, duplicate-label, missing-file, or overfull-
box diagnostic. Thirty-nine underfull-box notices, the known caption-package
warning, and two automatic `!h`-to-`!ht` adjustments remain. PDF SHA-256:
`82032cff68289df80e2376a43a2739cd33f904dc6a8d769f0ffc957b24ef4054`.

The Chapter 2 opening, the relocated package-design section, a dense LDVB
equation page, the Sunspots transition, the sparse-recovery table, and the
chapter ending were rasterized and inspected. Text, mathematics, and tables
were legible with no clipping or collisions. The chapter contains 14 retained
labeled displays after implementing its three MERGE and two TEXT-SUMMARY
decisions. This validates document integration and rendering, not a new run of
the external research computation.

## 2026-09-16 Chapter 3 milestone validation

The Chapter 3 milestone passed the chapter validation tier. The final build is
355 US Letter pages and 19,000,993 bytes, with no undefined citation or
reference, duplicate-label, missing-file, or overfull-box diagnostic. Thirty-
seven underfull-box notices, the known caption-package warning, and two
automatic `!h`-to-`!ht` adjustments remain. PDF SHA-256:
`04d9797e9d02b8cc501466c20a5e14f4933514bd2b38c7bb34a221e959fa2fc1`.

The Chapter 3 opening, modeling transition, dense variational algorithm page,
validation-design transition, component-removal section, interpretation text,
principal predictive-synthesis figure, paired cutoff panels, and chapter ending
were rasterized and inspected. Text, mathematics, tables, and figures were
legible with no clipping or collisions. The chapter contains 17 retained
labeled displays after implementing its six MERGE and three TEXT-SUMMARY
decisions. This validates integration and rendering; it does not constitute a
new forecast experiment, selected-model refit, or operational hindcast.

## 2026-09-16 Chapter 4 milestone validation

The Chapter 4 milestone passed the chapter validation tier against the retained
fixed-commit audit root. The final build is 343 US Letter pages and 18,913,562
bytes, with no undefined citation or reference, duplicate-label, missing-file,
or overfull-box diagnostic. Thirty-eight underfull-box notices, the known
caption-package warning, and two automatic `!h`-to-`!ht` adjustments remain.
PDF SHA-256: `910430f607f1f52f1c733c6e56ca3cf3df5d00ff61ac9c7466174a74dc848e32`.

The Chapter 4 opening; Q--DESN formulation; Gaussian baseline transition;
dense posterior, MCMC, VB--LD, and joint-quantile pages; simulation transition;
paired two-page forecast and fit-recovery figures; GloFAS table and paired
sensitivity figures; PriceFM regional figure; and chapter ending were
rasterized and inspected. Text, equations, tables, and figures were legible,
with no clipping or collisions. This validates dissertation integration and
rendering; it does not constitute a new simulation run, model fit, forecast
experiment, or computational reproduction.

## 2026-09-16 Chapter 5 milestone validation

The Chapter 5 milestone passed the chapter validation tier against the retained
fixed-commit audit root. The final build is 319 US Letter pages and 17,984,061
bytes, with no undefined citation or reference, duplicate-label, missing-file,
pdfTeX-destination, or overfull-box diagnostic. Thirty-eight underfull-box
notices, the known caption-package warning, and two automatic `!h`-to-`!ht`
adjustments remain. PDF SHA-256:
`78794d00fbd28bf43f791ed6d434ee8e13f225962f57ec22bb2951420571bc38`.

The Chapter 5 opening; quantile-window theorem and proof; MTI proposition and
global profiling proof; fractional empirical-balance section; fixed-target
generalized-Bayes computation; TCSP definition and proof-limit discussion;
validation protocol and principal table; pharmaceutical application table;
extension opening and corrected midpoint-loss sign; diagnostics; and final
discussion were rasterized and inspected. Text, equations, tables, and figures
were legible, with no clipping or collisions. This validates dissertation
integration and rendering. It does not supply the open action-matched TCSP
proof, rerun any simulation or application analysis, or establish an
implementation or empirical performance result for the proposed MTI
extensions.

## 2026-09-16 cross-chapter prose and typography validation

The Chapter 2--5 global pass removed preamble-wide small-type rules for tables
and algorithms and replaced Chapter 4's blanket equation compression with
case-specific layout. The API reference, four long Chapter 3 algorithms,
reservoir-design table, and tolerance-validation table retain locally justified
compact type. Wide equations were instead split across lines; only the DESN
state recursion retains a local `small` setting.

The chapter validation tier passed under Python 3.11 against the retained
fixed-commit audit root. It rechecked 102 immutable source blobs, 398 unique
labels, and all 118 cited keys. The final pdfLaTeX pass produced 323 US Letter
pages and 18,014,949 bytes, with no undefined citations or references,
duplicate labels, missing files, oversized floats, pdfTeX destination warnings,
or overfull boxes. Thirty-nine underfull-box notices, the known legacy-class
caption warning, and one automatic `!h`-to-`!ht` adjustment remain. PDF
SHA-256: `ac53dddd1bf1765a08be027cfa813c5dcccc627958556c0bb3ef237a4c68c5f9`.

Rendered pages for the Chapter 2 API table, Chapter 3 MCMC algorithm, Chapter 4
reservoir table and DESN recursion, finite-grid scoring equations, error-model
discussion, weighted augmented likelihood, and Chapter 5 tolerance-validation
table were inspected. Text, equations, and tables were legible with no visible
clipping or collisions. This validates document layout and integration; no
research computation or Overleaf build was performed.

## 2026-09-16 dissertation-framing validation

The Chapter 1, Chapter 6, and global-abstract pass completed the substantive
dissertation framing. The abstract contains approximately 319 words, within the
350-word indexing recommendation documented in `REQUIREMENTS-REPORT.md`. The
introduction defines the common target/update/evidence framework and the
synthesis compares all four projects without strengthening their mathematical
or empirical claims.

Fast and chapter validation passed under Python 3.11 against the retained
fixed-commit audit root. The final chapter-tier build produced a 345-page US
Letter PDF of 18,147,184 bytes with SHA-256
`a568e8fc4cc954adb08e16921e3eb9979b2bf8431542ce9c95c0af8caf37fffe`.
The log contains no undefined citation or reference, duplicate label, missing
file, oversized float, pdfTeX destination warning, or overfull box. Forty-one
underfull-box notices, the known legacy-class caption warning, and one automatic
`!h`-to-`!ht` adjustment remain.

The first build exposed one inherited Type 3 DejaVuSans font inside the PriceFM
regional-comparison source PDF. The source asset was preserved byte-for-byte;
a Ghostscript `pdfwrite` derivative converts only its plot lettering to vector
outlines. The source and derivative hashes and transformation are recorded in
`display-ledger.json`. An all-page `pdffonts` audit of the rebuilt dissertation
finds no Type 3 or Type 0 font, and all remaining reported fonts are embedded.
Rendered comparison confirmed that the plotted points, labels, legend, and
caption remain legible and visually unchanged.

The two abstract pages; Chapter 1 opening, interval-object table, contribution
boundary, and transition to Chapter 2; Chapter 6 opening, synthesis table,
principal findings, future-work section, concluding page, and transition to the
bibliography; and the font-safe PriceFM page were rasterized and inspected.
No clipping, collision, margin violation, or illegible display was observed.
The working title and approval metadata remain unresolved, the acknowledgments
remain an author task, and `\StarterDrafttrue` therefore remains active. This
validation does not establish coauthor or publisher reuse permission,
candidate-specific role allocation, committee approval, research-computation
reproduction, an Overleaf build, or filing readiness.

## 2026-09-16 final release validation

The release tier was run from an empty timestamped output directory with:

```text
bash scripts/validate.sh --tier release --audit-root /tmp/dissertation-audit-20260915.xusw2e
```

It rechecked all eight fixed source snapshots and 102 immutable source blobs,
the 29 editorial issues, 97 display decisions, 11 bibliography reconciliation
groups, four import manifests, 398 unique labels, and all 118 cited keys. The
exact accepted artifact is `build/release-20260916T081243Z/main.pdf`: 344 US
Letter pages, 18,146,885 bytes, SHA-256
`30b4e0bb3c3230544e941f7eae82dcabb44f08e9283ae9809aaade45196c9900`.
The release directory is ignored build output and the PDF is not committed.
Ordinary pdfTeX creation metadata means a later correct rebuild need not have
the same byte hash.

The final log has zero undefined citations, undefined references, multiply
defined labels, missing files, overfull boxes, fatal errors, or emergency
stops. It retains 41 underfull-box notices, the documented legacy-class caption
warning, and one automatic `!h`-to-`!ht` float adjustment. Those notices were
reviewed and do not identify clipped or missing content.

Independent PDF checks found 344 of 344 pages at 612 by 792 points, 33 font
records all embedded, no Type 3 or Type 0 font, no encryption, and no
JavaScript. A word-coordinate audit found zero body-text envelope violations
using 107.4--522.6 pt horizontally and 89--702.6 pt vertically. It found one
physically centered footer on every page except the unnumbered first two
leaves: centers range from 305.999 to 306.001 pt on a 612 pt page, and the
minimum footer-to-bottom clearance is 65.819 pt.

Physical chapter openings are pages 27, 39, 103, 148, 245, and 323; the
bibliography begins on page 334 and ends on page 344. The title/front-matter
sequence, first and last contents/list pages, both abstract pages,
acknowledgments, every chapter opening and ending, the bibliography opening,
and its final two pages were rasterized. Twenty-three pre-bibliography control
rasters were pixel-identical to the already inspected framing build. The final
bibliography opening and ending were then inspected directly. Text, equations,
tables, figures, headings, and page numbers are legible with no visible
clipping, collision, or stranded final reference line.

The inspection exposed a DOI stranded alone on a 345th page when bibliography
entries were separated by 12 pt. Reducing only `\bibsep` to 11.5 pt preserves
single-spaced entries and a visible near-baseline inter-entry separation while
placing the complete final entry on page 344. No bibliography content or
citation changed; the clean release build and all independent checks were
rerun after this adjustment.

This is a technically validated working dissertation, not a filing-ready
artifact. The title, committee/dean/date fields, acknowledgments, granular
contribution statements, publication/reuse clearances, and applicable AI-use
disclosure remain unresolved, so `\StarterDrafttrue` remains active. No
research computation was rerun, no research repository was modified, and no
Overleaf build or artifact was inspected during this release audit.

## 2026-10-08 reader-first restructuring release

The approved reader-first conversion was validated from a fresh timestamped
output directory with:

```text
bash scripts/validate.sh --tier release --audit-root /PATH/TO/IMMUTABLE/AUDIT-CLONES
```

The public record deliberately omits the machine-local audit path. Fresh
detached clones were checked out at the eight commits already fixed in
`source-manifest.json`; none of the original research working trees was fetched,
switched, reset, cleaned, built, or edited. The release gate passed 10 unit
tests and rechecked eight source records, 32 claim-evidence records, 29
editorial issues, 97 display decisions, 11 bibliography groups, four chapter
manifests, nine source documents, 96 section dispositions, and all 102
immutable imported Git blobs. It also resolved 48 active TeX files, including
one macro-expanded compiler input; found 421 unique active labels; verified all
14 body-to-appendix records and bridges; and covered all 33 active visuals in
the accessibility ledger.

The accepted local release candidate is ignored build output at
`build/release-20261008T063557Z/main.pdf`: 361 US Letter pages, 18,176,334
bytes, SHA-256
`80cee7e8e46f831029d6a810434b47fef742d1be95677e70830e6eca601d476c`.
Its final log has zero undefined citations or references, multiply defined
labels, unstable-label notices, missing files, overfull boxes, fatal errors, or
emergency stops. Forty underfull-box notices remain and were treated as
line-breaking diagnostics rather than failures. All 33 reported font rows are
embedded; no Type 3 or Type 0 font is present. The PDF is searchable, uses PDF
1.5, and is untagged.

The reading body ends on numbered page 203. Appendix A begins on 204,
Appendices B--E begin on 208, 222, 231, and 296, and the bibliography begins on
323 and ends on 333. Their corresponding physical PDF pages are 232, 236, 250,
259, 324, and 351--361. Chapter openings, the Chapter 6/Appendix A boundary,
all five appendix openings, and both bibliography endpoints were rasterized.
Direct visual inspection and word-coordinate checks found no clipping,
collision, stranded heading, or margin anomaly; inspected text bounds remained
inside the established manuscript envelope. The opening statements of
Chapters 3--5 were corrected during this review so that they accurately
describe which technical material is retained in Appendices C--E.

The fallback build now uses four pdfLaTeX passes around BibTeX on muscat's
legacy TeX Live 2018 installation, because the class writes list and
cross-reference state late. Release validation rejects a remaining
`Label(s) may have changed` warning. It also records TeX's `.fls` dependency
graph and regression-tests missing literal inputs, active duplicate labels,
inactive demonstration content, macro-expanded inputs, moved displays, and
absolute machine paths.

This release validates the structural reorganization and preservation of the
fixed-source evidence. It does not rerun research computation, establish
material-specific reuse permission, resolve candidate/coauthor role detail,
verify an Overleaf build, or establish filing readiness. Muscat's PDF is not
tagged and therefore is not claimed to satisfy WCAG 2.1 AA or PDF/UA. A modern
tagging-capable build, external accessibility checking, and manual review of
reading order, mathematics, tables, contrast, metadata, and alternative text
remain filing gates.

## 2026-10-28 final reader and statistical revision release

The advisor-directed reader and statistical revision was validated from a new
timestamped output directory with the release tier and the five immutable audit
clones used by the current import manifests. The machine-local audit path is
intentionally omitted from this public record. The gate passed 10 unit tests;
rechecked eight source records, 30 claim-evidence records, 29 prioritized
editorial issues, 102 display decisions, four import manifests, nine source
documents, 96 section dispositions, and all 102 imported Git blobs; verified
120 cited keys; and resolved 83 active TeX files, 482 active labels, six
migration records, and 47 active visual records.

The accepted ignored artifact is
`build/release-20261028T044714Z/main.pdf`: 414 US-Letter pages, 20,457,322
bytes, PDF 1.7, SHA-256
`49b0bc25f5c4b46c474379d3b7f33bfbfd01a3a28cb77660db63a4a8c5f0e409`.
The final log has zero undefined citations or references, unstable or multiply
defined labels, missing files, overfull boxes, pdfTeX warnings, fatal errors,
or emergency stops. It retains 26 underfull-box notices, two automatic
`!h`-to-`!ht` adjustments, and the documented legacy-class caption warning;
none indicates lost or clipped content. All 52 reported font rows are embedded
and no Type 3 font is present. The PDF remains untagged.

PDF-text inspection found none of the malformed appendix strings or internal
production terms targeted by this revision. The title page, contents, figure
and table lists, abstract, acknowledgments, all six chapter openings, all five
appendix openings, the corrected statistical passages, the Chapter 5
body-to-extension transition, and both bibliography endpoints were rasterized
and reviewed. The chapter openings are physical pages 25, 37, 84, 123, 151,
and 187; Appendices A--E open on physical pages 199, 203, 217, 226, and 337;
the bibliography occupies physical pages 403--414. The inspected headings,
text, equations, page numbers, and transitions are legible without visible
clipping, collision, or stranded content. Appendix displays remain numbered
and locally referenceable but are excluded from the global lists, reducing the
front matter from the prior 38 Roman-numbered pages to 24; the abstract now
begins on page xxii.

This release validates the thesis source and local muscat artifact, not filing
readiness. The title, committee/dean/date fields and acknowledgments remain
explicitly unresolved; material-specific reuse permission and granular
candidate/coauthor roles remain open; and no research computation or source
repository was changed. The untagged PDF still requires a modern accessible
build and external/manual accessibility review. A GitHub push does not itself
verify an Overleaf pull, compile, or rendered artifact, so that remains a
separate handoff.
