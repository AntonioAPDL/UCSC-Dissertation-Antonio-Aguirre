#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 /path/to/Evironmetrics----Corrected-3-audit-clone" >&2
  exit 2
fi

source_repo=$1
project_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
source_commit=c0bfccaa7cec698c016626ee30187f18a56d495c

if [[ ! -d "$source_repo/.git" ]]; then
  echo "not a Git repository: $source_repo" >&2
  exit 2
fi

git -C "$source_repo" cat-file -e "${source_commit}^{commit}"

entries=(
  "Figures/manuscript/site_context_usgs.png|figures/ch03-environ/site_context_usgs.png|eeef68672852e4a5362455147b84212ca5bd28d02f9774bb40bdc2a495dc8d8c"
  "Figures/manuscript/predictive_synthesis_2022_12_25.pdf|figures/ch03-environ/predictive_synthesis_2022_12_25.pdf|48fc5c19a82454783826f1750676c4461ec6e648f1d11fd44774dd8a76dba9eb"
  "Figures/manuscript/no_refit_quantile_reliability.png|figures/ch03-environ/no_refit_quantile_reliability.png|c0097bd2684b17565c328871d08c3b0ee7117cf2be3d5fb9833906f885e8d4e6"
  "tables/compact_publication/main_aggregate.tex|tables/ch03-environ/corrected3/main_aggregate.tex|794bd770af9e8628513f70943cd7f991535673f7905edcc793ecacc0a979f991"
  "tables/compact_publication/main_quantile_loss.tex|tables/ch03-environ/corrected3/main_quantile_loss.tex|7c1a3c228a745a4c1770eac7f3aa70b7333395b6ef750b2c4deacfbdd667a5b7"
  "tables/compact_publication/main_calibration.tex|tables/ch03-environ/corrected3/main_calibration.tex|104f62fbed21cd05724a87d7d1b73943a66469d3df8b0ded001e2d5f9da95838"
  "tables/compact_publication/si_origin_crps.tex|tables/ch03-environ/corrected3/si_origin_crps.tex|7788901838b02db4605c4bd9fc3fae8f98b4e53882df09a0de6f115e81483bb4"
  "tables/compact_publication/si_component_comparison.tex|tables/ch03-environ/corrected3/si_component_comparison.tex|e30b9dd76cfe68320f8128a4d9bd746747a8c4addd43b1db4e86f9494351e266"
  "tables/compact_publication/si_discharge_score.tex|tables/ch03-environ/corrected3/si_discharge_score.tex|cefddc0abfb2a78f058ced16ae3a28c155c158616494e12c710dbcd833d9af80"
)

temporary_dir=$(mktemp -d)
trap 'rm -rf "$temporary_dir"' EXIT

for entry in "${entries[@]}"; do
  IFS='|' read -r source_path destination expected_sha256 <<< "$entry"
  temporary_file="$temporary_dir/$(basename "$destination")"
  git -C "$source_repo" show "${source_commit}:${source_path}" > "$temporary_file"
  actual_sha256=$(sha256sum "$temporary_file" | awk '{print $1}')
  if [[ "$actual_sha256" != "$expected_sha256" ]]; then
    echo "hash mismatch for $source_path" >&2
    exit 1
  fi
  mkdir -p "$project_root/$(dirname "$destination")"
  install -m 0644 "$temporary_file" "$project_root/$destination"
  echo "$destination  $actual_sha256"
done
