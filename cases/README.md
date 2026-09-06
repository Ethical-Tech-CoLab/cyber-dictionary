# Case studies

One file per case. Each is a real, documented incident, written the way the dictionary
entries are written: plainly, for someone who wants to understand what happened and why
it mattered, not for someone who already does.

`tools/build_cases.py` reads every `*.md` in this folder and writes `cases.js`, which the
site loads. The markdown is the source of truth — edit here, then re-run the build.

## Format

A YAML front-matter block, then the prose under fixed headings:

```markdown
---
title: The name the case is known by
year: 2017
where: Ukraine, then everywhere
actor: Sandworm (GRU Unit 74455)
sector: Logistics, pharmaceuticals, government
kind: Destructive attack
cost: About $10bn in global damage
terms: [Wiper, Supply chain attack, Sandworm]
sources:
  - title: Something published and checkable
    url: https://example.org/
---

## What happened
## How it worked
## How it was found
## What changed
```

Every heading is required. Keep `terms` to entries that actually exist in `terms.js` —
the build fails otherwise, which is the point: the case studies and the dictionary are
meant to hold together.
