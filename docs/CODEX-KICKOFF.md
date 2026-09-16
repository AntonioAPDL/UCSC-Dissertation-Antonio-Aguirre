# Use this prompt in the dissertation-workspace Codex chat

The research-audit process defined in `docs/research-audit-master-plan.md` was
executed on 2026-09-15. Read `docs/research-audit.md`,
`docs/research-audit-validation.md`, `docs/chapter-plan.md`,
`docs/manuscript-integration-plan.md`, `docs/research-decisions.md`,
`docs/claim-evidence.json`, and
`source-manifest.json` before further work.
Do not repeat the whole source audit unless an approved snapshot changes. For
current editorial work, also read `docs/editorial-review.md` and
`docs/revision-ledger.json`.

The author has selected the audited commits as working drafting snapshots,
supplied the official/scholarly name mapping, and directed a four-project
architecture: exdqlm, Environmetrics, QDESN, and combined MTI. Repository
evidence supplies collaborators and project-level contributions. Granular
candidate/coauthor roles, direct-reuse rights, the committee's exdqlm counting
decision, and any final snapshot replacements remain open. Gate G4 is complete:
the author approved the conversion, it was merged into GitHub `main`, and the
author reports a successful Overleaf handoff. Gate G5 scientific/editorial
integration is current. The checklist below remains the substantive-fidelity
protocol for a targeted re-audit; `manuscript-integration-plan.md` documents the
completed structural import, and the revision ledger protects later edits.

You are working in my UCSC Statistical Science PhD dissertation repository.
I entered in Fall 2021 and plan around Fall 2026, but my defense, conferral and
filing dates remain unconfirmed. My advisors are Raquel Prado and Bruno Sansó;
use only my approved committee record to fill formal roles. The present project
is a formatting scaffold. Do not invent substantive dissertation content.

Complete the inspection-and-planning stage below. You may read the source
repositories/locations that I explicitly authorize in this chat or in my
local source manifest, and you may maintain this dissertation scaffold locally.
Leave original article repositories and their uncommitted work unchanged.
A source URL alone does not establish access or an authoritative version.
Do not expand write permissions, publish, push, merge or contact others merely
to make progress. Diagnose access gaps and offer a narrowly scoped route.

1. Read all applicable AGENTS.md instructions, README.md, metadata.tex,
   docs/STATUS.md, docs/REQUIREMENTS-REPORT.md, the compliance matrix,
   docs/VALIDATION.md, docs/WORKFLOW.md, source-manifest.example.json and my
   local source manifest. Read any academic-writing guidelines I supply.
   State the working directory, source-read scope and dissertation-write scope.
   Note unresolved rules and conflicts without reopening settled choices
   unnecessarily. Build the current scaffold as a baseline if tools permit.

2. Inventory each authorized repository. Record verified identity, local path,
   branch, exact commit and dirty state; do not modify it. Locate manuscript
   roots, supplements, bibliography databases, theory notes, implementations,
   experiment configurations, result tables and figure-generation scripts.
   Use selective search, not indiscriminate dumping of data or credentials.
   Mark generated, duplicated, superseded, experimental and inaccessible files.
   Record whether the inventory covers a whole checkout or a partial snapshot.

3. Establish the intended manuscript version with evidence. Distinguish it
   from newer experimental code, older accepted text and stale cached output.
   Cross-check manuscript, code and output disagreements; do not silently
   select whichever version supports an attractive story. Treat observed
   default-branch heads in the manifest as historical discovery, not approval.

4. Create docs/research-audit.md with a source inventory, contribution inventory,
   source-to-chapter map and prioritized contradictions/gaps. For important
   claims, equations, tables and figures, record exact commit/path and locator,
   target destination, supporting artifacts and verification status. Keep
   tracking proportionate: do not make a ledger entry for every ordinary
   sentence. Use docs/claim-evidence.example.json as a compact starting point.

5. Assess novelty and overlap. Separate my work from coauthors and prior
   scholarship. Explicitly compare related exDQLM, exAL and joint-quantile
   content with Barata's 2021 dissertation and the original papers it cites.
   Do not treat a package extension or renamed model as an independent chapter
   without a defensible contribution. Do not force every candidate repository
   into the dissertation or count introduction/conclusion as research chapters.

6. Audit repeated literature, shared models/priors/likelihoods, algorithms,
   datasets and experiments. Identify notation collisions, differing assumptions,
   incompatible parameterizations, bibliography duplicates, labels/macros,
   theorem numbering and journal formatting. Propose a documented mapping
   for notation and citation keys before imports. Preserve distinctions that
   cannot be safely unified.

7. Assess the statistics appropriate to the actual material. Where relevant,
   distinguish likelihood-based posterior inference from generalized updating,
   the inferential target from a working-model assumption, predictive intervals
   from credible or tolerance intervals, and empirical performance from proved
   guarantees. Preserve assumptions, qualifications and negative findings.
   Flag source-supported issues rather than launching unrelated new research.

8. For central numerical results, check available provenance and targeted
   consistency: model variant, prior/hyperparameters, data version/preprocessing,
   train/test split, horizon, replication count, uncertainty summaries and
   score definition. Record seeds/environment where available. Classify a result
   as reproduced only if you actually reproduce it. Do not invent missing
   results or run expensive simulations just to populate a chapter.

9. Produce a concrete proposed dissertation plan in docs/chapter-plan.md:
   common question; purpose and distinct contribution per chapter; source
   project/version; prerequisites; shared background; new exposition; overlap
   risk; main-text versus appendix allocation; evidence gaps and next steps.
   Explain whether at least three independently defensible research units
   are supported. Treat catalog “should” and “must” precisely. Present any
   chapter-count uncertainty to me and my advisors.

10. Present the completed audit and plan, then ask for my decision on chapter
    selection and substantive scientific reinterpretations. This is the
    transition to drafting; do not skip the audit or stop after merely offering
    to perform it. Routine scaffold, citation-import tooling and build repairs
    may proceed as needed without blocking on formatting preferences.

After I approve the conversion plan, perform the manuscript-first structural
conversion defined there: preserve all four main article bodies initially,
integrate unique supplement material by topic, import only selected final
display assets, and keep code/data/computation external. Work in recoverable
chapter-sized local commits even though the campaign covers all four chapters.
Only after all four compile should you deduplicate background and write
monograph transitions. Preserve coauthor attribution, source-specific rights
status, limitations and citation accuracy. Use visible TODOs for missing
support. Do not fabricate novelty, publication status, theorems, numbers, an
abstract or acknowledgments. Build and inspect after meaningful changes and
keep compilation independent of sibling repositories and expensive
computations. Do not infer reuse permission from the completed GitHub/Overleaf
handoff. Further pushes and synchronization follow the explicit reviewed-unit
workflow.

At each handoff update docs/STATUS.md with completed work, decisions, source
versions, material changes, missing evidence, validation results and the next
concrete task. Update the assistance log factually. Finish this first stage
with the actual audit artifacts, a short evidence-backed recommendation and
only the decisions that genuinely require my scientific judgment.
