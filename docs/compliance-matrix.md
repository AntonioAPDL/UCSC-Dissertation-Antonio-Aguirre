# Compliance matrix

Audit date: 2026-09-15. JSON is the editable structured record. “Implemented”
is a source/layout status, not institutional or substantive approval. Every
source ID resolves to the exact URL below and to `source-register.json` for
issuer, revision, access date and locator. Two linked tables per group keep
the complete rule-to-check mapping readable.

## Program

| ID / topic | Rule and applicability | Authority | Source / locator |
|---|---|---|---|
| A01 Degree wording | PhD field is Statistical Science; confirm candidate record. | program requirement | [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/); Program title; G1 pp. 5-6 |
| A02 Committee/cohort | 2021 and current coadvisor committee-size clauses differ; use approved appointment and applicable ruling. | unresolved | [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/); Reading Committee; compare P1 same section |
| A03 Research chapters | At least three journal-suitable chapters is stated with should; accepted papers are not specified. | program requirement (stated expectation: should) | [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/); Dissertation; P2 same section |
| A04 Committee lead time | Completed dissertation must reach reading committee at least one month before defense. | program requirement | [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/); Dissertation; P2 same section |
| A05 Defense | Public presentation followed by private examination. Announcement lead time not verified. | program requirement / unresolved logistics | [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/); Dissertation |

| ID | Implementation | Verification | Status / issue |
|---|---|---|---|
| A01 | metadata.tex uses DOCTOR OF PHILOSOPHY / STATISTICAL SCIENCE | Compare MyUCSC and approved title page | Program verified; personal record unresolved |
| A02 | Four visible illustrative slots; no roles assumed | Program/Graduate Division confirmation | Open; no committee approved by this project |
| A03 | Three research placeholders plus integration chapters | Advisor/program assessment of independent contributions and counting | Text verified; chapter substance unverified |
| A04 | No LaTeX change; completion plan | Dated delivery of complete version relative to confirmed D | Rule verified; defense date unresolved |
| A05 | No LaTeX change | Program scheduling and current forms | Format verified; dates/announcement open |

## Page layout

| ID / topic | Rule and applicability | Authority | Source / locator |
|---|---|---|---|
| L01 Paper and sides | US Letter portrait, one-sided output chosen from sample/template practice; no numeric paper-size clause found. | implementation choice | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); Sample p. 10 |
| L02 Margins | Ordinary pages: left >=1.5 in; right/top/bottom >=1.25 in. | university requirement | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 2, Margins |
| L03 Number position | Page number >=0.75 in from edge and centred on sheet. | university requirement | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 2, Margins |
| L04 Headers | No special running-header format verified; empty headers chosen. | implementation choice | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 2 and sample |
| L05 Landscape | Sideways content retains portrait-oriented page number at normal position. | university requirement (conditional) | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 3, Charts and illustrations |
| L06 Full-page figures | Special facing-caption page reverses side margins and list entry points to figure page. | university requirement (conditional) | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 3, Charts and illustrations |

| ID | Implementation | Verification | Status / issue |
|---|---|---|---|
| L01 | letterpaper; oneside; fixed left/right geometry | PDF page boxes and rotations | Implemented; verify any newer instruction |
| L02 | geometry fixed margins; no additional gutter | Geometry log plus rendered text/float bounds on every page | Implemented; evaluated in VALIDATION.md |
| L03 | fancyhdr footer offset corrects asymmetrical text area | Measure number bounding box centre and lower clearance | Implemented; measured |
| L04 | Clear fancyhdr headers and rules | Visual all-page review | Implemented |
| L05 | No landscape mode used; add focused implementation if needed | Check rotated content and unrotated centred footer | Not applicable to starter; untested |
| L06 | Normal caption-with-figure floats only | Re-read special instructions and inspect both pages if introduced | Conditional mode not implemented |

## Typography

| ID / topic | Rule and applicability | Authority | Source / locator |
|---|---|---|---|
| T01 Fonts | Embedded PostScript Type 1; readable non-ornamental primary font with equivalent size >=12 pt Times or 10 pt Arial. | university requirement | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 2, Type size and style |
| T02 Body spacing | Double spacing; listed exceptions may be single-spaced. | university requirement | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 2, Spacing |
| T03 Spacing exceptions | Footnotes, indented quotations, multiline reference entries, captions/tables and specified appendices have exceptions. Do not assume all equations are exempt. | university requirement / permitted exceptions | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 2, Spacing; p. 8, Bibliography |
| T04 Paragraphs/headings | Indentation and heading hierarchy not prescribed in detail in reviewed guide. | implementation choice | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 2, general type/spacing |

| ID | Implementation | Verification | Status / issue |
|---|---|---|---|
| T01 | 12 pt mathptmx text/math, no deliberate shrinking of ordinary captions/notes | pdffonts; PDF text sizes; inspect every imported asset | Starter fonts tested; imports require repeat check |
| T02 | setspace doublespacing overrides legacy 1.37; current-size compatibility hook | Measure 12 pt body baseline in PDF and log, rather than checking command alone | Implemented; measured |
| T03 | Single-spaced notes/captions/table cells/bib entries; body math stays in body flow | Inspect affected page and compare exact exception when new material added | Demonstrated subset tested |
| T04 | 0.3 in indent; no paragraph gap; class headings | Visual consistency; check long imported headings | Implemented, not a claimed university rule |

## Front matter

| ID / topic | Rule and applicability | Authority | Source / locator |
|---|---|---|---|
| F01 Order | Title; copyright/blank; contents; lists; abstract; dedication/acknowledgments; text; conditional endnotes; appendices; conditional supplement list; bibliography. | university requirement | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 4, Order of required/optional sections |
| F02 Pagination | Title i and second leaf ii counted, numbers hidden; TOC starts iii; Roman front matter; Arabic 1 restarts main text and continues through end. | university requirement | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); pp. 2, 4, 6 |
| F03 Title/approval | Use required institution/degree wording and integrated approval sample; filed PDF unsigned. | university requirement | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 4 and sample p. 10 |
| F04 Name and dates | Full candidate name; title-page date follows conferral quarter: March/June/September/December. | university requirement | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); pp. 4-6 |
| F05 Dean and signatures | Current dean, title, signatory and routing must be verified; 2021 personnel/process may be stale. | unresolved | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 4 and sample p. 10; compare U1 |
| F06 Copyright leaf | Copyright notice optional; otherwise retain a blank counted second leaf. | university requirement / optional notice | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 6 |
| F07 Abstract | Global abstract with heading/title/name, double spacing and Roman numbering. No hard PDF word cap found; <=350 is indexing recommendation. | university requirement / official recommendation | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); pp. 6-7 |
| F08 Dedication/acknowledgments | Optional personal pages; reuse/contribution requirements can make acknowledgments necessary for reused material. | university requirement (conditional) / optional | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); pp. 3, 6-7 |
| F09 Contents and lists | TOC required; figure/table lists when applicable; consistent titles and page references. | university requirement (lists conditional) | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); pp. 4, 6 |

| ID | Implementation | Verification | Status / issue |
|---|---|---|---|
| F01 | Explicit main.tex sequence; unused optional sections absent | Compare PDF sequence and source root | Implemented |
| F02 | pagenumbering roman; empty first two; Arabic reset before chapter 1 | PDF labels, extracted footer numbers and visual review | Implemented; tested |
| F03 | Adapted integrated title block; starter does not assert approval | Current sample and confirmed committee comparison | Structure demonstrated; metadata/approval open |
| F04 | Central placeholders; planned Fall would use December only after confirmation | Student record and conferral term | Unresolved personal fields |
| F05 | Dean placeholders; no signature images | Graduate Division current instructions | Open; historical names deliberately not copied |
| F06 | Blank page ii, no printed number | PDF second page and numbering | Implemented; notice decision remains author choice |
| F07 | Class abstract environment with 319-word dissertation-level abstract | Word count, compiled layout and rendered-page review | Substantive draft implemented; final title remains unresolved |
| F08 | Acknowledgment instructions only; no dedication | Author content and rights/contribution review | No acknowledgments invented |
| F09 | Automatic TOC, LoF and LoT; double spacing | Resolve reruns and compare page references | Implemented and demonstrated |

## Mathematical content

| ID / topic | Rule and applicability | Authority | Source / locator |
|---|---|---|---|
| M01 Equations/theorems | Consistent readable mathematical layout; no specified theorem style or numbering system verified. | implementation choice | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); General margins/type rules, pp. 2-3 |
| M02 Algorithm | No mandated algorithm package/style identified. | implementation choice | Project choice; Editorial choice |
| M03 Tables/figures | Fit margins; numbers and captions; figures should remain legible. | university requirement / official recommendation | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 3 |
| M04 Appendices/supplements | Continue numbering; retain margins; supplement list when applicable; final bibliography follows. | university requirement (conditional sections) | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); pp. 4, 7-8 |

| ID | Implementation | Verification | Status / issue |
|---|---|---|---|
| M01 | AMS environments; chapter-scoped labels, one elementary proof | Compilation, labels and equation placement | Demonstration only; math verified as elementary identity |
| M02 | Numbered prose algorithm environment; no extra float dependency | Read algorithm and check numbering | Demonstration only |
| M03 | Normal floats, 12 pt captions/table text; vector TikZ demo | All bounds/labels/captions; inspect imported figures individually | Starter demonstrated; future assets untested |
| M04 | Appendix A before bibliography; no actual supplements | PDF ordering; cross-references; later supplement inventory | Demonstration appendix only |

## References

| ID / topic | Rule and applicability | Authority | Source / locator |
|---|---|---|---|
| R01 Bibliography | Alphabetize by author; bibliography last; professional style chosen with advisors. | university requirement / advisor choice | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 8 |
| R02 Reference spacing | Double spacing between entries; multiline entries may be single-spaced. | university requirement / permitted exception | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); pp. 2, 8 |
| R03 Chapter bibliographies | No Statistics-specific mandate verified; compatibility with required final bibliography needs confirmation. | unresolved | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 8; P1 Dissertation |
| R04 Bibliographic quality | Verify references, DOI/URLs and merged citation keys; do not invent records. | implementation choice | Project choice; Editorial practice |

| ID | Implementation | Verification | Status / issue |
|---|---|---|---|
| R01 | BibTeX plainnat; one references.bib; final bibliography | Check bbl/order, rendered entries and contents | Implemented; citation-system choice provisional |
| R02 | Single-spaced bibfont; 12 pt separation between entries | Inspect multi-line entries and separation | Implemented; demonstrated |
| R03 | Single dissertation-wide bibliography selected | Advisor decision if per-chapter references requested | Alternative not implemented |
| R04 | Shared database; later import/key map | Match important references to source publications | Two real institutional demonstration records; research references absent |

## Electronic submission

| ID / topic | Rule and applicability | Authority | Source / locator |
|---|---|---|---|
| E01 PDF and fonts | Deposit PDF; required font embedding/type rules apply to imported graphics as well. | university requirement | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); pp. 1-2, 8 |
| E02 Search/accessibility | Searchable text and bookmarks chosen; no UCSC PDF/A, tagging or numerical PDF-size mandate verified here. | implementation choice / unresolved current limits | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); Electronic filing sections; L2 archival recommendations |
| E03 Submission channel | ProQuest deposit then eScholarship distribution per Library. | university requirement | [L1](https://guides.library.ucsc.edu/etds/submitting-at-UCSC); Submitting at UCSC |
| E04 Fees and embargo | Paid services optional; initial embargo options 6/12/24 months, extension route described. | official recommendation / documented submission options | [L1](https://guides.library.ucsc.edu/etds/submitting-at-UCSC); Fees; embargoes; copyright |
| E05 Supplementary files | Describe supplementary files and favor suitable open archival formats. | official recommendation | [L2](https://guides.library.ucsc.edu/etds/supplementaryfiles); File naming, README and formats |

| ID | Implementation | Verification | Status / issue |
|---|---|---|---|
| E01 | pdfLaTeX output; font inventory | pdfinfo and pdffonts plus imported-asset checks | Local PDF generated; actual deposit untested |
| E02 | hyperref and PDF text; no PDF/A/tagging claim | Text extraction, outline/page-label check; current office confirmation | Search/bookmarks tested; conformance tagging not asserted |
| E03 | No submission automation | Current checklist and final acceptance confirmation | Workflow described only |
| E04 | Candidate decision outside LaTeX | Actual portal choices and rights agreements | Current Library page verified; no selection made |
| E05 | No data bundled; later separately curated files | File inventory, access/rights checks and descriptive README | Not applicable yet |

## Completion and reuse

| ID / topic | Rule and applicability | Authority | Source / locator |
|---|---|---|---|
| C01 Graduation/filing dates | Application, initial submission, correction and final acceptance are separate milestones; exact Fall 2026 dates unverified. | unresolved | [U3](https://registrar.ucsc.edu/calendars-resources/academic-calendar/); Current calendar inaccessible; G1 pp. 1, 8 |
| C02 Revisions/signatures/surveys | Obtain approvals and required submission materials; older guide describes surveys and signed title routing. Confirm current checklist. | university requirement / unresolved current procedure | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); pp. 4, 8; U1 |
| C03 Article/coauthor reuse | Department/committee approval, integrative account, candidate contribution and applicable coauthor/copyright permissions. | university requirement (conditional) | [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf); p. 3, Previously published material |
| C04 AI use/disclosure | No dissertation-specific UCSC rule established in accessible sources; confirm actual policy. | unresolved | [U1](https://graduate.ucsc.edu/); Current policy evidence unavailable |

| ID | Implementation | Verification | Status / issue |
|---|---|---|---|
| C01 | Relative completion plan; no guessed dates | Registrar/Graduate Division current calendar/checklist | Open |
| C02 | No signatures or forms generated | Graduate Division current forms; final accepted record | Open current procedure |
| C03 | Controlled imports; acknowledgments and manifest | Actual article/version, contribution records and agreements | No reuse authorized or performed |
| C04 | Assistance log only; no invented formal disclosure | Advisors/program and relevant current policy office | Open |
