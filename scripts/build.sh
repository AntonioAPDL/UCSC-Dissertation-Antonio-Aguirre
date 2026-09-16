#!/usr/bin/env bash
set -euo pipefail
project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "$project_root"
mkdir -p build

if command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
    -outdir=build main.tex
else
  # A complete TeX installation may omit the latexmk Perl driver. Keep the
  # documented entry point usable with the standard engines already present.
  for command_name in pdflatex bibtex; do
    command -v "$command_name" >/dev/null 2>&1 || {
      echo "Missing required TeX command: $command_name; see README.md." >&2
      exit 1
    }
  done
  tex_args=(-interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory=build main.tex)
  pdflatex "${tex_args[@]}"
  bibtex build/main
  pdflatex "${tex_args[@]}"
  pdflatex "${tex_args[@]}"
fi
