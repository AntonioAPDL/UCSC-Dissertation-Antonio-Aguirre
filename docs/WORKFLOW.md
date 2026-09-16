# Overleaf, GitHub and muscat Codex workflow

Verified against linked official documentation on 2026-09-15. The existing
GitHub repository and muscat Remote-SSH workspace were audited separately in
`SETUP-AUDIT.md`; Overleaf account linking, project linkage and compilation
have not been performed. Commands below retain placeholders only where the
future handoff must supply an actual branch, source path or reviewed file.

## 1. Establish the Overleaf side once

The GitHub-first alternative is now the applicable path: this repository
already exists and is the muscat checkout's origin. Do not follow the older
starter route in which Overleaf creates another repository.

1. Before changing any linkage, determine whether an Overleaf project already
   contains dissertation work. Preserve its source, comments and tracked
   changes and record any current GitHub linkage. Do not infer linkage from the
   Git commit message or repository name.
2. If no Overleaf project must be preserved and the author authorizes the
   handoff, open [UCSC's Overleaf portal](https://www.overleaf.com/edu/ucsantacruz),
   verify the institutional entitlement, and use Integrations / GitHub to
   import this existing repository as a new Overleaf project. Review requested
   account and repository permissions. Only the project owner can establish
   the initial link, and organization policy may add OAuth requirements.
3. Select `main.tex` as the root document and pdfLaTeX. Use TeX Live 2023 if
   offered, or an available newer version. Compile and compare the result with
   `VALIDATION.md` and `SETUP-AUDIT.md`.
4. Record the actual linked default branch and the successful Overleaf build
   checkpoint. If an existing project is already linked to this repository,
   skip creation and use the explicit editing handoff in section 3.

An existing unlinked or differently linked Overleaf project cannot simply be
rebound without a preservation and reconciliation decision. Do not create two
competing repositories or overwrite either source state to make linkage appear
clean.

See [Overleaf GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization)
and [GitHub clone instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

Native GitHub synchronization is recommended because GitHub is the desired
shared repository. [Direct Overleaf Git access](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration)
is another premium feature, with a Git remote for the Overleaf project; it
adds a different transport workflow. Do not configure both synchronization
paths for this starter without a concrete need. Sync is manual, not continuous.

## 2. Give the muscat Codex chat the intended scope

Open the dissertation as a single-folder VS Code Remote-SSH project on muscat.
Use a fresh Codex chat in that window and verify both the hostname and working
directory before relying on its instruction scope. Opening a window does not
move an existing chat. A cloud task or a session on another host cannot see
muscat sources merely because the VS Code interface can. Follow the current
[IDE documentation](https://learn.chatgpt.com/docs/codex/ide).

Create `source-manifest.local.json` from the example and fill in only the
source locations you authorize for inspection. In the Codex permissions
control, inspect the effective configuration. The intended boundary is
write access to the dissertation workspace and read access to specified
research sources. `workspace-write` is the usual bounded local mode; actual
read scope can be restricted by platform or managed policy. The supplied
project does not install or change permission settings.

First ask Codex to report its current directory and test read access to one
known manuscript, then inventory the authorized repositories. These are
read-only examples; substitute a real source path:

```bash
research_repo='/ABSOLUTE/AUTHORIZED/SOURCE/PATH'
git --no-optional-locks -C "$research_repo" status --short --branch
git -C "$research_repo" rev-parse --show-toplevel
git -C "$research_repo" rev-parse --abbrev-ref HEAD
git -C "$research_repo" rev-parse HEAD
git -C "$research_repo" ls-files
```

Do not fetch, checkout, reset, stash, clean, update submodules or run builds in
original source repositories during this inspection. Existing uncommitted
files are evidence to record and preserve, not permission to edit them.

If a source is unreadable, use a supported narrowly scoped read exception
where the actual client/policy allows it, or provide an authorized snapshot
of selected files. A small local `audit-inputs/` directory is an acceptable
fallback for copies; it is ignored by Git, excluded from the Overleaf upload,
and never a compilation dependency. Record snapshot source commit and dirty
state so omissions are visible. Do not broaden original-repository write
access as a read-access workaround. In particular, writable roots and CLI
additional-directory options can expand write scope; a repository URL is not
an access grant. A VS Code multi-root workspace is optional viewing convenience,
not proof of Codex access or isolation.

The technical boundary comes from the
[sandbox and permissions](https://learn.chatgpt.com/docs/sandboxing), with
[platform details](https://learn.chatgpt.com/docs/agent-approvals-security).
`AGENTS.md` supplies behavior and scope instructions; it does not enforce an
ACL. Check inherited and nested instructions as described by
[OpenAI's AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
Config locations and IDE entry points are documented in
[Config Basics](https://learn.chatgpt.com/docs/config-file/config-basic).
For editor-only folder grouping see
[VS Code multi-root workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces).

## 3. Use an explicit editing handoff

**Before a local/Codex editing session:**

1. Ask collaborators to pause source editing in Overleaf for the agreed
   local-edit window. Save or export important pending review comments.
2. In Overleaf, push its latest source changes to GitHub. Resolve a reported
   conflict before continuing. Confirm the resulting default-branch commit.
3. Locally, inspect status. Preserve existing changes on their current branch;
   do not discard or hide them automatically. Start from a clean checkpoint.
4. Fetch GitHub and fast-forward the linked default branch. If fast-forward
   is refused, inspect divergence and merge deliberately; do not force it.

```bash
# Replace the branch name with the actual linked default branch.
git status --short --branch
git fetch origin
git switch 'REPLACE_WITH_LINKED_DEFAULT_BRANCH'
git pull --ff-only origin 'REPLACE_WITH_LINKED_DEFAULT_BRANCH'
git switch -c 'draft/chapter-a-audit'
```

Use a new, unused branch name. Work in small batches. Review diffs, compile,
inspect affected PDF pages, update provenance and `STATUS.md`, then stage
explicit files and commit. Push the branch and review/merge it into the linked
default branch. This document does not authorize a later agent to push or
merge unless the user requests it.

```bash
bash scripts/build.sh
git diff --check
git diff --stat
git diff
git add 'REPLACE_WITH_REVIEWED_FILE_1' 'REPLACE_WITH_REVIEWED_FILE_2'
git commit -m 'Draft reviewed chapter material with source provenance'
git push -u origin 'draft/chapter-a-audit'
```

After the reviewed merge, use Overleaf's **Pull from GitHub**, then compile
there and check the changed pages. Overleaf exchanges the linked default
branch and does not implement a local branch workflow. Finish the handoff
before advisors resume editing.

**For an advisor/Overleaf editing session:** first synchronize the reviewed
GitHub state into Overleaf. Pause local source changes while advisors edit.
Resolve/accept tracked changes and preserve outstanding comments as appropriate
before another GitHub pull. Then push Overleaf source changes to GitHub,
record the checkpoint, and fetch/pull locally before the next local session.

Overleaf warns that GitHub pulls can disturb comments and tracked changes.
Do not treat them as Git-tracked review records. A sync commit also does not
preserve every local author attribution in the same way as GitHub history.
The source is synchronized; this project ignores the generated main PDF and
build files. Download review PDFs explicitly when sharing a fixed version.
These limitations are documented in the
[GitHub synchronization guide](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization).

## 4. Recover a conflict or broken build

Preserve all three states first: local uncommitted work, GitHub branch heads,
and an Overleaf source ZIP/history checkpoint. Do not overwrite one with
another to silence a conflict. Overleaf may create a dated branch containing
its changes when a push conflicts; record the actual branch name shown.

Fetch, inspect the divergent commits and compare files in a review branch.
Merge the Overleaf branch, resolve each conflict with both versions visible,
compile and inspect, then merge the reviewed result into the linked default
branch. Use
[GitHub's command-line conflict procedure](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line).
Pull into Overleaf only after its unsynchronized edits have been preserved.
Never use a force push or hard reset as routine sync repair.

For a known compiling version, create a review branch from its recorded
commit or use a fresh disposable clone. Keep current work on its existing
branch. A selected revert commit on the shared branch can restore behavior
while preserving history, but review merges and later dependencies first.
Record compiler version as well as commit; a TeX-version change can explain
an apparent regression. Do not delete source evidence to obtain a clean build.

## 5. Keep the project small and self-contained

Use `source-manifest.example.json` as the schema, recording exact source commit
and path, imported destination, adaptation, rights status and verification.
Import text as ordinary chapter LaTeX after macro/notation review. Merge
bibliographic entries by DOI/title/author, then preserve a citation-key map.
Import final figure/table assets and their provenance; keep large data,
simulation output, caches and external Git histories in their source projects.

Overleaf documents no support for submodules or Git LFS. Symlinks do not provide
portable external dependencies, and executable permission bits are lost; call
`bash scripts/build.sh`. Current plan documentation lists 2,000 project files,
7 MB total editable text, 2 MB per editable text file, and a 50 MB single-upload
limit. The sync guide recommends keeping individual sync commits small
(fewer than 100 files and under 100 MB). Limits and compilation time allowances
can change; this starter is much smaller. See
[Overleaf plan limits](https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits).
The Overleaf build must not need a source snapshot, private repository,
absolute local path, remote symlink or expensive research rerun.
