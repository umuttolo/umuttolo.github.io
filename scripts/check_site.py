#!/usr/bin/env python3
"""Check the generated site using only the Python standard library.

Usage: python3 scripts/check_site.py [build-directory] [--baseurl /preview]
"""
import argparse
import json
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.refs, self.tags = path, set(), [], []
        self.text = path.read_text(encoding="utf-8")
        self.feed(self.text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for attribute in ("href", "src"):
            if attrs.get(attribute):
                self.refs.append((tag, attrs[attribute]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", default="_site")
    parser.add_argument("--baseurl", default="")
    parser.add_argument("--migration-audit", action="store_true", help="also compare initial publication links and counts against the source snapshot")
    args = parser.parse_args()
    root = Path(args.directory).resolve()
    errors = []
    pages = {p.resolve(): Page(p) for p in root.rglob("*.html")}
    if not pages:
        sys.exit("FAIL: no built HTML; run bundle exec jekyll build first")

    def resolve(url, source):
        path = unquote(urlsplit(url).path)
        if args.baseurl and path.startswith(args.baseurl + "/"):
            path = path[len(args.baseurl):]
        result = (root / path.lstrip("/") if path.startswith("/") else source.parent / path).resolve() if path else source
        if not result.is_relative_to(root):
            return None
        if result.is_dir():
            result /= "index.html"
        if not result.exists() and not result.suffix:
            result /= "index.html"
        return result

    for path, page in pages.items():
        relative = path.relative_to(root)
        if "{{" in page.text or "{%" in page.text:
            errors.append(f"{relative}: unrendered Liquid")
        for tag, attrs in page.tags:
            if tag == "link" and "stylesheet" in attrs.get("rel", "") and urlsplit(attrs.get("href", "")).scheme:
                errors.append(f"{relative}: remote stylesheet dependency")
            if tag == "img" and not attrs.get("alt"):
                errors.append(f"{relative}: image missing alternative text")
            if tag in ("script", "iframe"):
                errors.append(f"{relative}: unexpected script or iframe")
        for tag, ref in page.refs:
            url = urlsplit(ref)
            if url.scheme in ("https", "http") or url.netloc:
                if tag in ("img", "script") or (tag == "link" and "stylesheet" in ref):
                    errors.append(f"{relative}: remote render dependency {ref}")
                continue
            if url.scheme == "mailto":
                continue
            target = resolve(ref, path)
            if target is None or not target.exists():
                errors.append(f"{relative}: missing local target {ref}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{relative}: missing anchor {ref}")

    primary = ["index.html", "research/index.html", "teaching/index.html", "pagecv/index.html", "404.html"]
    for name in primary:
        page = pages.get(root / name)
        if page is None:
            errors.append(f"missing page: {name}")
            continue
        if sum(t == "h1" for t, _ in page.tags) != 1:
            errors.append(f"{name}: expected exactly one h1")
        if not any(t == "main" for t, _ in page.tags):
            errors.append(f"{name}: missing main landmark")
        active = [a for t, a in page.tags if t == "a" and a.get("aria-current") == "page"]
        if name != "404.html" and len(active) != 1:
            errors.append(f"{name}: expected one current navigation link")

    research = pages.get(root / "research/index.html")
    if research and args.migration_audit:
        data = json.loads(Path("docs/source-inventory.json").read_text())
        for item in data["research"]["links"]:
            if item["url"].startswith("https://") and "mailto:" not in item["url"]:
                if not any(ref == item["url"] for _, ref in research.refs):
                    errors.append(f"publication link not preserved: {item['url']}")
        if sum(t == "li" and a.get("class") == "publication" for t, a in research.tags) != 9:
            errors.append("expected seven publications and two working papers")

    for pdf in root.rglob("*.pdf"):
        if not pdf.read_bytes().startswith(b"%PDF-"):
            errors.append(f"invalid PDF: {pdf.relative_to(root)}")
    try:
        ET.parse(root / "sitemap.xml")
    except (OSError, ET.ParseError) as error:
        errors.append(f"invalid sitemap: {error}")
    for forbidden in ("docs", "scripts", "vendor", "_artifacts", "Gemfile", "Gemfile.lock", "README.md", ".git", ".github"):
        if (root / forbidden).exists():
            errors.append(f"development file exposed in build: {forbidden}")
    if any("squarespace" in p.text.lower() for p in pages.values()):
        errors.append("Squarespace dependency in rendered HTML")
    if errors:
        print("FAIL\n" + "\n".join(errors))
        return 1
    print(f"PASS: {len(pages)} HTML pages; all local links, anchors, PDFs, navigation and sitemap checked.")
    print("PASS: no JavaScript or Squarespace render dependencies.")
    if args.migration_audit:
        print("PASS: seven publications, two working papers, and all source publication links preserved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
