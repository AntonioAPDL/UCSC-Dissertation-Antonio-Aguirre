#!/usr/bin/env Rscript

# Dissertation presentation derivatives of frozen RQR-GIBBS ECM summaries.
# No fitting, endpoint reconstruction, calibration, or stochastic computation.
# Source: AntonioAPDL/RQR-GIBBS@cab844d0695fe13fa3f610615d282972112eba51.

script_arg <- grep("^--file=", commandArgs(FALSE), value = TRUE)
stopifnot(length(script_arg) == 1L)
root <- normalizePath(file.path(dirname(sub("^--file=", "", script_arg)), ".."))
setwd(root)
summary_path <- "tables/ch05-mti/ecm_family_case_summary_20261111.csv"
oracle_path <- "tables/ch05-mti/ecm_population_width_reference_20261111.csv"
hash <- function(path) {
  answer <- system2("sha256sum", shQuote(path), stdout = TRUE)
  stopifnot(length(answer) == 1L)
  strsplit(answer, "[[:space:]]+")[[1L]][1L]
}
stopifnot(
  identical(hash(summary_path), "c66c9525b954d31bf76560274099213358f082724fdfff2a115864a195b32e47"),
  identical(hash(oracle_path), "946fc574dae08978c05ee30e69f59b0cac16d1c2b963aca007b18fc5ce7242bf")
)
data <- read.csv(summary_path, stringsAsFactors = FALSE)
oracle <- read.csv(oracle_path, stringsAsFactors = FALSE)
methods <- c("mti_ecm_adaptive_cell", "young_mathew", "wilks")
method_labels <- c("MTI-ECM", "Young-Mathew", "Wilks")
colors <- c("#009E73", "#CC79A7", "#333333")
families <- c("normal", "student_t3", "exponential", "asym_laplace_tau010",
              "two_piece_normal_1_12", "beta18", "gamma05", "lognormal_hard")
family_labels <- c("Gaussian", "Student t(3)", "Exponential", "AL(0.10)",
                   "Two-piece N", "Beta(1,8)", "Gamma(0.5)", "Lognormal")
design <- unique(data[c("n", "content")])
design <- design[order(design$n, design$content), ]
key <- paste(data$n, data$content, data$dgp_id, data$method)
stopifnot(nrow(data) == 216L, nrow(design) == 9L, !anyDuplicated(key),
          all(data$replications == 1000L), all(data$returned == 1000L),
          all(data$attainment == data$successes / data$replications),
          all(data$width_q025 > 0), all(data$width_q975 >= data$width_q025),
          setequal(data$method, methods), setequal(data$dgp_id, families))
outputs <- "figures/ch05-mti/generated"
dir.create(outputs, recursive = TRUE, showWarnings = FALSE)
open_device <- function(filename, height) {
  png(file.path(outputs, filename), width = 5.5, height = height, units = "in",
      res = 360, pointsize = 9, type = "cairo-png", bg = "white")
}

# Ranges are min/max across the eight distributions, not uncertainty intervals.
open_device("fig04_tolerance_validation_primary.png", 4.7)
layout(matrix(c(1L, 2L), ncol = 1), heights = c(8, 1))
par(mar = c(3.1, 6.1, 0.5, 0.5), family = "sans", cex = 1, mex = 1,
    mgp = c(2, 0.55, 0),
    tcl = -0.2, cex.axis = 1, cex.lab = 1)
y <- rev(seq_len(nrow(design)))
plot(NA, xlim = c(0.932, 1.002), ylim = c(0.5, 9.5), axes = FALSE,
     xlab = "Content-attainment rate (%)", ylab = "", xaxs = "i", yaxs = "i")
abline(h = y, col = "#E8E8E8", lwd = 0.55)
abline(v = 0.95, col = "#888888", lty = 2, lwd = 0.8)
axis(1, at = seq(0.94, 1, 0.02), labels = seq(94, 100, 2))
axis(2, at = y, labels = sprintf("%d / %.2f", design$n, design$content),
     las = 1, tick = FALSE)
mtext("Sample size / content", side = 2, line = 4.8)
offsets <- c(0.19, 0, -0.19)
for (i in seq_len(nrow(design))) for (j in seq_along(methods)) {
  selected <- data$n == design$n[i] & data$content == design$content[i] &
    data$method == methods[j]
  values <- data$attainment[selected]
  stopifnot(length(values) == 8L)
  yy <- y[i] + offsets[j]
  segments(min(values), yy, max(values), yy, col = colors[j], lwd = 1.5)
  segments(c(min(values), max(values)), yy - 0.055,
           c(min(values), max(values)), yy + 0.055, col = colors[j], lwd = 1.1)
}
box(bty = "l", col = "#555555")
par(mar = c(0, 0, 0, 0))
plot.new()
legend("center", legend = method_labels, col = colors, lwd = 1.5,
       bty = "n", horiz = TRUE, cex = 1, x.intersp = 0.6)
dev.off()

# Family names occupy a separate shared column: panel axes remain the same size.
open_device("fig05_tolerance_validation_width_ranges.png", 6.5)
panel_matrix <- matrix(seq_len(12), nrow = 3, byrow = TRUE)
layout(rbind(panel_matrix, rep(13L, 4)),
       widths = c(0.90, 1.53, 1.53, 1.53), heights = c(1.88, 1.88, 1.88, 0.40))
par(oma = c(0.2, 0, 0.8, 0), cex = 1, mex = 1)
for (row in 1:3) {
  par(mar = c(2.3, 0, 1.6, 0.15), family = "sans", cex = 1, mex = 1,
      xaxs = "i", yaxs = "i")
  plot(NA, xlim = c(0, 1), ylim = c(0.5, 8.5), axes = FALSE, xlab = "", ylab = "")
  text(1, rev(seq_along(families)), family_labels, adj = 1, cex = 0.94)
  for (column in 1:3) {
    cell <- 3L * (row - 1L) + column
    n <- design$n[cell]
    content <- design$content[cell]
    z <- data[data$n == n & data$content == content, ]
    reference <- oracle[abs(oracle$content - content) < 1e-12, ]
    reference <- reference[match(families, reference$dgp_id), ]
    stopifnot(nrow(z) == 24L, !anyNA(reference$width), all(reference$status == "ok"))
    limits <- range(c(z$width_q025, z$width_q975, reference$width))
    limits <- exp(log(limits) + c(-0.08, 0.08))
    par(mar = c(2.3, 0.35, 1.6, 0.35), family = "sans", cex = 1, mex = 1,
        mgp = c(1.6, 0.45, 0),
        tcl = -0.15, xaxs = "i", yaxs = "i")
    plot(NA, xlim = limits, ylim = c(0.5, 8.5), log = "x", axes = FALSE,
         xlab = "", ylab = "")
    abline(h = 1:8, col = "#E8E8E8", lwd = 0.45)
    ticks <- 2^seq(floor(log2(limits[1])), ceiling(log2(limits[2])))
    ticks <- ticks[ticks >= limits[1] & ticks <= limits[2]]
    fraction <- (log(ticks) - log(limits[1])) / diff(log(limits))
    ticks <- ticks[fraction > 0.05 & fraction < 0.95]
    if (length(ticks) > 4L) ticks <- ticks[seq(1L, length(ticks), by = 2L)]
    axis(1, at = ticks, labels = format(ticks, trim = TRUE, digits = 3), cex.axis = 0.95)
    mtext(sprintf("n = %d, c = %.2f", n, content), side = 3, line = 0.45, cex = 1)
    for (f in seq_along(families)) {
      yy <- 9 - f
      segments(reference$width[f], yy - 0.35, reference$width[f], yy + 0.35,
               col = "#888888", lwd = 0.8, lty = 2)
      for (j in seq_along(methods)) {
        value <- z[z$dgp_id == families[f] & z$method == methods[j], ]
        stopifnot(nrow(value) == 1L)
        ypos <- yy + c(0.22, 0, -0.22)[j]
        segments(value$width_q025, ypos, value$width_q975, ypos,
                 col = colors[j], lwd = 1.05)
        points(value$width_mean, ypos, col = colors[j], pch = 3, cex = 0.57, lwd = 0.85)
      }
    }
    box(bty = "l", col = "#555555")
    if (row == 3L) mtext("Width (log scale)", side = 1, line = 1.55, cex = 0.92)
  }
}
par(mar = c(0, 0, 0, 0))
plot.new()
legend("center", legend = c(method_labels, "Population shortest"),
       col = c(colors, "#888888"), lty = c(1, 1, 1, 2), lwd = c(1.1, 1.1, 1.1, 0.8),
       bty = "n", horiz = TRUE, cex = 0.94, x.intersp = 0.45, seg.len = 1.4)
dev.off()

# Generated receipts are ignored build products, not manuscript inputs.
receipt_dir <- "build/review/ch05_mti_ecm_figures"
dir.create(receipt_dir, recursive = TRUE, showWarnings = FALSE)
recorded <- c(summary_path, oracle_path, "scripts/generate_ch05_mti_ecm_figures.R",
  file.path(outputs, c("fig04_tolerance_validation_primary.png",
                       "fig05_tolerance_validation_width_ranges.png")))
write.csv(data.frame(path = recorded, sha256 = vapply(recorded, hash, character(1))),
          file.path(receipt_dir, "source_and_derivative_sha256.csv"), row.names = FALSE)
cat("CH05_ECM_PRESENTATION_DERIVATIVES=PASS\n")
cat("SOURCE_METHOD_ROWS=216; SOURCE_DISTRIBUTION_CASES=72; NEW_FITS=0\n")
