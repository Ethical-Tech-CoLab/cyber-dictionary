#!/usr/bin/env python3
"""Build the printed editions from the same data the site uses.

Two volumes, because the dictionary and the library are read differently:
a dictionary is scanned A to Z, a catalogue is browsed shelf by shelf.

    python3 tools/build_book.py

Produces, for each volume, a PDF and the page images the in-browser
page-turn viewer reads:

    book/dictionary/cyber-dictionary.pdf   book/dictionary/pages/*.webp
    book/library/database-library.pdf      book/library/pages/*.webp

Needs Google Chrome (headless, for printing), PyMuPDF and Pillow.
"""
import json, os, re, shutil, subprocess, sys, tempfile, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
YEAR = datetime.date.today().year


# ---------- read the site's own data, so the book can never drift ----------

def read_js_array(path, var):
    """Pull one `window.X = [...]` literal out of a plain data script."""
    src = open(os.path.join(ROOT, path), encoding="utf-8").read()
    start = src.index("window.%s" % var)
    start = src.index("[", start)
    depth, i = 0, start
    while True:
        c = src[i]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                break
        elif c == '"':                       # skip strings, brackets and all
            i += 1
            while src[i] != '"':
                i += 2 if src[i] == "\\" else 1
        i += 1
    body = src[start:i + 1]
    body = re.sub(r"/\*.*?\*/", "", body, flags=re.S)          # drop comments
    body = re.sub(r"([{,])\s*([A-Za-z_]\w*)\s*:", r'\1"\2":', body)  # quote keys
    body = re.sub(r",\s*([\]}])", r"\1", body)                 # trailing commas
    return json.loads(body)


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


# ---------- the shared look of both volumes ----------

CSS = """
@page { size: A5; margin: 14mm 13mm 16mm; }
@page:first { margin: 0; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; }
body {
  font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  font-size: 8.6pt; line-height: 1.34; color: #16121c;
  /* Narrow justified columns need hyphenation or the word spacing goes to
     pieces; Chrome still wants the prefix, and the language on <html>. */
  hyphens: auto; -webkit-hyphens: auto; hyphenate-limit-chars: 6 3 3;
}
h1, h2, h3, .mono { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }
.mono { font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; }

/* ---- title page ---- */
.title {
  page-break-after: always; height: 100vh; display: flex; flex-direction: column;
  justify-content: center; padding: 26mm 20mm; color: #f3eefb;
  background: linear-gradient(160deg, #241636 0%, #120c1a 55%, #1b1226 100%);
}
.title .vol { font-size: 8pt; letter-spacing: .34em; text-transform: uppercase;
  color: #c8f04b; margin-bottom: 10mm; }
.title h1 { font-size: 27pt; line-height: 1.04; margin: 0 0 6mm; letter-spacing: -.02em; }
.title .sub { font-size: 10pt; line-height: 1.5; color: rgba(243,238,251,.72);
  max-width: 78mm; margin: 0 0 16mm; }
.title .count { font-size: 8pt; letter-spacing: .1em; color: rgba(243,238,251,.55); }
.title .foot { margin-top: auto; font-size: 8pt; letter-spacing: .1em;
  color: rgba(243,238,251,.5); }
.title .rule { width: 26mm; height: 2px; background: #c8f04b; margin: 0 0 9mm; }

/* ---- front matter ---- */
.front { page-break-after: always; }
.front h2 { font-size: 13pt; margin: 0 0 5mm; letter-spacing: -.01em; }
.front p { margin: 0 0 3.4mm; text-align: justify; }
.toc { width: 100%; border-collapse: collapse; margin-top: 6mm; font-size: 8.2pt; }
.toc td { padding: 1.5mm 0; border-bottom: .4pt solid #e5dff0; }
.toc td:last-child { text-align: right; color: #6b6478; width: 16mm; }

/* ---- the body: two justified columns ---- */
.cols { column-count: 2; column-gap: 6.5mm; column-fill: auto;
  column-rule: .4pt solid #e9e4f2; text-align: justify; }
.sec { break-inside: avoid-column; break-after: avoid-column;
  font-size: 15pt; letter-spacing: .1em; color: #3d1f75;
  margin: 5mm 0 2.5mm; padding-bottom: 1mm; border-bottom: 1.4pt solid #3d1f75; }
.sec:first-child { margin-top: 0; }
.shelf { break-inside: avoid-column; break-after: avoid-column;
  font-size: 9.4pt; font-weight: 700; letter-spacing: .04em; color: #3d1f75;
  margin: 5mm 0 2.4mm; padding-bottom: .9mm; border-bottom: .8pt solid #cfc4e4; }
.e { break-inside: avoid; margin: 0 0 2.1mm; orphans: 2; widows: 2; }
.e b { font-weight: 700; }
.e .abbr { font-style: italic; color: #4a4356; }
.e .dom { font-size: 6.4pt; letter-spacing: .08em; text-transform: uppercase;
  color: #7a7288; }
.e .syn { color: #6b6478; font-style: italic; }
.e .lbl { font-size: 6.4pt; letter-spacing: .07em; text-transform: uppercase;
  color: #3d1f75; }
.e a { color: #16121c; text-decoration: none; }
"""


def title_page(volume, title, subtitle, counts):
    return """
<section class="title">
  <div class="vol">%s</div>
  <div class="rule"></div>
  <h1>%s</h1>
  <p class="sub">%s</p>
  <p class="count">%s</p>
  <div class="foot">Ethical Tech CoLab · %d · CC BY 4.0</div>
</section>""" % (esc(volume), esc(title), esc(subtitle), esc(counts), YEAR)


# ---------- volume I: the dictionary ----------

def build_dictionary():
    domains = read_js_array("terms.js", "DOMAINS")
    terms = read_js_array("terms.js", "TERMS")
    terms.sort(key=lambda x: (x["t"].lower(), x["t"]))

    counts = {}
    for t in terms:
        counts[t["d"]] = counts.get(t["d"], 0) + 1

    rows = "".join('<tr><td>%s</td><td>%d</td></tr>' % (esc(d), counts.get(d, 0))
                   for d in domains)
    front = """
<section class="front">
  <h2>How to use this volume</h2>
  <p>Every term in the dictionary, set A to Z across two columns. Each entry gives the
  term, its abbreviation or expansion where it has one, a definition of a sentence or
  two in plain English, the other names it goes by, and the domain it belongs to.</p>
  <p>The domains are a way of dividing the subject, not a hierarchy: a term appears once,
  under the domain where someone would most likely go looking for it. The companion
  volume, <i>The Database Library</i>, catalogues the open data sources and open-source
  technologies to build with.</p>
  <p>Definitions are written in-house and released under CC BY 4.0. Coverage of the
  classical vocabulary was checked against the SANS Institute's
  <i>Glossary of Security Terms</i>; the wording here is our own throughout.</p>
  <table class="toc">%s<tr><td><b>Total</b></td><td><b>%d</b></td></tr></table>
</section>""" % (rows, len(terms))

    body, letter = [], None
    for t in terms:
        first = t["t"][0].upper()
        if not first.isalpha():
            first = "#"
        if first != letter:
            letter = first
            body.append('<h2 class="sec">%s</h2>' % esc(letter))
        e = ['<p class="e"><b>%s</b>' % esc(t["t"])]
        if t.get("a"):
            e.append(' <span class="abbr">%s</span>' % esc(t["a"]))
            e.append(' — ')
        else:
            e.append(' — ')
        e.append(esc(t["def"]))
        if t.get("s"):
            e.append(' <span class="syn">Also called %s.</span>' % esc(t["s"]))
        e.append(' <span class="dom">%s</span></p>' % esc(t["d"]))
        body.append("".join(e))

    html = ("<!doctype html><html lang='en'><meta charset='utf-8'>"
            "<title>The Cyber Dictionary</title>"
            "<style>%s</style>%s%s<div class='cols'>%s</div>" % (
                CSS,
                title_page("Volume I",
                           "The Cyber Dictionary",
                           "Technology and cybersecurity, defined plainly — from the "
                           "protocol on the wire to the agency that investigates when "
                           "it goes wrong.",
                           "%s terms · %d domains" % (f"{len(terms):,}", len(domains))),
                front, "".join(body)))
    return html, len(terms)


# ---------- volume II: the database library ----------

def build_library():
    shelves = read_js_array("library.js", "SHELVES")
    sources = read_js_array("library.js", "SOURCES")

    counts = {}
    for s in sources:
        counts[s["s"]] = counts.get(s["s"], 0) + 1
    rows = "".join('<tr><td>%s</td><td>%d</td></tr>' % (esc(s), counts.get(s, 0))
                   for s in shelves)
    front = """
<section class="front">
  <h2>How to use this volume</h2>
  <p>A catalogue of open data sources, open-source technologies and the communities
  behind them — satellite imagery, street maps, climate records, conflict data, threat
  feeds — arranged by shelf rather than alphabetically, because this is a volume you
  browse rather than look things up in.</p>
  <p>Each entry records what the source actually gives you, how to connect to it —
  the API, the client library or the download route, including whether you need a key —
  and what it costs. Every entry links to its own project: check each one's licence
  before you ship.</p>
  <p>The companion volume, <i>The Cyber Dictionary</i>, defines the vocabulary.</p>
  <table class="toc">%s<tr><td><b>Total</b></td><td><b>%d</b></td></tr></table>
</section>""" % (rows, len(sources))

    body = []
    for shelf in shelves:
        items = [s for s in sources if s["s"] == shelf]
        if not items:
            continue
        body.append('<h2 class="shelf">%s</h2>' % esc(shelf))
        for s in sorted(items, key=lambda x: x["n"].lower()):
            e = ['<p class="e"><b>%s</b> <span class="abbr">%s</span><br>'
                 % (esc(s["n"]), esc(s["o"]))]
            e.append(esc(s["w"]))
            e.append(' <span class="lbl">Connect</span> %s' % esc(s["h"]))
            e.append(' <span class="lbl">Access</span> %s' % esc(s["c"]))
            e.append(' <span class="dom">%s</span></p>'
                     % esc(re.sub(r"^https?://", "", s["u"]).rstrip("/")))
            body.append("".join(e))

    html = ("<!doctype html><html lang='en'><meta charset='utf-8'>"
            "<title>The Database Library</title>"
            "<style>%s</style>%s%s<div class='cols'>%s</div>" % (
                CSS,
                title_page("Volume II",
                           "The Database Library",
                           "Open data sources, open-source technologies and the "
                           "communities behind them — what each one gives you, and how "
                           "to wire it in.",
                           "%d sources · %d shelves" % (len(sources), len(shelves))),
                front, "".join(body)))
    return html, len(sources)


# ---------- print, then rasterise for the page-turn viewer ----------

def to_pdf(html, pdf_path):
    tmp = tempfile.mkdtemp()
    src = os.path.join(tmp, "book.html")
    open(src, "w", encoding="utf-8").write(html)
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf-no-header", "--virtual-time-budget=20000",
                    "--print-to-pdf=" + pdf_path, "file://" + src],
                   check=True, capture_output=True)
    shutil.rmtree(tmp, ignore_errors=True)


def to_pages(pdf_path, pages_dir, width=1100):
    import fitz
    from PIL import Image
    if os.path.isdir(pages_dir):
        shutil.rmtree(pages_dir)
    os.makedirs(pages_dir)
    doc = fitz.open(pdf_path)
    names = []
    for i, page in enumerate(doc, 1):
        zoom = width / page.rect.width
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        name = "p%02d.webp" % i
        img.save(os.path.join(pages_dir, name), "WEBP", quality=76, method=6)
        names.append(name)
    aspect = round(doc[0].rect.width / doc[0].rect.height, 4)
    json.dump({"generatedFrom": os.path.basename(pdf_path),
               "pageCount": len(names), "aspect": aspect, "pages": names},
              open(os.path.join(pages_dir, "manifest.json"), "w"), indent=2)
    doc.close()
    return len(names)


def build(name, html, count, folder, pdf_name, unit):
    pdf = os.path.join(ROOT, "book", folder, pdf_name)
    to_pdf(html, pdf)
    n = to_pages(pdf, os.path.join(ROOT, "book", folder, "pages"))
    size = os.path.getsize(pdf) / 1024
    print("  %-22s %5d %-8s %3d pages  %6.0f KB" % (name, count, unit, n, size))


if __name__ == "__main__":
    if not os.path.exists(CHROME):
        sys.exit("Google Chrome not found at %s" % CHROME)
    print("Building the printed editions:")
    html, n = build_dictionary()
    build("Volume I  Dictionary", html, n, "dictionary", "cyber-dictionary.pdf", "terms")
    html, n = build_library()
    build("Volume II Library", html, n, "library", "database-library.pdf", "sources")
    print("Done.")
