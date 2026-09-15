# Research inclusion, contribution, rights, and architecture decisions

Status: **awaiting author/committee input**
Prepared: 2026-09-15
Evidence: `research-audit.md`, `chapter-plan.md`, `claim-evidence.json`, and
`../source-manifest.json`

This is the decision record for Gates G1–G4. Blank fields are deliberate. A
repository owner, author position, public URL, or audit recommendation is not a
substitute for a confirmed scholarly version, contribution statement, reuse
permission, or committee decision.

## G1 — inclusion snapshots

For each seed, record `confirm`, `replace`, or `exclude`. A replacement needs a
full commit, manuscript root, and reason. Approval of a commit does not approve
every branch, ignored result, or asset in that repository.

| Source | Audited commit | Audited manuscript | Decision | Replacement/reason | Confirmed by/date |
| --- | --- | --- | --- | --- | --- |
| Environmetrics | `1272bfc10442a28add5a4c74ff641e9b9a8e9666` | `wileyNJD-APA.tex` | PENDING | — | — |
| QDESN Version 2 | `757522db0f85815244370ec92a194de132268883` | `main.tex` plus two supplements | PENDING | — | — |
| RQR-GIBBS | `73887b9c86ef767aa1567c660718667945630aef` | `main.tex` plus supplement | PENDING | — | — |
| MTI-EXTENSIONS | `f345d946aa5a81b94795838bec58d874a0fdd0c9` | `main.tex` plus supplement | PENDING | — | — |
| exdqlm article | `d5534e97db8414fd875022261d4c530eae4676e4` | `exdqlm-jss.tex` | PENDING | — | — |

Additional G1 decisions:

- QDESN Search Phase II remains future work and outside the present inclusion
  snapshot: **PENDING**.
- MTI-EXTENSIONS is the intended companion to the RQR/MTI foundation:
  **PENDING**.
- The exdqlm article targets 1.1.1, Environmetrics retains 1.1.0, and current
  package `main` remains 1.1.2 support rather than a provenance replacement:
  **PENDING**.

## G2 — candidate contribution records

Complete one row per proposed research chapter. Name inherited/coauthor work
explicitly and attach a date or other evidence for confirmations. “Joint” is
not specific enough when a central theorem, algorithm, experiment, or text is
being attributed.

- Official dissertation name: **PENDING**
- Preferred scholarly/citation name and ORCID mapping: **PENDING**
- Resolution of “Antonio De Leon” in manuscripts versus “Antonio Aguirre” in
  package metadata: **PENDING**

| Chapter/source | Conceptual | Theory | Computation | Empirical | Writing/revision | Inherited/coauthor work | Confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Environmetrics | PENDING | PENDING | PENDING | PENDING | PENDING | exAL/exDQLM and named coauthor roles | PENDING |
| QDESN | PENDING | PENDING | PENDING | PENDING | PENDING | ESN/DESN, exAL/exDQLM, and named coauthor roles | PENDING |
| RQR/MTI | PENDING | PENDING | PENDING | PENDING | PENDING | residual-product/tolerance antecedents and named coauthor roles | PENDING |
| exdqlm software, if used | PENDING | PENDING | PENDING | PENDING | PENDING | Yan/Barata foundations and named package/article roles | PENDING |

## G2 — material-specific rights

Record a decision separately for each material class. Public access alone is
not reuse permission. The San Lorenzo bundle is inspection-only at the audited
snapshot. Publisher policy may differ for dissertation adaptation, accepted
manuscript text, and final formatted articles.

| Source | Adapted text | Figures | Tables | Code | Data/staged inputs | Evidence/conditions |
| --- | --- | --- | --- | --- | --- | --- |
| Environmetrics article | PENDING | PENDING | PENDING | PENDING | PENDING | coauthor and publisher review needed |
| San Lorenzo bundle | PENDING | PENDING | PENDING | PENDING | PENDING | current LICENSE is restrictive |
| QDESN | PENDING | PENDING | PENDING | PENDING | PENDING | coauthor and publication-status review needed |
| RQR-GIBBS | PENDING | PENDING | PENDING | PENDING | PENDING | coauthor and publication-status review needed |
| MTI-EXTENSIONS | PENDING | PENDING | PENDING | PENDING | N/A unless supplied | no repository license located |
| exdqlm article | PENDING | PENDING | PENDING | PENDING | PENDING | article rights and missing archive status needed |
| exdqlm package | N/A for prose | N/A unless used | N/A unless used | MIT-licensed subject to notice | N/A unless supplied | preserve license and exact version |

## G3 — architecture

Recommended decision:

- **Option A:** three research chapters—Environmetrics, QDESN, and combined
  RQR/MTI—with exdqlm in shared methods/reproducibility material.

Consequential alternatives:

- **Option B:** promote exdqlm to a research chapter only after the distinct
  candidate contribution and immutable 1.1.1 archive are established.
- **Option C:** split MTI-EXTENSIONS only after snapshot-matched implementation,
  targeted static/dynamic validation, a distinct contribution record, and
  committee approval.

Architecture decision: **PENDING**
TCSP proof-language resolution: **PENDING**
Committee/advisor confirmation and date: **PENDING**

## G4 — drafting authorization

Gate G4 is **CLOSED**. After G1–G3 are recorded, specify exactly one authorized
unit, its approved sources, allowed asset classes, and review owner.

- Authorized unit: **NONE**
- Source snapshots: **NONE**
- Allowed imports: **NONE**
- Required qualification/repair before drafting: **NONE RECORDED**
- Authorization by/date: **PENDING**

When a decision is made, update this file, the public manifest, and
`STATUS.md` together. Never replace a `PENDING` value by inference.
