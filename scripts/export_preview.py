#!/usr/bin/env python3
"""Export a file-openable review copy and ZIPs without changing the Jekyll source.

Run after building: python3 scripts/export_preview.py
Output is ignored by Git and Jekyll in _artifacts/.
"""
import os
import re
import shutil
import subprocess
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


root = Path(__file__).resolve().parent.parent
build = root / "_site"
artifacts = root / "_artifacts"
preview = artifacts / "preview"
if not (build / "index.html").is_file():
    raise SystemExit("Build Jekyll before exporting a preview.")
artifacts.mkdir(exist_ok=True)
if preview.exists():
    shutil.rmtree(preview)
shutil.copytree(build, preview)


def local_url(value, page):
    url = urlsplit(value)
    if not value.startswith("/") or value.startswith("//"):
        return value
    target = preview / unquote(url.path).lstrip("/")
    if target.is_dir():
        target /= "index.html"
    value = os.path.relpath(target, page.parent)
    if url.query:
        value += "?" + url.query
    if url.fragment:
        value += "#" + url.fragment
    return value


for page in preview.rglob("*.html"):
    html = page.read_text()
    html = re.sub(r'(\b(?:href|src)=")([^"]+)(")', lambda m: m[1] + local_url(m[2], page) + m[3], html)
    html = re.sub(r'(content="0; url=)([^"]+)(")', lambda m: m[1] + local_url(m[2], page) + m[3], html)
    page.write_text(html)

with zipfile.ZipFile(artifacts / "website-review.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(preview.rglob("*")):
        if path.is_file():
            archive.write(path, "website-review/" + path.relative_to(preview).as_posix())

files = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root).decode().split("\0")
with zipfile.ZipFile(artifacts / "umuttolo.github.io-source.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    for name in sorted(set(filter(None, files))):
        path = root / name
        if path.is_file():
            archive.write(path, "umuttolo.github.io/" + name)

print("Review: " + str(preview / "index.html"))
print("Review ZIP: " + str(artifacts / "website-review.zip"))
print("Source ZIP: " + str(artifacts / "umuttolo.github.io-source.zip"))
