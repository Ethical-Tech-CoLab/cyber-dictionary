---
title: Marks & Spencer
year: 2025
where: United Kingdom
actor: Scattered Spider, deploying DragonForce ransomware
sector: Retail
kind: Social engineering into ransomware
cost: Around £300m of operating profit; online ordering suspended for roughly six weeks
terms: [Social engineering, Vishing, Help desk fraud, Third-party risk, Multi-factor authentication, Ransomware, Account takeover, Privileged access management, Business continuity, Identity lifecycle]
sources:
  - title: "UK National Cyber Security Centre — advice following the 2025 retail attacks"
    url: https://www.ncsc.gov.uk/news/incidents-impacting-retailers-recommendations-from-the-ncsc
  - title: "Marks & Spencer plc — regulatory announcements and results statements"
    url: https://corporate.marksandspencer.com/investors
  - title: "Marks & Spencer plc — full year results statement quantifying the impact"
    url: https://corporate.marksandspencer.com/investors/results-reports-and-presentations
  - title: "UK Parliament, Business and Trade Committee — evidence session with M&S and Co-op on the 2025 attacks"
    url: https://committees.parliament.uk/
---

## What happened

Over the Easter weekend of 2025, Marks & Spencer's systems were disrupted. Contactless
payment and click-and-collect failed first; then online ordering was suspended entirely and
stayed off for about six weeks, through what is normally a strong trading period. Empty
shelves appeared in stores as logistics systems went down. The company put the hit to
operating profit at roughly £300m before insurance and mitigation.

Co-op and Harrods were attacked in the same period, by the same crew.

## How it worked

Not through a vulnerability. Scattered Spider is an English-speaking, largely young,
social-engineering group whose speciality is the help desk: call IT support, impersonate an
employee convincingly enough — using details harvested from LinkedIn, breaches and public
records — and have a password reset or a multi-factor device re-enrolled. Reporting
indicated the initial compromise came via a third party providing IT support services.

From that account they escalated, moved to the identity infrastructure, and eventually
deployed DragonForce ransomware. The technical stage was the last stage.

## How it was found

Customers found it, at the tills. The point of interest is the target: the group attacks
the identity recovery process, which exists precisely to help people who have lost access,
and which is therefore designed to be accommodating. Every control that protects an account
can be undone by the process for restoring it.

## What changed

It moved help desk verification from a service-quality question to a security control. The
NCSC's guidance after the retail attacks focused on exactly that: how support staff verify
identity before resetting a factor, whether privileged accounts can be reset by phone at
all, and how third-party support providers are held to the same standard. It also
demonstrated at scale that the modern perimeter is a person answering a phone.
