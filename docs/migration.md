# Migration audit — 20 October 2026

Source: https://www.umutyuksel.net/. Discovery used its public sitemap, all navigation links and the HTML of every published content page. The About page at `/about` duplicates the homepage. No Squarespace account, site settings, subscription or DNS records were modified.

## Page coverage

| Original route | New route | Content |
| --- | --- | --- |
| `/` and `/about` | `/` with `/about/` redirect | Full biography, institutional links, original portrait, research interests |
| `/research` | `/research/` | CLAIMAX project, research overview, 7 publications with venues/coauthors/details, 2 working papers, draft request note |
| `/teaching` | `/teaching/` | Both graduate courses, both undergraduate courses, methods sequence, 3 modules, 2022 workshop, teaching in 2023–25, invited teaching and assistantship |
| `/pagecv` | `/pagecv/` plus `/cv/` alias | Original 8-page CV, labelled May 2026 from its filename |
| Shared footer | All main pages | Contact invitation, email and six original language invitations |
| Shared Twitter link | Shared footer | https://twitter.com/umuttolo (upgraded from HTTP) |

`source-inventory.json` retains extracted source text, links, titles and image URLs to support review. It is excluded from the published build. The sitemap contained no additional content pages. The unused `/cart` link is Squarespace template infrastructure, not academic content.

## Design observed and simplified

The original uses a white background, serif typography, a horizontal name/navigation header, underlined muted-blue links, a portrait to the left of the biography, text-led research, four teaching sections, a minimal CV page and a shared multilingual footer. The migration retains that information structure, portrait and restrained presentation. System sans-serif typography, dark teal links, consistent content widths and quiet dividers simplify it. Mobile navigation stays visible and requires no JavaScript. Squarespace scripts, commerce, animation, tracking, remote fonts and stock-template components are omitted.

The teaching sitemap lists three stock images (`20140301_Trade-151_012-2.jpg`, `20140228_Trade 151_0046.jpg`, `Aro Ha_0428.jpg`). They are template metadata, not rendered `<img>` elements in the teaching page. They are not added as new visible content. The original portrait was served by its CDN as WebP despite its `.jpg` URL; the local filename uses the actual `.webp` format.

## Assets copied and verified

| Local path | Source path | Result |
| --- | --- | --- |
| `assets/images/umut-yuksel.webp` | Squarespace CDN portrait in source inventory | 111,630-byte WebP, 736 × 928 |
| `s/YukselUmut_CV_May26_EN-78lc.pdf` | Same `/s/` path | 140,168-byte PDF, 8 pages |
| `s/Guia-docent-nou-esborrany-2023_20624_ca.pdf` | Same `/s/` path | 11,215-byte PDF, 2 pages |
| `s/2024_23616_ca.pdf` | Same `/s/` path | 15,354-byte PDF, 4 pages |

Source files are copied without editing. Existing valid document URLs are retained on the new site. Future content editing is centralised in Markdown/YAML rather than embedded in layouts.

## Missing on the original site

These source URLs returned **HTTP 404** on 20 October 2026:

- https://www.umutyuksel.net/s/RI-SP038-Syllabus-October-update.pdf
- https://www.umutyuksel.net/s/MINT203-Syllabus-August.pdf
- https://www.umutyuksel.net/s/Poster_ESIL-Workshop.pdf

No replacement documents were fabricated. Their associated courses and workshop remain on the Teaching page, with clear request-by-email links. Add the PDFs and update `teaching.md` if you recover them.

## Content editing choices

Academic claims, publication order, publication status and existing institutional/publisher destinations are preserved as observed; no dates or publication metadata were guessed. Minor source grammar was corrected: “institutions influences” → “institutions influence” and “I have this compulsory course” → “I have taught this compulsory course”. Punctuation/quotation marks are normalised. The multilingual invitations have individual language attributes. Page titles and descriptive download labels were added for navigation and accessibility.

## Publication status

The initial requested URL `umutyuksel.github.io` requires the `umutyuksel` account or organization. The available connection reports `umuttolo` and returns no accessible repositories; `umutyuksel/umutyuksel.github.io` returns 404. The site is configured for `umuttolo.github.io` and can later use `umutyuksel.net`. See the README for the publishing steps. No `CNAME` file or domain cutover is included in the review version.

The `umuttolo/umuttolo.github.io` repository also returned 404 through the connection. The browser's repository-creation page redirects to GitHub sign-in. No repository has been created, source pushed, or deployment claimed. Publishing requires a signed-in GitHub session or access to a repository you create.

## External link verification

`external-link-check.json` records the source destinations' HTTP responses. Several institutional and publisher sites return 403 to automated requests; Springer redirects through its cookie-handling flow. These results do not establish that their pages are missing. Their original URLs are retained, with no substitute destinations guessed. The old HTTP Twitter link was upgraded to HTTPS. Unlike these restricted external responses, the three missing `/s/` files return Squarespace's actual 404 page.
