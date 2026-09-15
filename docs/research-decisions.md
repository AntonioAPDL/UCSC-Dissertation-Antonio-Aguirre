# Research inclusion, contribution, rights, and architecture decisions

Status: **partially resolved by author direction; focused confirmations remain**
Prepared: 2026-09-15
Revised: 2026-09-15
Evidence: `research-audit.md`, `chapter-plan.md`, `claim-evidence.json`,
`../source-manifest.json`, and the fixed-snapshot source manuscripts

This record separates facts documented by the repositories, decisions supplied
by the author, provisional working choices, and matters that still require
author, coauthor, publisher, or committee confirmation. A source-documented
joint contribution is not silently converted into an individual contribution.

## G1 — working source snapshots

The author directed the dissertation plan to use the current documentation in
the four project lines rather than reconstructing the research from scratch.
The audited commits below are therefore the **working drafting snapshots**.
They remain replaceable if the author identifies a later submitted manuscript
or a different authoritative file. Approval of a snapshot does not approve all
branches, ignored outputs, or assets in that repository.

| Project/source | Working commit | Working manuscript | State | Final check still needed |
| --- | --- | --- | --- | --- |
| Environmetrics | `1272bfc10442a28add5a4c74ff641e9b9a8e9666` | `wileyNJD-APA.tex` | AUTHOR-DIRECTED WORKING SOURCE | Replace only if a later submission is intended |
| QDESN Version 2 | `757522db0f85815244370ec92a194de132268883` | `main.tex` plus two supplements | AUTHOR-DIRECTED WORKING SOURCE | Replace only if an unpromoted branch becomes authoritative |
| RQR-GIBBS | `73887b9c86ef767aa1567c660718667945630aef` | `main.tex` plus supplement | AUTHOR-DIRECTED WORKING SOURCE | Confirm any later submitted revision |
| MTI-EXTENSIONS | `f345d946aa5a81b94795838bec58d874a0fdd0c9` | `main.tex` plus supplement | AUTHOR-DIRECTED WORKING SOURCE | Implementation/evidence remain incomplete |
| exdqlm article | `d5534e97db8414fd875022261d4c530eae4676e4` | `exdqlm-jss.tex` | AUTHOR-DIRECTED WORKING SOURCE | Confirm exact submitted archive if located |

Associated decisions:

- QDESN Search Phase II remains outside the working chapter because its own
  promotion gates are unfinished. This is a source-evidence safeguard, not a
  rejection of later inclusion.
- RQR-GIBBS and MTI-EXTENSIONS form one MTI project chapter.
- Preserve the declared `exdqlm` version graph: Environmetrics uses 1.1.0; the
  software article and relevant QDESN comparator use 1.1.1; package `main`
  remains 1.1.2 support and is not substituted retroactively.

G1 is sufficiently resolved for source-packet preparation. Original-prose
drafting may begin only after the author opens G4 for a named unit. These
snapshots are not final submission freezes.

## G2 — identity

Author-supplied decisions:

- Official long dissertation name: **Jose Antonio Aguirre Perez de Leon**.
- Primary scholarly name: **Antonio de Leon**.
- Identity mapping: manuscript forms “Antonio De Leon” and package metadata
  using “Antonio Aguirre” refer to the same candidate. Use the primary
  scholarly name in new dissertation prose; preserve immutable source and
  bibliographic spellings where necessary for accurate citation.
- ORCID: **PENDING**.

## G2 — documented collaborators and project contributions

The following statements come directly from author lists, correspondence or
acknowledgment fields, package metadata, and manuscript contribution
paragraphs. “Project contribution” describes the jointly authored work unless
the source says otherwise.

| Project | Documented collaborators | Repository-documented project contribution | Candidate-specific evidence | Granular allocation state |
| --- | --- | --- | --- | --- |
| `exdqlm` | Raquel Barata, Raquel Prado, Bruno Sansó | Integrated R workflow: composable dynamic models; MCMC/VB interfaces; fitted-object methods; diagnostics/scoring/forecasting/synthesis; compiled utilities; static shrinkage; tests and reproducibility materials | Candidate is first author of the software article and an `aut` in package metadata; the author has resolved the package-name mismatch | PENDING confirmation of which APIs, algorithms, compiled paths, tests, examples, and article sections the candidate personally led |
| Environmetrics | Raquel Prado, Bruno Sansó | Source-aware quantile correction and synthesis; dynamic source discrepancies; LDVB adaptation; five-origin San Lorenzo evaluation; predictive synthesis and interpretation | Candidate is first and corresponding author; acknowledgment identifies the work as part of the candidate's dissertation | PENDING confirmation of individual conceptual, computational, empirical, and writing roles |
| QDESN | Raquel Prado, Bruno Sansó | Fixed-feature Bayesian QDESN; independent and joint quantile-grid variants; MCMC and model-specific VB; simulations; GloFAS and PriceFM applications | Candidate is first author; repository and manuscript are candidate-facing project records | PENDING confirmation of individual theory, software, experiment, and writing roles |
| MTI foundation/extensions | Raquel Prado, Bruno Sansó | MPI characterization and MTI family; TCSP empirical tolerance action; validation and pharmaceutical application; static regression, pseudo-AL/ECM computation, basis expansions, and dynamic endpoint states | Candidate is first author of both manuscripts; both are explicitly linked as companion works | PENDING confirmation of individual theorem, calibration, implementation, validation, and writing roles |

This evidence is enough to draft the scientific content with collective or
chapter-centered wording and explicit antecedent credit. Before finalizing a
candidate-contribution preface, acknowledgments, or any singular first-person
claim, the author should confirm or correct the following compact role record:

| Project | Conceptual lead | Theory lead | Software/computation lead | Empirical/data lead | Writing/revision lead | Confirmation/date |
| --- | --- | --- | --- | --- | --- | --- |
| `exdqlm` | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING |
| Environmetrics | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING |
| QDESN | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING |
| MTI foundation/extensions | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING |

Inherited and collaborator work that must remain visible:

- Yan and coauthors: exAL distribution/static exAL foundations;
- Barata and coauthors: exDQLM state-space formulation, original MCMC/ISVB, and
  transfer-function foundations;
- Prado and Sansó: coauthors on all four project lines and candidate advisors;
- Barata: `exdqlm` package creator/maintainer and article coauthor; and
- named ESN/DESN, generalized-Bayes, residual-product, and tolerance-method
  antecedents cited by the source papers.

## G2 — material-specific rights and reuse

The author has rejected a blank rewrite and requested a manuscript-first
conversion plan. The proposed working boundary is:

- preserve the main article text initially and edit it later for integration;
- place unique supplement prose, equations, proofs, algorithms, and
  claim-relevant tables/figures next to the corresponding main material;
- import selected final display assets only, never code/data/output archives;
- record exact provenance for every imported component; and
- keep all imports local until coauthor/publisher reuse status is reviewed for
  external synchronization or submission.

| Source | Local manuscript conversion | Integrated equations/proofs | Selected final figures/tables | Code/data/computation | External reuse clearance |
| --- | --- | --- | --- | --- | --- |
| Environmetrics article | PROPOSED | PROPOSED WITH ATTRIBUTION | PROPOSED FROM MANIFESTED ASSETS | EXTERNAL ONLY | PENDING coauthor/publisher review |
| San Lorenzo bundle | INSPECTION/PROVENANCE ONLY | N/A | RESTRICTED unless separately cleared | EXTERNAL ONLY | current license is restrictive |
| QDESN | PROPOSED | PROPOSED WITH ATTRIBUTION | PROPOSED FROM CURRENT AUTHORITY ASSETS | EXTERNAL ONLY | PENDING coauthor/publication-status review |
| RQR-GIBBS | PROPOSED | PROPOSED WITH ATTRIBUTION | PROPOSED FROM CURRENT AUTHORITY ASSETS | EXTERNAL ONLY | PENDING coauthor/publication-status review |
| MTI-EXTENSIONS | PROPOSED | PROPOSED WITH ATTRIBUTION | none currently tracked | EXTERNAL ONLY | PENDING; no repository license located |
| exdqlm article | PROPOSED | PROPOSED WITH ATTRIBUTION | PROPOSED FROM ARTICLE ASSETS | EXTERNAL ONLY | PENDING coauthor/article review |
| exdqlm package | DOCUMENTATION/AUTHORITY SOURCE | IMPLEMENTATION REFERENCE ONLY | N/A unless selected | REMAINS EXTERNAL under MIT | preserve license and exact version |

“Proposed” authorizes nothing by itself. It is the execution design in
`manuscript-integration-plan.md`; the author must approve its seven defaults to
open G4. Local conversion does not establish permission to push, publish, or
submit verbatim text or a collaborator's asset.

## G3 — architecture

Author-directed working decision:

- **four research chapters:** `exdqlm`, Environmetrics, QDESN, and one combined
  MTI foundation/extensions chapter;
- **recommended final reading order:** `exdqlm`, Environmetrics, QDESN, MTI;
- **MTI split:** RQR-GIBBS and MTI-EXTENSIONS remain one project chapter at the
  current evidence level; and
- **TCSP language:** use conservative numerical-calibration/empirical wording
  unless an exact action-matched theorem is later completed and audited.

Architecture state: **AUTHOR-DIRECTED WORKING ARCHITECTURE**.

Committee/advisor confirmation that the software-centered `exdqlm` chapter
counts as a journal-suitable research unit: **PENDING**.

## G4 — drafting authorization

Gate G4 is **CLOSED FOR MANUSCRIPT CONVERSION** until the author accepts or
modifies the seven defaults in `manuscript-integration-plan.md`. Planning,
source inventory, citation/provenance preparation, metadata updates, and empty
chapter placeholders remain authorized.

- Recommended first implementation unit: one local bulk structural conversion
  campaign covering all four research chapters.
- Conversion rule: preserve article prose first, integrate supplements by
  topic, then perform the monograph/deduplication pass.
- Default asset rule: all non-superseded main figures/tables; claim-relevant
  supplement assets; no code, data, fitted objects, or full output archives.
- Publication boundary: local commits only; no push, Overleaf sync, or external
  submission of imported material before reuse review.
- Authorization by/date: **PENDING**.

When the author authorizes a unit, update this file, the public manifest,
`docs/STATUS.md`, and the relevant chapter source together.
