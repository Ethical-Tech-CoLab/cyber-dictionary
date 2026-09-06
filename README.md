# Cyber Dictionary

**A vocabulary of technology and cybersecurity, defined plainly — and a library of open
sources you can build with.**

Live site: <https://ethical-tech-colab.github.io/cyber-dictionary/>

Two rooms, one site.

## 1. The Dictionary

A working dictionary of the terms, protocols, attacks and frameworks that come up on the
job — from `zero-day` and `Kerberoasting` down to the everyday delivery vocabulary of
`push`, `commit`, `sync` and `deploy`, down to the `GPU`, `VRAM` and `quantisation`
underneath it all — and out to the agencies that investigate when it goes wrong, and the
classification and personal-data categories that decide who may see what. Built for quick lookups, not long reading, and divided by term and by
domain.

**1,170 terms across 15 domains:**

| Domain | Terms |
|---|---|
| Networking & Protocols | 205 |
| Cryptography | 81 |
| Identity & Access | 89 |
| Attacks & Exploitation | 112 |
| Malware & Threat Actors | 61 |
| Application Security | 62 |
| Cloud & Infrastructure | 42 |
| Endpoints & Systems | 85 |
| Defense & Operations | 78 |
| Governance, Risk & Compliance | 77 |
| AI & Emerging Tech | 38 |
| Dev & Delivery | 65 |
| Compute & Hardware | 54 |
| Intelligence & Investigations | 92 |
| Classification & Personal Data | 29 |

Every definition is one or two sentences of plain English, written to answer the question
you actually had when you looked the term up. Terms that go by more than one name carry
their synonyms — *MitM*, *2FA*, *pentest*, *rDNS*, *K8s*, *laptop farm* — which are searched
and shown, so you find the entry using the words you already use. The search forgives
spacing and punctuation (*MI 5*, *MI-5* and *MI5* are one query), forgives a typo or two
(*kerberoasing*, *ransomeware*, *sandwrom*), and answers to initials even where nobody wrote
the acronym down (*MLAT*, *SoD*, *CCDCOE*). Coverage of the classical vocabulary was
checked against the SANS Institute's *Glossary of Security Terms*; the wording here is our
own throughout.

## 2. The Database Library

The feeling of walking into a library — except instead of books you find **open data
sources, open-source technologies and the communities behind them**, ready to wire into a
project. Browse the shelves, pull a spine, and you get what it is, how to reach the API,
and what it costs.

**105 sources across 11 shelves:** Satellite & Earth Observation · Maps & Geospatial ·
Climate & Weather · Population & Development · Conflict, Rights & Humanitarian ·
Environment & Biodiversity · Health · Economy, Trade & Corporate · Security & Threat Data ·
Geospatial Tooling · Communities & Programmes.

Each entry records:

- **What it is** — what the dataset or tool actually gives you
- **How to connect** — the specific API, client library, or download route, including
  whether you need a key and what the gotchas are
- **Access** — free, free tier, non-commercial, or paid

## 3. The case studies

Twenty documented incidents, 2010 to 2025 — Stuxnet, Silk Road, Target, Sony Pictures,
Ashley Madison, Mirai, the Bangladesh Bank heist, Equifax, NotPetya, WannaCry, SolarWinds,
the 2020 Twitter takeover, Colonial Pipeline, Log4Shell, the Irish health service, Conti
against Costa Rica, the British Library, Jaguar Land Rover, Marks & Spencer, and the North
Korean IT worker schemes — each written to the same four headings: what happened, how it worked,
how it was found, and what changed. The third is usually the most interesting.

Every case cites public primary sources, and cross-references the dictionary terms it turns
on. Those cross-references are checked at build time: `tools/build_cases.py` refuses to
build if a case points at a term nobody has written, which is how several terms came to
exist.

The markdown in [`cases/`](cases/) is the source of truth; `cases.js` is generated from it.

```sh
python3 tools/build_cases.py
```

## 4. The printed editions

Two volumes, because a dictionary and a catalogue are read differently — one is scanned
A to Z, the other browsed shelf by shelf.

| | | |
|---|---|---|
| **Volume I** | *The Cyber Dictionary* | 1,170 terms, A–Z in two justified columns · [PDF](book/dictionary/cyber-dictionary.pdf) |
| **Volume II** | *The Database Library* | 105 sources, by shelf, with how to connect · [PDF](book/library/database-library.pdf) |

Both are readable in the browser as page-turn books — the two buttons in the header —
and downloadable as A5 PDFs.

Neither is written by hand. Both are generated from the same `terms.js` and `library.js`
the site itself loads, so the book can never drift from the website:

```sh
python3 tools/build_book.py
```

It prints each volume through headless Chrome, then renders the pages to WebP for the
in-browser reader. Needs Google Chrome, PyMuPDF and Pillow. Re-run it after adding terms.

## Methodology

The site's fourth tab documents how all of this was assembled — how a definition is
written and what that costs in precision, where the terms came from, how the library
entries were checked, how case studies are chosen, what is verified mechanically, how the
search scores a match, and what this reference is *not*. Worth reading before citing it.

## Editing

No build step, no dependencies, no framework. Three files do the work:

- `terms.js` — the dictionary. `{t: term, a: abbreviation, d: domain, def: definition, s: synonyms}`
- `library.js` — the library. `{n: name, o: organisation, u: url, s: shelf, w: what it is,
  h: how to connect, c: cost}`
- `index.html` — the whole interface, inline

Add an entry by appending an object to the relevant array. To add a domain or shelf, add it
to `window.DOMAINS` / `window.SHELVES` first — entries whose category is not listed there
will not render.

Open `index.html` in a browser to check your change. It works from `file://` — the data is
loaded as plain scripts rather than fetched, precisely so it does. The one exception is the
book reader, which is an ES module: it needs the page served over HTTP, so use the server
command below if you are testing that.

```bash
git clone https://github.com/Ethical-Tech-CoLab/cyber-dictionary.git
cd cyber-dictionary
open index.html          # or: python3 -m http.server 8000
```

## Deployment

GitHub Pages, serving `main` at the repository root. Pushing to `main` publishes.

## Contributing

Corrections and additions are welcome by pull request. Two rules:

1. **Define it plainly.** If a definition needs another definition to make sense, rewrite it.
   Say what the term means and, where it earns its place, why it matters in practice.
2. **Database library entries must be verifiable.** Link the real project, and describe the access
   route specifically enough that someone could follow it — name the API, the client
   library, the key requirement.

## Credits

Built and maintained by [Ethical Tech CoLab](https://github.com/Ethical-Tech-CoLab).

The idea for a plain-language cyber dictionary came from a shared artifact by a colleague
of the CoLab; this repository is an independent implementation, written from scratch, with
the library section added as a second half.

## Licence

Prose — definitions and source notes — is released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Code is released under the MIT licence (see `LICENSE`).

Every project in the library carries its own licence. Check it before you ship.
