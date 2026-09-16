# UCSC Statistical Science PhD: dissertation foundation audit

Research and implementation date: **15 September 2026**. Prepared for Toni, a Fall 2021 entrant planning around Fall 2026 completion. The author later supplied the official long name, **Jose Antonio Aguirre Perez de Leon**, and scholarly name, **Antonio de Leon**. Conferral quarter, defense date and committee appointments remain unconfirmed.

## Executive decisions

The delivered starter was a self-contained writing foundation with three provisional research chapters, an integrative introduction, a synthesis, and a removable formatting appendix. The research audit and author direction have since expanded it to four empty project-chapter placeholders. It contains no invented abstract, results, contributions, acknowledgments or approval. It is not ready for institutional filing.

The current and 2021 catalogs both describe a dissertation that **should** contain at least three chapters of journal-suitable work and require delivery of the completed dissertation to the reading committee at least one month before the defense. Neither statement requires three accepted articles. The committee-size language differs between those catalogs, so an entry-year assumption cannot settle the candidate's approved committee. [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/) [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/)

Use the current Library-linked preparation PDF as the documented formatting baseline. Its own revision is July 2021; its CDN folder says 2024, and search snippets can display more recent dates. Those are not evidence of a revised rule. Current Graduate Division forms, deadlines, dean and signature routing could not all be retrieved. Those unresolved procedural items are separated from the implemented layout. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf) [L1](https://guides.library.ucsc.edu/etds/submitting-at-UCSC)

Use the pinned community `ucscthesis` class with small project-level corrections. Use native Overleaf GitHub synchronization. The initial report proposed creating the GitHub repository from a new Overleaf project; that repository now exists, so the current GitHub-first import/preservation route in `docs/WORKFLOW.md` supersedes that bootstrap step. Keep research repositories separate and import only reviewed, attributed assets at recorded commits.

A consequential scholarly issue: Barata's 2021 dissertation already develops exDQLM methods, associated computation and an R package. Any later chapter from the candidate's related repositories must identify the candidate's distinct contribution and preserve attribution. A repository name or recent commit cannot establish novelty. [E1](https://escholarship.org/uc/item/0bq4107v)

## 1. Authority, cohort and evidence limits

University formatting and deposit instructions govern the submitted document; the Statistics program governs its disciplinary expectations; advisors and the approved committee assess the work. Template source and deposited dissertations illustrate implementation and practice. They do not override those jurisdictions.

This audit uses six categories: university requirement, program requirement, official recommendation, observed practice, implementation choice, and unresolved. A program's use of “should” is retained as an expectation rather than rewritten as “must.” Each matrix row records its scope, source, implementation and check. No universal precedence rule or graduate catalog-rights rule was verified that resolves every conflict by date.

The formal catalog program is **Statistical Science Ph.D.** The guide lists **Statistical Science** among degree fields. The title page therefore uses DOCTOR OF PHILOSOPHY in STATISTICAL SCIENCE, subject to checking the actual student record. “Statistics” is the department name; the older “Statistics and Applied Mathematics” appearing in historical dissertations is not copied into this candidate's metadata. [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/) [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/) [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The 2021-2022 catalog describes an advisor or coadvisors plus at least two additional readers, explicitly yielding at least four committee members with two coadvisors. The current catalog permits two graduate-faculty coadvisors plus at least one additional graduate-faculty reader. Conditions differ for an external coadvisor. Both require the prescribed approvals. These are differences in policy text, not evidence that the candidate's committee must now be changed. Obtain the existing approved reading-committee record and a program/Graduate Division determination of the applicable rule. Four illustrative metadata slots make no appointment or approval. [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/) [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/)

The complete current Graduate Division checklist and Baskin planning page were inaccessible during repeated retrieval attempts. The Registrar's catalog-linked calendar was also unavailable. No Fall 2026 deadline, defense-announcement lead time, current dean name, or current signature route is asserted. Searches did not establish a UCSC dissertation-specific generative-AI disclosure rule; that is an evidence gap, not a finding that no policy exists. No policy from another campus or an undergraduate catalog-rights policy is substituted. [U1](https://graduate.ucsc.edu/) [U2](https://grad.engineering.ucsc.edu/advising/planning-to-graduate/) [U3](https://registrar.ucsc.edu/calendars-resources/academic-calendar/)

## 2. Formatting and deposit decisions

The full editable audit is `docs/compliance-matrix.md` and its companion JSON. This section explains decisions with the greatest consequences for implementation.

### Layout and type

The starter uses US Letter portrait pages. The guide requires at least 1.5 inches on the left and 1.25 inches on the other sides. The implementation uses 1.5 left, 1.25 right, 1.30 top and 1.35 bottom; the small vertical allowance keeps visible glyphs within the minimum margins. Letter size is consistent with the sample and audited templates; no explicit numerical paper-size clause was located in the guide text, so Letter and one-sided output are documented implementation choices. There is no added binding gutter. Ordinary even-numbered pages keep the same left margin. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The text uses 12-point Times-compatible Type 1 fonts. The guide requires embedding and specifies PostScript Type 1; the starter checks the fonts actually present in the compiled PDF. The body uses double spacing. Footnotes, captions, table cells and bibliography entries use documented exceptions without reducing their ordinary text below 12 points. A LaTeX factor alone is not proof of spacing: the validation record measures the actual body baseline distance. Paragraph indentation and chapter-scoped equation/theorem numbering are editorial choices. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

Page numbers are centred on the physical sheet, not on the asymmetrical text block, and remain above the minimum 0.75-inch edge clearance. Headers are empty. The title and second leaf are counted as i and ii without printed numbers; the contents begin at iii. Front matter uses lower-case Roman numbers, and the first main-text page starts at Arabic 1. The starter's PDF page labels and visible numbers are checked separately. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

Landscape content must retain a correctly oriented portrait-positioned page number. The special facing-caption arrangement for full-page illustrations has different margin handling and list-of-figures references. Neither special mode is implemented or validated in this small starter. Ordinary figures remain inside the text area with their captions; introducing the special cases triggers a focused implementation and review against guide p. 3. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

### Front matter and references

Order: integrated title/approval page; copyright or blank leaf; contents; figure/table lists when applicable; abstract; optional dedication/acknowledgments; text; endnotes if used; appendices; supplement list if applicable; final bibliography. The demonstration includes acknowledgment instructions because coauthored reuse is likely, and a blank second leaf. It adds no separate approval page that would shift the contents to iv. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The official title-page sample is the model for institution, degree and conferral-date layout. The filed title page is unsigned; current collection of signatures must be confirmed separately. The starter deliberately replaces approval assertions with an unconfirmed block. For Fall conferral the guide prescribes December on the title page, regardless of the defense month; the quarter itself is not yet confirmed. The author supplied the long name “Jose Antonio Aguirre Perez de Leon”; its match to the final university record and any required diacritics should still be checked before filing. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The abstract has its own heading, dissertation title and author, double spacing and Roman numbering. The guide does not impose a hard PDF abstract word limit; it recommends staying within 350 words for print indexing. A global dissertation abstract is necessary even when source articles have abstracts. Dedication is optional. Acknowledgments must accurately handle contributions and reuse when those provisions apply. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The bibliography is last, after appendices, and alphabetized by author. The guide directs the author to an appropriate professional style in consultation with advisors. No Statistics-specific mandated citation system was verified. The default is one dissertation-wide `references.bib`, BibTeX and `plainnat` author-year citations: a practical choice for consolidating papers, not a departmental mandate. Chapter bibliographies, if desired, require clarification of the required final bibliography and ordering. DOI/URL completeness and reference deduplication are editorial checks. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

### Submission, reuse and distribution

The Library describes submission through ProQuest and automatic forwarding to eScholarship. The paid ProQuest open-access option, copyright registration service and printed copies are optional; the ordinary route provides eScholarship open access without those purchases. Copyright notice, ownership and paid registration are different concepts. A blank copyright leaf does not waive copyright. Initial embargo choices are six months, one year or two years; the Library describes an extension request through Graduate Division before expiry. Metadata remains public. Verify the current selection with the candidate and any publisher agreements. [L1](https://guides.library.ucsc.edu/etds/submitting-at-UCSC)

The guide permits previously published/coauthored material subject to committee/department approval, suitable graduate research and an integrative account. Record the candidate's contribution, source article and applicable permissions. Advisor-only coauthorship is acknowledged; the guide contains additional permission provisions for other coauthors and copyright holders. Confirm the actual agreement and version rather than inferring permission from GitHub ownership or a software license. Reformat imported material into the dissertation's margins and continuous pagination. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf)

The starter produces a searchable PDF with embedded fonts, hyperlinks and bookmarks. The guide establishes the PDF submission and font baseline; this investigation did not establish a UCSC mandate for PDF/A, PDF/UA, tagged PDF, a particular accessibility conformance level, encryption settings or a numerical PDF size limit. Searchability and bookmarks are sensible implementation choices. Library archival-format recommendations for supplementary files do not by themselves establish a dissertation PDF/A requirement. Supplementary research data and code need descriptions, appropriate formats and permissions; they do not belong in the Overleaf build simply because they support a chapter. [G1](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf) [L2](https://guides.library.ucsc.edu/etds/supplementaryfiles)

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

Let D be the unconfirmed defense date and F the confirmed final-acceptance deadline for the intended conferral term. **D minus one month is the catalog's completed-dissertation delivery requirement**, not merely a suggested outline review. Do not replace “one month” with a guessed fixed day count. Work backward from both D and F; a late defense can leave too little time for revisions even if the one-month rule is met. [P1](https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/statistics/statistical-science-phd/) [P2](https://catalog.ucsc.edu/en/2021-2022/general-catalog/academic-units/baskin-school-of-engineering/statistics/statistical-science-phd/)

| When / priority | Action and responsible party | Evidence or output |
|---|---|---|
| Now | Candidate and Statistics graduate coordinator confirm approved committee, degree record and applicable cohort rules. | Existing committee appointment plus documented determination; metadata updated. |
| Now | Candidate and Graduate Division obtain current guideline/checklist and Fall 2026 dates. | Verified application, initial filing, correction and final-acceptance deadlines; signature/dean instructions. |
| Before substantive drafting | Candidate runs the Codex source audit and decides the chapter plan with advisors. | Contribution inventory, source-to-chapter map and resolved overlap questions. |
| Planning buffer: roughly D minus 8-10 weeks | Send advisors a coherent full draft and settle major gaps. This is an editorial buffer, not a UCSC deadline. | Reviewed dissertation-level argument and revision plan. |
| No later than D minus one month | Deliver the completed dissertation to the reading committee. | Dated delivery record and complete version. |
| Before D, exact lead time unresolved | Arrange public announcement and defense logistics with Statistics/Baskin. | Approved date, venue, announcement and required forms. |
| D and afterward, before F | Public presentation, private examination, requested revisions, signatures and filing checks. | Committee-approved final version, administrative forms, current surveys/checklist. |
| Before applicable term deadlines | Apply for graduation; obtain any formatting precheck; submit to ProQuest; address corrections and verify final acceptance. | Actual acceptance, not just an upload receipt. |

Unresolved decisions are intentionally narrow:

1. **Statistics graduate director/coordinator and Graduate Division:** Which reading-committee rule governs this Fall 2021 entrant, and what is the currently approved committee with exact chair/cochair roles? The two catalogs differ.
2. **Advisors/program:** Do the three proposed research units count as sufficiently distinct journal-suitable chapters? May material from one paper be divided, and how should overlap and coauthored contributions be documented? No manuscript audit has yet answered this.
3. **Graduate Division, via the Library-listed `gss-group@ucsc.edu`:** Is the July 2021 Library-linked guide still the controlling preparation document? Supply the current checklist, title sample, dean wording, signature route and all Fall 2026 filing milestones. Inaccessible pages prevent reliable current answers.
4. **Candidate:** Confirm official full name, final title, intended conferral quarter, defense date, approved committee record and authoritative local manuscript versions. A Fall plan alone does not finalize title-page dates.
5. **Advisors/program and appropriate research policy office:** What current rules and disclosures apply to AI-assisted dissertation research, writing and editing? Keep an assistance log meanwhile; do not invent an institutional disclosure statement.
6. **Candidate/coauthors/Library research support:** Which articles and figures will be reused, what versions and rights apply, and is an embargo needed? The Library lists `research@library.ucsc.edu` for publication questions. Public GitHub access is insufficient evidence of these permissions. [L1](https://guides.library.ucsc.edu/etds/submitting-at-UCSC)

No messages were sent, remote repositories created, Overleaf projects linked, or research repositories edited. The delivered package completes the requirements-and-scaffold stage; substantive drafting begins only after the concrete source audit and chapter decision described in `docs/CODEX-KICKOFF.md`.

## 8. Source register and reproducibility

Every source below was accessed or attempted on 2026-09-15. Dates describe the document, not the crawler. Complete structured metadata is in `docs/source-register.json`. G1 was downloaded in full; policy pages and product documentation were read; the three dissertation examples were examined at the specified passages. Template commits are pinned. Repository checks were metadata-only. Unavailable sources are explicitly retained to show the evidence gap.

**G1 - [Dissertation and Thesis Preparation Guidelines](https://bpb-us-w2.wpmucdn.com/wordpress.ucsc.edu/dist/4/136/files/2024/09/dissertation-thesis-guidelines.pdf).** UCSC Division of Graduate Studies. July 2021 revision printed in PDF; Library currently links this copy. Locator: All 11 PDF pages, including title-page sample on p. 10. Full PDF downloaded and read; current linked copy, not proof that no newer rule exists.

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
