---
title: North Korean IT workers
year: 2018-present
where: Hired remotely by companies in the US, Europe and Asia; operating from China, Russia, Laos and Cambodia
actor: Democratic People's Republic of Korea, through state-run IT organisations
sector: Technology, finance, media — anyone hiring remote engineers
kind: Employment fraud, sanctions evasion, insider access
cost: Hundreds of millions of dollars a year to the DPRK; sanctions exposure for employers
terms: [DPRK IT worker scheme, Remote worker fraud, Laptop farm, Facilitator, Interview fraud, Identity rental, Impossible travel, Know your employee, Insider by design, Geoblocking, Remote access software abuse]
sources:
  - title: "US Department of State, Treasury and FBI advisory on DPRK IT workers"
    url: https://ofac.treasury.gov/media/923126/download
  - title: "US Department of Justice — laptop farm prosecutions"
    url: https://www.justice.gov/opa/pr/justice-department-announces-arrest-facilitator-and-seizures-laptop-farms-nation-state-it
  - title: "KnowBe4 — how a North Korean fake IT worker was hired and detected"
    url: https://blog.knowbe4.com/how-a-north-korean-fake-it-worker-tried-to-infiltrate-us
  - title: "UN Panel of Experts on North Korea — reports on sanctions evasion through IT work"
    url: https://www.un.org/securitycouncil/sanctions/1718/panel_experts/reports
---

## What happened

Thousands of North Korean IT workers have been hired, as ordinary remote employees and
contractors, by companies that believed they were hiring Americans and Europeans. They did
the work. They were paid, and the pay went to a sanctioned state's weapons programmes. In
many cases they also kept access, or attempted extortion after being let go.

This is not a hack. Every step — the application, the interview, the onboarding, the VPN,
the payroll — is a legitimate business process working exactly as designed.

## How it works

Identities are bought or stolen from real people, so background checks pass against real
records. Interviews are sat by proxies, or assisted with live translation and face
filters. Once hired, the company laptop is shipped to a US or European address — a *laptop
farm* run by a local facilitator who plugs the machines in and installs remote access
software, so the connection comes from the country the employer expects. Geoblocking sees
a domestic address; the worker is in Shenyang.

Pay is routed through the facilitator or through cryptocurrency. A single operative often
holds several jobs at once.

## How it is found

Not by security tooling, which sees a legitimate employee doing legitimate work. It is
found by the mismatches around the edges: impossible travel between logins, payroll details
shared across supposedly unrelated employees, addresses that recur across hires, reluctance
to appear on camera, a laptop that has never once connected from the home its address
claims. Amazon, KnowBe4 and others have published their own detections, all of which turn
on identity and human resources data rather than on malware.

## What changed

It has forced identity assurance backwards into hiring. *Know your employee* — document
verification, liveness checks, right-to-work confirmation, repeated rather than done once —
is now a security control, not a compliance formality. It also broke the assumption
underneath insider threat programmes: the insider need not be an employee who turned. They
may have been placed.
