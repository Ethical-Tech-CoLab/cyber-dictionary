#!/usr/bin/env python3
"""Turn cases/*.md into cases.js, the way terms.js and library.js are loaded.

The markdown is the source of truth. This only reshapes it, and checks two
things worth failing over: that every case has the headings the site renders,
and that every term a case cross-references actually exists in the dictionary.
A case study that points at a term nobody wrote is a broken link.

    python3 tools/build_cases.py
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADINGS = ["What happened", "How it worked", "How it was found", "What changed"]
# Two cases are written in the present tense, because they are still running.
HEADING_ALIASES = {"How it works": "How it worked", "How it is found": "How it was found"}


def parse_front_matter(text, path):
    """Enough YAML for this format, and no more.

    Scalars, inline lists, and a list of indented mappings for sources. Values
    are split on the first colon only, because every URL contains one.
    """
    if not text.startswith("---\n"):
        sys.exit("%s: no front matter" % path)
    _, fm, body = text.split("---\n", 2)
    meta, key = {}, None
    for raw in fm.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indented = raw[0] in " \t"
        line = raw.strip()

        if line.startswith("- "):                       # a new item in a list
            if key is None:
                sys.exit("%s: list item outside a list: %s" % (path, line))
            item = line[2:].strip()
            if ":" in item:
                k, v = item.split(":", 1)
                meta[key].append({k.strip(): v.strip().strip('"')})
            else:
                meta[key].append(item.strip('"'))
            continue

        if indented and key and meta[key] and isinstance(meta[key][-1], dict):
            k, v = line.split(":", 1)               # a field of the last item
            meta[key][-1][k.strip()] = v.strip().strip('"')
            continue

        if ":" not in line:
            sys.exit("%s: cannot parse front matter line: %s" % (path, line))
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if v == "":
            key, meta[k] = k, []
        elif v.startswith("[") and v.endswith("]"):
            meta[k] = [t.strip() for t in v[1:-1].split(",") if t.strip()]
            key = None
        else:
            meta[k] = v.strip('"')
            key = None
    return meta, body


def parse_sections(body, path):
    parts = re.split(r"^##\s+(.+)$", body, flags=re.M)[1:]
    out = {}
    for heading, text in zip(parts[0::2], parts[1::2]):
        heading = HEADING_ALIASES.get(heading.strip(), heading.strip())
        # Rewrap: the file is hard-wrapped for reading, the page is not.
        paragraphs = [re.sub(r"\s+", " ", p).strip()
                      for p in re.split(r"\n\s*\n", text) if p.strip()]
        out[heading] = paragraphs
    missing = [h for h in HEADINGS if h not in out]
    if missing:
        sys.exit("%s: missing heading(s): %s" % (path, ", ".join(missing)))
    return out


def js_safe(text):
    """JSON is not quite a subset of JavaScript.

    U+2028 and U+2029 are ordinary characters in JSON and line terminators in
    JavaScript, so a case study containing one would produce a file that parses
    as JSON and not as the script this actually is.
    """
    return text.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def link_status():
    """What the last link check found, keyed by URL.

    Absent file means nothing has been checked, and every reference is
    therefore unverified — which is the honest default rather than a failure.
    """
    path = os.path.join(ROOT, "link-status.json")
    if not os.path.exists(path):
        return {}
    return json.load(open(path, encoding="utf-8")).get("links", {})


def main():
    # The dictionary is the authority on what a term is called.
    terms_src = open(os.path.join(ROOT, "terms.js"), encoding="utf-8").read()
    known = set(re.findall(r'\{t:"((?:[^"\\]|\\.)*)"', terms_src))

    status = link_status()
    cases, problems = [], []
    folder = os.path.join(ROOT, "cases")
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md") or name == "README.md":
            continue
        path = os.path.join(folder, name)
        meta, body = parse_front_matter(open(path, encoding="utf-8").read(), path)
        sections = parse_sections(body, path)
        for src in meta.get("sources", []):
            if not isinstance(src, dict) or not src.get("url") or not src.get("title"):
                problems.append("%s: source needs both a title and a url: %r" % (name, src))
            # A reference becomes an href on the page. Anything but http(s) —
            # javascript:, data: — would run rather than navigate, so the
            # scheme is checked here rather than trusted at render time.
            elif not re.match(r"^https?://", src["url"]):
                problems.append("%s: source url must be http(s): %r" % (name, src["url"]))
        for term in meta.get("terms", []):
            if term not in known:
                problems.append("%s: cross-references unknown term %r" % (name, term))
        cases.append({
            "id": name[:-3],
            "title": meta.get("title", name[:-3]),
            "year": str(meta.get("year", "")),
            "where": meta.get("where", ""),
            "actor": meta.get("actor", ""),
            "sector": meta.get("sector", ""),
            "kind": meta.get("kind", ""),
            "cost": meta.get("cost", ""),
            "terms": meta.get("terms", []),
            "sources": [dict(src,
                             state=status.get(src["url"], {}).get("state", "unverified"),
                             checked=status.get(src["url"], {}).get("checked", ""))
                        for src in meta.get("sources", [])],
            "sections": [{"heading": h, "paragraphs": sections[h]} for h in HEADINGS],
        })

    if problems:
        sys.exit("Broken cross-references:\n  " + "\n  ".join(problems))

    cases.sort(key=lambda c: (c["year"], c["title"]))
    out = ("/* Cyber Dictionary — case studies.\n"
           "   GENERATED by tools/build_cases.py from cases/*.md — do not edit by hand.\n"
           "   Loaded as a plain script, like terms.js, so the page works from file://. */\n"
           "window.CASES = %s;\n" % js_safe(json.dumps(cases, indent=1, ensure_ascii=False)))
    open(os.path.join(ROOT, "cases.js"), "w", encoding="utf-8").write(out)
    linked = sum(len(c["terms"]) for c in cases)
    print("✓ %d case studies, %d term cross-references, all resolving → cases.js"
          % (len(cases), linked))


if __name__ == "__main__":
    main()
