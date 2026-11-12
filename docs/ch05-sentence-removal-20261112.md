# Chapter 5 requested sentence removal

Baseline main: `98057360b05cdeab4b1247827586b39e543c4d93`.

The author-requested sentence about data-dependent fitted endpoints and
finite-sample tolerance guarantees was removed from Section 5.3, following
the discussion of Proposition 5.2. The paragraph now ends:

> Linear and other restricted root classes satisfy design-weighted equations,
> not necessarily Eqs. (5.3)–(5.4) at every \(x\).

A literal source comparison confirms that removing this one sentence is the
only manuscript change. Equations, numerical results, figures, scientific
sources, and all other manuscript files are unchanged. The existing
population/empirical/calibration distinctions remain elsewhere in the chapter.

Current derivative hashes and shifted line locators were refreshed. The
previous release and publication receipts are retained as explicit history
inside the polish record. The current receipt supersedes its earlier proof
only for this author-requested follow-up.

The full source-aware release gate passed all 71 tests, 132 immutable source
blob checks, the additional migration controls, and the clean build. Accepted
artifact: `build/release-20261112T060155Z/main.pdf`, 189 pages, 3,987,188 bytes,
SHA-256 `f9da6ff8d05299dca8978b3a9e6f569427cb353ce811dd8a850a5157f07ad894`.
The log has ten underfull and zero overfull boxes. Whole-document layout-text
comparison found only physical page 108 (printed page 96) changed; that page
was rendered and inspected. The removed sentence is absent from the PDF.

Git promotion and Drive upload are recorded only after verified remote
readback. The requested Drive destination is the existing Dissertation
Documents folder. No sharing permissions are changed and no prior files are
deleted. No Overleaf publication or independent Overleaf compile is claimed.
