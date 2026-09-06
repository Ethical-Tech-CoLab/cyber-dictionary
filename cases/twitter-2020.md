---
title: The 2020 Twitter takeover
year: 2020
where: Twitter, internally
actor: Three young people, coordinated over Discord
sector: Social media
kind: Social engineering and insider tool abuse
cost: About $118,000 in bitcoin; the accounts of presidents and corporations posting fraud
terms: [Social engineering, Vishing, Pretexting, Privileged access management, Insider threat, Segregation of duties, Account takeover, Just-in-time access, Least privilege]
sources:
  - title: "New York Department of Financial Services — investigation report"
    url: https://www.dfs.ny.gov/Twitter_Report
  - title: "US Department of Justice — charges in the Twitter hack"
    url: https://www.justice.gov/usao-ndca/pr/three-individuals-charged-alleged-roles-twitter-hack
  - title: "Twitter — the company's own account of the incident and the controls that followed"
    url: https://blog.x.com/en_us/topics/company/2020/an-update-on-our-security-incident
  - title: "US Attorney, Northern District of California — the charging documents"
    url: https://www.justice.gov/usao-ndca
---

## What happened

On 15 July 2020 the accounts of Barack Obama, Joe Biden, Elon Musk, Apple and dozens more
posted the same bitcoin scam. Twitter eventually stopped every verified account on the
platform from tweeting in order to end it. The attackers were teenagers, and their take was
about $118,000.

## How it worked

There was no malware. They phoned Twitter employees, claiming to be from the company's own
IT help desk, and walked them through a credential page that captured the login and the
multi-factor code in real time. That got them into internal tooling — an administration
panel that could change the email address on any account, and so take it over without ever
knowing its password.

The panel was reachable by a large number of employees, and it did not require a second
person to approve an account takeover.

## How it was found

Immediately and publicly, because the attack was noisy by design. The interesting
investigation was the regulator's. New York's Department of Financial Services examined why
a help desk call could reach the account of a presidential candidate, and its report is
unusually direct about the structural answer: too many people held too much internal
capability, with too little friction on its most dangerous actions.

## What changed

It reframed the risk of internal administrative tooling. The controls the report pushed
toward — least privilege on support tools, just-in-time elevation, two-person approval for
irreversible actions, and phishing-resistant authentication for staff — are now standard
recommendations. It also made the political point unavoidable: the same panel could have
been used quietly, during an election, by an actor with more patience than these three had.
