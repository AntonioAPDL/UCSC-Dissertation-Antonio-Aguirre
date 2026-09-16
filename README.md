# UCSC dissertation starter

Audited 2026-09-15. **Formatting starter, not a dissertation approved for filing.**

Start with `docs/REQUIREMENTS-REPORT.md`, then `docs/WORKFLOW.md`. The report
contains the completion plan and specific questions for the candidate,
advisors, program and Graduate Division. `docs/compliance-matrix.md` links
rules to implementation and checks; JSON is the editable structured version.

## Build

From the project root, with an existing TeX installation:

```bash
bash scripts/build.sh
```

Output: `build/main.pdf`. Main document: `main.tex`. Engine: pdfLaTeX;
bibliography: BibTeX. The script uses latexmk when available and otherwise
runs the required pdfLaTeX/BibTeX passes directly. Tested environment and
results are in `docs/VALIDATION.md`. No sibling repository, data file, network
fetch, R/Python analysis, shell escape or separate figure-generation command
is required.

Packages: PSNFSS (mathptmx), AMS math/fonts/theorems, mathtools, bm, geometry,
setspace, fancyhdr, graphicx, booktabs, array/tabularx/longtable, float,
enumitem, xcolor, etoolbox, PGF/TikZ, algorithm/algorithmic, caption, natbib,
url and hyperref; base LaTeX encoding and dependencies. The four UCSC
class/size files are vendored. A reasonably complete TeX Live installation
includes these mature packages. No installation was performed on the user's
machine.

## Manuscript conversion

Research Chapters 2--5 are local manuscript-first structural conversions at
the immutable source commits in source-manifest.json. Main article prose is
the initial baseline; selected supporting proofs, derivations, algorithms,
diagnostics, tables, and figures are integrated into the chapter bodies. Code,
data, fitted objects, computation, source histories, and full output archives
remain external. Imported text and assets are not cleared for external reuse.

Routine thesis builds need only this checkout. To regenerate the conversion
from the retained exact-commit audit clones, run:

    python3.11 scripts/import_manuscripts.py --audit-root /PATH/TO/AUDIT-CLONES
    python3.11 scripts/validate_manuscript_imports.py \
      --audit-root /PATH/TO/AUDIT-CLONES

The validator may also run without --audit-root; that checks the local
manifests, destinations, citations, labels, dependencies, paths, and file
types, but cannot recheck source Git blobs. Chapter records are under
docs/imports/.

For Linux without an existing TeX installation, use the official TeX Live
installer in a user-owned directory; choose an adequate scheme and add its
platform `bin` directory to PATH. Follow the current instructions at
https://tug.org/texlive/quickinstall.html rather than running a sudo command
from this project. Overleaf provides its own TeX environment.

For a clean build, move any existing `build/` aside first if its PDF is worth
keeping, then run the same command. `build/` contains generated files only.

## Overleaf

This project already has Git history and a GitHub origin. Do not create a
second GitHub repository from Overleaf or assume an Overleaf project is already
linked. At an authorized synchronization handoff, first preserve any existing
Overleaf edits, comments and tracked changes, then follow `docs/WORKFLOW.md`.
Use `main.tex`, pdfLaTeX and TeX Live 2023 if offered, or an available newer
version, and repeat the documented checks. The muscat build is not an Overleaf
test.

## Files to edit first

- `docs/research-audit.md`: completed fixed-snapshot research audit, source
  conflicts, evidence limits, and decisions required before drafting.
- `docs/chapter-plan.md`: evidence-backed four-project architecture and
  chapter boundaries.
- `docs/manuscript-integration-plan.md`: controlling manuscript-first conversion
  plan, including per-repository supplement placement, asset selection,
  bibliography/LaTeX normalization, provenance, execution, and acceptance
  criteria.
- `docs/research-decisions.md`: author-supplied identity/architecture decisions,
  repository-documented collaborators/contributions, and the focused role,
  rights, committee, and drafting confirmations that remain.
- `source-manifest.json` and `docs/claim-evidence.json`: public immutable source,
  validation-run, and claim provenance. Check with
  `python3 scripts/validate_research_audit.py`.
- `metadata.tex`: official author name, final title, conferral month/year,
  approved committee size/names/roles and current dean wording.
- `docs/STATUS.md`: decisions, gaps and next work.
- `source-manifest.local.json`: ignored exact paths, original-tree guards, and
  audit-clone records. Do not publish it.
- `docs/CODEX-KICKOFF.md`: use for the gated source-decision and drafting
  workflow.

The chapters directory contains an unfinished introduction, four converted
research chapters, and an unfinished synthesis. The blank second leaf is
intentional. The abstract and acknowledgments contain instructions only. The
starter demonstration appendix is no longer part of the document; technical
supporting material is integrated into the research chapter bodies. The
consolidated bibliography is generated from the fixed manuscript snapshots
plus the two administrative starter records.
Do not disable `\StarterDrafttrue` merely to make an unfinished file look final.

## Portability and provenance

Use relative paths inside the dissertation. Put imported final assets in
`figures/` or `tables/` as needed, and record source commit/path, adaptation and
checks in the manifest. Never import complete research histories, large data,
caches or credentials. `notation.tex` centralizes notation. Keep journal
classes and conflicting macros out of imported chapters.

See `TEMPLATE-NOTES.md` and `vendor/ucscthesis/LICENSE` for community-template
attribution, license and project changes. No institutional approval is implied.
