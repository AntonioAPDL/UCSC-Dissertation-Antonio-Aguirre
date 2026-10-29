# UCSC Statistical Science PhD: dissertation foundation audit

Research and implementation date: **15 September 2026**; administrative
evidence refreshed **28 October 2026**. Prepared for Toni, a Fall 2021 entrant
with a confirmed Fall 2026 degree application. The official long name is
**Jose Antonio Aguirre Perez de Leon** and the scholarly name is **Antonio de
Leon**. The approved reading committee, December 2026 title-page date, dean
wording, filing deadline, and defense date are now confirmed as recorded below.

## Executive decisions

The repository began as a self-contained writing foundation and now contains an integrative introduction, four substantive manuscript-derived research chapters, a synthesis, five scientific appendices, and a dissertation-wide bibliography. The abstract is drafted; acknowledgments, final administrative metadata, granular role statements, reuse clearances, and an accessibility-conformant filing artifact remain open. It is not ready for institutional filing.

The current and 2021 catalogs both describe a dissertation that **should** contain at least three chapters of journal-suitable work and require delivery of the completed dissertation to the reading committee at least one month before the defense. Neither statement requires three accepted articles. The committee-size language differs between those catalogs, so an entry-year assumption cannot settle the candidate's approved committee. [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/) [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/)

Use the July 2026 Graduate Division preparation PDF as the formatting baseline.
Graduate Division supplied that exact guide to the candidate on 2026-10-15,
together with the Fall 2026 deadline and signature/submission route. It
requires December 2026 on this title page and identifies Donald Smith as
Interim Vice Provost and Dean of Graduate Studies. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2026/07/Dissertation-guidelines-7.26.pdf) [L1](https://guides.library.ucsc.edu/etds/submitting-at-UCSC)

Use the pinned community `ucscthesis` class with small project-level corrections. Use native Overleaf GitHub synchronization. The initial report proposed creating the GitHub repository from a new Overleaf project; that repository now exists, so the current GitHub-first import/preservation route in `docs/WORKFLOW.md` supersedes that bootstrap step. Keep research repositories separate and import only reviewed, attributed assets at recorded commits.

A consequential scholarly issue: Barata's 2021 dissertation already develops exDQLM methods, associated computation and an R package. Any later chapter from the candidate's related repositories must identify the candidate's distinct contribution and preserve attribution. A repository name or recent commit cannot establish novelty. [E1](https://escholarship.org/uc/item/0bq4107v)

## 1. Authority, cohort and evidence limits

University formatting and deposit instructions govern the submitted document; the Statistics program governs its disciplinary expectations; advisors and the approved committee assess the work. Template source and deposited dissertations illustrate implementation and practice. They do not override those jurisdictions.

This audit uses six categories: university requirement, program requirement, official recommendation, observed practice, implementation choice, and unresolved. A program's use of “should” is retained as an expectation rather than rewritten as “must.” Each matrix row records its scope, source, implementation and check. No universal precedence rule or graduate catalog-rights rule was verified that resolves every conflict by date.

The formal program and degree field are **Statistical Science Ph.D.** The Fall
2021 entry-year catalog and current catalog both use that exact program name
and state that students obtain a Ph.D. in statistical science; the July 2026
guide lists Statistical Science among the permitted title-page disciplines.
The title page therefore correctly uses DOCTOR OF PHILOSOPHY in STATISTICAL
SCIENCE. “Statistics” is the department name, not the degree field, and the
older “Statistics and Applied Mathematics” field does not apply to this
candidate's entry-year program. [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/) [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/) [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2026/07/Dissertation-guidelines-7.26.pdf)

The 2021-2022 catalog describes an advisor or coadvisors plus at least two
additional readers, while the current catalog uses different coadvisor
language. The candidate-specific administrative record now controls this
question: Graduate Division approved the revised four-member committee and
updated AIS on 2026-10-09, with Raquel Prado first as chair, followed by Bruno
Sansó, Paul Parker, and Athanasios Kottas. [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/) [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/)

Candidate-specific Graduate Division instructions establish December 11, 2026
as the deadline to complete all requirements; require an unsigned ProQuest
copy and a separately emailed, single-page title page bearing the committee
signatures; require the Survey of Earned Doctorates and UCSC Exit Survey; and
identify Donald Smith's exact title. Defense correspondence establishes
November 30, 2026 at 10:00 a.m. Pacific. The planned November 6 delivery is
only 24 days before the defense, however, and no reviewed record expressly
waives the catalog's one-month delivery rule. Obtain a written program
determination. Searches still did not establish a UCSC dissertation-specific
generative-AI disclosure rule. [U1](https://graduate.ucsc.edu/) [U2](https://grad.engineering.ucsc.edu/advising/planning-to-graduate/) [U3](https://registrar.ucsc.edu/calendars-resources/academic-calendar/)

## 2. Formatting and deposit decisions

The full editable audit is `docs/compliance-matrix.md` and its companion JSON. This section explains decisions with the greatest consequences for implementation.

### Layout and type

The starter uses US Letter portrait pages. The guide requires at least 1.5 inches on the left and 1.25 inches on the other sides. The implementation uses 1.5 left, 1.25 right, 1.30 top and 1.35 bottom; the small vertical allowance keeps visible glyphs within the minimum margins. Letter size is consistent with the sample and audited templates; no explicit numerical paper-size clause was located in the guide text, so Letter and one-sided output are documented implementation choices. There is no added binding gutter. Ordinary even-numbered pages keep the same left margin. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The text uses 12-point Times-compatible Type 1 fonts. The guide requires embedding and specifies PostScript Type 1; the starter checks the fonts actually present in the compiled PDF. The body uses double spacing. Footnotes, captions, table cells and bibliography entries use documented exceptions without reducing their ordinary text below 12 points. A LaTeX factor alone is not proof of spacing: the validation record measures the actual body baseline distance. Paragraph indentation and chapter-scoped equation/theorem numbering are editorial choices. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

Page numbers are centred on the physical sheet, not on the asymmetrical text block, and remain above the minimum 0.75-inch edge clearance. Headers are empty. The title and second leaf are counted as i and ii without printed numbers; the contents begin at iii. Front matter uses lower-case Roman numbers, and the first main-text page starts at Arabic 1. The starter's PDF page labels and visible numbers are checked separately. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

Landscape content must retain a correctly oriented portrait-positioned page number. The special facing-caption arrangement for full-page illustrations has different margin handling and list-of-figures references. Neither special mode is implemented or validated in this small starter. Ordinary figures remain inside the text area with their captions; introducing the special cases triggers a focused implementation and review against guide p. 3. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

### Front matter and references

Order: integrated title/approval page; copyright or blank leaf; contents; figure/table lists when applicable; abstract; optional dedication/acknowledgments; text; endnotes if used; appendices; supplement list if applicable; final bibliography. The demonstration includes acknowledgment instructions because coauthored reuse is likely, and a blank second leaf. It adds no separate approval page that would shift the contents to iv. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The official title-page sample is the model for institution, degree and date
layout. The signed degree application confirms the university-record name and
Fall 2026 application; the current guide and candidate instructions therefore
fix the displayed date as December 2026. They also fix the dean block as Donald
Smith, with `Interim Vice Provost and Dean of Graduate Studies` beneath his
name. The ProQuest copy is unsigned; the separately emailed approval page must
carry all committee signatures on one page. The draft deliberately avoids an
approval assertion until that future approval. The author-selected title is
**Statistical Inference for Conditional Quantiles and Fixed-Content Intervals:
Models, Computation, and Applications**. It matches the dissertation abstract,
four research units, and statistically oriented scope; page one now has no
unresolved bibliographic field.
[G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2026/07/Dissertation-guidelines-7.26.pdf)

The abstract has its own heading, dissertation title and author, double spacing and Roman numbering. The guide does not impose a hard PDF abstract word limit; it recommends staying within 350 words for print indexing. A global dissertation abstract is necessary even when source articles have abstracts. Dedication is optional. Acknowledgments must accurately handle contributions and reuse when those provisions apply. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The bibliography is last, after appendices, and alphabetized by author. The guide directs the author to an appropriate professional style in consultation with advisors. No Statistics-specific mandated citation system was verified. The default is one dissertation-wide `references.bib`, BibTeX and `plainnat` author-year citations: a practical choice for consolidating papers, not a departmental mandate. Chapter bibliographies, if desired, require clarification of the required final bibliography and ordering. DOI/URL completeness and reference deduplication are editorial checks. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

### Submission, reuse and distribution

The Library describes submission through ProQuest and automatic forwarding to
eScholarship. The paid ProQuest open-access option, copyright registration
service and printed copies are optional; the ordinary route provides
eScholarship open access without those purchases. Copyright notice, ownership
and paid registration are different concepts. The author selected the standard
2026 copyright notice on page ii; this does not purchase or assert registration.
Initial embargo choices are six months, one year or two years, and must still
be reconciled with publisher agreements. [L1](https://guides.library.ucsc.edu/etds/submitting-at-UCSC)

The guide permits previously published/coauthored material subject to committee/department approval, suitable graduate research and an integrative account. Record the candidate's contribution, source article and applicable permissions. Advisor-only coauthorship is acknowledged; the guide contains additional permission provisions for other coauthors and copyright holders. Confirm the actual agreement and version rather than inferring permission from GitHub ownership or a software license. Reformat imported material into the dissertation's margins and continuous pagination. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The current Graduate Division notice states that electronic theses and dissertations must conform to WCAG 2.1 Level AA as of April 2026. The present muscat build is searchable and has embedded fonts, hyperlinks, and bookmarks, but it is untagged and is not claimed conformant. Current LaTeX guidance calls for a recent tagging-capable release, semantic structure, a description or artifact designation for each graphic, table headers, appropriate mathematics handling, and external plus manual validation. The project now maintains a complete reviewed visual-description ledger, but muscat's TeX Live 2018 cannot exercise the current tagging route. A modern candidate build must be tested without assuming that tagging alone establishes accessibility. Library archival-format recommendations for supplementary files do not by themselves establish a PDF/A requirement, and research data/code remain outside the thesis build. [U4](https://graduate.ucsc.edu/academics/applications-and-forms/) [O5](https://docs.overleaf.com/writing-and-editing/creating-accessible-pdfs) [T3](https://tagging-project.latex-project.org/documentation/usage-instructions) [L2](https://guides.library.ucsc.edu/etds/supplementaryfiles)

## 3. Scholarly criteria and a provisional architecture

The program's clearest public dissertation-specific criteria are journal-suitable chapter material, committee review and a public presentation followed by a private examination. The guide's conditions for reused material require a dissertation-level integration and a defensible account of the student's work. The public sources do not specify a required page count, three accepted publications, a fixed theorem count or a universal chapter rubric. [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/) [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/) [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

As editorial recommendations, each selected research chapter should establish a specific inferential target, a contribution beyond existing work, appropriate assumptions, sufficiently explained computation, evidence suited to the claim, and an honest assessment of limitations. Theory is needed where a claim relies on a guarantee; simulation cannot stand in for a proof. Conversely, a useful applied or computational contribution should not acquire an invented theorem to satisfy an imagined template.

A provisional common question is: **How can dynamic quantile and interval methods deliver interpretable uncertainty statements and useful forecasts under realistic computational constraints?** This is a planning hypothesis based on the supplied topics, not a summary of verified research findings.

| Architecture | Advantage | Main risk |
|---|---|---|
| Integrated monograph | Shared notation and arguments can be developed once, with a single continuous story. | Substantial rewriting and harder attribution if independent papers are blended too aggressively. |
| Research chapters with integrative framing | Preserves identifiable contributions and source provenance while connecting the papers. | Repeated background and overlapping results can make the dissertation look like a compilation. |

**Current provisional choice:** four project research chapters with a shared introduction and final synthesis. The author selected exdqlm, Environmetrics, QDESN, and combined MTI as the working project lines. Do not equate file slots with four proven independent contributions: the author/advisors should confirm chapter counting, especially the software-centered exdqlm unit, and should not split the two closely related MTI papers merely to increase the count.

Proposed contents: (1) Introduction and common framework; (2) exdqlm software and computation; (3) hydrologic correction and synthesis; (4) QDESN; (5) combined MTI foundation and extensions; (6) synthesis, limitations and future work; appendices; bibliography. The detailed source, prerequisite, new-exposition and overlap analysis is in `docs/chapter-plan.md`.

Place common definitions and literature in the introduction when assumptions truly match. Give each chapter a short local statement of its assumptions and contribution, with cross-references to shared material. Do not unify notation by silently changing conditioning sets, priors, scale parameterizations, quantile conventions or interval targets. Reuse a common dataset description with explicit chapter-specific splits, horizons and preprocessing. A repeated experiment is supporting evidence, not a second independent contribution. Keep proofs essential to the principal claim near that claim; move lengthy auxiliary derivations, implementation detail and robustness tables to appendices with precise pointers. No arbitrary page targets are imposed.

## 4. Deposited dissertation precedents

Three relevant documents were inspected through their deposited PDF text, including front matter, contents and selected chapter openings. This was an organizational review, not a full scientific review or visual compliance certification. Barata is an especially relevant earlier program-name precedent; Zhao and Trubey use Statistical Science. More recent Tang/Horton leads could not be reliably opened and are not counted as inspected.

| Verified dissertation | Organization and front matter | Reuse and lesson |
|---|---|---|
| Raquel A. Barata, *Flexible Dynamic Quantile Linear Models*, December 2021; Statistics and Applied Mathematics. [E1](https://escholarship.org/uc/item/0bq4107v) | Introduction, four substantive chapters spanning inference, application, software and multivariate models, then conclusion. Contents iii; abstract xviii; acknowledgments xxi. Prado and Sansó are co-chairs with two additional readers. | Acknowledgments explicitly connect chapters 2-3 to one article and chapter 4 to a package vignette. Paper count and chapter count differ in this example; it does not establish general permission to split work. |
| Chunyi Zhao, *Bayesian Nonparametric Modeling for Spatial Nonhomogeneous and Clustered Point Pattern Data*, September 2022; Statistical Science. [E2](https://escholarship.org/uc/item/5800b879) | Introduction, spatial Poisson, spatial Hawkes and space-time Hawkes chapters, then conclusion. Contents iii; abstract ix; dedication xi; acknowledgments xii. | Chapter openings explain how later models build on a shared intensity construction. This is useful cross-chapter integration. A specific article-reuse permission or statement was not established from the examined passages. |
| Peter Trubey, *Exploring Multivariate Extreme Value Theory with Applications to Anomaly Detection*, March 2025; Statistical Science. [E3](https://escholarship.org/uc/item/6c80077v) | Introduction, three substantive chapters on multivariate peaks-over-threshold inference, anomaly detection and storm surge, then conclusion. Contents iii; abstract vii. | Related chapters share a modeling foundation. No blanket article-reuse permission is inferred. The deposited order places references before an appendix; the starter follows the guide's explicit bibliography-last order instead. |

Barata is prior scholarship that the later audit must compare directly against exDQLM/exAL and joint-quantile materials. The candidate may have substantial subsequent contributions, but they must be established from source versions and contribution records. The 2021 dissertation's existing results cannot be attributed to the candidate by association. [E1](https://escholarship.org/uc/item/0bq4107v)

## 5. Template audit and implementation decision

No current official endorsement of either community repository was established. The audit read actual source, not just gallery descriptions. An Overleaf-hosted copy is not a separate compliance authority. The unavailable current Graduate Division site limits discovery of any newer officially linked template.

| Candidate and provenance | Audit findings | Decision |
|---|---|---|
| `adamnovak/ucscthesis`, pinned December 2020 snapshot; class March 2017; LPPL 1.3c+. [T1](https://github.com/adamnovak/ucscthesis/tree/38a711c243bd78f1ace969f4dacb15e9c52c39de) | Compact UCSC-specific front-matter machinery. Legacy spacing factor 1.37, hardcoded Chair suffix and older sample metadata need correction. Modern `setspace` needs a current-size hook with this legacy class. | Selected, with unchanged vendored class/size files and explicit project overrides. Locally tested, not advertised as actively updated or officially approved. |
| `GauSyu/thesisucsc`, pinned July 2023 snapshot; GPL-3.0; KOMA-Script. [T2](https://github.com/GauSyu/thesisucsc/tree/4a946f0693e38286129dc39842a458fb09fddcca) | Targets July 2021 guide; many split settings and useful modern packages. Two-sided inner/outer margins yield a smaller left margin on even pages. Title role/dean and PDF metadata need review; bibliography ordering depends on its chosen configuration. | Credible alternative, but would need several corrections and extra dependencies here. Source-reviewed only; no claim that its unmodified output was tested. |

The default keeps the class recognizable and changes the project layer: fixed ordinary-page margins; explicit double spacing; physically centred page numbers; 12-point captions/footnotes; unconfirmed title roles; a blank counted leaf; correct front-matter and bibliography order; portable notation and reference files. `TEMPLATE-NOTES.md` records provenance, license and changes. No source archive or online template is treated as submission approval.

The removable appendix exercises an equation, an elementary theorem/proof, a prose algorithm, a vector figure, a table, a footnote, citations, cross-references and appendix numbering. Its mathematical example is explicitly not the candidate's research. The central source tree is small and can compile without any article repository or network access. `docs/VALIDATION.md` records actual local tests and distinguishes them from the unperformed Overleaf compile.

## 6. Workflow and repository readiness

The live UCSC Overleaf portal offers institutional premium access to faculty, staff and students; eligibility activation on the candidate's own account was not tested. Follow the portal's UCSC sign-in/account-linking flow. An old announcement with a 2023 subscription end date is not used to assert current expiry. [O1](https://www.overleaf.com/edu/ucsantacruz)

Native GitHub sync is a premium, manually initiated source-sync feature. Overleaf can create a new repository from a project or create a new project by importing a repository; independently created existing objects cannot simply be bound together. The linked default branch is the exchange point, while local branches and pull requests remain on GitHub. Submodules and LFS are unsupported, symlink and executable-bit behavior is unsuitable for build dependencies, and review comments/tracked changes need care before source pulls. The detailed preservation and conflict procedure is in `docs/WORKFLOW.md`. [O2](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization) [O3](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration)

Only public repository metadata and default-branch heads were checked in this assignment. These observations do not approve a manuscript version, establish licensing, or constitute a scientific audit. The source manifest keeps observed heads separate from author-approved commits.

| Candidate repository | Discovery result on 2026-09-15 | Consequence |
|---|---|---|
| `AntonioAPDL/Article-Q-DESN---Version-2` | Public; default branch `main`; observed head `757522db0f85815244370ec92a194de132268883`. | Manuscript path, intended version and chapter suitability unverified. |
| `AntonioAPDL/exdqlm---Article` | Public; default branch `main`; observed head `d5534e97db8414fd875022261d4c530eae4676e4`. | Distinguish new candidate contributions from earlier exDQLM work. |
| `AntonioAPDL/RQR-GIBBS` | Public; default branch `main`; observed head `73887b9c86ef767aa1567c660718667945630aef`. | Audit actual targets, updating rule and outputs before describing the method. |
| `AntonioAPDL/itpu-interval-regression` | Unauthenticated GitHub API returned 404. | Could be private, renamed or unavailable; absence is not established. Obtain an authorized local path or corrected identity. |

Open the dissertation as the active Codex working project on muscat and verify the shell host and directory. A GitHub URL or an extra VS Code folder does not automatically grant the agent access or supply repository contents. Record the active project and effective permissions, then perform a read-only check of each explicitly authorized source location. Writable roots expand write access; do not add all source repositories merely to enable reading. If the configured environment blocks reading, use supported narrowly scoped read access or author-provided snapshots and state the resulting coverage limit. `AGENTS.md` is behavioral guidance, not a filesystem access control. Remote-SSH, local IDE and cloud environments have different accessible files. [C1](https://learn.chatgpt.com/docs/codex/ide) [C2](https://learn.chatgpt.com/docs/agent-configuration/agents-md) [C3](https://learn.chatgpt.com/docs/sandboxing) [C4](https://learn.chatgpt.com/docs/agent-approvals-security) [V1](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces)

## 7. Completion plan and decisions

The defense is confirmed for November 30, 2026 and Graduate Division's
completion deadline is December 11, 2026. The catalog states that the completed
dissertation must reach the reading committee at least one month before the
defense. The correspondence instead records a planned November 6 delivery, a
24-day interval. Do not treat the committee's scheduling agreement as an
implicit waiver; obtain a written program determination and, if necessary,
move delivery earlier or adjust the defense. [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/) [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/)

| When / priority | Action and responsible party | Evidence or output |
|---|---|---|
| Now | Preserve the confirmed title, Statistical Science degree field, official name, December 2026 date, committee, and dean block through final approval. | Approved title page compared with the validated draft metadata. |
| Immediate | Candidate obtains a written program determination on the November 6 delivery / November 30 defense interval. | Confirmation of compliance, earlier delivery, or revised defense date. |
| Before substantive drafting | Candidate runs the Codex source audit and decides the chapter plan with advisors. | Contribution inventory, source-to-chapter map and resolved overlap questions. |
| Planning buffer: roughly D minus 8-10 weeks | Send advisors a coherent full draft and settle major gaps. This is an editorial buffer, not a UCSC deadline. | Reviewed dissertation-level argument and revision plan. |
| At the program-confirmed compliant date | Deliver the completed dissertation to the reading committee. | Dated delivery record and complete version. |
| Before November 30 | Confirm venue, public announcement, and defense logistics with Statistics/Baskin. | Published announcement, venue/link, and required forms. |
| November 30 and afterward | Public presentation, private examination, requested revisions, and signatures. | Committee-approved final version and one-page signed title page. |
| By December 11 | Submit through ProQuest, email the signed title page, complete both required surveys, address formatting corrections, and verify final acceptance. | Actual acceptance, not just an upload receipt. |

Unresolved decisions are intentionally narrow:

1. **Statistics program:** Confirm in writing whether the planned November 6
   delivery satisfies the one-month rule for the November 30 defense; otherwise
   establish an earlier delivery or revised defense date.
2. **Advisors/program:** Confirm that the four implemented project chapters are
   sufficiently distinct journal-suitable units and approve the detailed
   candidate-contribution statements.
3. **Candidate/coauthors/rights holders:** Complete the required acknowledgment
   of reused coauthored material, granular candidate contributions, applicable
   permissions, and any embargo decision. Public GitHub access is insufficient
   evidence of permission. [L1](https://guides.library.ucsc.edu/etds/submitting-at-UCSC)
4. **Advisors/program and appropriate research policy office:** Determine any
   current disclosure required for AI-assisted writing and editing. Keep the
   assistance log meanwhile; do not invent an institutional statement.

No messages were sent, remote repositories created, Overleaf projects linked, or research repositories edited. The delivered package completes the requirements-and-scaffold stage; substantive drafting begins only after the concrete source audit and chapter decision described in `docs/CODEX-KICKOFF.md`.

## 8. Source register and reproducibility

The original sources were accessed or attempted on 2026-09-15; G1 and the
candidate-specific administrative evidence were refreshed on 2026-10-28.
Dates describe the document, not the crawler. Complete public structured
metadata is in `docs/source-register.json`; private messages and forms are not
stored in this repository.

**G1 - [Dissertation and Thesis Preparation Guidelines](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2026/07/Dissertation-guidelines-7.26.pdf).** UCSC Division of Graduate Studies. July 2026. Locator: All 12 PDF pages, including title-page sample on p. 11. Full current PDF read; Graduate Division supplied the same URL to the candidate on 2026-10-15.

**P1 - [Statistical Science Ph.D., current General Catalog](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/).** UCSC Statistics / General Catalog. 2026-2027 catalog at access. Locator: Dissertation; Dissertation Reading Committee; Applying for Graduation. Full program text read.

**P2 - [Statistical Science Ph.D., 2021-2022 General Catalog](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/).** UCSC Statistics / General Catalog. 2021-2022. Locator: Dissertation; Dissertation Reading Committee. Full program text read; cohort applicability unresolved.

**L1 - [Electronic Theses and Dissertations: Submitting at UCSC](https://guides.library.ucsc.edu/etds/submitting-at-UCSC).** UCSC University Library. No revision date established. Locator: Formatting; submission; fees; copyright; embargoes. Full page read; also reached through /etds.

**L2 - [Electronic Theses and Dissertations: Supplementary Files](https://guides.library.ucsc.edu/etds/supplementaryfiles).** UCSC University Library. No revision date established. Locator: File descriptions and recommended archival formats. Full page read.

**E1 - [Flexible Dynamic Quantile Linear Models, Raquel A. Barata](https://escholarship.org/uc/item/0bq4107v).** UCSC / eScholarship. December 2021. Locator: Title; contents iii-v; acknowledgments xxi-xxii; chapter openings, especially ch. 4 p. 57. Deposited PDF text inspected; Statistics and Applied Mathematics.

**E2 - [Bayesian Nonparametric Modeling for Spatial Nonhomogeneous and Clustered Point Pattern Data, Chunyi Zhao](https://escholarship.org/uc/item/5800b879).** UCSC / eScholarship. September 2022. Locator: Title; contents iii-iv; introduction pp. 6-10; ch. 2 opening p. 11; ch. 4 pp. 104 and 120. Deposited PDF text inspected; Statistical Science.

**E3 - [Exploring Multivariate Extreme Value Theory with Applications to Anomaly Detection, Peter Trubey](https://escholarship.org/uc/item/6c80077v).** UCSC / eScholarship. March 2025. Locator: Title; contents iii-iv; introduction and chapter 4 opening. Deposited PDF text inspected; Statistical Science; repository cover sheet excluded from thesis numbering.

**T1 - [ucscthesis](https://github.com/adamnovak/ucscthesis/tree/38a711c243bd78f1ace969f4dacb15e9c52c39de).** Adam Novak and upstream contributors. Snapshot 38a711c243bd78f1ace969f4dacb15e9c52c39de; 2020-12-05; class 2017-03-29. Locator: Class, size files, example and license. Source downloaded and audited; local build of adapted starter tested separately.

**T2 - [thesisucsc](https://github.com/GauSyu/thesisucsc/tree/4a946f0693e38286129dc39842a458fb09fddcca).** GauSyu and upstream contributors. Snapshot 4a946f0693e38286129dc39842a458fb09fddcca; 2023-07-09. Locator: README; layout, font, title, metadata, bibliography settings; license. Source downloaded and audited; original project not compiled.

**O1 - [University of California, Santa Cruz on Overleaf](https://www.overleaf.com/edu/ucsantacruz).** Overleaf institutional portal. Live page; no expiry established. Locator: Institutional access and account linking. Page read.

**O2 - [GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization).** Overleaf Documentation. Live documentation; revision not established. Locator: Linking; import/export; branch behavior; limitations; conflicts. Page read.

**O3 - [Git integration](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration).** Overleaf Documentation. Live documentation; revision not established. Locator: Premium prerequisite; direct Git access. Page read.

**O4 - [Plan limits](https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits).** Overleaf Documentation. Live documentation; revision not established. Locator: File counts, text limits, upload and compile limits. Page read.

**C1 - [Codex IDE extension](https://learn.chatgpt.com/docs/codex/ide).** OpenAI. Live documentation; revision not established. Locator: Local IDE workflow. Official developers.openai.com/codex/ide/ redirected here.

**C2 - [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).** OpenAI. Live documentation; revision not established. Locator: Discovery, scope and precedence of project instructions. Page read.

**C3 - [Sandbox](https://learn.chatgpt.com/docs/sandboxing).** OpenAI. Live documentation; revision not established. Locator: Sandbox modes; IDE permissions; writable roots. Official /codex/sandboxing redirected here.

**C4 - [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security).** OpenAI. Live documentation; revision not established. Locator: OS sandbox; read-only; workspace boundaries. Official /codex/agent-approvals-security redirected here.

**C5 - [Config Basics](https://learn.chatgpt.com/docs/config-file/config-basic).** OpenAI. Live documentation; revision not established. Locator: User and project configuration; IDE settings access. Page read.

**V1 - [Multi-root Workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces).** Microsoft Visual Studio Code. Live documentation; revision not established. Locator: Adding folders and workspace files. Page read.

**H1 - [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).** GitHub Docs. Live documentation; revision not established. Locator: Clone instructions. Page read.

**H2 - [Resolving a merge conflict using the command line](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line).** GitHub Docs. Live documentation; revision not established. Locator: Review, resolve and commit conflicts. Page read.

**U1 - [Graduate Division website](https://graduate.ucsc.edu/).** UCSC Graduate Division. Current content not retrieved. Locator: Current forms, signatures, dean and deadlines. Access attempts failed; no current procedural claims inferred.

**U2 - [Planning to Graduate](https://grad.engineering.ucsc.edu/advising/planning-to-graduate/).** Baskin Engineering Graduate Advising. Current content not retrieved. Locator: Local completion and announcement instructions. Access attempts failed.

**U3 - [Academic Calendar](https://registrar.ucsc.edu/calendars-resources/academic-calendar/).** UCSC Registrar. Current content not retrieved. Locator: Fall 2026 graduation and filing dates. Catalog-linked page could not be retrieved; dates unverified.

Repository discovery endpoints: [GitHub Article-Q-DESN---Version-2](https://api.github.com/repos/AntonioAPDL/Article-Q-DESN---Version-2), [GitHub exdqlm---Article](https://api.github.com/repos/AntonioAPDL/exdqlm---Article), [GitHub RQR-GIBBS](https://api.github.com/repos/AntonioAPDL/RQR-GIBBS), [GitHub itpu-interval-regression](https://api.github.com/repos/AntonioAPDL/itpu-interval-regression). Branch-head observations were obtained from the corresponding `/commits/main` endpoints for the three accessible repositories.
