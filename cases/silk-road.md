---
title: Silk Road
year: 2013
where: The Tor network
actor: Ross Ulbricht, operating as Dread Pirate Roberts
sector: Dark web marketplace
kind: Criminal marketplace and its takedown
cost: About $1.2bn in sales; a life sentence, commuted in 2025
terms: [Silk Road, Dark web, Tor, Hidden service, Operational security failure, Blockchain analysis, Cash-out, Takedown, Dark web archive]
sources:
  - title: "US Attorney, SDNY — Ross Ulbricht sentencing"
    url: https://www.justice.gov/usao-sdny/pr/ross-ulbricht-aka-dread-pirate-roberts-sentenced-manhattan-federal-court-life-prison
  - title: "FBI complaint against Ross Ulbricht (2013)"
    url: https://www.justice.gov/sites/default/files/usao-sdny/legacy/2015/03/25/Ulbricht%2C%20Ross%20Complaint.pdf
---

## What happened

Silk Road sold drugs at scale, on the open web, for two and a half years. It ran as a Tor
hidden service, took payment in bitcoin, and worked like any marketplace: vendor ratings,
escrow, dispute resolution, a customer service culture. It was seized in October 2013 and
its operator was arrested in a San Francisco public library, mid-session, with the laptop
open and unencrypted.

## How it worked

The anonymity was real and it was layered. The site was reachable only through Tor, so
neither buyers nor the server learned each other's addresses. Payment was in bitcoin, then
widely and wrongly believed to be anonymous. Escrow held funds until delivery, which gave
strangers a reason to trust each other.

None of that failed. What failed was everything around it.

## How it was found

Investigators did not break Tor. They found the earliest posts advertising the site on a
public forum, made months before launch under the handle *altoid* — and one later post by
the same handle giving a Gmail address containing Ulbricht's real name. Other threads
tied in: a Stack Overflow question about connecting to a hidden service, edited to change
the name a minute after posting. Customs intercepted forged identity documents shipped to
his address. Undercover agents bought from vendors and worked upward.

Bitcoin, meanwhile, turned out to be the opposite of anonymous. Every transaction was
public and permanent, so once any address was tied to a person, the ledger could be walked
in both directions from there.

## What changed

It is the standing case study in dark web investigation, and its lesson is not technical.
The anonymity system held; the person using it did not. Years of listings, vendor profiles
and forum threads were seized and archived, and remain evidence — the site is gone and its
contents are still searchable. Successor markets learned the operational lessons and mostly
still end the same way, in a takedown or an exit scam.
