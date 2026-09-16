# Research-audit validation record

Status: **bounded validation complete; no full research workflow reproduced**
Date: 2026-09-15
Related records: `research-audit.md`, `claim-evidence.json`, and
`../source-manifest.json`

## 1. Execution boundary

Validation used eight full-history ordinary Git clones at the immutable commits
in the public source manifest. The clones lived in a dedicated temporary
server-local audit root outside the dissertation and original research trees.
The first attempt on the persistent project filesystem stalled in server I/O;
it was cancelled without producing usable checkouts, and the full clones were
recreated on the server's local temporary filesystem. Exact machine paths are
recorded only in the ignored local manifest.

The audit did not fetch, switch, reset, stash, clean, build, or write in any
original research checkout. End-of-audit guards confirmed that every original
tree inspected before execution retained its original branch, HEAD, and clean
tracked/untracked status. The QDESN original remained a non-authoritative work
branch, and the RQR original remained at its stale cached `main`; neither was
used for current scientific conclusions.

The server provided TeX Live 2018, R 4.6.0, a default Python 3.6.8, and Python
3.11. Checks requiring newer Python syntax were run explicitly with Python
3.11. No root installation, global package change, remote publication, or
expensive simulation campaign was performed.

## 2. Results by source

| Run | Result | Evidence obtained | Deliberate limit |
| --- | --- | --- | --- |
| `RUN-QDESN-CURRENT-ASSETS` | PASS | 14 single-quantile, 17 corrected-v4 joint, 12 GloFAS, and 10 PriceFM declared hashes passed; corrected-v4 checker/test, PriceFM R98 checker, and GloFAS publication-contract test passed | Upstream simulation/application campaigns not rerun |
| `RUN-QDESN-STALE-CONTROLS` | ISSUE FOUND | 13 of 14 rows in the historical joint-asset manifest mismatch current files; Phase 181 projection and interval-figure checks expect superseded manuscript inputs | Current corrected-v4 authority passes and must remain distinct from these historical controls |
| `RUN-QDESN-TEX` | PASS | Main article, main supplement, and Gaussian supplement built to 22, 49, and 9 pages with resolved citations/references | Document build only |
| `RUN-ENV-LINEAGE` | PASS | All 13 manuscript figure paths and the authoritative-output lineage contract passed, including the corrections dependency | No selected-model refit, live workflow, or raw-data reconstruction |
| `RUN-SAN-VALIDATE` | PASS | Public repository file, hash, size, and hygiene validation passed with Python 3.11 | Default Python 3.6 cannot parse the validator's future-annotations import; no model rerun |
| `RUN-RQR-FOCUSED` | PASS | Seven theory-table tests, five theory-figure suites, and manuscript-language checks passed | Figure tests required a temporary Cairo bitmap profile because the SSH session has no X11; 1000-replication campaign not rerun |
| `RUN-MTI-TEX` | PASS | Main and supplement built to 7 and 4 pages with resolved citations/references | Repository contains no implementation or numerical study to test |
| `RUN-EXDQLM-ARTICLE` | PASS | `code.R` parsed and the article completed a BibTeX/pdflatex build to 55 pages with resolved citations/references | Named 1.1.1/replication archives and full approximately 64-minute batch were absent or not run |
| `RUN-EXDQLM-PKG` | PASS | Version 1.1.2 source package built and installed in an isolated library; focused inference-configuration, structured scale-skewness, and RNG-repeatability tests passed | Full package check/CI and cross-platform matrix not run |

No result reached `E4`. Passing a build, hash contract, or focused test supports
only the bounded scope named in the table.

## 3. Reproduction commands

Create fresh immutable clones in a dedicated location:

```bash
bash scripts/prepare_research_audit_clones.sh "${AUDIT_ROOT}"
```

The helper refuses the filesystem root, a relative target, a location inside
the dissertation, a nonempty non-Git destination, a wrong remote, a wrong
commit, or a dirty reused audit clone. It performs no cleanup and never touches
an original source checkout. Its no-argument, relative-path, resolved-root, and
inside-thesis guards each returned the intended usage failure in bounded safety
tests. Exact per-source commands, environment overrides, and raw output
summaries from this run are retained in the ignored
`audit-inputs/` record.

Validate the public audit wiring from the dissertation root:

```bash
python3 scripts/validate_research_audit.py
bash scripts/build.sh
```

The audit validator checks schemas, stable IDs, exact commits, source/claim
linkage, evidence vocabulary, validation-run records, the ignored local
boundary, and accidental public absolute paths or credential-like strings. It
uses only the Python standard library and is compatible with the server's
default Python 3.6.

## 4. Interpretation of failures

The QDESN historical-manifest and Phase 181 failures are source-maintenance
findings. They do not overturn the current corrected-v4 result line, whose
manifests and focused checks pass. The San Lorenzo default-Python failure and
RQR default-graphics failure are environment-entry-point defects with verified
workarounds; they do not constitute scientific replication failures.

These distinctions must be preserved during repair. A later source change
should update or archive the stale controls, specify supported Python and
headless-graphics environments, and rerun the same bounded contracts before
any dissertation import.

## 5. Dissertation-level checks

After the audit records were wired, the standard-library validator passed with
8 sources and 32 claim/evidence records. Separate object checks confirmed all
12 audit/related snapshot commits and all 32 claim paths at their declared
commits. The dissertation scaffold then rebuilt to 20 pages with
resolved citations and references. The only logged warning is the already
documented caption-package warning from the legacy UCSC class.
