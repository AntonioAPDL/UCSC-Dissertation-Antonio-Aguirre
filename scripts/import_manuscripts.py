#!/usr/bin/env python3.11
"""Import the four audited manuscript packets into the dissertation.

The importer reads Git blobs at the immutable commits recorded below.  It does
not inspect or modify a source working tree, execute research code, or import
data and fitted objects.  Only manuscript prose, recursively referenced TeX
display fragments, and recursively referenced display assets are copied.

Usage:
    python3.11 scripts/import_manuscripts.py --audit-root /path/to/audit/clones

The audit root must contain the five clone directories named in SOURCES.  The
path is deliberately supplied at run time so machine-local paths never enter a
tracked dissertation file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Source:
    key: str
    source_id: str
    clone_dir: str
    commit: str
    bib_path: str
    citation_prefix: str
    label_prefix: str
    claim_ids: tuple[str, ...]


SOURCES = {
    "exd": Source(
        "exd",
        "SRC-EXDQLM-ARTICLE",
        "exdqlm-article",
        "d5534e97db8414fd875022261d4c530eae4676e4",
        "references.bib",
        "exd",
        "exd",
        ("CLM-EXDQLM-001", "CON-EXDQLM-004"),
    ),
    "env": Source(
        "env",
        "SRC-ENVIRON",
        "environmetrics",
        "1272bfc10442a28add5a4c74ff641e9b9a8e9666",
        "wileyNJD-APA.bib",
        "env",
        "env",
        ("CLM-ENV-001", "ART-ENV-002", "ART-ENV-003", "CLM-ENV-004"),
    ),
    "qdesn": Source(
        "qdesn",
        "SRC-QDESN",
        "qdesn",
        "757522db0f85815244370ec92a194de132268883",
        "refs.bib",
        "qdesn",
        "qdesn",
        (
            "CLM-QDESN-001",
            "CLM-QDESN-002",
            "CLM-QDESN-003",
            "ART-QDESN-004",
            "ART-QDESN-005",
            "ART-QDESN-008",
        ),
    ),
    "rqr": Source(
        "rqr",
        "SRC-RQR",
        "rqr",
        "73887b9c86ef767aa1567c660718667945630aef",
        "refs.bib",
        "rqr",
        "rqr",
        ("CLM-RQR-001", "CLM-RQR-002", "ART-RQR-003", "CON-RQR-004"),
    ),
    "mti": Source(
        "mti",
        "SRC-MTI-EXT",
        "mti-extensions",
        "f345d946aa5a81b94795838bec58d874a0fdd0c9",
        "refs.bib",
        "mti",
        "mti",
        ("CLM-MTI-001", "CLM-MTI-002", "CON-MTI-003"),
    ),
}


CHAPTERS = {
    "ch02-exdqlm": ("chapters/02-research-a.tex", ("exd",)),
    "ch03-environ": ("chapters/03-research-b.tex", ("env",)),
    "ch04-qdesn": ("chapters/04-research-c.tex", ("qdesn",)),
    "ch05-mti": ("chapters/05-research-d.tex", ("rqr", "mti")),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_if_changed(path: Path, data: bytes) -> None:
    """Avoid needless rewrites of large display assets on network storage."""
    if path.exists() and path.read_bytes() == data:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def run_git(repo: Path, *args: str, binary: bool = False) -> bytes | str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout if binary else result.stdout.decode("utf-8")


class Importer:
    def __init__(self, audit_root: Path) -> None:
        self.audit_root = audit_root
        self.cite_maps: dict[str, dict[str, str]] = {}
        self.bibliography = ""
        self.manifests: dict[str, list[dict[str, object]]] = {
            chapter: [] for chapter in CHAPTERS
        }
        self.documents: dict[str, list[dict[str, object]]] = {
            chapter: [] for chapter in CHAPTERS
        }
        self.copied: set[tuple[str, str, str]] = set()
        self.current_chapter = ""

    def repo(self, source_key: str) -> Path:
        return self.audit_root / SOURCES[source_key].clone_dir

    def validate_sources(self) -> None:
        errors: list[str] = []
        for source in SOURCES.values():
            repo = self.repo(source.key)
            if not (repo / ".git").exists():
                errors.append(f"missing Git clone: {source.clone_dir}")
                continue
            actual = str(run_git(repo, "rev-parse", "HEAD")).strip()
            if actual != source.commit:
                errors.append(
                    f"{source.clone_dir}: expected {source.commit}, found {actual}"
                )
            run_git(repo, "cat-file", "-e", f"{source.commit}^{{commit}}")
        if errors:
            raise SystemExit("\n".join(errors))

    def blob(self, source_key: str, path: str) -> bytes:
        source = SOURCES[source_key]
        return run_git(
            self.repo(source_key), "show", f"{source.commit}:{path}", binary=True
        )  # type: ignore[return-value]

    def text(self, source_key: str, path: str) -> str:
        return self.blob(source_key, path).decode("utf-8")

    def exists(self, source_key: str, path: str) -> bool:
        source = SOURCES[source_key]
        result = subprocess.run(
            [
                "git",
                "-C",
                str(self.repo(source_key)),
                "cat-file",
                "-e",
                f"{source.commit}:{path}",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return result.returncode == 0

    @staticmethod
    def parse_bib_entries(text: str) -> list[tuple[str, str, str]]:
        entries: list[tuple[str, str, str]] = []
        cursor = 0
        while True:
            match = re.search(r"@[A-Za-z]+\s*[({]", text[cursor:])
            if not match:
                break
            start = cursor + match.start()
            opening = text[cursor + match.end() - 1]
            closing = "}" if opening == "{" else ")"
            depth = 0
            quote = False
            escape = False
            end = None
            for index in range(cursor + match.end() - 1, len(text)):
                char = text[index]
                if escape:
                    escape = False
                    continue
                if char == "\\":
                    escape = True
                    continue
                if char == '"':
                    quote = not quote
                if quote:
                    continue
                if char == opening:
                    depth += 1
                elif char == closing:
                    depth -= 1
                    if depth == 0:
                        end = index + 1
                        break
            if end is None:
                raise ValueError(f"unbalanced BibTeX entry near byte {start}")
            raw = text[start:end].strip()
            kind_match = re.match(r"@([A-Za-z]+)\s*[({]", raw)
            assert kind_match
            kind = kind_match.group(1).lower()
            if kind in {"preamble", "string", "comment"}:
                entries.append((kind, "", raw))
            else:
                key_match = re.match(r"@[A-Za-z]+\s*[({]\s*([^,\s]+)\s*,", raw)
                if not key_match:
                    raise ValueError(f"cannot parse BibTeX key in {raw[:80]!r}")
                entries.append((kind, key_match.group(1), raw))
            cursor = end
        return entries

    @staticmethod
    def bib_field(raw: str, field: str) -> str:
        pattern = re.compile(
            rf"(?is)(?:^|,)\s*{re.escape(field)}\s*=\s*(\{{(?:[^{{}}]|\{{[^{{}}]*\}})*\}}|\"[^\"]*\"|[^,\n]+)"
        )
        match = pattern.search(raw)
        return match.group(1).strip(" {}\"\t\r\n") if match else ""

    @staticmethod
    def normalized(value: str) -> str:
        value = re.sub(r"\\[A-Za-z]+\s*", "", value)
        return re.sub(r"[^a-z0-9]+", "", value.lower())

    def build_bibliography(self) -> None:
        existing = (PROJECT_ROOT / "references.bib").read_text(encoding="utf-8")
        # Keep only the two administrative starter records.  Imported records
        # from a previous run are regenerated below, making the importer
        # idempotent instead of inventing ``-2`` citation keys on every run.
        starter_entries = [
            entry
            for entry in self.parse_bib_entries(existing)
            if entry[1].lower() in {"ucscguide2021", "ucsclibrary2026"}
        ]
        output = [raw for _, _, raw in starter_entries]
        fingerprints: dict[str, str] = {}
        emitted_keys = {key.lower() for _, key, _ in starter_entries if key}
        preamble_seen = any(kind == "preamble" for kind, _, _ in starter_entries)

        for source_key in SOURCES:
            source = SOURCES[source_key]
            mapping: dict[str, str] = {}
            for kind, old_key, raw in self.parse_bib_entries(
                self.text(source_key, source.bib_path)
            ):
                if not old_key:
                    if kind == "preamble" and not preamble_seen:
                        output.append(raw)
                        preamble_seen = True
                    continue
                doi = self.normalized(self.bib_field(raw, "doi"))
                title = self.normalized(self.bib_field(raw, "title"))
                if doi:
                    fingerprint = f"doi:{doi}"
                elif len(title) >= 12:
                    fingerprint = f"title:{title}"
                else:
                    fingerprint = f"key:{old_key.lower()}"
                canonical = fingerprints.get(fingerprint)
                if canonical is None:
                    candidate = f"{source.citation_prefix}-{old_key}"
                    suffix = 2
                    while candidate.lower() in emitted_keys:
                        candidate = f"{source.citation_prefix}-{old_key}-{suffix}"
                        suffix += 1
                    canonical = candidate
                    fingerprints[fingerprint] = canonical
                    emitted_keys.add(canonical.lower())
                    raw = re.sub(
                        r"(@[A-Za-z]+\s*[({]\s*)[^,\s]+(\s*,)",
                        rf"\g<1>{canonical}\g<2>",
                        raw,
                        count=1,
                    )
                    output.append(raw)
                mapping[old_key] = canonical
                mapping[old_key.lower()] = canonical
            self.cite_maps[source_key] = mapping
        self.bibliography = (
            "% Generated by scripts/import_manuscripts.py from the fixed audit snapshots.\n"
            "% Do not edit imported records without updating their source mapping.\n\n"
            + "\n\n".join(output)
            + "\n"
        )
        self.bibliography = re.sub(r"[ \t]+(?=\n)", "", self.bibliography)

    @staticmethod
    def macro_argument(text: str, command: str) -> str:
        start_match = re.search(re.escape(command) + r"(?:\[[^\]]*\])?\s*\{", text)
        if not start_match:
            return ""
        start = start_match.end() - 1
        depth = 0
        for index in range(start, len(text)):
            if text[index] == "{" and (index == 0 or text[index - 1] != "\\"):
                depth += 1
            elif text[index] == "}" and (index == 0 or text[index - 1] != "\\"):
                depth -= 1
                if depth == 0:
                    return text[start + 1 : index]
        return ""

    @staticmethod
    def environment(text: str, name: str) -> str:
        match = re.search(
            rf"\\begin\{{{re.escape(name)}\}}(.*?)\\end\{{{re.escape(name)}\}}",
            text,
            flags=re.S,
        )
        return match.group(1).strip() if match else ""

    @staticmethod
    def section_map(text: str) -> dict[str, str]:
        body_match = re.search(r"\\begin\{document\}(.*)", text, flags=re.S)
        body = body_match.group(1) if body_match else text
        body = re.split(r"^\\bibliograph(?:y|ystyle)\b", body, maxsplit=1, flags=re.M)[0]
        body = re.split(r"^\\end\{document\}", body, maxsplit=1, flags=re.M)[0]
        matches = list(re.finditer(r"(?m)^\\section\*?\{([^}\n]+)\}", body))
        sections: dict[str, str] = {}
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
            sections[match.group(1).strip()] = body[match.start() : end].strip()
        return sections

    @staticmethod
    def split_subsections(section: str) -> tuple[str, dict[str, str]]:
        matches = list(re.finditer(r"(?m)^\\subsection\*?\{([^}\n]+)\}", section))
        if not matches:
            return section, {}
        lead = section[: matches[0].start()].strip()
        chunks: dict[str, str] = {}
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
            chunks[match.group(1).strip()] = section[match.start() : end].strip()
        return lead, chunks

    @staticmethod
    def pick(sections: dict[str, str], title: str) -> str:
        if title not in sections:
            choices = "\n".join(f"  - {key}" for key in sections)
            raise KeyError(f"missing section {title!r}; available:\n{choices}")
        return sections[title]

    @staticmethod
    def demote(text: str, levels: int = 1) -> str:
        commands = ["section", "subsection", "subsubsection", "paragraph"]
        for _ in range(levels):
            for index in range(len(commands) - 2, -1, -1):
                text = re.sub(
                    rf"(?m)^\\{commands[index]}(\*?)\{{",
                    rf"\\{commands[index + 1]}\1{{",
                    text,
                )
        return text

    def citation_rewrite(self, text: str, source_key: str) -> str:
        mapping = self.cite_maps[source_key]

        def replace(match: re.Match[str]) -> str:
            keys = []
            for key in match.group(2).split(","):
                stripped = key.strip()
                keys.append(mapping.get(stripped, mapping.get(stripped.lower(), stripped)))
            return f"{match.group(1)}{{{','.join(keys)}}}"

        return re.sub(
            r"(\\(?:cite|citep|citet|citealp|citeauthor|citeyear|citeyearpar|nocite)(?:\[[^\]]*\])?(?:\[[^\]]*\])?)\{([^}]+)\}",
            replace,
            text,
        )

    @staticmethod
    def label_rewrite(text: str, prefix: str) -> str:
        return re.sub(
            r"\\(label|ref|eqref|pageref|autoref)\{([^}:][^}]*)\}",
            lambda match: f"\\{match.group(1)}{{{prefix}:{match.group(2)}}}",
            text,
        )

    @staticmethod
    def cleanup(text: str, source_key: str) -> str:
        text = re.sub(r"\\begin\{CodeChunk\}.*?\\end\{CodeChunk\}", "", text, flags=re.S)
        text = re.sub(r"\\begin\{Code(?:Input|Output)\}.*?\\end\{Code(?:Input|Output)\}", "", text, flags=re.S)
        text = re.sub(r"(?m)^\\(?:appendix|exdqlmAppendixSetup)\s*$", "", text)
        text = re.sub(r"(?m)^\\(?:clearpage|newpage)\s*$", "", text)
        text = text.replace("\\begin{figure*}", "\\begin{figure}")
        text = text.replace("\\end{figure*}", "\\end{figure}")
        text = text.replace("\\begin{table*}", "\\begin{table}")
        text = text.replace("\\end{table*}", "\\end{table}")
        text = re.sub(r"S\[table-format=[^\]]+\]", "r", text)
        text = re.sub(r"\\multirow\{\d+\}\{\*\}\{([^{}]*)\}", r"\1", text)
        text = re.sub(r"\\includegraphics\[width=450pt\]", r"\\includegraphics[width=\\textwidth]", text)
        text = text.replace("Appendix~\\ref", "Section~\\ref")
        text = text.replace("appendix uses", "integrated algorithms use")
        text = text.replace("The appendix uses", "The integrated section uses")
        text = text.replace("the appendix uses", "the integrated section uses")
        text = text.replace("appendix algorithms", "integrated algorithms")
        text = text.replace("The supplement", "The integrated material")
        text = text.replace("This supplement", "This integrated material")
        text = text.replace("this supplement", "this integrated material")
        text = re.sub(r"\\small\b", r"\\scriptsize", text)
        if source_key == "exd":
            text = text.replace(
                "Appendices A--F collect",
                "the integrated technical sections collect",
            )
            text = text.replace(
                "provided in Appendices A--F",
                "provided in the integrated technical sections below",
            )
            text = text.replace(
                "The appendix aims",
                "The integrated technical material aims",
            )
            text = text.replace(
                "Appendix notation follows",
                "The notation below follows",
            )
            text = text.replace(
                "documented in the appendices",
                "documented in the integrated technical sections",
            )
            text = text.replace(
                "The main text, appendices, and replication materials have separate roles: the main text describes the user-facing workflow, the appendices record",
                "The user-facing sections, integrated technical material, and replication sources have separate roles: the user-facing sections describe the workflow, the integrated technical material records",
            )
            text = text.replace(
                r"\caption{Transfer-function inputs for \code{exdqlmTransferLDVB()} and \code{exdqlmTransferMCMC()}.",
                r"\caption[Transfer-function inputs]{Transfer-function inputs for \code{exdqlmTransferLDVB()} and \code{exdqlmTransferMCMC()}.",
            )
            text = text.replace(
                r"\caption{Example 3: Big Tree water flow. Package diagnostics from",
                r"\caption[Big Tree water-flow diagnostics]{Example 3: Big Tree water flow. Package diagnostics from",
            )
            text = text.replace(
                """\\begin{equation}
\\elbo(q)=
\\elbo_{\\mathrm{like}}+\\elbo_{\\mathrm{Gaussian}}
+\\elbo_v+\\elbo_s+\\elbo_{\\sigma\\gamma}
+H(q_{\\mathrm{Gaussian}})
+\\sum H\\{q(v)\\}+\\sum H\\{q(s)\\}+H\\{q_{\\sigma\\gamma}(\\sigma,\\gamma)\\}.
\\label{eq:dyn_exdqlm_elbo}
\\end{equation}""",
                """\\begin{align}
\\elbo(q)
&=\\elbo_{\\mathrm{like}}+\\elbo_{\\mathrm{Gaussian}}
+\\elbo_v+\\elbo_s+\\elbo_{\\sigma\\gamma}\\notag\\\\
&\\quad+H(q_{\\mathrm{Gaussian}})
+\\sum H\\{q(v)\\}+\\sum H\\{q(s)\\}
+H\\{q_{\\sigma\\gamma}(\\sigma,\\gamma)\\}.
\\label{eq:dyn_exdqlm_elbo}
\\end{align}""",
            )
            text = re.sub(
                r"(Here, \$p = p\(p_0,\\gamma\).*?Introducing the latent variables .*? gives the hierarchical representation:)",
                r"\\begin{sloppypar}\1\\end{sloppypar}",
                text,
                flags=re.S,
            )
        if source_key == "env":
            text = text.replace("Appendix Tables~", "Tables~")
            text = text.replace("Appendix Figures~", "Figures~")
            text = text.replace("Appendix Figure~", "Figure~")
            text = text.replace(
                r"\section{Supplementary Source-Specific Shape and Scale Parameters}",
                r"\section{Additional Source-Specific Shape and Scale Parameters}",
            )
            text = text.replace(
                "For completeness, this appendix reports",
                "For completeness, this section reports",
            )
            text = re.sub(
                r"\\begin\{alignat\}(\{[^}]+\})",
                r"\\begingroup\\scriptsize\\begin{alignat}\1",
                text,
            )
            text = text.replace("\\end{alignat}", "\\end{alignat}\\endgroup")

            def compact_display(match: re.Match[str]) -> str:
                body = match.group(1)
                if "boldsymbol{\\Lambda}_t" in body:
                    return (
                        "\\[\\resizebox{\\textwidth}{!}{$\\displaystyle "
                        + body
                        + "$}\\]"
                    )
                if "BlockDiag" in body or "F}_t^{\\text{trans}" in body:
                    return "\\begingroup\\scriptsize\\[" + body + "\\]\\endgroup"
                return match.group(0)

            text = re.sub(r"\\\[(.*?)\\\]", compact_display, text, flags=re.S)
            text = text.replace(
                r"\begin{tabular*}{\textwidth}",
                "\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}",
            )
            text = text.replace(r"\end{tabular*}", "\\end{tabular}}")
            text = re.sub(
                r"\\begin\{algorithm\}\s*\\caption\{([^{}]+)\}\s*\\label\{([^}]+)\}",
                r"\\begin{algorithmblock}{\1}\n\\label{\2}",
                text,
            )
            text = text.replace("\\end{algorithm}", "\\end{algorithmblock}")
        if source_key == "qdesn":
            text = re.sub(
                r"\bthe\s+supplement\b",
                "the integrated technical material",
                text,
                flags=re.I,
            )
            text = text.replace(
                "in the supplement",
                "in the integrated technical material",
            )
            text = text.replace(
                "collected in the supplement",
                "collected in the integrated technical material",
            )
            text = text.replace(
                "described earlier in the supplement",
                "described earlier in this chapter",
            )
            text = text.replace(
                "described in the supplement",
                "described in the integrated technical material",
            )
            text = text.replace(
                "the supplement records",
                "the integrated technical material records",
            )
            text = text.replace(
                "the supplement reports",
                "the integrated technical material reports",
            )
            text = text.replace(
                "the supplement displays",
                "the integrated technical material displays",
            )
            text = text.replace(
                "without repeating the supplementary forecast tables",
                "without repeating the additional forecast tables",
            )
            text = text.replace(
                r"\subsection{Numerical Qualification and Supplementary Results}",
                r"\subsection{Numerical Qualification and Additional Results}",
            )
            text = text.replace(
                r"\input{figures/quantile_initialization/quantile_initialization_picture.tex}",
                r"\resizebox{\textwidth}{!}{\input{figures/quantile_initialization/quantile_initialization_picture.tex}}",
            )
            text = re.sub(
                r"(\\begin\{equation\}\s*\\begin\{alignedat\}.*?\\end\{alignedat\}.*?\\end\{equation\})",
                r"\\begingroup\\scriptsize\1\\endgroup",
                text,
                flags=re.S,
            )
            text = re.sub(
                r"(\\begin\{align\}.*?\\end\{align\})",
                r"\\begingroup\\scriptsize\1\\endgroup",
                text,
                flags=re.S,
            )

            def compact_qdesn_display(match: re.Match[str]) -> str:
                body = match.group(1)
                if (
                    "a_\\sigma^\\star" in body
                    or "a_\\sigma^\star" in body
                    or "m_{\\varepsilon,b}" in body
                ):
                    return "\\begingroup\\scriptsize\\[" + body + "\\]\\endgroup"
                return match.group(0)

            text = re.sub(r"\\\[(.*?)\\\]", compact_qdesn_display, text, flags=re.S)
            text = re.sub(
                r"(\\begin\{equation\}(?:(?!\\end\{equation\}).)*?\\label\{eq:supp_glofas_weighted_augmented_likelihood\}(?:(?!\\end\{equation\}).)*?\\end\{equation\})",
                r"\\begingroup\\scriptsize\1\\endgroup",
                text,
                flags=re.S,
            )
            text = text.replace(
                r"\section{Joint Quantile-Vector Regression with Regularized-Horseshoe Shrinkage}",
                r"\section[Joint Quantile-Vector Regression with Regularized-Horseshoe Shrinkage]{Joint Quantile-Vector Regression with\\Regularized-Horseshoe Shrinkage}",
            )
            text = re.sub(
                r"(Conditional on the reservoir features, the ridge and Nishimura--Suchard.*?nonconjugate update\.)",
                r"\\begin{sloppypar}\1\\end{sloppypar}",
                text,
                count=1,
                flags=re.S,
            )
        if source_key == "rqr":
            text = text.replace(
                "the supplement gives",
                "the integrated technical material gives",
            )
            text = text.replace(
                "the supplement counterpart",
                "the integrated counterpart",
            )
            text = text.replace(
                "the supplement records",
                "the integrated validation material records",
            )
            text = text.replace(
                "the supplement keeps",
                "the integrated tables retain",
            )
            text = text.replace(
                r"\paragraph{Supplementary extensions.}",
                r"\paragraph{Additional extensions.}",
            )
            text = text.replace(
                r"\caption{\textbf{Supplementary weight-RSD application.}",
                r"\caption{\textbf{Additional weight-RSD application.}",
            )
            text = text.replace(
                r"p{0.24\textwidth}rr>{\raggedright\arraybackslash}p{0.20\textwidth}",
                r"p{0.195\textwidth}rr>{\raggedright\arraybackslash}p{0.165\textwidth}",
            )
            text = text.replace(
                r"\begin{tabular}{@{}llrrrrrr@{}}",
                r"\setlength{\tabcolsep}{2pt}\begin{tabular}{@{}llrrrrrr@{}}",
            )
            text = text.replace(
                "Then \\(M_{c,x}\\) is strictly increasing and there is a unique index \\(u_c(x)\\)\nsuch that \\(M_{c,x}\\{u_c(x)\\}=\\mu_x\\). The nondegenerate unrestricted MPI\nstationary interval is therefore",
                "Then \\(M_{c,x}\\) is strictly increasing. There is a unique index \\(u_c(x)\\)\nsatisfying\n\\[\nM_{c,x}\\{u_c(x)\\}=\\mu_x.\n\\]\nThe nondegenerate unrestricted MPI stationary interval is therefore",
            )
        if source_key == "mti":
            text = text.replace(
                "A pseudo-asymmetric-Laplace normal-exponential representation gives",
                "The pseudo-AL normal--exponential representation gives",
            )
        # The Environmetrics source uses algorithmicx-style mixed-case command
        # names, while muscat provides the older algorithmic package.  Their
        # semantics are identical for the commands used in this manuscript.
        for mixed, upper in (
            ("Statex", "STATE"),
            ("State", "STATE"),
            ("EndWhile", "ENDWHILE"),
            ("While", "WHILE"),
            ("EndFor", "ENDFOR"),
            ("For", "FOR"),
            ("EndIf", "ENDIF"),
            ("Else", "ELSE"),
            ("If", "IF"),
        ):
            text = re.sub(rf"\\{mixed}\b", rf"\\{upper}", text)
        if source_key in {"qdesn", "rqr", "mti"}:
            text = text.replace("\\begin{suppalgorithm}", "\\begin{algorithmblock}")
            text = text.replace("\\end{suppalgorithm}", "\\end{algorithmblock}")
        if source_key == "rqr":
            text = re.sub(
                r"(\\begin\{algorithmblock\}\{[^}]+\})",
                r"\1\n\\begin{enumerate}[leftmargin=2.2em,itemsep=0.3em,parsep=0pt]",
                text,
            )
            text = text.replace(
                "\\end{algorithmblock}",
                "\\end{enumerate}\n\\end{algorithmblock}",
            )
        if source_key == "exd":
            text = text.replace("\\begin{appalgorithm}", "\\begin{algorithmblock}")
            text = text.replace("\\end{appalgorithm}", "\\end{algorithmblock}")
        text = re.sub(r"[ \t]+(?=\n)", "", text)
        return text.strip() + "\n"

    def source_destination(self, source_key: str, source_path: str) -> str:
        chapter = self.current_chapter
        if source_path.startswith("tables/"):
            return f"tables/{chapter}/{source_path[len('tables/'):]}"
        if source_path.startswith("figures/"):
            return f"figures/{chapter}/{source_path[len('figures/'):]}"
        if source_path.startswith("Figures/"):
            return f"figures/{chapter}/{Path(source_path).name}"
        return f"figures/{chapter}/{Path(source_path).name}"

    def record(
        self,
        source_key: str,
        source_path: str,
        destination: str,
        source_data: bytes,
        destination_data: bytes,
        material_type: str,
        handling: str,
    ) -> None:
        source = SOURCES[source_key]
        item = {
            "source_id": source.source_id,
            "commit": source.commit,
            "source_path": source_path,
            "locator": source_path,
            "material_type": material_type,
            "destination": destination,
            "handling": handling,
            "source_sha256": sha256(source_data),
            "destination_sha256": sha256(destination_data),
            "claim_ids": list(source.claim_ids),
            "rights_status": "UNVERIFIED_LOCAL_ONLY",
            "validation": "exact source blob and destination hash recorded; dissertation build checked separately",
        }
        self.manifests[self.current_chapter].append(item)

    def resolve_asset(self, source_key: str, path: str) -> str:
        path = path.strip()
        if self.exists(source_key, path):
            return path
        candidates: list[str] = []
        if source_key == "exd":
            candidates.extend([f"figures/{path}", f"analysis/manuscript/outputs/figures/{path}"])
        elif source_key == "env":
            candidates.extend(
                [
                    f"Figures/manuscript/{path}",
                    f"Figures/appendix_cutoff_panels/{path}",
                    f"Figures/multivariate_synthesis_by_cutoff/{path}",
                ]
            )
        if not Path(path).suffix:
            extended: list[str] = []
            for candidate in [path, *candidates]:
                extended.extend(candidate + ext for ext in (".pdf", ".png", ".jpg", ".jpeg"))
            candidates.extend(extended)
        for candidate in candidates:
            if self.exists(source_key, candidate):
                return candidate
        raise FileNotFoundError(f"{source_key}: cannot resolve referenced asset {path!r}")

    def copy_dependency(self, source_key: str, source_path: str) -> str:
        source_path = self.resolve_asset(source_key, source_path)
        destination = self.source_destination(source_key, source_path)
        marker = (self.current_chapter, source_key, source_path)
        if marker in self.copied:
            return destination
        self.copied.add(marker)
        source_data = self.blob(source_key, source_path)
        if source_path.endswith(".tex"):
            imported = self.transform(source_data.decode("utf-8"), source_key)
            destination_data = imported.encode("utf-8")
            material_type = "display_tex_fragment"
            handling = "transformed paths, citations, and cross-references; no computation imported"
        else:
            destination_data = source_data
            material_type = "figure_asset"
            handling = "byte-for-byte copy of a manuscript-referenced display asset"
        target = PROJECT_ROOT / destination
        write_if_changed(target, destination_data)
        self.record(
            source_key,
            source_path,
            destination,
            source_data,
            destination_data,
            material_type,
            handling,
        )
        return destination

    def rewrite_dependencies(self, text: str, source_key: str) -> str:
        source = SOURCES[source_key]

        def input_replace(match: re.Match[str]) -> str:
            argument = match.group(1).strip()
            if argument.startswith("\\"):
                return match.group(0)
            candidate = argument if Path(argument).suffix else f"{argument}.tex"
            if not self.exists(source_key, candidate):
                return match.group(0)
            destination = self.copy_dependency(source_key, candidate)
            return f"\\input{{{destination}}}"

        text = re.sub(r"\\input\{([^}]+)\}", input_replace, text)

        def graphics_replace(match: re.Match[str]) -> str:
            options = match.group(1) or ""
            argument = match.group(2).strip()
            if argument.startswith("\\"):
                return match.group(0)
            source_path = self.resolve_asset(source_key, argument)
            destination = self.copy_dependency(source_key, source_path)
            return f"\\includegraphics{options}{{{destination}}}"

        text = re.sub(r"\\includegraphics(\[[^\]]*\])?\{([^}]+)\}", graphics_replace, text)

        # Alias files store paths in macro bodies rather than direct input or
        # includegraphics calls.  Copy those targets and make their paths local.
        path_pattern = re.compile(
            r"(?<![A-Za-z0-9_-])((?:tables|figures)/[A-Za-z0-9_./-]+\.(?:tex|pdf|png|jpg|jpeg))"
        )

        def path_replace(match: re.Match[str]) -> str:
            path = match.group(1)
            if path.startswith(f"tables/{self.current_chapter}/") or path.startswith(
                f"figures/{self.current_chapter}/"
            ):
                return path
            if not self.exists(source_key, path):
                return path
            return self.copy_dependency(source_key, path)

        return path_pattern.sub(path_replace, text)

    def transform(self, text: str, source_key: str) -> str:
        text = self.cleanup(text, source_key)
        text = self.citation_rewrite(text, source_key)
        text = self.label_rewrite(text, SOURCES[source_key].label_prefix)
        text = self.rewrite_dependencies(text, source_key)
        return text

    def chapter_header(self, title: str, label: str, note: str, abstract: str) -> str:
        return (
            f"\\chapter{{{title}}}\n"
            f"\\label{{{label}}}\n\n"
            "\\begin{singlespace}\n"
            f"\\noindent\\textit{{{note}}}\n"
            "\\end{singlespace}\n\n"
            "\\section{Chapter overview}\n"
            f"{abstract.strip()}\n"
        )

    def write_chapter(
        self,
        chapter: str,
        source_paths: Iterable[tuple[str, str]],
        text: str,
    ) -> None:
        destination = CHAPTERS[chapter][0]
        destination_data = text.strip().encode("utf-8") + b"\n"
        write_if_changed(PROJECT_ROOT / destination, destination_data)
        for source_key, source_path in source_paths:
            source_data = self.blob(source_key, source_path)
            self.record(
                source_key,
                source_path,
                destination,
                source_data,
                destination_data,
                "manuscript_prose_and_equations",
                "journal wrapper removed; article spine retained; supporting sections integrated topically",
            )

    def record_document_disposition(
        self,
        source_key: str,
        source_path: str,
        sections: dict[str, str],
        included: Iterable[str],
        *,
        partial: dict[str, Iterable[str]] | None = None,
        omitted_reasons: dict[str, str] | None = None,
        note: str,
    ) -> None:
        """Record the fate of every top-level manuscript section."""
        source = SOURCES[source_key]
        included_set = set(included)
        partial = partial or {}
        omitted_reasons = omitted_reasons or {}
        dispositions: list[dict[str, object]] = []
        for title in sections:
            if title in partial:
                dispositions.append(
                    {
                        "section": title,
                        "disposition": "integrated_selected_subsections",
                        "included_subsections": list(partial[title]),
                    }
                )
            elif title in included_set:
                dispositions.append(
                    {"section": title, "disposition": "integrated"}
                )
            else:
                dispositions.append(
                    {
                        "section": title,
                        "disposition": "omitted",
                        "reason": omitted_reasons.get(
                            title,
                            "source navigation or prefatory material duplicated by the integrated chapter",
                        ),
                    }
                )
        self.documents[self.current_chapter].append(
            {
                "source_id": source.source_id,
                "commit": source.commit,
                "source_path": source_path,
                "source_sha256": sha256(self.blob(source_key, source_path)),
                "rights_status": "UNVERIFIED_LOCAL_ONLY",
                "integration_note": note,
                "section_dispositions": dispositions,
            }
        )

    def build_ch02(self) -> None:
        self.current_chapter = "ch02-exdqlm"
        path = "exdqlm-jss.tex"
        raw = self.text("exd", path)
        sections = self.section_map(raw)
        abstract = self.macro_argument(raw, r"\Abstract")
        order = [
            "Introduction",
            "Technical overview and notation",
            "Extended dynamic quantile linear models",
            "Posterior targets and model blocks",
            "LDVB scale--skewness implementation for exAL models",
            "Static regression with the Nishimura--Suchard regularized horseshoe",
            "Forecasting, diagnostics, and posterior-predictive synthesis",
            "Package design and implementation",
            "Nonconjugate VB and backend notes",
            "Examples",
            "Conclusion",
        ]
        self.record_document_disposition(
            "exd",
            path,
            sections,
            order,
            note="All scientific sections integrated; journal wrapper and article front/back matter removed.",
        )
        content = self.chapter_header(
            r"Computational infrastructure for flexible dynamic quantile models",
            "ch:research-a",
            "This chapter is based on joint work by Antonio de Leon, Raquel Barata, Raquel Prado, and Bruno Sans\'o. The audited manuscript is used as the initial chapter baseline. Methodological foundations inherited from earlier exAL and exDQLM work remain attributed in the text; candidate-specific role allocation remains to be confirmed.",
            abstract,
        )
        content += "\n\n".join(self.pick(sections, title) for title in order)
        content = self.transform(content, "exd")
        content = content.replace(r"\label{exd:ch:research-a}", r"\label{ch:research-a}", 1)
        self.write_chapter(self.current_chapter, [("exd", path)], content)

    def build_ch03(self) -> None:
        self.current_chapter = "ch03-environ"
        path = "wileyNJD-APA.tex"
        raw = self.text("env", path)
        sections = self.section_map(raw)
        abstract = self.macro_argument(raw, r"\abstract")
        _, support = self.split_subsections(
            self.pick(sections, "Supplementary Parameter Summaries and Illustrations")
        )
        env_sections = [
            "INTRODUCTION",
            "METHODOLOGY",
            "Markov Chain Monte Carlo Algorithms",
            "Variational Bayes Algorithms",
            "FORECASTING THE SAN LORENZO RIVER FLOW",
            "FORECAST VALIDATION RESULTS",
            "INTERPRETATION OF THE SELECTED SPECIFICATION",
            "Conclusions",
        ]
        support_sections = [
            "Component-Removal Sensitivity Analysis",
            "Supplementary Source-Specific Shape and Scale Parameters",
            "Univariate Transfer-Active Predictive Synthesis",
            "Additional Cutoff-Specific Predictive Synthesis Panels",
        ]
        boilerplate_reason = {
            title: "article submission/availability boilerplate retained in the source repository, not repeated in the chapter body"
            for title in (
                "Acknowledgments",
                "Funding Statement",
                "Conflict of Interest Statement",
                "Data Availability Statement",
                "Code availability",
            )
        }
        self.record_document_disposition(
            "env",
            path,
            sections,
            env_sections,
            partial={
                "Supplementary Parameter Summaries and Illustrations": support_sections
            },
            omitted_reasons=boilerplate_reason,
            note="The article spine, algorithms, and all four supporting-result subsections are integrated by topic.",
        )

        def promote(chunk: str) -> str:
            return re.sub(r"(?m)^\\subsection(\*?)\{", r"\\section\1{", chunk, count=1)

        pieces = [
            self.pick(sections, "INTRODUCTION"),
            self.pick(sections, "METHODOLOGY"),
            self.pick(sections, "Markov Chain Monte Carlo Algorithms"),
            self.pick(sections, "Variational Bayes Algorithms"),
            self.pick(sections, "FORECASTING THE SAN LORENZO RIVER FLOW"),
            self.pick(sections, "FORECAST VALIDATION RESULTS"),
            promote(support[support_sections[0]]),
            self.pick(sections, "INTERPRETATION OF THE SELECTED SPECIFICATION"),
            promote(support[support_sections[1]]),
            promote(support[support_sections[2]]),
            promote(support[support_sections[3]]),
            self.pick(sections, "Conclusions"),
        ]
        content = self.chapter_header(
            "Bayesian quantile-based correction and synthesis of hydrologic products",
            "ch:research-b",
            "This chapter is based on joint work by Antonio de Leon, Raquel Prado, and Bruno Sans\'o. The revised audited manuscript supplies the chapter spine. Its supporting algorithms, sensitivity analyses, parameter summaries, and additional forecast-origin panels are integrated next to the corresponding methods and results.",
            abstract,
        )
        content += "\n\n".join(pieces)
        content = self.transform(content, "env")
        content = content.replace(r"\label{env:ch:research-b}", r"\label{ch:research-b}", 1)
        self.write_chapter(self.current_chapter, [("env", path)], content)

    def build_ch04(self) -> None:
        self.current_chapter = "ch04-qdesn"
        main_path = "main.tex"
        supp_path = "qdesn-supplement.tex"
        gauss_path = "gaussian_desn_scaled_ridge_supplement.tex"
        main_raw = self.text("qdesn", main_path)
        supp_raw = self.text("qdesn", supp_path)
        gauss_raw = self.text("qdesn", gauss_path)
        main = self.section_map(main_raw)
        supp = self.section_map(supp_raw)
        gauss = self.section_map(gauss_raw)
        _, result_subsections = self.split_subsections(
            self.pick(supp, "Supplementary Simulation and Application Tables")
        )
        single_results = "\n\n".join(
            result_subsections[title]
            for title in (
                "Single-Quantile Posterior Metric Summaries",
                "Single-Quantile Computation and Diagnostics",
                "Single-Quantile Five-Chain Point-Path Sensitivity",
                "Joint Multi-Quantile MCMC Evaluation Details",
            )
        )
        pricefm_results = result_subsections["Additional PriceFM Results"]
        gaussian_order = [
            "Scope and Relation to Q--DESN",
            "Fixed DESN Design and Notation",
            "Distributional Conventions",
            "Exact Scaled-Ridge Gaussian DESN",
            "Posterior Predictive Distributions",
            "Exact Log Marginal Likelihood",
            "Exact Direct Posterior Sampler",
            "Use as Initialization for AL and exAL Q--DESN",
            "Omitted Variants and Why They Are Not Main Derivations",
            "Implementation Notes",
            "Validation and Consistency Checks",
        ]
        main_order = [
            "Introduction",
            "Fixed-Feature Bayesian Quantile Models",
            "Posterior Computation",
            "Forecasting, Scoring, and Model Selection",
            "Simulation Studies",
            "Application: GloFAS Retrospective Streamflow Quantile Forecasting",
            "Application: Region-Frozen PriceFM Comparison",
            "Discussion",
        ]
        supp_order = [
            "Reservoir Specification, Selection, and Diagnostics",
            "Distributional Conventions",
            "DESN Feature Map and Fixed-Design Quantile Regression",
            "Q--DESN Working Likelihoods, Priors, and Augmented Posterior",
            "MCMC Full Conditionals",
            "Variational Bayes and Laplace--Delta Approximation",
            "ELBO Monitoring",
            "Joint Quantile-Vector Regression with Regularized-Horseshoe Shrinkage",
            "Multi-Step Quantile Forecasting and Monotone Rearrangement",
            "Supplementary Simulation and Application Tables",
            "GloFAS Latent-Path Ensemble-Likelihood Model with DESN Features",
        ]
        self.record_document_disposition(
            "qdesn",
            main_path,
            main,
            main_order,
            note="All main scientific sections integrated; article wrapper removed.",
        )
        self.record_document_disposition(
            "qdesn",
            supp_path,
            supp,
            supp_order,
            omitted_reasons={
                "Purpose and Relation to the Main Article": "supplement navigation duplicated by the chapter overview and topical integration"
            },
            note="All technical and empirical support sections integrated topically; only supplement-navigation prose omitted.",
        )
        self.record_document_disposition(
            "qdesn",
            gauss_path,
            gauss,
            gaussian_order,
            note="All Gaussian-baseline and initialization sections integrated before Q--DESN computation.",
        )
        pieces = [
            r"\input{tables/glofas_application_current_outputs.tex}",
            r"\input{tables/pricefm_full_current_outputs.tex}",
            self.pick(main, "Introduction"),
            r"\input{figures/quantile_initialization/quantile_initialization_styles.tex}",
            self.pick(supp, "Reservoir Specification, Selection, and Diagnostics"),
            *[
                self.label_rewrite(self.pick(gauss, title), "gauss")
                for title in gaussian_order
            ],
            self.pick(main, "Fixed-Feature Bayesian Quantile Models"),
            self.pick(supp, "Distributional Conventions"),
            self.pick(supp, "DESN Feature Map and Fixed-Design Quantile Regression"),
            self.pick(supp, "Q--DESN Working Likelihoods, Priors, and Augmented Posterior"),
            self.pick(main, "Posterior Computation"),
            self.pick(supp, "MCMC Full Conditionals"),
            self.pick(supp, "Variational Bayes and Laplace--Delta Approximation"),
            self.pick(supp, "ELBO Monitoring"),
            self.pick(supp, "Joint Quantile-Vector Regression with Regularized-Horseshoe Shrinkage"),
            self.pick(main, "Forecasting, Scoring, and Model Selection"),
            self.pick(supp, "Multi-Step Quantile Forecasting and Monotone Rearrangement"),
            self.pick(main, "Simulation Studies"),
            r"\section{Additional simulation evidence}" + "\n" + single_results,
            self.pick(main, "Application: GloFAS Retrospective Streamflow Quantile Forecasting"),
            self.pick(supp, "GloFAS Latent-Path Ensemble-Likelihood Model with DESN Features"),
            self.pick(main, "Application: Region-Frozen PriceFM Comparison"),
            r"\section{Additional PriceFM evidence}" + "\n" + pricefm_results,
            self.pick(main, "Discussion"),
        ]
        content = self.chapter_header(
            "Bayesian quantile deep echo state networks for nonlinear time series",
            "ch:research-c",
            "This chapter is based on joint work by Antonio de Leon, Raquel Prado, and Bruno Sans\'o. The current corrected-v4 manuscript line supplies the chapter spine. The Gaussian baseline, complete posterior derivations, algorithms, crossing diagnostics, and claim-relevant empirical displays are integrated by topic rather than retained as a separate document.",
            self.environment(main_raw, "abstract"),
        )
        content += "\n\n".join(pieces)
        content = self.transform(content, "qdesn")
        content = content.replace(r"\label{qdesn:ch:research-c}", r"\label{ch:research-c}", 1)
        self.write_chapter(
            self.current_chapter,
            [("qdesn", main_path), ("qdesn", supp_path), ("qdesn", gauss_path)],
            content,
        )

    def build_ch05(self) -> None:
        self.current_chapter = "ch05-mti"
        rqr_main_path = "main.tex"
        rqr_supp_path = "rqr-gibbs-supplement.tex"
        mti_main_path = "main.tex"
        mti_supp_path = "mti-extensions-supplement.tex"
        rqr_main_raw = self.text("rqr", rqr_main_path)
        rqr_supp_raw = self.text("rqr", rqr_supp_path)
        mti_main_raw = self.text("mti", mti_main_path)
        mti_supp_raw = self.text("mti", mti_supp_path)
        main = self.section_map(rqr_main_raw)
        supp = self.section_map(rqr_supp_raw)
        ext = self.section_map(mti_main_raw)
        ext_supp = self.section_map(mti_supp_raw)

        rqr_pieces = [
            self.pick(main, "Introduction"),
            self.pick(main, "Fixed-Content Interval Targets"),
            self.pick(supp, "Fixed-Content Interval Targets").replace(
                r"\section{Fixed-Content Interval Targets}",
                r"\section{Proofs for Fixed-Content Interval Targets}",
                1,
            ),
            self.pick(main, "The Mean-Preserving Interval Target"),
            self.pick(supp, "Mean-Preserving Interval Scores"),
            self.pick(main, "Mean-Tilted Intervals"),
            self.pick(supp, "Mean-Tilted Interval Loss and Target"),
            self.pick(main, "Empirical Balance and Fixed-Target Computation"),
            self.pick(supp, "Empirical Balance"),
            self.pick(supp, "Fixed-Target MTI-ECM Calculation"),
            self.pick(supp, "Direct DP Content Check"),
            self.pick(main, "Calibrated Minimum-Width Tolerance Intervals"),
            self.pick(supp, "Width-Regularized Interval Loss"),
            self.pick(main, "Validation Design"),
            self.pick(supp, "Tolerance-Validation Protocol and Feasibility"),
            self.pick(main, "Pharmaceutical Batch Application"),
            self.pick(supp, "Pharmaceutical Application Details"),
            self.pick(supp, "Reproducibility and Validation Limits"),
            self.pick(main, "Discussion"),
        ]
        ext_order = [
            "Introduction",
            "Fixed-Content Targets and Generalized Bayes",
            "Static Endpoint Regression",
            "Pseudo-AL Computation",
            "Basis Expansions and Time-Varying Endpoints",
            "Uncertainty Calibration and Diagnostics",
            "Discussion",
        ]
        ext_supp_order = [
            "Notation and Targets",
            "Root Labels and Endpoint Summaries",
            "Pseudo-AL Augmentation",
            "Gaussian Root Updates and Fixed Tilt",
            "ECM Mode Calculation",
            "Conditionally Gaussian Shrinkage",
            "Deterministic Basis Expansions",
            "Dynamic Endpoint-State Updates",
            "Diagnostics and Validation Limits",
        ]
        rqr_main_order = [
            "Introduction",
            "Fixed-Content Interval Targets",
            "The Mean-Preserving Interval Target",
            "Mean-Tilted Intervals",
            "Empirical Balance and Fixed-Target Computation",
            "Calibrated Minimum-Width Tolerance Intervals",
            "Validation Design",
            "Pharmaceutical Batch Application",
            "Discussion",
        ]
        rqr_supp_order = [
            "Fixed-Content Interval Targets",
            "Mean-Preserving Interval Scores",
            "Mean-Tilted Interval Loss and Target",
            "Empirical Balance",
            "Width-Regularized Interval Loss",
            "Fixed-Target MTI-ECM Calculation",
            "Direct DP Content Check",
            "Tolerance-Validation Protocol and Feasibility",
            "Pharmaceutical Application Details",
            "Reproducibility and Validation Limits",
        ]
        self.record_document_disposition(
            "rqr",
            rqr_main_path,
            main,
            rqr_main_order,
            note="All main scientific sections integrated as the foundation and tolerance portion of Chapter 5.",
        )
        self.record_document_disposition(
            "rqr",
            rqr_supp_path,
            supp,
            rqr_supp_order,
            note="All substantive proof, computation, validation, and application sections integrated; part dividers and navigation guides omitted.",
        )
        self.record_document_disposition(
            "mti",
            mti_main_path,
            ext,
            ext_order,
            note="All regression and dynamic-extension scientific sections integrated after the RQR foundation.",
        )
        self.record_document_disposition(
            "mti",
            mti_supp_path,
            ext_supp,
            ext_supp_order,
            note="All computational detail and validation-limit sections integrated within the extension movement.",
        )
        ext_pieces = [self.demote(self.pick(ext, title), 1) for title in ext_order]
        ext_details = [self.demote(self.pick(ext_supp, title), 2) for title in ext_supp_order]
        rqr_content = self.chapter_header(
            "Mean-tilted intervals: foundations, tolerance inference, and dynamic extensions",
            "ch:research-d",
            "This chapter combines two closely related manuscript lines by Antonio de Leon, Raquel Prado, and Bruno Sans\'o. The mean-tilted interval and tolerance article provides the first spine; its proofs and validation details are placed with the corresponding claims. The regression and dynamic endpoint paper then extends the same target, with its computational details integrated in the same body.",
            self.environment(rqr_main_raw, "abstract"),
        )
        rqr_content += "\n\n".join(rqr_pieces)
        rqr_content = self.transform(rqr_content, "rqr")
        rqr_content = rqr_content.replace(
            r"\label{rqr:ch:research-d}", r"\label{ch:research-d}", 1
        )
        ext_intro = (
            "\n\\section{Regression and dynamic endpoint extensions}\n"
            + self.environment(mti_main_raw, "abstract")
            + "\n\n"
            + "\n\n".join(ext_pieces)
            + "\n\n\\subsection{Integrated computational details}\n"
            + "\n\n".join(ext_details)
        )
        ext_content = self.transform(ext_intro, "mti")
        content = rqr_content + "\n" + ext_content
        self.write_chapter(
            self.current_chapter,
            [
                ("rqr", rqr_main_path),
                ("rqr", rqr_supp_path),
                ("mti", mti_main_path),
                ("mti", mti_supp_path),
            ],
            content,
        )

    def write_manifests(self) -> None:
        manifest_dir = PROJECT_ROOT / "docs" / "imports"
        manifest_dir.mkdir(parents=True, exist_ok=True)
        for chapter, items in self.manifests.items():
            output = {
                "schema_version": 1,
                "generated_at": "2026-09-15",
                "chapter": chapter,
                "policy": {
                    "scope": "manuscript prose, equations, referenced TeX displays, and referenced final display assets only",
                    "excluded": "source code, data, fitted objects, caches, simulations, source histories, and complete output archives",
                    "rights": "local structural conversion only; direct-reuse review required before synchronization, publication, or submission",
                },
                "documents": self.documents[chapter],
                "items": sorted(items, key=lambda item: (str(item["source_id"]), str(item["source_path"]))),
            }
            write_if_changed(
                manifest_dir / f"{chapter}.json",
                (json.dumps(output, indent=2) + "\n").encode("utf-8"),
            )

    def run(self) -> None:
        self.validate_sources()
        self.build_bibliography()
        self.build_ch02()
        self.build_ch03()
        self.build_ch04()
        self.build_ch05()
        write_if_changed(PROJECT_ROOT / "references.bib", self.bibliography.encode("utf-8"))
        self.write_manifests()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--audit-root",
        required=True,
        type=Path,
        help="directory containing the immutable audit clones",
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    Importer(arguments.audit_root.resolve()).run()
