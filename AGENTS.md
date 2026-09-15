# Dissertation workspace instructions

This repository is a UCSC Statistical Science PhD dissertation starter.
Read `docs/STATUS.md`, `docs/REQUIREMENTS-REPORT.md`, the compliance matrix,
`metadata.tex`, `README.md`, `docs/VALIDATION.md`, and any author-supplied
academic-writing instructions before substantive work. Identify conflicts;
do not silently replace a cited requirement with a template convention.

## Scope and stages

The initial stage authorizes inspection of explicitly authorized research
sources, a concrete contribution/chapter plan, and routine local scaffold
maintenance. Keep all original article repositories unchanged. Preserve dirty
worktrees and do not fetch, checkout, stash, clean or run source builds there.
Do not change access controls to get around a blocked read. AGENTS.md does not
enforce filesystem permissions. Verify actual local/remote access first.

After presenting an evidence-backed audit, obtain the author's decision on
chapter selection and substantive scientific reinterpretation. Then draft
incrementally from approved sources. Routine format/build fixes can proceed.
Do not create remote projects, publish, push, merge, submit or message others
without the user's instruction for that action.

## Research fidelity

Record repository identity, branch/commit, dirty state and manuscript version.
A default-branch head is discovery evidence, not an approved manuscript.
Separate candidate contributions from inherited and collaborative work;
compare related exDQLM/exAL material with Barata's 2021 dissertation.
Audit inconsistent assumptions, notation, parameterizations, labels, macros,
references and output versions before importing. Preserve a mapping when
standardizing notation or citation keys.

Support material claims, equations and results with exact source provenance.
Distinguish likelihood-based posterior inference from generalized updating,
scientific targets from working-model assumptions, predictive/credible/tolerance
intervals, and empirical results from proved guarantees when relevant.
Check numerical provenance proportionately: model variant, prior, split,
horizon, replications, uncertainty and score definition. Do not run expensive
experiments or execute untrusted source scripts merely to fill gaps.

No fabricated citations, proofs, results, novelty, publication status,
permissions or approval. Preserve coauthor credit, qualifications, negative
findings and limitations. Use visible TODOs for missing evidence. Keep a brief
AI-assistance log; the applicable institutional disclosure rule remains open.

## Implementation and continuity

Use `bash scripts/build.sh`. Root is `main.tex`; metadata and notation are
centralized. Vendor class files stay unchanged. The bibliography follows
appendices. Compilation must use only tracked project sources/assets.
No large data, source histories, credentials, LFS or submodules in this project.

After meaningful changes, compile, inspect affected PDF pages, check log/font/
reference/overflow issues, and review the diff. Update the source manifest,
claim evidence where material, `docs/STATUS.md`, and verification limitations.
Keep the formatting demonstration and unresolved metadata visibly identified
until intentionally replaced. A clean PDF is not Graduate Division approval.
