#!/usr/bin/env python3.11
"""Refresh the dissertation from the audited 2026-10-26 source snapshots.

This is a manuscript-only projection.  It reads immutable Git blobs from
isolated audit clones, preserves the article main texts as chapter spines,
places technical supplements in the existing reader-first appendices, and
copies only manuscript-referenced display assets.  It never executes research
code and never imports data, fitted objects, caches, or source histories.

Run without ``--apply`` to verify the source snapshots and destination state.
Run with ``--apply`` once on the dedicated refresh branch to write the refresh.
After application, check mode validates the recorded destination hashes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

import import_manuscripts as legacy


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-10-26"
REVISION_ID = "REV-CURRENT-SOURCES-20261026"
REFRESH_RECORD = ROOT / "docs/source-refresh-20261026.json"

CURRENT = {
    "exd": legacy.Source(
        "exd", "SRC-EXDQLM-ARTICLE", "exdqlm-article",
        "98cec593d11bf32715a690ae168086f16160e7f0",
        "references.bib", "exd", "exd",
        ("CLM-EXDQLM-001", "CON-EXDQLM-004"),
    ),
    "env": legacy.SOURCES["env"],
    "qdesn": legacy.Source(
        "qdesn", "SRC-QDESN", "qdesn",
        "483e6edbec72ec76e48f2259e943e674b76e5041",
        "refs.bib", "qdesn", "qdesn2026",
        ("CLM-QDESN-001", "CLM-QDESN-002", "CLM-QDESN-003",
         "ART-QDESN-004", "ART-QDESN-005", "ART-QDESN-008"),
    ),
    "rqr": legacy.Source(
        "rqr", "SRC-RQR", "rqr",
        "4223c6a3a44f376255bacdca91db71cdf4f3afde",
        "refs.bib", "rqr", "rqr2026",
        ("CLM-RQR-001", "CLM-RQR-002", "ART-RQR-003", "CON-RQR-004"),
    ),
    "mti": legacy.SOURCES["mti"],
}

PRE_REFRESH = {
    "chapters/02-research-a.tex": "ac8f2438467ae498192c68703bee099c0b47b8b6dd026e090f11760603300102",
    "chapters/04-research-c.tex": "37d4304b17fd5e326e281f2e19bc1a44bf8dd95dd268d7094e1288626d12934a",
    "chapters/05-research-d.tex": "2fd9033e73156cb1ee15f03a940d26db42cfac0458e0b094cf342166fa2771d8",
    "appendices/b-exdqlm-technical.tex": "4878511125af9db709dc46230fde2b56ef70d7ffe8ac85a1a4d56ab2946bbb08",
    "appendices/d-qdesn-technical.tex": "c7bf5852cd301cb427853b634570c699fedc2b2968f7a43d6d0a86e1de87301e",
    "appendices/e-mti-technical.tex": "ec4fa6d44b4d288722909a9b7087e90624e420d6f7e8e17c20153e2d356212d6",
    "references.bib": "9f9ee13601f628b1572cdd7a4050fdde411a576ae40538ee6159e2792e61b960",
}

OLD_COMMITS = {
    "SRC-QDESN": "757522db0f85815244370ec92a194de132268883",
    "SRC-RQR": "73887b9c86ef767aa1567c660718667945630aef",
    "SRC-EXDQLM-ARTICLE": "d5534e97db8414fd875022261d4c530eae4676e4",
}

Q_ALIAS_CHAIN = (
    "tables/glofas_application_current_outputs.tex",
    "tables/glofas_review_figure_overrides.tex",
    "tables/glofas_figure4_common_window_outputs.tex",
    "tables/glofas_mq_display_overrides.tex",
    "tables/pricefm_full_current_outputs.tex",
    "tables/qdesn_sections5_7_main_display_overrides.tex",
    "tables/qdesn_sections5_7_supp_display_overrides.tex",
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_digest(relative: str) -> str:
    return digest((ROOT / relative).read_bytes())


def configure_sources() -> None:
    legacy.SOURCES.clear()
    legacy.SOURCES.update(CURRENT)


def validate_destination_state(apply: bool) -> str:
    if REFRESH_RECORD.is_file():
        record = json.loads(REFRESH_RECORD.read_text(encoding="utf-8"))
        expected = record.get("destination_sha256", {})
        if expected and all(
            (ROOT / path).is_file() and file_digest(path) == value
            for path, value in expected.items()
        ):
            return "CURRENT_REFRESH_EXACT"
    mismatches = [
        f"{path}: expected {expected}, found "
        f"{file_digest(path) if (ROOT / path).is_file() else 'MISSING'}"
        for path, expected in PRE_REFRESH.items()
        if not (ROOT / path).is_file() or file_digest(path) != expected
    ]
    if mismatches:
        raise SystemExit(
            "refusing refresh because destinations match neither the approved "
            "pre-refresh state nor the recorded current refresh:\n- "
            + "\n- ".join(mismatches)
        )
    return "APPROVED_PRE_REFRESH"


def build_citation_maps(importer: legacy.Importer) -> int:
    """Map current source keys onto the existing curated bibliography."""
    existing = (ROOT / "references.bib").read_text(encoding="utf-8")
    existing_entries = legacy.Importer.parse_bib_entries(existing)
    fingerprints: dict[str, str] = {}
    emitted = {key.lower() for _, key, _ in existing_entries if key}
    for _, key, raw in existing_entries:
        if not key:
            continue
        doi = legacy.Importer.normalized(legacy.Importer.bib_field(raw, "doi"))
        title = legacy.Importer.normalized(legacy.Importer.bib_field(raw, "title"))
        if doi:
            fingerprints[f"doi:{doi}"] = key
        if len(title) >= 12:
            fingerprints.setdefault(f"title:{title}", key)

    marker = "% Added by scripts/refresh_current_research.py from the 2026-10-26 audited source snapshots."
    previously_added = 0
    if marker in existing:
        previously_added = len(
            legacy.Importer.parse_bib_entries(existing.split(marker, 1)[1])
        )
    additions: list[str] = []
    for source_key, source in CURRENT.items():
        mapping: dict[str, str] = {}
        for kind, old_key, raw in legacy.Importer.parse_bib_entries(
            importer.text(source_key, source.bib_path)
        ):
            if not old_key:
                continue
            doi = legacy.Importer.normalized(legacy.Importer.bib_field(raw, "doi"))
            title = legacy.Importer.normalized(legacy.Importer.bib_field(raw, "title"))
            candidates = []
            if doi:
                candidates.append(f"doi:{doi}")
            if len(title) >= 12:
                candidates.append(f"title:{title}")
            canonical = next(
                (fingerprints[item] for item in candidates if item in fingerprints),
                None,
            )
            if canonical is None:
                candidate = f"{source.citation_prefix}-{old_key}"
                suffix = 2
                while candidate.lower() in emitted:
                    candidate = f"{source.citation_prefix}-{old_key}-{suffix}"
                    suffix += 1
                canonical = candidate
                emitted.add(canonical.lower())
                for item in candidates:
                    fingerprints[item] = canonical
                renamed = re.sub(
                    r"(@[A-Za-z]+\s*[({]\s*)[^,\s]+(\s*,)",
                    rf"\g<1>{canonical}\g<2>", raw, count=1,
                )
                additions.append(renamed)
            mapping[old_key] = canonical
            mapping[old_key.lower()] = canonical
        importer.cite_maps[source_key] = mapping
    importer.bibliography = existing.rstrip() + (
        "\n\n" + marker + "\n\n"
        + "\n\n".join(additions)
        + "\n" if additions else "\n"
    )
    return len(additions) or previously_added


def appendix_references(text: str, label: str) -> str:
    target = rf"Appendix~\ref{{{label}}}"
    text = re.sub(r"\b[Tt]he supplement's\b", target + "'s", text)
    text = re.sub(r"\b[Tt]he supplement\b", target, text)
    text = re.sub(r"\b[Tt]his supplement\b", "This appendix", text)
    text = re.sub(r"\bin the supplement\b", f"in {target}", text, flags=re.I)
    text = re.sub(r"\bsupplementary\b", "additional", text, flags=re.I)
    text = text.replace("the integrated technical material", target)
    text = text.replace("The integrated technical material", target)
    text = text.replace("the integrated material", target)
    text = text.replace("The integrated material", target)
    return text


def appendix_self_references(text: str) -> str:
    text = re.sub(r"\b[Tt]his supplement\b", "This appendix", text)
    text = re.sub(r"\b[Tt]he supplement\b", "this appendix", text)
    text = text.replace("the integrated technical material", "this appendix")
    text = text.replace("The integrated technical material", "This appendix")
    text = text.replace("the integrated material", "this appendix")
    text = text.replace("The integrated material", "This appendix")
    return text


def transformed_header(importer: legacy.Importer, title: str, label: str,
                       note: str, abstract: str, source_key: str) -> str:
    text = importer.chapter_header(title, label, note, abstract)
    return text


def build_qdesn_alias_file(importer: legacy.Importer) -> str:
    """Collapse the upstream override chain to its final active definitions.

    The source intentionally retains several historical presentation overrides.
    Copying each alias recursively would import superseded displays.  Resolving
    the chain once preserves the exact final macro values while ensuring that
    only active main-text and claim-relevant appendix dependencies are copied.
    """
    final: dict[str, str] = {}
    raw_by_path: dict[str, bytes] = {}
    pattern = re.compile(
        r"^\\(?:newcommand|renewcommand|providecommand)\{(\\[A-Za-z@]+)\}\{(.*)\}$"
    )
    for source_path in Q_ALIAS_CHAIN:
        raw = importer.blob("qdesn", source_path)
        raw_by_path[source_path] = raw
        for line in raw.decode("utf-8").splitlines():
            match = pattern.match(line.strip())
            if match:
                final[match.group(1)] = match.group(2)
    if not final:
        raise SystemExit("could not resolve the Q--DESN alias chain")
    used_text = (
        importer.text("qdesn", "main.tex")
        + importer.text("qdesn", "qdesn-supplement.tex")
        + importer.text("qdesn", "gaussian_desn_scaled_ridge_supplement.tex")
    )
    final = {name: body for name, body in final.items() if name in used_text}
    if not final:
        raise SystemExit("no active Q--DESN alias definitions were found")
    generated = (
        "% Generated by scripts/refresh_current_research.py from the final values\n"
        "% in the audited Q--DESN presentation-override chain.\n"
        + "\n".join(
            rf"\newcommand{{{name}}}{{{body}}}" for name, body in final.items()
        )
        + "\n"
    )
    generated = importer.transform(generated, "qdesn")
    pricefm_source = (
        "figures/ch04-qdesn/pricefm_application/"
        "pricefm_regional_aql_editorial_20261013.pdf"
    )
    pricefm_fontsafe = (
        "figures/ch04-qdesn/pricefm_application/"
        "pricefm_regional_aql_editorial_20261013_fontsafe.pdf"
    )
    source_file = ROOT / pricefm_source
    fontsafe_file = ROOT / pricefm_fontsafe
    if not source_file.is_file():
        raise SystemExit("current PriceFM display was not copied from the audited source")
    if not fontsafe_file.is_file():
        ghostscript = shutil.which("gs")
        if not ghostscript:
            raise SystemExit(
                "Ghostscript is required once to create the font-safe PriceFM "
                "rendering derivative"
            )
        subprocess.run([
            ghostscript, "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pdfwrite",
            "-dNoOutputFonts", "-dCompatibilityLevel=1.7",
            f"-sOutputFile={fontsafe_file}", str(source_file),
        ], check=True)
    generated = generated.replace(pricefm_source, pricefm_fontsafe)
    source_blob = next(
        item for item in importer.manifests["ch04-qdesn"]
        if item.get("destination") == pricefm_source
    )
    importer.record(
        "qdesn", str(source_blob["source_path"]), pricefm_fontsafe,
        importer.blob("qdesn", str(source_blob["source_path"])),
        fontsafe_file.read_bytes(), "figure_asset",
        "Ghostscript pdfwrite 9.27 NoOutputFonts derivative; plot lettering "
        "converted to vector outlines without changing plotted data, dimensions, "
        "caption, or claim",
    )
    destination = "tables/ch04-qdesn/current_source_aliases_20261026.tex"
    destination_data = generated.encode("utf-8")
    legacy.write_if_changed(ROOT / destination, destination_data)
    for source_path, source_data in raw_by_path.items():
        importer.record(
            "qdesn", source_path, destination, source_data, destination_data,
            "display_tex_fragment",
            "resolved presentation-override chain; retained final active macro definitions only",
        )
    return destination


def braced_argument(text: str, opening: int) -> tuple[str, int]:
    """Return a balanced TeX braced argument and the index after its close."""
    if opening >= len(text) or text[opening] != "{":
        raise ValueError("expected a TeX braced argument")
    depth = 0
    for index in range(opening, len(text)):
        if text[index] == "{" and (index == 0 or text[index - 1] != "\\"):
            depth += 1
        elif text[index] == "}" and (index == 0 or text[index - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[opening + 1:index], index + 1
    raise ValueError("unterminated TeX braced argument")


def table_to_longtable(text: str, label: str, columns: int,
                       column_spec: str | None = None,
                       font: str = r"\footnotesize") -> str:
    """Convert one labelled floating table into a page-breaking longtable.

    The current Q--DESN source contains several complete evidence tables that
    are taller than a dissertation page.  The values, headings, caption, and
    label remain unchanged; only the presentation container is changed.
    """
    label_token = rf"\label{{{label}}}"
    label_at = text.find(label_token)
    if label_at < 0:
        raise ValueError(f"missing table label {label}")
    table_at = text.rfind(r"\begin{table}", 0, label_at)
    table_end_at = text.find(r"\end{table}", label_at)
    if table_at < 0 or table_end_at < 0:
        raise ValueError(f"could not delimit table {label}")
    table_end = table_end_at + len(r"\end{table}")

    tabular_at = text.find(r"\begin{tabular}", table_at, label_at)
    tabularx_at = text.find(r"\begin{tabularx}", table_at, label_at)
    if tabular_at >= 0:
        argument_at = text.find("{", tabular_at + len(r"\begin{tabular}"))
        original_spec, body_at = braced_argument(text, argument_at)
        tabular_end = text.find(r"\end{tabular}", body_at, label_at)
    elif tabularx_at >= 0:
        width_at = text.find("{", tabularx_at + len(r"\begin{tabularx}"))
        _, after_width = braced_argument(text, width_at)
        argument_at = text.find("{", after_width)
        original_spec, body_at = braced_argument(text, argument_at)
        tabular_end = text.find(r"\end{tabularx}", body_at, label_at)
    else:
        raise ValueError(f"missing tabular body for {label}")
    if tabular_end < 0:
        raise ValueError(f"could not delimit tabular body for {label}")

    body = text[body_at:tabular_end].strip()
    midrule = body.find(r"\midrule")
    bottomrule = body.rfind(r"\bottomrule")
    if midrule < 0 or bottomrule < 0 or bottomrule <= midrule:
        raise ValueError(f"table rules are not in the expected form for {label}")
    header = body[:midrule + len(r"\midrule")].strip()
    rows = body[midrule + len(r"\midrule"):bottomrule].strip()

    caption_at = text.find(r"\caption", tabular_end, label_at)
    caption_open = text.find("{", caption_at + len(r"\caption"))
    caption, _ = braced_argument(text, caption_open)
    spec = column_spec or original_spec
    continuation = "Continued."
    replacement = (
        "\\begingroup\n"
        f"{font}\n"
        "\\setlength{\\tabcolsep}{3pt}\n"
        "\\renewcommand{\\arraystretch}{1.08}\n"
        f"\\begin{{longtable}}{{{spec}}}\n"
        f"\\caption{{{caption}}}\\label{{{label}}}\\\\\n"
        f"{header}\n"
        "\\endfirsthead\n"
        f"\\caption[]{{{continuation}}}\\\\\n"
        f"{header}\n"
        "\\endhead\n"
        "\\midrule\n"
        f"\\multicolumn{{{columns}}}{{r}}{{\\footnotesize Continued on next page}}\\\\\n"
        "\\endfoot\n"
        "\\bottomrule\n"
        "\\endlastfoot\n"
        f"{rows}\n"
        "\\end{longtable}\n"
        "\\endgroup"
    )
    return text[:table_at] + replacement + text[table_end:]


def make_qdesn_tables_reader_safe(importer: legacy.Importer,
                                  technical: str) -> str:
    """Apply reproducible, content-preserving pagination to tall Q--DESN tables."""
    technical = technical.replace(
        r"\Normal(\beta_j\mid0,a)\Normal(0\mid\beta_j,b)"
        "\n"
        r"&=\Normal(0\mid0,a+b)\Normal(\beta_j\mid0,ab/(a+b)).",
        r"\Normal(\beta_j\mid0,a)\Normal(0\mid\beta_j,b)"
        "\n"
        r"&=\Normal(0\mid0,a+b)\\"
        "\n"
        r"&\quad{}\times\Normal(\beta_j\mid0,ab/(a+b)).",
    )
    technical = technical.replace(
        "The induced density on the constrained parameters is\n"
        r"\(q_{\sigma,\gamma}(\sigma,\gamma)=q_\eta\{T^{-1}(\sigma,\gamma)\}/"
        "\n"
        r"J\{T^{-1}(\sigma,\gamma)\}\); it is not Gaussian on the original scale.",
        "The induced density on the constrained parameters is\n"
        r"\["
        "\n"
        r"q_{\sigma,\gamma}(\sigma,\gamma)"
        "="
        r"\frac{q_\eta\{T^{-1}(\sigma,\gamma)\}}"
        r"{J\{T^{-1}(\sigma,\gamma)\}}."
        "\n"
        r"\]"
        "\n"
        "It is not Gaussian on the original scale.",
    )
    technical = table_to_longtable(
        technical, "qdesn2026:tab:supp-reservoir-selection", 4,
        r"@{}>{\raggedright\arraybackslash}p{0.18\textwidth}"
        r">{\raggedright\arraybackslash}p{0.22\textwidth}"
        r">{\raggedright\arraybackslash}p{0.26\textwidth}"
        r">{\raggedright\arraybackslash}p{0.22\textwidth}@{}",
        r"\small",
    )
    layouts = {
        "qdesn_multiquantile_score_display.tex": (
            "qdesn2026:tab:joint-qdesn-pure-desn-v2-score", 7,
            r"@{}>{\raggedright\arraybackslash}p{0.18\textwidth}"
            r">{\raggedright\arraybackslash}p{0.14\textwidth}"
            r"*{4}{>{\raggedleft\arraybackslash}p{0.09\textwidth}}"
            r">{\raggedleft\arraybackslash}p{0.125\textwidth}@{}",
        ),
        "qdesn_multiquantile_secondary_score_display.tex": (
            "qdesn2026:tab:joint-qdesn-pure-desn-v2-secondary", 4,
            r"@{}>{\raggedright\arraybackslash}p{0.23\textwidth}"
            r">{\raggedright\arraybackslash}p{0.19\textwidth}"
            r"*{2}{>{\raggedleft\arraybackslash}p{0.20\textwidth}}@{}",
        ),
        "qdesn_multiquantile_recursive_policy_display.tex": (
            "qdesn2026:tab:joint-qdesn-pure-desn-v2-recursive-policy", 4,
            r"@{}>{\raggedright\arraybackslash}p{0.18\textwidth}"
            r">{\raggedright\arraybackslash}p{0.14\textwidth}"
            r"*{2}{>{\raggedleft\arraybackslash}p{0.28\textwidth}}@{}",
        ),
        "qdesn_multiquantile_vb_score_display.tex": (
            "qdesn2026:tab:joint-qdesn-pure-desn-v2-vb-score", 7,
            r"@{}>{\raggedright\arraybackslash}p{0.18\textwidth}"
            r">{\raggedright\arraybackslash}p{0.14\textwidth}"
            r"*{4}{>{\raggedleft\arraybackslash}p{0.09\textwidth}}"
            r">{\raggedleft\arraybackslash}p{0.125\textwidth}@{}",
        ),
        "qdesn_multiquantile_oracle_recovery_display.tex": (
            "qdesn2026:tab:joint-qdesn-pure-desn-v2-oracle", 6,
            r"@{}>{\raggedright\arraybackslash}p{0.21\textwidth}"
            r">{\raggedright\arraybackslash}p{0.15\textwidth}"
            r"*{4}{>{\raggedleft\arraybackslash}p{0.12\textwidth}}@{}",
        ),
    }
    for filename, (label, columns, spec) in layouts.items():
        relative = f"tables/ch04-qdesn/{filename}"
        path = ROOT / relative
        rendered = table_to_longtable(
            path.read_text(encoding="utf-8"), label, columns, spec
        )
        legacy.write_if_changed(path, rendered.encode("utf-8"))
        current_hash = digest(rendered.encode("utf-8"))
        for item in importer.manifests["ch04-qdesn"]:
            if item.get("destination") == relative:
                item["destination_sha256"] = current_hash
                item["handling"] = (
                    "transformed paths, citations, and cross-references; "
                    "converted to a content-preserving page-breaking longtable; "
                    "no computation imported"
                )
    crossing = "tables/ch04-qdesn/qdesn_multiquantile_crossing_display.tex"
    crossing_path = ROOT / crossing
    crossing_text = crossing_path.read_text(encoding="utf-8").replace(
        r"\setlength{\tabcolsep}{3pt}", r"\setlength{\tabcolsep}{2pt}", 1
    )
    legacy.write_if_changed(crossing_path, crossing_text.encode("utf-8"))
    crossing_hash = digest(crossing_text.encode("utf-8"))
    for item in importer.manifests["ch04-qdesn"]:
        if item.get("destination") == crossing:
            item["destination_sha256"] = crossing_hash
            item["handling"] = (
                "transformed paths, citations, and cross-references; reduced "
                "intercolumn padding to fit the dissertation text block; no "
                "computation imported"
            )
    return technical


def make_mti_tables_reader_safe(importer: legacy.Importer) -> None:
    """Fit the two wide application-sensitivity tables without scaling text."""
    for filename in (
        "pharma_application_primary_sensitivity.tex",
        "pharma_application_rsd_sensitivity.tex",
    ):
        relative = f"tables/ch05-mti/{filename}"
        path = ROOT / relative
        rendered = path.read_text(encoding="utf-8").replace(
            r"\setlength{\tabcolsep}{3pt}", r"\setlength{\tabcolsep}{2.5pt}", 1
        ).replace(
            r"Method & Width & Held-out content & Held-out $\ge c$ & Omitted below/above & Returned\\",
            r"Method & Width & \shortstack{Held-out\\content} & "
            r"\shortstack{Held-out\\$\ge c$} & "
            r"\shortstack{Omitted\\below/above} & Returned\\",
        )
        legacy.write_if_changed(path, rendered.encode("utf-8"))
        current_hash = digest(rendered.encode("utf-8"))
        for item in importer.manifests["ch05-mti"]:
            if item.get("destination") == relative:
                item["destination_sha256"] = current_hash
                item["handling"] = (
                    "transformed paths, citations, and cross-references; reduced "
                    "intercolumn padding to fit the dissertation text block; no "
                    "computation imported"
                )


def build_qdesn(importer: legacy.Importer) -> tuple[str, str, dict[str, str]]:
    importer.current_chapter = "ch04-qdesn"
    main_path = "main.tex"
    supp_path = "qdesn-supplement.tex"
    gauss_path = "gaussian_desn_scaled_ridge_supplement.tex"
    main_raw = importer.text("qdesn", main_path)
    supp_raw = importer.text("qdesn", supp_path)
    gauss_raw = importer.text("qdesn", gauss_path)
    main = importer.section_map(main_raw)
    supp = importer.section_map(supp_raw)
    gauss = importer.section_map(gauss_raw)

    main_order = [
        "Introduction",
        "Fixed-Feature Bayesian Quantile Models",
        "Posterior Computation",
        "Forecasting, Scoring, and Model Selection",
        "Simulation Studies",
        "Application: Streamflow Quantile Forecast Correction",
        "Application: Electricity-Price Quantile Forecasting",
        "Discussion",
    ]
    supp_order = [
        "Distributional Conventions",
        "DESN Feature Map and Fixed-Design Quantile Regression",
        "Q--DESN Likelihoods, Priors, and Augmented Posterior",
        "MCMC Full Conditionals",
        "Variational Bayes and Laplace--Delta Approximation",
        "Variational Objectives and Numerical Stopping",
        "MQ--DESN with Regularized-Horseshoe Shrinkage",
        "Forecast Summaries and Scores",
        "Reservoir Specification, Selection, and Diagnostics",
        "Supplementary Simulation and Application Tables",
        "GloFAS Reference--Discrepancy Forecast Correction",
    ]
    gauss_order = [
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

    abstract = importer.environment(main_raw, "abstract")
    abstract = abstract.replace(
        r"\textit{[PriceFM findings to be updated.]}",
        "Across 114 matched region--fold comparisons, Q--DESN has the lower "
        "average quantile loss in 54 cases and PriceFM in 60; the aggregate "
        "difference slightly favors PriceFM and varies across regions and folds.",
    )
    note = (
        "This chapter is based on joint work by Antonio de Leon, Raquel Prado, "
        "and Bruno Sans\\'o. It follows the current article at the audited "
        "2026-10-26 source snapshot. The main article supplies the reader-facing "
        "spine; complete distributional conventions, posterior derivations, "
        "algorithms, and supporting diagnostics are preserved in "
        "Appendix~\\ref{app:qdesn-technical}."
    )
    alias_path = build_qdesn_alias_file(importer)
    aliases = (
        rf"\input{{{alias_path}}}" + "\n"
        r"\input{figures/quantile_initialization/quantile_initialization_styles.tex}"
    )
    content = transformed_header(
        importer,
        "Bayesian quantile regression with deep echo state network features",
        "ch:research-c", note, abstract, "qdesn",
    )
    content += (
        "\nThe chapter distinguishes single-level Q--DESN from MQ--DESN, "
        "whose composite likelihood reuses the observed response across quantile "
        "levels and is not a normalized joint response likelihood. Empirical "
        "comparisons are reported for their stated targets and evaluation "
        "windows; no uniform dominance claim is made.\n\n"
        + aliases + "\n\n"
        + "\n\n".join(importer.pick(main, title) for title in main_order)
    )
    content = importer.transform(content, "qdesn")
    content = content.replace(r"\label{qdesn2026:ch:research-c}", r"\label{ch:research-c}", 1)
    content = content.replace(
        r"Section~\ref{qdesn2026:app:qdesn-technical}",
        r"Appendix~\ref{app:qdesn-technical}",
    )
    content = appendix_references(content, "app:qdesn-technical")

    technical = (
        "\\chapter{Technical details for Bayesian quantile deep echo state networks}\n"
        "\\label{app:qdesn-technical}\n\n"
        "% migration-id: MIG-CH04-CURRENT-QDESN\n"
        "This appendix preserves the current article's detailed likelihoods, "
        "priors, posterior calculations, algorithms, reservoir-selection "
        "protocols, and supporting empirical results. Chapter~\\ref{ch:research-c} "
        "retains the inferential targets, principal comparisons, interpretation, "
        "and limitations needed for a continuous read.\n\n"
        + "\\section{Q--DESN and MQ--DESN technical development}\n"
        + "\n\n".join(importer.demote(importer.pick(supp, title), 1)
                          for title in supp_order)
        + "\n\n\\section{Gaussian baseline and initialization details}\n"
        + "\n\n".join(
            importer.demote(importer.label_rewrite(importer.pick(gauss, title), "gauss"), 1)
            for title in gauss_order
        )
    )
    technical = importer.transform(technical, "qdesn")
    technical = technical.replace(
        r"\label{qdesn2026:app:qdesn-technical}", r"\label{app:qdesn-technical}", 1
    )
    technical = technical.replace(
        r"\ref{qdesn2026:ch:research-c}", r"\ref{ch:research-c}"
    )
    technical = appendix_self_references(technical)
    technical = technical.replace("the main article", r"Chapter~\ref{ch:research-c}")
    technical = technical.replace("The main article", r"Chapter~\ref{ch:research-c}")
    technical = make_qdesn_tables_reader_safe(importer, technical)
    source_hashes = {
        main_path: digest(importer.blob("qdesn", main_path)),
        supp_path: digest(importer.blob("qdesn", supp_path)),
        gauss_path: digest(importer.blob("qdesn", gauss_path)),
    }
    return content.strip() + "\n", technical.strip() + "\n", source_hashes


def build_mti(importer: legacy.Importer) -> tuple[str, str, dict[str, str]]:
    importer.current_chapter = "ch05-mti"
    rqr_main_path = "main.tex"
    rqr_supp_path = "rqr-gibbs-supplement.tex"
    mti_main_path = "main.tex"
    mti_supp_path = "mti-extensions-supplement.tex"
    rqr_main_raw = importer.text("rqr", rqr_main_path)
    rqr_supp_raw = importer.text("rqr", rqr_supp_path)
    mti_main_raw = importer.text("mti", mti_main_path)
    mti_supp_raw = importer.text("mti", mti_supp_path)
    main = importer.section_map(rqr_main_raw)
    supp = importer.section_map(rqr_supp_raw)
    ext = importer.section_map(mti_main_raw)
    ext_supp = importer.section_map(mti_supp_raw)

    main_order = [
        "Introduction", "Fixed-Content Interval Targets",
        "The Mean-Preserving Interval Target", "Mean-Tilted Intervals",
        "Empirical Balance and Fixed-Target Computation",
        "Calibrated MTI Tolerance Intervals", "Validation Design",
        "Pharmaceutical Batch Application", "Discussion",
    ]
    supp_order = [
        "Fixed-Content Interval Targets", "Mean-Preserving Interval Scores",
        "Mean-Tilted Interval Loss and Target", "Empirical Balance",
        "Width-Regularized Interval Loss", "Fixed-Target MTI Computation",
        "Direct DP Content Check", "Tolerance-Validation Protocol and Feasibility",
        "Pharmaceutical Application Details", "Reproducibility and Validation Limits",
    ]
    ext_order = [
        "Introduction", "Fixed-Content Targets and Generalized Bayes",
        "Static Endpoint Regression", "Pseudo-AL Computation",
        "Basis Expansions and Time-Varying Endpoints",
        "Uncertainty Calibration and Diagnostics", "Discussion",
    ]
    ext_supp_order = [
        "Notation and Targets", "Root Labels and Endpoint Summaries",
        "Pseudo-AL Augmentation", "Gaussian Root Updates and Fixed Tilt",
        "ECM Mode Calculation", "Conditionally Gaussian Shrinkage",
        "Deterministic Basis Expansions", "Dynamic Endpoint-State Updates",
        "Diagnostics and Validation Limits",
    ]

    note = (
        "This chapter combines two closely related manuscript lines by Antonio "
        "de Leon, Raquel Prado, and Bruno Sans\\'o. The current tolerance article "
        "provides the population foundations and calibrated profiled MTI procedure. "
        "The companion extension manuscript develops generalized-Bayes regression "
        "and dynamic endpoint models. Proofs, calibration details, and computational "
        "derivations are preserved in Appendix~\\ref{app:mti-technical}."
    )
    content = transformed_header(
        importer,
        "Mean-tilted intervals: calibrated tolerance inference and dynamic extensions",
        "ch:research-d", note, importer.environment(rqr_main_raw, "abstract"), "rqr",
    )
    content += "\n\n".join(importer.pick(main, title) for title in main_order)
    content = importer.transform(content, "rqr")
    content = content.replace(r"\label{rqr2026:ch:research-d}", r"\label{ch:research-d}", 1)
    content = content.replace(
        r"Section~\ref{rqr2026:app:mti-technical}",
        r"Appendix~\ref{app:mti-technical}",
    )
    content = appendix_references(content, "app:mti-technical")

    ext_intro = importer.pick(ext, "Introduction").replace(
        "The companion tolerance paper\n"
        "develops this geometry and uses it to define scan-calibrated tolerance\n"
        "procedures.",
        "The preceding sections develop this geometry and the calibrated profiled\n"
        "MTI tolerance procedure.",
    )
    ext_chunks = [ext_intro] + [importer.pick(ext, title) for title in ext_order[1:]]
    ext_text = (
        "\n\\section{Regression and dynamic endpoint extensions}\n"
        + importer.environment(mti_main_raw, "abstract")
        + "\n\nThe extension manuscript predates the final profiled tolerance "
        "procedure reported above. Its regression and dynamic constructions are "
        "conditional on a specified content and tilt and remain proposals until "
        "implemented and validated; they do not inherit the empirical tolerance "
        "attainment of the fixed-target study.\n\n"
        + "\n\n".join(importer.demote(chunk, 1) for chunk in ext_chunks)
    )
    ext_text = ext_text.replace(
        "Tolerance validation requires a\n"
        "content-confidence tolerance procedure, such as the TCSP construction in the companion\n"
        "tolerance paper.",
        "Tolerance validation requires an explicitly calibrated content--confidence\n"
        "procedure, such as the profiled MTI procedure developed earlier in this\n"
        "chapter; its empirical attainment does not transfer automatically to the\n"
        "regression and dynamic endpoint proposals.",
    )
    content += importer.transform(ext_text, "mti")

    technical_rqr = (
        "\\chapter{Technical details for mean-preserving and mean-tilted intervals}\n"
        "\\label{app:mti-technical}\n\n"
        "% migration-id: MIG-CH05-CURRENT-RQR\n"
        "% migration-id: MIG-CH05-CURRENT-MTI-EXT\n"
        "This appendix preserves the proofs, profile calculation, content checks, "
        "calibration protocol, application diagnostics, and proposed regression "
        "and dynamic computations supporting Chapter~\\ref{ch:research-d}.\n\n"
        "\\section{Foundations, profiled computation, and validation details}\n"
        + "\n\n".join(importer.demote(importer.pick(supp, title), 1)
                          for title in supp_order)
    )
    technical_rqr = importer.transform(technical_rqr, "rqr")
    technical_rqr = technical_rqr.replace(
        r"\label{rqr2026:app:mti-technical}", r"\label{app:mti-technical}", 1
    )
    technical_rqr = technical_rqr.replace(
        r"\ref{rqr2026:ch:research-d}", r"\ref{ch:research-d}"
    )
    technical_rqr = technical_rqr.replace(
        "\\input{tables/ch05-mti/pharma_application_numbers.tex}\n", ""
    )
    technical_rqr = technical_rqr.replace(
        "\\input{tables/ch05-mti/pharma_source_numbers.tex}\n", ""
    )
    technical_rqr = appendix_self_references(technical_rqr)
    technical_ext = (
        "\n\\section{Regression and dynamic endpoint computation}\n"
        + "\n\n".join(importer.demote(importer.pick(ext_supp, title), 1)
                          for title in ext_supp_order)
    )
    technical = technical_rqr + importer.transform(technical_ext, "mti")
    make_mti_tables_reader_safe(importer)
    source_hashes = {
        f"rqr:{rqr_main_path}": digest(importer.blob("rqr", rqr_main_path)),
        f"rqr:{rqr_supp_path}": digest(importer.blob("rqr", rqr_supp_path)),
        f"mti:{mti_main_path}": digest(importer.blob("mti", mti_main_path)),
        f"mti:{mti_supp_path}": digest(importer.blob("mti", mti_supp_path)),
    }
    return content.strip() + "\n", technical.strip() + "\n", source_hashes


def refresh_exdqlm_text(text: str) -> str:
    replacements = {
        "version 1.1.1": "version 1.1.2",
        "Version 1.1.1": "Version 1.1.2",
        "exdqlm} 1.1.1": "exdqlm} 1.1.2",
        "171.974": "78.458",
        "0.2003": "0.2067",
        "0.02553": "0.02494",
        "-4.5720": "-4.3171",
        "0.93906": "0.88387",
        "-0.039": "-0.004",
        "(-0.397, 0.291)": "(-0.388, 0.475)",
        "0.375": "0.373",
        "(0.302, 0.460)": "(0.279, 0.461)",
        "42.04": "22.53", "282.85": "125.48", "0.175": "0.170",
        "7.608": "7.580", "2969.0": "2966.0", "98.07": "73.46",
        "383.95": "174.66", "0.152": "0.212", "5.147": "5.120",
        "2216.1": "2206.8", "177.944": "177.9", "160.624": "160.6",
        "141.694": "141.7", "50.49": "31.46", "104.39": "71.92",
        "43.30": "27.74", "110.19": "71.19", "22.01": "12.66",
        "142.12": "71.77", "2.1-fold": "2.4-fold", "2.5-fold": "2.4-fold",
        "6.5-fold": "6.1-fold",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace(
        "In version 1.1.2, compiled stochastic helper paths used by the "
        "manuscript run through serial \\proglang{R}-controlled random-number "
        "streams, rather than worker-thread or private C++ random-number streams.",
        "In the 1.1.x patch line, compiled stochastic helper paths used by the "
        "manuscript run through serial \\proglang{R}-controlled random-number "
        "streams, rather than worker-thread or private C++ random-number streams; "
        "version 1.1.2 also uses a platform-stable covariance square root for the "
        "fast dynamic MCMC state-simulation path.",
    )
    text = text.replace(
        "These versions are related but not interchangeable provenance records: "
        "neither 1.1.0 nor 1.1.2 is substituted for the 1.1.1 analysis reported here.",
        "These versions are related but not interchangeable provenance records: "
        "the Chapter~\\ref{ch:research-b} results remain attached to their 1.1.0 "
        "application snapshot, while the analyses reported here use 1.1.2.",
    )
    return text


def copy_current_exdqlm_assets(importer: legacy.Importer) -> None:
    importer.current_chapter = "ch02-exdqlm"
    for name in (
        "ex1mcmc.png", "ex1quants.png", "ex2quant.png", "ex2checks.png",
        "ex3data.png", "ex3quantcomps.png", "ex3zetapsi.png",
        "ex3forecast.png", "ex4static.png",
    ):
        importer.copy_dependency(
            "exd", f"analysis/manuscript/outputs/figures/{name}"
        )


def baseline_destination_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in sorted((ROOT / "docs/imports").glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for item in payload.get("items", []):
            destination = str(item.get("destination", ""))
            value = str(item.get("destination_sha256", ""))
            if destination and value:
                hashes.setdefault(destination, value)
    return hashes


def update_revision_ledger(changed_paths: list[str]) -> None:
    path = ROOT / "docs/revision-ledger.json"
    ledger = json.loads(path.read_text(encoding="utf-8"))
    baseline = baseline_destination_hashes()
    artifacts = {item["path"]: item for item in ledger["artifacts"]}
    for relative in changed_paths:
        target = ROOT / relative
        if not target.is_file():
            continue
        current_hash = digest(target.read_bytes())
        artifact = artifacts.get(relative)
        if artifact is None and relative in baseline and current_hash != baseline[relative]:
            artifact = {
                "path": relative,
                "baseline_sha256": baseline[relative],
                "current_sha256": current_hash,
                "state": "EDITED",
                "revision_ids": [REVISION_ID],
            }
            ledger["artifacts"].append(artifact)
            artifacts[relative] = artifact
        elif artifact is not None:
            artifact["current_sha256"] = current_hash
            if current_hash != artifact.get("baseline_sha256"):
                artifact["state"] = "EDITED" if artifact.get("baseline_sha256") else "DERIVED_NEW"
            if REVISION_ID not in artifact["revision_ids"]:
                artifact["revision_ids"].append(REVISION_ID)
    if not any(item.get("id") == REVISION_ID for item in ledger["revisions"]):
        ledger["revisions"].append({
            "id": REVISION_ID,
            "date": DATE,
            "paths": changed_paths,
            "summary": (
                "Projected the current audited Q--DESN, profiled-MTI, and exDQLM "
                "article snapshots into the reader-first dissertation, retaining "
                "main texts as chapter spines and technical supplements as appendices."
            ),
            "evidence": (
                "docs/current-source-refresh-audit.md; "
                "docs/source-refresh-20261026.json; source-manifest.json"
            ),
            "validation": (
                "Source-blob, structure, citation, dependency, build, PDF, font, "
                "and rendered-page checks required before merge."
            ),
        })
    ledger["artifacts"] = [
        artifact for artifact in ledger["artifacts"]
        if not (
            artifact.get("revision_ids") == [REVISION_ID]
            and artifact.get("baseline_sha256")
            and (ROOT / str(artifact.get("path", ""))).is_file()
            and digest((ROOT / str(artifact["path"])).read_bytes())
            == artifact.get("baseline_sha256")
        )
    ]
    ledger["recorded_at"] = DATE
    legacy.write_if_changed(path, (json.dumps(ledger, indent=2) + "\n").encode())


def update_migration_map(q_hashes: dict[str, str], mti_hashes: dict[str, str]) -> None:
    path = ROOT / "docs/appendix-migration-map.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    retained = [
        item for item in payload.get("records", [])
        if item.get("source_path") in {
            "chapters/02-research-a.tex", "chapters/03-research-b.tex"
        }
    ]
    common = {
        "disposition": "MOVE_APPENDIX",
        "body_bridge_present": True,
        "review_status": "IMPLEMENTED_VALIDATION_PENDING",
        "source_claim_ids": [],
        "source_display_ids": [],
    }
    retained.extend([
        {
            **common,
            "id": "MIG-CH04-CURRENT-QDESN",
            "source_path": "chapters/04-research-c.tex",
            "source_heading": "current Q--DESN article technical support",
            "source_unit_sha256": q_hashes["qdesn-supplement.tex"],
            "semantic_class": "likelihoods, derivations, algorithms, and supporting evidence",
            "destination_path": "appendices/d-qdesn-technical.tex",
            "destination_heading": "Q--DESN and MQ--DESN technical development",
            "appendix_label": "app:qdesn-technical",
            "risk": "high",
            "source_file_sha256_after": file_digest("chapters/04-research-c.tex"),
            "destination_file_sha256_after": file_digest("appendices/d-qdesn-technical.tex"),
        },
        {
            **common,
            "id": "MIG-CH05-CURRENT-RQR",
            "source_path": "chapters/05-research-d.tex",
            "source_heading": "current profiled-MTI article technical support",
            "source_unit_sha256": mti_hashes["rqr:rqr-gibbs-supplement.tex"],
            "semantic_class": "proofs, profiling, calibration, and application diagnostics",
            "destination_path": "appendices/e-mti-technical.tex",
            "destination_heading": "Foundations, profiled computation, and validation details",
            "appendix_label": "app:mti-technical",
            "risk": "high",
            "source_file_sha256_after": file_digest("chapters/05-research-d.tex"),
            "destination_file_sha256_after": file_digest("appendices/e-mti-technical.tex"),
        },
        {
            **common,
            "id": "MIG-CH05-CURRENT-MTI-EXT",
            "source_path": "chapters/05-research-d.tex",
            "source_heading": "MTI regression and dynamic extension technical support",
            "source_unit_sha256": mti_hashes["mti:mti-extensions-supplement.tex"],
            "semantic_class": "generalized-Bayes computational derivations",
            "destination_path": "appendices/e-mti-technical.tex",
            "destination_heading": "Regression and dynamic endpoint computation",
            "appendix_label": "app:mti-technical",
            "risk": "high",
            "source_file_sha256_after": file_digest("chapters/05-research-d.tex"),
            "destination_file_sha256_after": file_digest("appendices/e-mti-technical.tex"),
        },
    ])
    payload["plan_id"] = "reader-first-current-source-refresh-v4"
    payload["implemented_at"] = DATE
    payload["records"] = retained
    legacy.write_if_changed(path, (json.dumps(payload, indent=2) + "\n").encode())


def write_refresh_record(importer: legacy.Importer, added_bib: int,
                         q_hashes: dict[str, str], mti_hashes: dict[str, str],
                         changed_paths: list[str]) -> None:
    destinations = {
        path: file_digest(path) for path in changed_paths if (ROOT / path).is_file()
    }
    source_documents = {
        "SRC-QDESN": {
            "previous_commit": OLD_COMMITS["SRC-QDESN"],
            "current_commit": CURRENT["qdesn"].commit,
            "documents": q_hashes,
        },
        "SRC-RQR": {
            "previous_commit": OLD_COMMITS["SRC-RQR"],
            "current_commit": CURRENT["rqr"].commit,
            "documents": {key.removeprefix("rqr:"): value for key, value in mti_hashes.items() if key.startswith("rqr:")},
        },
        "SRC-MTI-EXT": {
            "previous_commit": CURRENT["mti"].commit,
            "current_commit": CURRENT["mti"].commit,
            "documents": {key.removeprefix("mti:"): value for key, value in mti_hashes.items() if key.startswith("mti:")},
        },
        "SRC-EXDQLM-ARTICLE": {
            "previous_commit": OLD_COMMITS["SRC-EXDQLM-ARTICLE"],
            "current_commit": CURRENT["exd"].commit,
            "documents": {"exdqlm-jss.tex": digest(importer.blob("exd", "exdqlm-jss.tex"))},
        },
    }
    items = sorted(
        importer.manifests["ch02-exdqlm"]
        + importer.manifests["ch04-qdesn"]
        + importer.manifests["ch05-mti"],
        key=lambda item: (str(item["source_id"]), str(item["source_path"])),
    )
    payload = {
        "schema_version": 1,
        "refresh_id": "current-research-20261026",
        "recorded_at": DATE,
        "policy": {
            "scope": "current manuscript prose, equations, referenced TeX display fragments, and referenced final display assets",
            "excluded": "research code, data, fitted objects, caches, simulations, complete output archives, and source histories",
            "rights": "UNVERIFIED; private-source access and technical integration do not establish permission to publish",
            "source_worktrees": "original research working trees were not fetched, checked out, built, or modified",
        },
        "source_documents": source_documents,
        "unchanged_authorities": [
            {"source_id": "SRC-ENVIRON", "commit": CURRENT["env"].commit},
            {"source_id": "SRC-MTI-EXT", "commit": CURRENT["mti"].commit},
        ],
        "editorial_resolutions": [
            "Replaced the unresolved PriceFM abstract placeholder with the matched 114-comparison result already reported by the current Q--DESN article.",
            "Treated the current RQR article as authority for the profiled MTI tolerance procedure and retained the unchanged extension article only for conditional regression and dynamic models.",
            "Preserved current main texts in Chapters 4 and 5 and placed current supplements in Appendices D and E.",
            "Updated Chapter 2 to the exdqlm 1.1.2 rerun and copied its nine current manuscript figures.",
        ],
        "bibliography_entries_added": added_bib,
        "items": items,
        "destination_sha256": destinations,
        "validation_status": "PENDING_FULL_THESIS_VALIDATION",
    }
    legacy.write_if_changed(REFRESH_RECORD, (json.dumps(payload, indent=2) + "\n").encode())


def apply_refresh(importer: legacy.Importer, added_bib: int) -> None:
    q_chapter, q_appendix, q_hashes = build_qdesn(importer)
    mti_chapter, mti_appendix, mti_hashes = build_mti(importer)
    legacy.write_if_changed(ROOT / "chapters/04-research-c.tex", q_chapter.encode())
    legacy.write_if_changed(ROOT / "appendices/d-qdesn-technical.tex", q_appendix.encode())
    legacy.write_if_changed(ROOT / "chapters/05-research-d.tex", mti_chapter.encode())
    legacy.write_if_changed(ROOT / "appendices/e-mti-technical.tex", mti_appendix.encode())

    for relative in ("chapters/02-research-a.tex", "appendices/b-exdqlm-technical.tex"):
        path = ROOT / relative
        legacy.write_if_changed(path, refresh_exdqlm_text(path.read_text(encoding="utf-8")).encode())
    copy_current_exdqlm_assets(importer)
    legacy.write_if_changed(ROOT / "references.bib", importer.bibliography.encode())

    copied = sorted({str(item["destination"]) for group in importer.manifests.values() for item in group})
    core = [
        "chapters/02-research-a.tex", "appendices/b-exdqlm-technical.tex",
        "chapters/04-research-c.tex", "appendices/d-qdesn-technical.tex",
        "chapters/05-research-d.tex", "appendices/e-mti-technical.tex",
        "references.bib",
    ]
    changed_paths = sorted(set(core + copied))
    update_revision_ledger(changed_paths)
    update_migration_map(q_hashes, mti_hashes)
    changed_paths += ["docs/revision-ledger.json", "docs/appendix-migration-map.json"]
    write_refresh_record(importer, added_bib, q_hashes, mti_hashes, sorted(set(changed_paths)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit-root", required=True, type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    configure_sources()
    importer = legacy.Importer(args.audit_root.resolve())
    importer.validate_sources()
    state = validate_destination_state(args.apply)
    if not args.apply:
        print(f"Current-source refresh check: PASS ({state}); no files written")
        return 0
    added = build_citation_maps(importer)
    apply_refresh(importer, added)
    print(
        "Current-source refresh applied: Q--DESN, profiled MTI, and exdqlm 1.1.2 "
        f"projected; {added} bibliography entries added."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
