---
title: Ashley Madison
year: 2015
where: Toronto, and 30m users worldwide
actor: The Impact Team
sector: Online dating
kind: Extortion breach and full public dump
cost: About $11.2m in US settlements; the company restructured; deaths linked to the exposure
terms: [Exfiltration, Sensitive PII, Personally identifiable information, Data minimisation, Retention schedule, bcrypt, Hash function, Password cracking, Breach notification, Privacy by design]
sources:
  - title: "Office of the Privacy Commissioner of Canada and Australian Privacy Commissioner — joint investigation report"
    url: https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2016/pipeda-2016-005/
  - title: "FTC — Ashley Madison settlement"
    url: https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3284-ashley-madison
---

## What happened

In July 2015 a group calling itself the Impact Team told Avid Life Media to shut down Ashley
Madison, a site for arranging affairs, or they would publish everything. The company did
not. In August the attackers released the full customer database — names, addresses,
payment records, sexual preferences, and the messages — for anyone to download.

The consequences were not measured in fraud losses. Users were blackmailed, outed and
divorced, and several deaths were linked to the exposure. It remains the clearest
demonstration that a breach's harm depends on what the data is, not how much of it there is.

## How it worked

The intrusion itself was never fully explained publicly. What the regulators established was
what surrounded it: no documented security policy, no risk management framework, weak
authentication for administrative access, and a shared credential regime that made the
network easy to move through once entered.

Two decisions made it far worse. Passwords were stored with bcrypt — genuinely good — but a
legacy token in the same database used weak hashing, so most of them fell anyway. And the
company charged users for a "full delete" while retaining their payment records, which is
the detail that turned a breach into a regulatory finding and a class action.

## How it was found

The attackers announced it themselves. The investigation that mattered was the regulators':
Canada's Privacy Commissioner and Australia's, jointly, examined not the intrusion but the
company's handling of data it had promised to protect and delete. Their report is still one
of the more readable statements of what "appropriate safeguards" is supposed to mean.

## What changed

It made data minimisation and retention concrete rather than theoretical. Holding data you
no longer need is not neutral storage cost; it is retained liability that will be published
in full one day. It also broke the assumption that a breach's severity scales with record
count: thirty million rows here did more human damage than hundreds of millions of card
numbers elsewhere, because of what the rows said.
