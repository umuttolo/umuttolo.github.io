# Umut Yüksel — academic website

A lightweight Jekyll website prepared from **https://www.umutyuksel.net/** on 20 October 2026. The migration keeps the public content and navigation while simplifying the design. No JavaScript, remote fonts, theme dependency, analytics or Squarespace services are required to render the site.

The configured GitHub Pages address is **https://umuttolo.github.io**. GitHub is connected as `umuttolo`. The address `umutyuksel.github.io` would require an account or organization named `umutyuksel`; your custom domain **umutyuksel.net** can be attached to the `umuttolo` site later.

## Preview and test

Use Ruby **4.0.1** (see `.ruby-version`) and Bundler. On this Mac, the existing Homebrew Ruby is available at `/opt/homebrew/opt/ruby/bin`; the macOS system Ruby is too old for this project.

```sh
# On this Mac, select the installed Homebrew Ruby first:
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open **http://127.0.0.1:4000**. Content edits rebuild automatically; restart the server after changing `_config.yml`.

For a review copy that opens without running a server, build the site and run `python3 scripts/export_preview.py`, then open `_artifacts/preview/index.html` in your browser. This rewrites generated navigation and asset links for local files; the Jekyll source is unchanged. The same command creates a review ZIP and a source ZIP under `_artifacts/`. Extract the review ZIP before opening its `index.html`. Re-export after content edits.

```sh
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
```

The checker uses Python 3.9+ with no additional packages. It verifies generated pages, internal links, anchors, navigation, PDF signatures, sitemap validity and exclusion of development files. For the original migration only, add `--migration-audit` to compare publication links and counts with the source snapshot; normal content updates do not need that flag. External publisher links can block automated clients and are preserved as supplied. See `docs/migration.md` for the source audit and three missing source documents.

## Update the content

| Content | File or folder |
| --- | --- |
| Biography and affiliations | `index.md` |
| Publications | `_data/publications.yml` |
| Advanced working papers | `_data/working_papers.yml` |
| Research overview | `research.md` |
| Research projects | `_projects/`, one Markdown file per project |
| Teaching and course materials | `teaching.md`, PDFs in `s/` |
| CV PDF and its displayed date | `_data/profile.yml`, PDF in `s/` |
| CV page text | `cv.md` |
| Email, portrait and social link | `_data/profile.yml` |
| Navigation | `_data/navigation.yml` |
| Site address and metadata | `_config.yml` |
| Shared page structure | `_layouts/` and `_includes/` |
| Colours, spacing and responsive layout | `assets/css/style.css` |

### Add a publication

Append or insert an entry in `_data/publications.yml`. The list displays in file order. Quote titles or details containing a colon.

```yaml
- title: "Paper title: A subtitle"
  coauthors: First Author and Second Author # optional
  venue: Journal name
  details: "12(3), 100–120"                # optional
  status: Online first                    # optional
  url: https://doi.org/your-doi             # optional
```

### Update the CV

Replace `s/YukselUmut_CV_May26_EN-78lc.pdf` and update `cv.updated` in `_data/profile.yml`. You may choose a clearer filename (e.g. `/s/umut-yuksel-cv.pdf`) and update `cv.file`; retain the previous file if you want old direct links to keep working. All displayed CV links use this single setting.

### Add a research project

Create `_projects/project-name.md` with `title`, `short_name` and `order` in its YAML front matter, using `claimax.md` as an example. Write the project description in Markdown. Project descriptions appear on the Research page in ascending `order`.

### Restore missing teaching documents

The two graduate syllabuses and the ESIL flyer returned 404 on the source site. The new page provides contact links. Add the recovered PDFs to `s/` and replace the corresponding contact links in `teaching.md`. Original URLs are recorded in `docs/migration.md`.

## Publish a review version on GitHub Pages

1. Sign into **umuttolo** and create a **public** repository named **umuttolo.github.io**. Leave it empty (do not generate a README, license or `.gitignore`). If it already exists, inspect its contents before uploading anything.
2. Push this repository, with the Jekyll source at its root. Do not upload `_site/`, `vendor/`, `.bundle/` or the repository ZIP itself. If using the browser upload, include hidden `.github/workflows/pages.yml`; pushing with Git is less error-prone.

   ```sh
   git add .
   git commit -m "Migrate academic website to Jekyll"
   git remote add origin https://github.com/umuttolo/umuttolo.github.io.git
   git push -u origin main
   ```

3. In **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source.
4. In **Actions**, run **Build, check and deploy Jekyll** if the initial push happened before Pages was enabled. Later pushes to `main` deploy automatically; pull requests build and check without deployment.
5. Confirm the workflow succeeds, then review **https://umuttolo.github.io/** on desktop and mobile, including the CV and teaching downloads.

Official references: [Create a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site), [custom publishing workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Keep umutyuksel.net after review

There is deliberately **no `CNAME` file**, and no changes have been made to Squarespace, DNS or the existing domain. You can review the GitHub address while the current site keeps serving normally.

After you approve the replacement, follow `docs/domain-cutover.md` to connect **umutyuksel.net**. Keep the existing Squarespace subscription active through verification. Domain registration and Squarespace website hosting are separate services; moving the site does not require moving the domain registrar.

## Structure and compatibility

- Jekyll 4.4 with a committed dependency lockfile and a GitHub Actions workflow.
- Standard Markdown, YAML, Liquid, HTML and CSS; no custom Jekyll plugins.
- Responsive layouts, keyboard focus styles, skip link, semantic headings, descriptive image text and reduced-motion support.
- Existing page routes are retained: `/`, `/research/`, `/teaching/`, `/pagecv/`. `/about/` redirects to `/`; `/cv/` redirects to `/pagecv/`. GitHub Pages resolves extensionless paths to these directories.
- Working `/s/` document paths are preserved. A local portrait replaces the Squarespace CDN dependency.
- The HTML 404 page, sitemap, canonical metadata and social preview metadata are included.
- Source content and images belong to their respective owners. No blanket open-source license has been added to your academic content.
