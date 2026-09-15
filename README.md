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

Packages: PSNFSS (`mathptmx`), AMS math/fonts/theorems, geometry, setspace,
fancyhdr, graphicx, booktabs, PGF/TikZ, caption, natbib, url and hyperref;
base LaTeX encoding and dependencies. The four UCSC class/size files are
vendored. A reasonably complete TeX Live installation includes these mature
packages. No installation was performed on the user's machine.

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

- `metadata.tex`: official author name, final title, conferral month/year,
  approved committee size/names/roles and current dean wording.
- `docs/STATUS.md`: decisions, gaps and next work.
- `source-manifest.local.json`: create from the example; supply authorized
  absolute source paths locally. Do not publish local paths by accident.
- `docs/CODEX-KICKOFF.md`: use in the later muscat thesis-workspace chat.

`chapters/` contains five structured placeholders, including three research
slots. The blank second leaf is intentional. The abstract and acknowledgments
contain instructions only. The appendix contains elementary demonstration
material that must be removed before submission. Replace its institutional
example bibliography with verified research references as chapters develop.
Do not disable `\StarterDrafttrue` merely to make an unfinished file look final.

## Portability and provenance

Use relative paths inside the dissertation. Put imported final assets in
`figures/` or `tables/` as needed, and record source commit/path, adaptation and
checks in the manifest. Never import complete research histories, large data,
caches or credentials. `notation.tex` centralizes notation. Keep journal
classes and conflicting macros out of imported chapters.

See `TEMPLATE-NOTES.md` and `vendor/ucscthesis/LICENSE` for community-template
attribution, license and project changes. No institutional approval is implied.
