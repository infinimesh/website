#!/usr/bin/env python3
"""Fail if a sitemap URL or an infinimesh.org link in llms*.txt has no file in the repo."""
import os
import re
import sys
import xml.etree.ElementTree as ET

SITE = "https://infinimesh.org"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def to_file(url):
    path = url[len(SITE):].split("#")[0].split("?")[0] or "/"
    local = os.path.join(ROOT, path.lstrip("/"))
    if path.endswith("/"):
        local = os.path.join(local, "index.html")
    return local


def main():
    bad = []
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(os.path.join(ROOT, "sitemap.xml"))
    urls = [("sitemap.xml", loc.text.strip()) for loc in tree.findall(".//s:loc", ns)]
    for name in ("llms.txt", "llms-full.txt"):
        with open(os.path.join(ROOT, name), encoding="utf-8") as f:
            for url in re.findall(r"https?://infinimesh\.org[^\s)\]>\"'`]*", f.read()):
                urls.append((name, url.rstrip(".,;:")))
    for source, url in urls:
        if not url.startswith(SITE):
            bad.append(f"{source}: {url} is not on {SITE}")
        elif not os.path.isfile(to_file(url)):
            bad.append(f"{source}: {url} has no file ({os.path.relpath(to_file(url), ROOT)})")
    for line in bad:
        print(line)
    if bad:
        sys.exit(1)
    print(f"site urls ok: {len(urls)} checked")


if __name__ == "__main__":
    main()
