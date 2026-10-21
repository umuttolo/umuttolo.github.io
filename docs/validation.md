# Validation — 20 October 2026

## Completed locally

- Jekyll **4.4.1**, Ruby **4.0.1**, Bundler **4.0.3**: production build completed with strict front matter enabled.
- `python3 scripts/check_site.py --migration-audit`: passed. Seven generated HTML pages (four primary pages, two aliases and a 404), all internal navigation/assets/anchors, valid sitemap, valid PDF signatures, seven publications, two working papers and original publisher links.
- `python3 scripts/check_site.py _artifacts/preview --migration-audit`: passed for the exported review copy after rewriting its links for local files.
- Source and review ZIP integrity checks passed. The source archive includes the hidden GitHub Actions workflow and excludes local dependencies, generated site, Git internals and review artifacts.
- Generated site: approximately **310 KB**, including portrait and three PDFs. The stylesheet is approximately **7.3 KB**. There are no JavaScript files, remotely loaded fonts or Squarespace rendering dependencies.
- The local HTTP preview returned **200**. About and Research were inspected at the default 1280-pixel desktop width. About, Research, Teaching and CV were inspected at a 390-pixel mobile width. About also passed a 320-pixel layout check with no horizontal overflow. The portrait loaded at its original 736 × 928 dimensions.
- Browser navigation between primary pages works; research section anchors are checked against the generated headings. The CV points to the locally copied May 2026 PDF. Responsive screenshots are saved under `_artifacts/`.
- Every linked source document was attempted. The CV and both undergraduate teaching plans were copied and verified. Three source files returned 404 and have request-by-email alternatives.

## Verification limits and remaining publication work

- Several external institutions/publishers return 403 or cookie-handling pages to command-line clients; those destinations are preserved and their responses recorded in `external-link-check.json`.
- Browser QA used the local Jekyll HTTP preview. The embedded browser permits HTTP/HTTPS only and does not open `file://` URLs. The offline review copy's files and internal links passed the structural checker; open its `index.html` directly in your own browser after extraction.
- GitHub's Linux workflow has been prepared, with Linux dependency platforms in the lockfile and Pages actions checked against GitHub's current starter workflow. It has **not run on GitHub** because the connected account exposes no repositories and the browser is signed out. GitHub publication and a remote smoke test remain pending repository access.
- No Squarespace site, subscription, DNS record or custom-domain setting has been changed. The GitHub review target is `umuttolo.github.io`; connecting `umutyuksel.net` is a separate step after review.
