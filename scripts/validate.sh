#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "$project_root"

tier="fast"
audit_root=""
while (($#)); do
  case "$1" in
    --tier)
      tier="${2:?missing value for --tier}"
      shift 2
      ;;
    --audit-root)
      audit_root="${2:?missing value for --audit-root}"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

case "$tier" in
  fast|chapter|release) ;;
  *)
    echo "--tier must be fast, chapter, or release" >&2
    exit 2
    ;;
esac

python3.11 -m unittest tests/test_validate_research_audit.py
python3.11 scripts/validate_research_audit.py
python3.11 scripts/validate_editorial_audit.py
validator=(python3.11 scripts/validate_manuscript_imports.py)
if [[ -n "$audit_root" ]]; then
  validator+=(--audit-root "$audit_root")
fi
"${validator[@]}"
git diff --check

if [[ "$tier" == "fast" ]]; then
  echo "Fast validation: PASS"
  exit 0
fi

if [[ "$tier" == "release" ]]; then
  if [[ -z "$audit_root" ]]; then
    echo "Release validation requires --audit-root for source-blob verification." >&2
    exit 2
  fi
  build_dir="build/release-$(date -u +%Y%m%dT%H%M%SZ)"
else
  build_dir="build"
fi

THESIS_BUILD_DIR="$build_dir" bash scripts/build.sh
log_path="$build_dir/main.log"
pdf_path="$build_dir/main.pdf"

if rg -n \
  'LaTeX Warning: (Citation|Reference).*undefined|There were undefined references|multiply defined|! LaTeX Error|Emergency stop|Fatal error' \
  "$log_path"; then
  echo "TeX log contains a blocking diagnostic." >&2
  exit 1
fi

underfull_count="$(rg -c 'Underfull \\hbox|Underfull \\vbox' "$log_path" || true)"
overfull_count="$(rg -c 'Overfull \\hbox|Overfull \\vbox' "$log_path" || true)"
pdfinfo "$pdf_path" | rg '^(Pages|Page size|File size|PDF version|Tagged):'
printf 'TeX diagnostics: underfull=%s overfull=%s\n' \
  "${underfull_count:-0}" "${overfull_count:-0}"
printf '%s validation: PASS (%s)\n' "$tier" "$pdf_path"
