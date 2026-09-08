#!/usr/bin/env python3
"""Check every URL the collection points at, and record what was found.

A reference work's whole claim is that you can go and check it. These links
rot quietly: nothing in the repository notices when a government reshuffles
its site or a company retires a blog. This walks all of them and writes
link-status.json, which the build then stamps onto each entry so the page can
say plainly what is known about a link.

    python3 tools/check_links.py                  # check everything
    python3 tools/check_links.py --only cases     # or just one collection
    python3 tools/check_links.py --fail-on-dead   # exit non-zero for CI

Three states, and the distinction matters:

    ok          fetched successfully on the date recorded
    unverified  never successfully fetched — including everything that has
                not been checked yet. Not a claim that it is broken.
    dead        the server answered, and said there is nothing there (4xx),
                twice, on separate runs

Anything that merely timed out or refused a connection stays unverified
rather than being called dead: a network fault here is not evidence about
the far end.
"""
import argparse, concurrent.futures, datetime, json, os, re, ssl, sys
import urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATUS_FILE = os.path.join(ROOT, "link-status.json")
TODAY = datetime.date.today().isoformat()

# Plenty of government sites are slow, and some object to a default agent.
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
TIMEOUT = 25


def collect():
    """Every outbound URL, with where it came from, so a report can name it."""
    found = {}

    def add(url, where):
        found.setdefault(url, set()).add(where)

    for name in sorted(os.listdir(os.path.join(ROOT, "cases"))):
        if not name.endswith(".md") or name == "README.md":
            continue
        text = open(os.path.join(ROOT, "cases", name), encoding="utf-8").read()
        front = text.split("---\n")[1] if text.startswith("---\n") else ""
        for url in re.findall(r"^\s+url:\s*(\S+)", front, flags=re.M):
            add(url.strip('"'), "cases/" + name)

    lib = open(os.path.join(ROOT, "library.js"), encoding="utf-8").read()
    for entry in re.finditer(r'\{n:"((?:[^"\\]|\\.)*)".*?u:"([^"]+)"', lib):
        add(entry.group(2), "library: " + entry.group(1))

    return {u: sorted(w) for u, w in found.items()}


def fetch(url):
    """HEAD first, then GET: many servers refuse HEAD but serve the page."""
    ctx = ssl.create_default_context()
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method,
                                     headers={"User-Agent": UA,
                                              "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
                return r.status, None
        except urllib.error.HTTPError as e:
            if e.code in (403, 405, 406) and method == "HEAD":
                continue                      # try a real GET before judging
            if e.code in (403, 429):
                # Refused us, not missing. Bot protection is not rot.
                return e.code, "blocked"
            return e.code, None
        except Exception as e:                # DNS, TLS, timeout, reset
            if method == "GET":
                return None, type(e).__name__
    return None, "unknown"


def classify(code, err, previous):
    if code and 200 <= code < 400:
        return "ok"
    if err == "blocked":
        # The link is probably fine; we simply are not allowed to confirm it.
        return "unverified"
    if code and 400 <= code < 500:
        # One 4xx is a maybe; two in a row is a finding.
        return "dead" if previous in ("dead", "missing-once") else "missing-once"
    return "unverified"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["cases", "library"])
    ap.add_argument("--fail-on-dead", action="store_true")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    urls = collect()
    if args.only:
        urls = {u: w for u, w in urls.items()
                if any(s.startswith(args.only) for s in w)}

    previous = {}
    if os.path.exists(STATUS_FILE):
        previous = json.load(open(STATUS_FILE, encoding="utf-8")).get("links", {})

    results = {}
    with concurrent.futures.ThreadPoolExecutor(args.workers) as pool:
        for url, (code, err) in zip(urls, pool.map(fetch, urls)):
            was = previous.get(url, {}).get("state")
            state = classify(code, err, was)
            entry = {"state": state, "used_by": urls[url]}
            if code:
                entry["code"] = code
            if err:
                entry["error"] = err
            if state == "ok":
                entry["checked"] = TODAY
            elif was and previous[url].get("checked"):
                entry["checked"] = previous[url]["checked"]   # last known good
            results[url] = entry

    json.dump({"generated": TODAY, "links": dict(sorted(results.items()))},
              open(STATUS_FILE, "w", encoding="utf-8"), indent=1)

    counts = {}
    for r in results.values():
        counts[r["state"]] = counts.get(r["state"], 0) + 1
    order = ["ok", "unverified", "missing-once", "dead"]
    print("%d links: %s" % (len(results),
          ", ".join("%d %s" % (counts[k], k) for k in order if k in counts)))

    bad = {u: r for u, r in results.items() if r["state"] in ("dead", "missing-once")}
    if bad:
        print("\nNeeds attention:")
        for u, r in sorted(bad.items(), key=lambda kv: kv[1]["state"], reverse=True):
            print("  [%s %s] %s" % (r["state"], r.get("code", ""), u))
            for w in r["used_by"]:
                print("      used by %s" % w)

    if args.fail_on_dead and any(r["state"] == "dead" for r in results.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
