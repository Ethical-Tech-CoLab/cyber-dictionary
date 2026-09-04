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

**1,020 terms across 15 domains:**

| Domain | Terms |
|---|---|
| Networking & Protocols | 192 |
| Cryptography | 70 |
| Identity & Access | 75 |
| Attacks & Exploitation | 71 |
| Malware & Threat Actors | 56 |
| Application Security | 41 |
| Cloud & Infrastructure | 38 |
| Endpoints & Systems | 77 |
| Defense & Operations | 71 |
| Governance, Risk & Compliance | 74 |
| AI & Emerging Tech | 38 |
| Dev & Delivery | 65 |
| Compute & Hardware | 54 |
| Intelligence & Investigations | 70 |
| Classification & Personal Data | 28 |

Every definition is one or two sentences of plain English, written to answer the question
you actually had when you looked the term up. Terms that go by more than one name carry
their synonyms — *MitM*, *2FA*, *pentest*, *rDNS*, *K8s*, *laptop farm* — which are searched
and shown, so you find the entry using the words you already use. Coverage of the classical vocabulary was
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

## 3. The printed edition

The same collection set as a book: the dictionary in two justified columns running A to Z,
the library as catalogue cards walked shelf by shelf. **Read as book** in the header opens
a page-turning reader over it, and the PDF is at
[`book/cyber-dictionary.pdf`](book/cyber-dictionary.pdf).

The pages are typeset from `terms.js` and `library.js` — the same two files the search box
reads — so the printed and searchable editions cannot drift apart in wording. The typesetting
itself lives in the CoLab website repo at `src/app/print/cyber-dictionary/`, which pulls this
repo's data with `scripts/sync-cyber-dictionary.mjs` and prints the PDF with
`npm run render:books cyber-dictionary`. After a substantial round of new entries, re-run
those two there and copy the result back into `book/`.

The reader is [read-as-book](https://github.com/Ethical-Tech-CoLab/read-as-book) and its
`page-flip` dependency, both vendored under `vendor/` rather than pulled from a CDN so the
site stays buildless and needs no network beyond its own origin.

## Editing

No build step, no dependencies, no framework. Three files do the work:

- `terms.js` — the dictionary. `{t: term, a: abbreviation, d: domain, def: definition}`
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
