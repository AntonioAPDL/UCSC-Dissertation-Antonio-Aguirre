# Figure 5.1 distribution options

Date: 2026-11-10

Decision state: author selection pending

Generator: `scripts/generate_mti_figure5_1_candidates.R`

## Purpose

The active Figure 5.1 uses one continuous left-skewed population illustration,
but the equal-tailed, mean-preserving, and shortest-contiguous intervals remain
close enough to obscure their distinct placement rules. Five population
alternatives were therefore evaluated at content (c=0.80). Each distribution
is standardized before plotting, and every interval is computed from the
population distribution rather than a simulated sample.

The review artifact is
`build/figure5-1-candidates/figure5_1_distribution_options.pdf`. Its first page
reports the standardized interval endpoints; the remaining pages show one
complete Figure 5.1 alternative per distribution. The active dissertation
figure and caption remain unchanged until the author selects an option.

## Comparison

| Option | Distribution | Standardized skewness | ET | MPI | SH | Endpoint separation |
| --- | --- | ---: | --- | --- | --- | ---: |
| A | exAL, (p_0=0.50,gamma=0.80) | -1.33 | [-1.26, 1.05] | [-1.60, 0.93] | [-0.95, 1.26] | 0.98 |
| B | AL, (p_0=0.90) | -1.96 | [-1.30, 0.88] | [-2.04, 0.82] | [-0.72, 1.06] | 1.56 |
| C | reflected lognormal, `sdlog = 0.90` | -4.75 | [-1.00, 0.71] | [-2.29, 0.64] | [-0.39, 0.84] | 2.09 |
| D | reflected Gamma, shape 2 | -1.41 | [-1.34, 1.04] | [-1.78, 0.95] | [-0.76, 1.30] | 1.36 |
| E | Beta, shapes 6 and 1.5 | -0.92 | [-1.42, 1.12] | [-1.71, 1.05] | [-0.85, 1.40] | 1.22 |

Endpoint separation is the combined range of the standardized lower and upper
endpoints. It measures visual distinction among the three placements, not the
scientific value of a distribution.

## Assessment

Option B gives the strongest balance of visual separation, full support, and
continuity with the asymmetric-Laplace family already used elsewhere in the
dissertation. Option C gives the largest separation, but its heavy left tail
dominates the horizontal scale and makes the MPI width unusually prominent.
Option A provides an explicit exAL illustration but separates the three
placements less clearly. Option D is a smoother moderate alternative; Option E
is bounded and has the weakest asymmetry in the set.

The preferred default is Option B. Option C is preferable only if maximal
visual contrast is more important than using a full-support distribution. A
selection changes only the conceptual population illustration, its caption,
alternative text, and the corresponding accessibility/display records. It
does not change the Chapter 5 theory, algorithms, simulation results, or
application results.

## Reproduction

Run:

```bash
Rscript scripts/generate_mti_figure5_1_candidates.R
```

The generator uses base R population calculations and the installed
`exdqlm` 1.1.2 distribution functions for Option A. It writes the combined
review PDF, individual vector PDFs, high-resolution PNG previews, a metrics
CSV, and a generation record under the ignored `build/figure5-1-candidates/`
directory.
