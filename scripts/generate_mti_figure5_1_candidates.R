#!/usr/bin/env Rscript

# Generate review-only alternatives for Dissertation Figure 5.1. The active
# thesis figure is not changed by this script. All interval endpoints are
# population quantities for standardized versions of the stated distributions.

full_args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", full_args, value = TRUE)
if (length(file_arg) != 1L) {
  stop("Run this file with Rscript.")
}
script_path <- normalizePath(sub("^--file=", "", file_arg), mustWork = TRUE)
root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
args <- commandArgs(trailingOnly = TRUE)
install_selected <- "--install-selected" %in% args
path_args <- args[!startsWith(args, "--")]
output_dir <- if (length(path_args)) path_args[[1L]] else file.path(root, "build", "figure5-1-candidates")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

if (!requireNamespace("exdqlm", quietly = TRUE)) {
  stop("The exdqlm package is required for the exAL option.")
}

content <- 0.80
epsilon <- 1e-7

safe_integrate <- function(f, lower, upper, ...) {
  stats::integrate(
    f,
    lower = lower,
    upper = upper,
    subdivisions = 2000L,
    rel.tol = 1e-9,
    stop.on.error = TRUE,
    ...
  )$value
}

exal_quantile <- function(probability, p0, gamma) {
  one_quantile <- function(probability_value) {
    objective <- function(x) {
      exdqlm::pexal(
        x,
        p0 = p0,
        mu = 0,
        sigma = 1,
        gamma = gamma
      ) - probability_value
    }
    lower <- -1
    upper <- 1
    while (objective(lower) > 0) lower <- 2 * lower
    while (objective(upper) < 0) upper <- 2 * upper
    stats::uniroot(objective, c(lower, upper), tol = 1e-11)$root
  }
  vapply(probability, one_quantile, numeric(1))
}

make_exal <- function() {
  p0 <- 0.50
  gamma <- 0.80
  qfun <- function(p) exal_quantile(p, p0 = p0, gamma = gamma)
  dfun <- function(x) {
    exdqlm::dexal(x, p0 = p0, mu = 0, sigma = 1, gamma = gamma)
  }
  lower <- qfun(1e-8)
  upper <- qfun(1 - 1e-8)
  mass <- safe_integrate(dfun, lower, upper)
  mean_value <- safe_integrate(function(x) x * dfun(x), lower, upper) / mass
  sd_value <- sqrt(
    safe_integrate(function(x) (x - mean_value)^2 * dfun(x), lower, upper) / mass
  )
  skewness <- safe_integrate(
    function(x) ((x - mean_value) / sd_value)^3 * dfun(x),
    lower,
    upper
  ) / mass
  list(
    id = "A",
    slug = "exal_p050_gamma080",
    label = "exAL: p0 = 0.50, gamma = 0.80",
    note = "Full support; left-skewed exAL option",
    q = qfun,
    d = dfun,
    mean = mean_value,
    sd = sd_value,
    skewness = skewness
  )
}

make_al <- function() {
  p0 <- 0.90
  qfun <- function(p) {
    ifelse(
      p < p0,
      log(p / p0) / (1 - p0),
      -log((1 - p) / (1 - p0)) / p0
    )
  }
  dfun <- function(x) {
    check <- x * (p0 - as.numeric(x < 0))
    p0 * (1 - p0) * exp(-check)
  }
  mean_value <- (1 - 2 * p0) / (p0 * (1 - p0))
  sd_value <- sqrt(1 - 2 * p0 + 2 * p0^2) / (p0 * (1 - p0))
  lower <- qfun(1e-8)
  upper <- qfun(1 - 1e-8)
  skewness <- safe_integrate(
    function(x) ((x - mean_value) / sd_value)^3 * dfun(x),
    lower,
    upper
  )
  list(
    id = "B",
    slug = "al_p090",
    label = "AL: p0 = 0.90",
    note = "Full support; strongly left-skewed AL option",
    q = qfun,
    d = dfun,
    mean = mean_value,
    sd = sd_value,
    skewness = skewness
  )
}

make_reflected_lognormal <- function() {
  sdlog <- 0.90
  qfun <- function(p) -stats::qlnorm(1 - p, meanlog = 0, sdlog = sdlog)
  dfun <- function(x) {
    answer <- numeric(length(x))
    inside <- x < 0
    answer[inside] <- stats::dlnorm(-x[inside], meanlog = 0, sdlog = sdlog)
    answer
  }
  positive_mean <- exp(sdlog^2 / 2)
  positive_variance <- (exp(sdlog^2) - 1) * exp(sdlog^2)
  list(
    id = "C",
    slug = "reflected_lognormal_sd090",
    label = "Reflected lognormal: sdlog = 0.90",
    note = "Upper-bounded; strongly left-skewed option",
    q = qfun,
    d = dfun,
    mean = -positive_mean,
    sd = sqrt(positive_variance),
    skewness = -(exp(sdlog^2) + 2) * sqrt(exp(sdlog^2) - 1)
  )
}

make_reflected_gamma <- function() {
  shape <- 2
  rate <- 1
  qfun <- function(p) -stats::qgamma(1 - p, shape = shape, rate = rate)
  dfun <- function(x) {
    answer <- numeric(length(x))
    inside <- x < 0
    answer[inside] <- stats::dgamma(-x[inside], shape = shape, rate = rate)
    answer
  }
  list(
    id = "D",
    slug = "reflected_gamma_shape2",
    label = "Reflected Gamma: shape = 2",
    note = "Upper-bounded; moderately left-skewed option",
    q = qfun,
    d = dfun,
    mean = -shape / rate,
    sd = sqrt(shape) / rate,
    skewness = -2 / sqrt(shape)
  )
}

make_beta <- function() {
  shape1 <- 6
  shape2 <- 1.5
  qfun <- function(p) stats::qbeta(p, shape1 = shape1, shape2 = shape2)
  dfun <- function(x) {
    answer <- numeric(length(x))
    inside <- x > 0 & x < 1
    answer[inside] <- stats::dbeta(x[inside], shape1 = shape1, shape2 = shape2)
    answer
  }
  mean_value <- shape1 / (shape1 + shape2)
  variance <- shape1 * shape2 /
    ((shape1 + shape2)^2 * (shape1 + shape2 + 1))
  skewness <- 2 * (shape2 - shape1) * sqrt(shape1 + shape2 + 1) /
    ((shape1 + shape2 + 2) * sqrt(shape1 * shape2))
  list(
    id = "E",
    slug = "beta_6_1p5",
    label = "Beta: shape1 = 6, shape2 = 1.5",
    note = "Bounded; left-skewed option",
    q = qfun,
    d = dfun,
    mean = mean_value,
    sd = sqrt(variance),
    skewness = skewness
  )
}

interval_summary <- function(distribution) {
  retained_mean_difference <- function(u) {
    lower <- distribution$q(u)
    upper <- distribution$q(u + content)
    safe_integrate(function(x) x * distribution$d(x), lower, upper) / content -
      distribution$mean
  }
  search_grid <- seq(epsilon, 1 - content - epsilon, length.out = 201L)
  differences <- vapply(search_grid, retained_mean_difference, numeric(1))
  changes <- which(diff(sign(differences)) != 0)
  if (!length(changes)) {
    stop("No MPI root found for option ", distribution$id)
  }
  bracket <- search_grid[c(changes[[1L]], changes[[1L]] + 1L)]
  mpi_u <- stats::uniroot(
    retained_mean_difference,
    bracket,
    tol = 1e-11
  )$root
  width <- function(u) distribution$q(u + content) - distribution$q(u)
  shortest_u <- stats::optimize(
    width,
    c(epsilon, 1 - content - epsilon),
    tol = 1e-11
  )$minimum
  starts <- c(ET = (1 - content) / 2, MPI = mpi_u, SH = shortest_u)
  endpoints <- t(vapply(
    starts,
    function(u) c(lower = distribution$q(u), upper = distribution$q(u + content)),
    numeric(2)
  ))
  endpoints <- (endpoints - distribution$mean) / distribution$sd
  widths <- endpoints[, "upper"] - endpoints[, "lower"]
  list(
    starts = starts,
    endpoints = endpoints,
    widths = widths,
    endpoint_span = diff(range(endpoints[, "lower"])) +
      diff(range(endpoints[, "upper"]))
  )
}

distributions <- list(
  make_exal(),
  make_al(),
  make_reflected_lognormal(),
  make_reflected_gamma(),
  make_beta()
)
summaries <- lapply(distributions, interval_summary)

colors <- c(ET = "#228B57", MPI = "#2764E7", SH = "#D97706")
titles <- c(ET = "Equal-tailed", MPI = "Mean-preserving", SH = "Shortest contiguous")
principles <- c(
  ET = "Equal omitted probabilities",
  MPI = "Retained mean equals population mean",
  SH = "Minimum geometric width"
)

draw_option <- function(distribution, summary, selected = FALSE) {
  endpoints <- summary$endpoints
  left <- (distribution$q(0.005) - distribution$mean) / distribution$sd
  right <- (distribution$q(0.995) - distribution$mean) / distribution$sd
  interval_limits <- range(endpoints)
  x_limits <- range(c(left, right, interval_limits))
  padding <- 0.04 * diff(x_limits)
  x_limits <- x_limits + c(-padding, padding)
  x_grid <- seq(x_limits[[1L]], x_limits[[2L]], length.out = 1600L)
  raw_grid <- distribution$mean + distribution$sd * x_grid
  density <- distribution$sd * distribution$d(raw_grid)
  y_limit <- c(0, 1.16 * max(density, na.rm = TRUE))

  old_par <- graphics::par(
    mfrow = c(1, 3),
    oma = c(0.4, 0.2, 4.2, 0.2),
    mar = c(4.1, 4.2, 4.1, 0.8),
    mgp = c(2.4, 0.7, 0),
    tcl = -0.25,
    las = 1,
    family = "sans"
  )
  on.exit(graphics::par(old_par), add = TRUE)

  for (method in names(titles)) {
    interval <- endpoints[method, ]
    graphics::plot(
      x_grid,
      density,
      type = "n",
      xlim = x_limits,
      ylim = y_limit,
      xlab = "Standardized response, z",
      ylab = "Density",
      main = "",
      bty = "l"
    )
    inside <- x_grid >= interval[["lower"]] & x_grid <= interval[["upper"]]
    polygon_x <- c(interval[["lower"]], x_grid[inside], interval[["upper"]])
    polygon_y <- c(0, density[inside], 0)
    graphics::polygon(
      polygon_x,
      polygon_y,
      col = grDevices::adjustcolor(colors[[method]], alpha.f = 0.20),
      border = NA
    )
    graphics::lines(x_grid, density, lwd = 2.6, col = "#17202A")
    graphics::abline(v = interval, col = grDevices::adjustcolor(colors[[method]], 0.75), lwd = 1.1)
    segment_y <- 0.015 * y_limit[[2L]]
    graphics::segments(
      interval[["lower"]],
      segment_y,
      interval[["upper"]],
      segment_y,
      lwd = 6,
      lend = "round",
      col = colors[[method]]
    )
    graphics::mtext(
      titles[[method]], side = 3, line = 2.25, cex = 0.96, font = 2
    )
    graphics::mtext(principles[[method]], side = 3, line = 1.05, cex = 0.82)
    graphics::mtext(
      sprintf(
        "[%.2f, %.2f]   width %.2f",
        interval[["lower"]],
        interval[["upper"]],
        summary$widths[[method]]
      ),
      side = 3,
      line = -0.10,
      cex = 0.72,
      col = "#374151"
    )
  }
  outer_title <- if (selected) {
    sprintf("Strongly left-skewed illustration; interval content c = %.2f", content)
  } else {
    sprintf(
      "Option %s: %s; standardized skewness = %.2f; content c = %.2f",
      distribution$id, distribution$label, distribution$skewness, content
    )
  }
  outer_subtitle <- if (selected) {
    "Population intervals after standardization"
  } else {
    distribution$note
  }
  graphics::mtext(
    outer_title,
    outer = TRUE,
    side = 3,
    line = 2.25,
    cex = 1.18,
    font = 2
  )
  graphics::mtext(
    outer_subtitle,
    outer = TRUE,
    side = 3,
    line = 0.80,
    cex = 0.88,
    col = "#374151"
  )
}

metrics <- do.call(rbind, Map(function(distribution, summary) {
  data.frame(
    option = distribution$id,
    distribution = distribution$label,
    skewness = distribution$skewness,
    et_lower = summary$endpoints["ET", "lower"],
    et_upper = summary$endpoints["ET", "upper"],
    mpi_lower = summary$endpoints["MPI", "lower"],
    mpi_upper = summary$endpoints["MPI", "upper"],
    sh_lower = summary$endpoints["SH", "lower"],
    sh_upper = summary$endpoints["SH", "upper"],
    endpoint_span = summary$endpoint_span,
    stringsAsFactors = FALSE
  )
}, distributions, summaries))
utils::write.csv(
  metrics,
  file.path(output_dir, "figure5_1_candidate_metrics.csv"),
  row.names = FALSE
)

draw_summary_page <- function() {
  old_par <- graphics::par(mar = c(1, 1, 2, 1), family = "sans")
  on.exit(graphics::par(old_par), add = TRUE)
  graphics::plot.new()
  graphics::title(
    main = "Figure 5.1 distribution options",
    sub = paste0(
      "All quantities are population values after standardization; interval content c = ",
      sprintf("%.2f", content)
    ),
    cex.main = 1.45,
    cex.sub = 0.95
  )
  header <- sprintf(
    "%-6s %-42s %9s %19s %19s %19s %10s",
    "Option", "Distribution", "Skewness", "ET [L,U]", "MPI [L,U]", "SH [L,U]", "Separation"
  )
  rows <- vapply(seq_len(nrow(metrics)), function(index) {
    item <- metrics[index, ]
    sprintf(
      "%-6s %-42s %9.2f %8.2f,%8.2f %8.2f,%8.2f %8.2f,%8.2f %10.2f",
      item$option,
      substr(item$distribution, 1, 42),
      item$skewness,
      item$et_lower,
      item$et_upper,
      item$mpi_lower,
      item$mpi_upper,
      item$sh_lower,
      item$sh_upper,
      item$endpoint_span
    )
  }, character(1))
  graphics::text(0.03, 0.82, header, adj = c(0, 1), family = "mono", cex = 0.78, font = 2)
  graphics::text(
    0.03,
    0.76,
    paste(rows, collapse = "\n\n"),
    adj = c(0, 1),
    family = "mono",
    cex = 0.78
  )
  graphics::text(
    0.03,
    0.16,
    paste(
      strwrap(
        paste(
          "Separation is the combined range of the standardized lower and upper endpoints.",
          "A larger value makes the distinction among the three interval placements more visible.",
          "The selected distribution should also support the chapter's statistical explanation."
        ),
        width = 150
      ),
      collapse = "\n"
    ),
    adj = c(0, 1),
    cex = 0.88,
    col = "#374151"
  )
  graphics::text(
    0.03,
    0.06,
    paste0(
      "Generated with R ", getRversion(), " and exdqlm ",
      utils::packageVersion("exdqlm"), "."
    ),
    adj = c(0, 1),
    cex = 0.76,
    col = "#4B5563"
  )
}

combined_pdf <- file.path(output_dir, "figure5_1_distribution_options.pdf")
grDevices::cairo_pdf(
  combined_pdf,
  width = 14,
  height = 6.2,
  onefile = TRUE,
  family = "sans"
)
draw_summary_page()
invisible(Map(draw_option, distributions, summaries))
grDevices::dev.off()

for (index in seq_along(distributions)) {
  distribution <- distributions[[index]]
  summary <- summaries[[index]]
  pdf_path <- file.path(
    output_dir,
    sprintf("figure5_1_option_%s_%s.pdf", distribution$id, distribution$slug)
  )
  grDevices::cairo_pdf(
    pdf_path,
    width = 14,
    height = 6.2,
    onefile = FALSE,
    family = "sans"
  )
  draw_option(distribution, summary)
  grDevices::dev.off()

  png_path <- file.path(
    output_dir,
    sprintf("figure5_1_option_%s_%s.png", distribution$id, distribution$slug)
  )
  grDevices::png(
    png_path,
    width = 2520,
    height = 1116,
    res = 180,
    type = "cairo-png"
  )
  draw_option(distribution, summary)
  grDevices::dev.off()
}

writeLines(
  c(
    paste("Generated:", format(Sys.time(), tz = "America/Los_Angeles", usetz = TRUE)),
    paste("R:", R.version.string),
    paste("exdqlm:", as.character(utils::packageVersion("exdqlm"))),
    paste("Content:", content),
    "The active dissertation figure was not modified."
  ),
  file.path(output_dir, "generation_record.txt")
)

if (install_selected) {
  selected_index <- which(vapply(distributions, `[[`, character(1), "id") == "C")
  selected_path <- file.path(
    root,
    "figures",
    "ch05-mti",
    "generated",
    "fig01_three_balance_principles.png"
  )
  grDevices::png(
    selected_path,
    width = 2520,
    height = 1116,
    res = 180,
    pointsize = 18,
    type = "cairo-png"
  )
  draw_option(
    distributions[[selected_index]],
    summaries[[selected_index]],
    selected = TRUE
  )
  grDevices::dev.off()
  cat(normalizePath(selected_path), "\n")
}

cat(normalizePath(combined_pdf), "\n")
