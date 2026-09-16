#!/usr/bin/env bash
# Recreate the immutable research-audit checkouts without touching originals.

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 /absolute/path/to/a-dedicated-audit-root" >&2
  exit 2
fi

requested_root=$1
if [[ $requested_root != /* || $requested_root == / ]]; then
  echo "The audit root must be a specific absolute path other than /." >&2
  exit 2
fi

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
thesis_root=$(cd -- "$script_dir/.." && pwd -P)
audit_root=$(realpath -m -- "$requested_root")

if [[ $audit_root == / ]]; then
  echo "The resolved audit root must not be /." >&2
  exit 2
fi

case "$audit_root/" in
  "$thesis_root/"*)
    echo "The audit root must be outside the dissertation checkout." >&2
    exit 2
    ;;
esac

mkdir -p -- "$audit_root"
audit_root=$(cd -- "$audit_root" && pwd -P)

clone_at_commit() {
  local name=$1
  local url=$2
  local commit=$3
  local destination="$audit_root/$name"

  if [[ -e $destination && ! -d $destination/.git ]]; then
    if [[ -n $(find "$destination" -mindepth 1 -maxdepth 1 -print -quit 2>/dev/null) ]]; then
      echo "Refusing non-Git, nonempty destination: $destination" >&2
      return 1
    fi
  fi

  if [[ ! -d $destination/.git ]]; then
    git clone --origin audit-origin --no-checkout -- "$url" "$destination"
    git -C "$destination" checkout --detach "$commit"
  fi

  local actual_origin
  local actual_head
  actual_origin=$(git -C "$destination" remote get-url audit-origin)
  actual_head=$(git -C "$destination" rev-parse HEAD)
  [[ $actual_origin == "$url" ]] || {
    echo "Origin mismatch in $destination" >&2
    return 1
  }
  [[ $actual_head == "$commit" ]] || {
    echo "Commit mismatch in $destination: expected $commit, found $actual_head" >&2
    return 1
  }
  git -C "$destination" diff --quiet
  git -C "$destination" diff --cached --quiet
  [[ -z $(git -C "$destination" status --porcelain) ]] || {
    echo "Audit clone is not clean: $destination" >&2
    return 1
  }
  printf '%s %s\n' "$name" "$actual_head"
}

clone_at_commit qdesn \
  https://github.com/AntonioAPDL/Article-Q-DESN---Version-2 \
  757522db0f85815244370ec92a194de132268883
clone_at_commit environmetrics \
  https://github.com/AntonioAPDL/Evironmetrics---REVISED-DOC-Corrected-2 \
  1272bfc10442a28add5a4c74ff641e9b9a8e9666
clone_at_commit rqr \
  https://github.com/AntonioAPDL/RQR-GIBBS \
  73887b9c86ef767aa1567c660718667945630aef
clone_at_commit mti-extensions \
  https://github.com/AntonioAPDL/MTI-EXTENSIONS \
  f345d946aa5a81b94795838bec58d874a0fdd0c9
clone_at_commit exdqlm-article \
  https://github.com/AntonioAPDL/exdqlm---Article \
  d5534e97db8414fd875022261d4c530eae4676e4
clone_at_commit exdqlm-package \
  https://github.com/AntonioAPDL/exdqlm \
  e51045a4324901cced27ca2aaa22569afbc8e0e6
clone_at_commit san-lorenzo-repro \
  https://github.com/AntonioAPDL/san-lorenzo-exdqlm-reproducibility \
  a8797b804271b46c62bd04dab7dba6b84a10ab7d
clone_at_commit environmetrics-corrections \
  https://github.com/AntonioAPDL/Corrections---Project-1 \
  b1ceeb610d20f8287e4ca44e146c9cfdbcda1ee6
