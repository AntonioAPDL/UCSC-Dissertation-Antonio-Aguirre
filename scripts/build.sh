#!/usr/bin/env bash
set -euo pipefail
project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "$project_root"
build_dir="${THESIS_BUILD_DIR:-build}"
case "$build_dir" in
  /*|../*|*/../*|*/..)
    echo "THESIS_BUILD_DIR must be a project-relative path without '..'." >&2
    exit 1
    ;;
esac
mkdir -p "$build_dir"

if command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
    -outdir="$build_dir" main.tex
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
    -output-directory="$build_dir" main.tex)
  pdflatex "${tex_args[@]}"
  bibtex "$build_dir/main"
  pdflatex "${tex_args[@]}"
  pdflatex "${tex_args[@]}"
fi
