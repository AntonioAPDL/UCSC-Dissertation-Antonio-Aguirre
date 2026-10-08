#!/usr/bin/env python3.11
"""Apply the approved reader-first body/appendix migration exactly once.

The transformation is deliberately hash-guarded.  It moves existing article
prose verbatim, inserts short body bridges, and emits a machine-readable map.
It does not touch research repositories, imported assets, citations, or the
immutable import manifests.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASELINE_COMMIT = "c93d7b3ed9c228811b6b79f13a90b312319b9cf3"
SCIENTIFIC_BASELINE = "0c394122549e903b19edc8014709a6f4318bee26"
EXPECTED = {
    "chapters/02-research-a.tex": "0ca289a793bd6b9e1e5427a16b7cb818a4afdfbbe46eade38fca52b513d23e54",
    "chapters/03-research-b.tex": "2c7746f38055f89cc20bcab4c67ea7f0311cffd6ea48b27c4bf9bd98f6fb58d4",
    "chapters/04-research-c.tex": "47fd8acd8d66617d0043aad0091866ccc8f3f6b733aa27b73920e83944229f5d",
    "chapters/05-research-d.tex": "4b1dad25f4e7768d41578798934c7a7b0c9d94824374f236af7d13308fcec250",
}


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Move:
    ident: str
    start: str
    end: str
    destination_heading: str
    bridge: str
    semantic_class: str
    risk: str


def promote_headings(text: str, levels: int = 1) -> str:
    """Promote subsection material when it becomes an appendix section."""
    if levels != 1:
        raise ValueError("only one-level promotion is supported")
    marker = "__PROMOTED_SUBSUBSECTION__"
    text = text.replace(r"\subsubsection", marker)
    text = text.replace(r"\subsection", r"\section")
    return text.replace(marker, r"\subsection")


def move_regions(
    relative: str,
    moves: list[Move],
    appendix_path: str,
    appendix_title: str,
    appendix_label: str,
    *,
    promote: bool = False,
) -> list[dict[str, object]]:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    observed = sha(text)
    if observed != EXPECTED[relative]:
        raise SystemExit(
            f"refusing migration: {relative} hash {observed} does not match approved baseline"
        )

    records: list[dict[str, object]] = []
    appendix_parts = [
        f"\\chapter{{{appendix_title}}}\n",
        f"\\label{{{appendix_label}}}\n\n",
        "This appendix preserves the detailed derivations, algorithms, and\n",
        "secondary diagnostics supporting the corresponding research chapter.\n",
        "The chapter retains the inferential target, central model, principal\n",
        "evidence, interpretation, and limitations needed for a continuous read.\n\n",
    ]
    for move in moves:
        start_at = text.find(move.start)
        if start_at < 0:
            raise SystemExit(f"missing start anchor for {move.ident}: {move.start}")
        end_at = text.find(move.end, start_at)
        if end_at < 0:
            raise SystemExit(f"missing end anchor for {move.ident}: {move.end}")
        chunk = text[start_at:end_at].rstrip() + "\n"
        destination_chunk = promote_headings(chunk) if promote else chunk
        appendix_parts.extend(
            [
                f"% migration-id: {move.ident}\n",
                destination_chunk,
                "\n",
            ]
        )
        text = text[:start_at] + move.bridge.rstrip() + "\n\n" + text[end_at:]
        records.append(
            {
                "id": move.ident,
                "source_path": relative,
                "source_heading": move.start,
                "source_unit_sha256": sha(chunk),
                "disposition": "MOVE_APPENDIX",
                "semantic_class": move.semantic_class,
                "destination_path": appendix_path,
                "destination_heading": move.destination_heading,
                "appendix_label": appendix_label,
                "body_bridge_present": True,
                "risk": move.risk,
                "review_status": "IMPLEMENTED_PENDING_RENDERED_REVIEW",
                "source_claim_ids": [],
                "source_display_ids": sorted(set(re.findall(r"\\label\{([^}]+)\}", chunk))),
            }
        )

    appendix_text = "".join(appendix_parts).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
    (ROOT / appendix_path).write_text(appendix_text, encoding="utf-8")
    current_hash = sha(text)
    destination_hash = sha(appendix_text)
    for record in records:
        record["source_file_sha256_before"] = observed
        record["source_file_sha256_after"] = current_hash
        record["destination_file_sha256_after"] = destination_hash
    return records


def main() -> int:
    appendices = ROOT / "appendices"
    appendices.mkdir(exist_ok=True)
    target_paths = [
        appendices / "b-exdqlm-technical.tex",
        appendices / "c-hydrology-technical.tex",
        appendices / "d-qdesn-technical.tex",
        appendices / "e-mti-technical.tex",
        ROOT / "docs" / "appendix-migration-map.json",
    ]
    existing = [str(p.relative_to(ROOT)) for p in target_paths if p.exists()]
    if existing:
        raise SystemExit("refusing migration because outputs already exist: " + ", ".join(existing))

    records: list[dict[str, object]] = []
    records += move_regions(
        "chapters/02-research-a.tex",
        [
            Move(
                "MIG-CH02-01",
                r"\section{Nonconjugate VB and backend notes}",
                r"\section{Examples}",
                "Backend, posterior, and predictive details",
                r"""\section{Inference, diagnostics, and predictive use}
\label{exdqlm:sec:body-inference}

The implemented workflow supports exact or sampling-based updates where they
are available and explicitly nonconjugate variational blocks where the exAL
scale--asymmetry structure requires approximation.  Forecast distributions
are formed from posterior state and parameter uncertainty and are evaluated
with calibration diagnostics and proper scores.  These computational choices
are part of the method rather than interchangeable software settings.

Appendix~\ref{app:exdqlm-technical} gives the complete posterior blocks,
nonconjugate VB construction, LDVB scale--skewness implementation,
regularized-horseshoe updates, and posterior-predictive synthesis algorithm.
The examples below retain the primary empirical evidence and the limitations
needed to interpret those details.""",
                "posterior derivations and algorithms",
                "high",
            )
        ],
        "appendices/b-exdqlm-technical.tex",
        "Technical details for flexible dynamic quantile models",
        "app:exdqlm-technical",
    )

    records += move_regions(
        "chapters/03-research-b.tex",
        [
            Move(
                "MIG-CH03-01",
                r"\section{Markov chain Monte Carlo algorithms}",
                r"\section{San Lorenzo River application}",
                "MCMC and variational algorithms",
                r"""\section{Posterior computation}
\label{environ:sec:body-computation}

Inference is carried out with the MCMC and variational procedures induced by
the source-aware state-space model.  Both approaches preserve the distinction
between the response process, source-specific latent quantities, and the
subsequent synthesis across quantile levels.  The empirical comparisons below
therefore evaluate a fixed model-and-algorithm contract rather than a generic
post-processing rule.

The complete full-conditionals, filtering and smoothing recursions, and
stepwise MCMC and VB algorithms appear in
Appendix~\ref{app:hydrology-technical}.""",
                "algorithms",
                "high",
            ),
            Move(
                "MIG-CH03-02",
                r"\subsection{Source-specific exAL parameter summaries}",
                r"\section{Chapter summary and limitations}",
                "Source-specific and cutoff-specific diagnostics",
                r"""\subsection{Additional diagnostic evidence}
\label{environ:sec:body-additional-diagnostics}

Source-specific exAL summaries and cutoff-specific predictive-synthesis panels
support the interpretation above but are not required to follow the principal
five-origin comparison.  They are collected in
Appendix~\ref{app:hydrology-technical}, where their narrower diagnostic role
and the distinct evaluation horizons remain explicit.""",
                "secondary empirical diagnostics",
                "medium",
            ),
        ],
        "appendices/c-hydrology-technical.tex",
        "Technical details for hydrologic correction and synthesis",
        "app:hydrology-technical",
        promote=True,
    )

    records += move_regions(
        "chapters/04-research-c.tex",
        [
            Move(
                "MIG-CH04-01",
                r"\section{Shared distributional conventions}",
                r"\section[Joint quantile-vector regression with regularized-horseshoe shrinkage]{Joint quantile-vector regression with\\regularized-horseshoe shrinkage}",
                "Distributional, prior, posterior, and computational details",
                r"""\section{Inference and computation}
\label{qdesn:sec:body-inference}

The single-level Q--DESN uses AL or exAL working likelihoods for the selected
reservoir features, with ridge or regularized-horseshoe shrinkage chosen as
part of the stated model.  MCMC targets the corresponding augmented posterior;
the VB--LD alternative uses a variational factorization together with a local
Laplace--Delta treatment of the nonconjugate block.  Approximation quality is
therefore assessed empirically and is not treated as an exact posterior claim.

Appendix~\ref{app:qdesn-technical} records the parameterizations, prior
calibration, Gaussian initialization baseline, full conditionals, VB--LD
updates, and ELBO diagnostics.  Appendix~\ref{app:shared-conventions} gives a
cross-chapter concordance without erasing the scale conventions specific to
this chapter.""",
                "likelihood, priors, derivations, and algorithms",
                "high",
            ),
            Move(
                "MIG-CH04-02",
                r"\section[Joint quantile-vector regression with regularized-horseshoe shrinkage]{Joint quantile-vector regression with\\regularized-horseshoe shrinkage}",
                r"\section{Forecasting, scoring, and model selection}",
                "Joint quantile-vector posterior details",
                r"""\section{Joint quantile-vector inference}
\label{qdesn:sec:body-joint-inference}

For simultaneous quantile levels, the readout is stacked over a common
reservoir design and assigned quantile-indexed shrinkage.  This construction
shares nonlinear features while retaining quantile-specific coefficients and
diagnostics for crossing.  It supplies a coherent computational comparison,
not a claim that independent working likelihoods define a fully specified
joint response distribution.

The stacked likelihood, shrinkage hierarchy, posterior blocks, MCMC algorithm,
VB--LD relation, and crossing diagnostics are given in
Appendix~\ref{app:qdesn-technical}.""",
                "joint-model derivations and algorithms",
                "high",
            ),
            Move(
                "MIG-CH04-03",
                r"\subsection{Multi-step quantile forecasting and monotone rearrangement}",
                r"\section{Simulation studies}",
                "Multi-step forecasting and rearrangement",
                r"""\subsection{Multi-step prediction and crossing control}
\label{qdesn:sec:body-multistep}

Multi-step forecasts propagate the fixed reservoir recursion under the stated
future-input contract.  When several quantiles are fitted, monotone
rearrangement is reported as a post-processing operation and is distinguished
from the fitted joint posterior.  The complete recursion, scoring definitions,
and rearrangement mechanics are in Appendix~\ref{app:qdesn-technical}.""",
                "forecast derivations",
                "medium",
            ),
            Move(
                "MIG-CH04-04",
                r"\subsection{Simulation diagnostics and sensitivity}",
                r"\section{GloFAS retrospective streamflow application}",
                "Simulation diagnostics and sensitivity",
                r"""\subsection{Simulation diagnostics and sensitivity}
\label{qdesn:sec:body-simulation-diagnostics}

The principal simulation comparisons are accompanied by posterior summaries,
multi-chain checks, and joint-quantile sensitivity analyses.  Those supporting
diagnostics are collected in Appendix~\ref{app:qdesn-technical}; they qualify
the empirical results but do not change the estimands or the reported primary
comparisons.""",
                "secondary empirical diagnostics",
                "medium",
            ),
            Move(
                "MIG-CH04-05",
                r"\subsection{Latent-path ensemble-likelihood construction}",
                r"\section{Region-frozen PriceFM application}",
                "Latent-path ensemble-likelihood construction",
                r"""\subsection{Latent-path ensemble interpretation}
\label{qdesn:sec:body-latent-path}

The GloFAS ensemble experiment uses a latent-path augmented working likelihood
to connect ensemble members to the observed streamflow target.  The reported
comparison is conditional on that construction and its numerical
approximation.  Appendix~\ref{app:qdesn-technical} gives the full augmented
model and sensitivity evidence.""",
                "application-specific derivation and sensitivity",
                "high",
            ),
            Move(
                "MIG-CH04-06",
                r"\subsection{Regional heterogeneity and historical sensitivity}",
                r"\section{Chapter discussion}",
                "PriceFM regional and historical sensitivity",
                r"""\subsection{Regional and historical sensitivity}
\label{qdesn:sec:body-pricefm-sensitivity}

The region-frozen comparison is not uniform across regions or historical
windows.  Appendix~\ref{app:qdesn-technical} preserves the detailed
heterogeneity and sensitivity evidence; the discussion below retains the
resulting limitations on generalization.""",
                "secondary application diagnostics",
                "medium",
            ),
        ],
        "appendices/d-qdesn-technical.tex",
        "Technical details for Bayesian quantile deep echo state networks",
        "app:qdesn-technical",
        promote=True,
    )

    records += move_regions(
        "chapters/05-research-d.tex",
        [
            Move(
                "MIG-CH05-01",
                r"\subsection{Score derivation and consequences}",
                r"\section{Mean-Tilted Intervals}",
                "MPI score derivations, interval paths, and tail sensitivity",
                r"""\subsection{Consequences of the MPI score}
\label{rqr:sec:body-mpi-consequences}

The score equations establish the content and retained-mean identities stated
above.  They also imply a mean-preserving contraction under the recorded
regularity conditions, nested population interval paths on connected support,
and positive-affine equivariance.  These are population statements: restricted
regression classes satisfy design-weighted equations, and fitted endpoints do
not inherit a finite-sample guarantee merely by conditioning on their observed
values.  Appendix~\ref{app:mti-technical} contains the derivations, proofs,
endpoint-atom qualifications, and tail-sensitivity calculations.""",
                "proofs and population consequences",
                "high",
            ),
            Move(
                "MIG-CH05-02",
                r"\subsection{Identification proofs and restricted-score equations}",
                r"\section{Empirical balance and fixed-target computation}",
                "MTI identification proofs and recovery approximations",
                r"""\subsection{Identification, restricted classes, and recovery tilts}
\label{rqr:sec:body-mti-identification}

The fixed-content and retained-mean equations identify the regular population
target; profiling over the content-constrained radius yields the global result
under the theorem's connected-support and moment conditions.  Restricted root
classes instead target design-weighted projections.  Cornish--Fisher recovery
tilts are used only as initialization or external selection approximations,
not as target definitions.  Complete proofs and the numerical approximation
study are in Appendix~\ref{app:mti-technical}.""",
                "proofs, restricted scores, and approximation details",
                "high",
            ),
            Move(
                "MIG-CH05-03",
                r"\subsubsection{Protocol, calibration, and feasibility details}",
                r"\section{Pharmaceutical Batch Application}",
                "Tolerance calibration protocol and feasibility",
                r"""\subsubsection{Protocol and feasibility boundary}

The action-specific calibration protocol, feasibility checks, and secondary
diagnostics are reported in Appendix~\ref{app:mti-technical}.  The evidence
supports the numerical comparison made here; it does not establish an exact
finite-sample theorem for a different closed-window selection action.""",
                "calibration protocol and secondary diagnostics",
                "high",
            ),
            Move(
                "MIG-CH05-04",
                r"\subsection{Data, secondary response, and sensitivity analyses}",
                r"\subsection{Reproducibility and validation limits}",
                "Secondary pharmaceutical analyses",
                r"""\subsection{Secondary analyses}

The secondary response and sensitivity analyses support, but do not replace,
the primary pharmaceutical comparison.  Their data handling, alternative
summaries, and detailed results are preserved in
Appendix~\ref{app:mti-technical}.""",
                "secondary application evidence",
                "medium",
            ),
            Move(
                "MIG-CH05-05",
                r"\subsection{Computational derivation details}",
                r"\section{Chapter discussion}",
                "Regression and dynamic computational derivations",
                r"""\subsection{Computational scope of the proposed extensions}
\label{rqr:sec:body-extension-computation}

The pseudo-AL identity supplies conditionally Gaussian updates for proposed
root-regression and dynamic endpoint models, but it is not a response
likelihood and does not add empirical validation.  Appendix~\ref{app:mti-technical}
records the root labeling, augmentation, ECM, shrinkage, basis, and dynamic
state derivations.  The extensions remain proposed until implementation and
numerical evidence are supplied.""",
                "proposed-model computational derivations",
                "high",
            ),
        ],
        "appendices/e-mti-technical.tex",
        "Technical details for mean-preserving and mean-tilted intervals",
        "app:mti-technical",
        promote=True,
    )

    payload = {
        "schema_version": 1,
        "plan_id": "reader-first-restructure-v3",
        "implemented_at": "2026-10-08",
        "planning_baseline_commit": BASELINE_COMMIT,
        "scientific_content_baseline_commit": SCIENTIFIC_BASELINE,
        "accepted_before_artifact": {
            "path": "build/release-20260916T081243Z/main.pdf",
            "sha256": "30b4e0bb3c3230544e941f7eae82dcabb44f08e9283ae9809aaade45196c9900",
            "pages": 344,
        },
        "decision_meanings": {
            "MOVE_APPENDIX": "source unit moved verbatim except for heading-level promotion",
            "body_bridge_present": "body retains an interpretive summary and an appendix pointer",
        },
        "records": records,
    }
    (ROOT / "docs" / "appendix-migration-map.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"reader-first migration written: {len(records)} mapped units")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
