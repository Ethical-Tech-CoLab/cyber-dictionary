#!/usr/bin/env python3
"""Rewrite every count in README.md from the data itself.

Counts were being typed by hand and going stale within a commit or two. The
numbers live between markers so this can be run any time, and so a stale README
is a build failure rather than something a reader discovers.

    python3 tools/update_counts.py           # rewrite
    python3 tools/update_counts.py --check   # fail if the README is stale
"""
import argparse, datetime, os, re, subprocess, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def data():
    js = """
      global.window={};
      require('%s/terms.js'); require('%s/library.js'); require('%s/cases.js');
      const c={}; window.TERMS.forEach(x=>c[x.d]=(c[x.d]||0)+1);
      const s={}; window.SOURCES.forEach(x=>s[x.s]=(s[x.s]||0)+1);
      console.log(JSON.stringify({
        terms: window.TERMS.length, domains: window.DOMAINS,
        domainCounts: c, sources: window.SOURCES.length,
        shelves: window.SHELVES, shelfCounts: s, cases: window.CASES.length,
        refs: window.CASES.reduce((a,x)=>a+x.sources.length,0),
      }));""" % (ROOT, ROOT, ROOT)
    return json.loads(subprocess.run(["node", "-e", js], capture_output=True,
                                     text=True, check=True).stdout)


def render(d):
    """The generated block. Everything between the markers is replaced."""
    table = "\n".join("| %s | %d |" % (k, d["domainCounts"][k]) for k in d["domains"])
    shelves = " · ".join("%s (%d)" % (s, d["shelfCounts"][s]) for s in d["shelves"])
    return "\n".join([
        "**%s terms across %d domains, %d sources across %d shelves, and %d case studies "
        "citing %d references.**" % (f"{d['terms']:,}", len(d["domains"]), d["sources"],
                                     len(d["shelves"]), d["cases"], d["refs"]),
        "",
        "These figures are generated from the data by `tools/update_counts.py`, and they are"
        " correct as at the last commit rather than fixed. The collection grows: treat any"
        " number quoted elsewhere — in a paper, a slide, or an older copy of this file — as a"
        " snapshot of when it was written, and cite the dated release rather than the count.",
        "",
        "| Domain | Terms |",
        "|---|---|",
        table,
        "",
        "**Shelves:** " + shelves + ".",
    ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    path = os.path.join(ROOT, "README.md")
    text = open(path, encoding="utf-8").read()
    block = render(data())
    marker = re.compile(r"<!-- counts:start -->.*?<!-- counts:end -->", re.S)
    if not marker.search(text):
        raise SystemExit("README.md has no <!-- counts:start --> block")
    new = marker.sub(lambda m: "<!-- counts:start -->\n" + block + "\n<!-- counts:end -->",
                     text, count=1)

    if new == text:
        print("counts already current")
        return
    if args.check:
        raise SystemExit("README counts are stale — run: python3 tools/update_counts.py")
    open(path, "w", encoding="utf-8").write(new)
    print("counts updated")


if __name__ == "__main__":
    main()
