# Muscat setup audit

Performed 2026-09-15. This records the server checkout and technical scaffold
audit only. It does not select research chapters, approve a manuscript version,
or establish institutional filing compliance. Exact machine paths and launcher
details are kept in ignored `SETUP-LOCAL.md`.

## Checkout and access result

- A normal, non-shallow SSH clone with complete available history was made from
  `git@github.com:AntonioAPDL/UCSC-Dissertation-Antonio-Aguirre.git`.
- The remote default branch is `main`. The clean inspected checkpoint was
  `de4d124d5e10ece8e69fc483e951ee42cf06ec5f`, with `main` tracking
  `origin/main`. The remote repository already existed; no remote was created.
- Setup changes were isolated on `setup/muscat-audit-20260915`. GitHub CLI and
  shell Git authentication/connectivity were verified without retaining secret
  values. Git author name/email are not configured, so no commit was made.
- No fetch, checkout, build or write was performed in an article/research
  repository. No push, merge, visibility change, Overleaf action or publication
  occurred.
- Two ordinary clone attempts received the small pack but blocked in a local
  filesystem `fsync` during `index-pack`. The successful clone used Git's
  per-process test override to skip that sync call; no Git setting was changed.
  `git fsck --full` then verified the complete object database. This server
  condition is recorded with operational detail in `SETUP-LOCAL.md` and should
  be escalated if a later fetch that receives objects stalls similarly.

## Repository inventory at the inspected commit

The historical baseline is current: 46 tracked starter files were present and
intact before setup edits.

| Files | Purpose and audit result |
| --- | --- |
| `AGENTS.md`, `README.md`, `TEMPLATE-NOTES.md` | Project scope, entry point and community-template provenance. Instructions were read; the four root class/size hashes match the recorded upstream snapshot. |
| `main.tex`, `metadata.tex`, `preamble.tex`, `notation.tex`, `references.bib` | Root document, unresolved formal metadata, shared formatting/packages, notation and the two-entry demonstration bibliography. All root inputs resolve; bibliography remains last. |
| `frontmatter/abstract.tex`, `acknowledgments.tex`, `copyright.tex`, `title.tex` | Demonstration front matter. Official name, title, dates, committee, dean and approval remain explicit placeholders. |
| `chapters/01-introduction.tex` through `05-synthesis.tex` | Five structured placeholders: integration, three provisional research slots and synthesis. No scientific claims or chapters are present. |
| `appendices/a-format-demonstration.tex` | Removable equation/theorem/algorithm/figure/table/footnote/citation demonstration; retained intact. |
| `docs/ASSISTANCE-LOG.md`, `CODEX-KICKOFF.md`, `REQUIREMENTS-REPORT.md`, `STATUS.md`, `VALIDATION.md`, `WORKFLOW.md`, `chapter-plan.md` | Assistance record, research-audit prompt, cited requirements report, live status, historical validation, handoff workflow and provisional architecture. |
| `docs/claim-evidence.example.json`, `compliance-matrix.json`, `compliance-matrix.md`, `source-register.json`, `source-snapshots.json`, `source-manifest.example.json` | Structured provenance examples, rule mapping and source records. All JSON parses; discovery heads remain observations rather than approved versions. |
| `docs/validation/bibtex.log.txt`, `fonts.txt`, `latex-build.log.txt`, `results.json` | Retained evidence from the earlier TeX Live 2023 build. These are documentation, not build inputs. |
| `scripts/build.sh` | Single supported build entry point. It previously failed immediately when `latexmk` was absent. |
| `ucscthesis.cls`, `uct10.clo`, `uct11.clo`, `uct12.clo` | Vendored UCSC class and size files; unchanged and hash-consistent with `source-snapshots.json`. |
| `vendor/ucscthesis/CONTRIBUTING`, `LICENSE`, `README`, `README.UCSC`, `uctest.bib`, `uctest.tex` | LPPL attribution/license and retained upstream sample material. The vendor license does not impose a new license on future dissertation content. |

`main.tex` has no external figure or data dependency: the only figure is TikZ.
Required packages found in the system TeX tree are base encodings, PSNFSS
`mathptmx`, AMS math/fonts/theorems, `geometry`, `setspace`, `fancyhdr`,
`graphicx`, `booktabs`, PGF/TikZ, `caption`, `natbib`, `url`, `hyperref` and
`plainnat.bst`. There are no symlinks, submodules, LFS pointers, shell-escape
hooks, credentials, absolute server paths or large tracked artifacts. A
project-wide content license is not declared; the explicit LPPL scope for the
vendored template is preserved.

## Focused repairs

- Added `.gitignore` for `build/`, root `main.pdf`, common LaTeX auxiliaries,
  `.env` files, `source-manifest.local.json`, `audit-inputs/`, ignored local
  setup notes, and common editor/OS artifacts. No tracked file is newly hidden.
- Made `scripts/build.sh` use `latexmk` when available and otherwise perform the
  required pdfLaTeX/BibTeX passes with installed standard tools. Updated the
  README to describe the actual behavior.
- Enabled guarded `glyphtounicode` output so the older server pdfTeX embeds
  explicit Unicode maps without altering layout.
- Replaced the stale instruction to have Overleaf create a second GitHub
  repository. The workflow now treats the existing repository as the GitHub-
  first source and leaves all actual linkage/synchronization for an authorized
  handoff.
- Updated project status and assistance history. Preserved every unresolved
  administrative and candidate field and the full formatting demonstration.

## Muscat build and inspection

`bash scripts/build.sh` was run from an initially absent `build/` directory.
The fallback used pdfTeX 1.40.19, LaTeX2e 2017-04-15 and BibTeX 0.99d from TeX
Live 2018; `latexmk` and `biber` are unavailable. This is older than the prior
TeX Live 2023/pdfTeX 1.40.25/latexmk 4.83 baseline.

- Exit status 0; `build/main.pdf` has 20 US Letter portrait pages and SHA-256
  `61bce9fbbfb2c85b4956c40a8cd45a379b9128f289f8de89bd5fc133f20e988d`.
- Final logs have no undefined citations/references, duplicate labels or
  destinations, overfull/underfull boxes, rerun request or BibTeX warning.
  The one warning is the already documented `caption`/legacy-class warning.
- All seven fonts are embedded, subset Type 1 fonts with Unicode maps. Text is
  extractable. The older engine changes PDF bytes/producer metadata relative to
  the retained 2023 baseline, but not the demonstrated layout.
- Extracted non-footer text bounds are at least 1.500 inches left, 1.250 right,
  1.301 top and 1.285 bottom. All 18 visible page numbers are centered within
  0.001 PDF point, with 0.914-inch lower-edge clearance.
- Page order/labels are visually consistent with the scaffold: hidden title i
  and blank ii, contents iii, front matter through viii, chapter 1 at Arabic 1,
  Appendix A at 10-11, and bibliography last at 12. Representative title,
  contents, abstract, acknowledgments, chapter, proof, figure/table and
  bibliography pages were rendered and inspected. All 20 page rasters were
  unchanged by the Unicode-only repair.

The resulting PDF remains a formatting demonstration, not filing approval.
Landscape/facing-caption modes, real metadata, imported assets, substantive
chapters, Overleaf compilation and institutional acceptance remain untested.

## Handoff

Open this checkout as a single-folder workspace in a new VS Code Remote-SSH
window using the exact command in ignored `SETUP-LOCAL.md`. Start a fresh Codex
chat; opening the window does not migrate the present chat. The fresh chat must
read `AGENTS.md`, this audit, `STATUS.md`, `SETUP-LOCAL.md` and
`CODEX-KICKOFF.md`, then verify its hostname and working directory before the
author supplies the explicitly authorized research-repository list.
