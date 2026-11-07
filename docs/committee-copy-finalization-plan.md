# Final committee-copy preparation plan and implementation record

**Baseline:** `ba9fadb96d73783846189395b571d3032e26901a`

**Branch:** `editorial/committee-copy-finalization-20261106`

**Purpose:** prepare a fixed, reader-facing dissertation PDF for circulation to
the Dissertation Reading Committee. This pass does not create signatures,
assert committee approval, settle unverified copyright permissions, or replace
the later accessibility and ProQuest filing review.

## 1. Baseline diagnosis

The accepted baseline is a clean 227-page US-Letter PDF with 26 numbered
appendix pages. All repository tests and structure checks pass; citations,
references, labels, fonts, page geometry, and the selected rendered pages have
already been checked. The remaining issues are concentrated in attribution and
front-matter usability rather than scientific restructuring.

The baseline audit found the following concrete issues:

1. Chapters 2 and 3 render Bruno Sansó's name as `Sans'o` because two source
   strings omit the LaTeX accent command.
2. Editable bibliography records for the candidate's work render `Antonio De
   Leon`, although the author-selected scholarly form is `Antonio de Leon`.
3. Chapter-opening notices name collaborators but do not identify the related
   manuscript titles or public dissemination records.
4. The public record establishes that the candidate is first author on all
   four project lines, corresponding author on the hydrologic study, and a
   package author for `exdqlm`. It does not allocate theory, software,
   simulation, data, or writing tasks among the coauthors. Those roles must not
   be invented.
5. The abstract contains approximately 408 words. UCSC imposes no manuscript
   limit, but ProQuest may truncate doctoral abstracts after 350 words in its
   print index.
6. The List of Figures contains 23 entries over eight pages and the List of
   Tables contains 20 entries over five pages. Their roughly 2,800 words arise
   because most list entries reproduce complete analytical captions.
7. The title page, degree field, committee, date, copyright leaf, main chapter
   architecture, selective appendices, and final bibliography are already in
   the correct reader-facing order and do not need redesign.

## 2. Decisions and evidence boundaries

### 2.1 Contribution and prior-dissemination record

Add a front-matter acknowledgment devoted to scholarly attribution. It will:

- identify the manuscript or project associated with each research chapter;
- name every documented collaborator;
- record the candidate's documented first-author, corresponding-author, and
  package-author facts;
- describe scientific contributions as joint where the source records do not
  allocate individual tasks;
- distinguish inherited exAL/exDQLM, echo-state-network, residual-product, and
  tolerance-method foundations through the existing citations and Chapter 1
  contribution map; and
- state no permission, acceptance, or personal-role claim beyond the evidence.

Personal acknowledgments are optional and will not be invented. Granular
individual contribution allocation and material-specific reuse clearance
remain filing-stage confirmation items unless the author supplies them.

### 2.2 Chapter notices and bibliography

Replace each generic chapter notice with a concise chapter-specific notice
that identifies the related public preprint or working manuscript. Add missing
bibliographic records for the Q--DESN working manuscript and the two MTI
preprints, while retaining current arXiv identifiers and avoiding unsupported
journal-acceptance claims. Normalize the candidate's editable author name to
`Antonio de Leon`.

### 2.3 Abstract

Reduce the abstract to at most 350 words without removing any of the four
contributions, changing numerical results, broadening claims, or erasing the
distinctions among likelihood-based Bayes, generalized updating, predictive
synthesis, and tolerance calibration.

### 2.4 Lists of figures and tables

Give every main-text figure and table a concise optional caption for the
global lists while preserving the complete body caption. Appendix entries are
already intentionally excluded from the global lists. This change should
reduce front-matter navigation substantially without changing any figure,
table, number, label, or scientific qualification.

## 3. Implementation sequence

1. Freeze and record baseline Git and PDF evidence.
2. Correct collaborator and scholarly-name typography.
3. Add and activate the scholarly acknowledgment.
4. Add complete prior-dissemination records and update chapter notices.
5. Compress the abstract to the ProQuest indexing recommendation.
6. Add concise list captions to all 43 main-text displays.
7. Run bibliography, manuscript-import, essentiality, structure, and unit-test
   validation before building.
8. Build in a fresh timestamped directory and inspect the log, page count,
   fonts, PDF properties, front-matter pagination, and extracted text.
9. Render and inspect the title page, contents, shortened lists, abstract,
   acknowledgment, all four research-chapter openings, synthesis ending,
   appendix transition, bibliography opening, and final page.
10. Review the complete diff, create focused commits, fast-forward `main`, push
    without force, and verify local, tracking, and directly queried remote
    branch tips with zero divergence.

## 4. Acceptance criteria

- No unverified individual contribution or permission statement appears.
- All collaborator names and the candidate's scholarly name are consistent.
- Every research chapter has a precise attribution/prior-dissemination notice.
- The abstract is no longer than 350 words and retains all four contribution
  summaries and their central limitations.
- The figure and table lists use concise entries while body captions remain
  unchanged.
- No undefined citation/reference, duplicate label, overfull box, fatal TeX
  error, missing file, or Type 3/unembedded font is introduced.
- The committee PDF is searchable, unencrypted, US Letter, and visually clean.
- The repository is clean, `main` is synchronized, and the accepted artifact
  and validation limitations are recorded.

## 5. Explicit non-goals

- Do not add signatures or claim dissertation approval.
- Do not add personal thanks without author text.
- Do not infer coauthor permissions or publisher rights.
- Do not rerun research simulations or alter numerical findings.
- Do not add a vita, keyword page, code, data, or supplementary archive.
- Do not claim the committee PDF is the tagged WCAG-conformant filing PDF.

## 6. Implementation and validation record

The six approved actions were completed on
\`editorial/committee-copy-finalization-20261106\`.

1. The existing contribution map was checked against the four manuscript
   records, bibliography, package metadata, and recorded source snapshots.
   The available evidence supports first authorship on all four project lines,
   corresponding authorship on the hydrologic manuscript, and package
   authorship for \`exdqlm\`; it does not support an individual theory/code/data/
   writing allocation. The acknowledgment therefore records project-level
   contributions and states that evidence boundary.
2. The candidate's editable scholarly name is consistently \`Antonio de Leon\`.
   The two malformed collaborator accents in chapter notices were corrected to
   Bruno Sansó.
3. Each research chapter now identifies its associated manuscript, coauthors,
   and dissemination record. The acknowledgment distinguishes inherited
   methods from the jointly authored chapter contributions without asserting
   acceptance, permission, or publication status beyond the cited record.
4. The abstract is 333 words and retains all four contributions, the principal
   empirical findings, and the main inferential qualifications.
5. All 43 main-text displays have concise optional list captions. Full body
   captions, display numbers, labels, values, and appendix-list policy are
   unchanged. The List of Figures and List of Tables now occupy two pages each,
   compared with eight and five pages in the baseline.
6. The release gate rechecked 108 immutable source blobs and produced
   \`build/release-20261107T062045Z/main.pdf\`: 221 US-Letter pages, 15,695,810
   bytes, PDF 1.7, SHA-256
   \`941825216957c896f0c15b1dfebeb1432fde83c69ba1ed657a09af20187a7fb2\`.
   All 19 tests and all repository validators passed; 119 citation keys
   resolved; the final log has 26 underfull notices, no overfull boxes, and no
   blocking diagnostics; all 24 font rows are embedded and no Type 3 font
   occurs. The front matter, research-chapter openings, synthesis, appendix
   transition, and bibliography endpoints were rendered and inspected.

The remaining gates are external to this implementation: the author should
pull and compile the exact revision in Overleaf, the committee must review and
approve the dissertation, material-specific reuse permissions must be settled
where applicable, and the filing PDF must complete the university's
accessibility process.
