#!/usr/bin/env bash
set -euo pipefail
project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "$project_root"
command -v latexmk >/dev/null || { echo 'Install a user-level TeX distribution with latexmk; see README.md.' >&2; exit 1; }
mkdir -p build
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
