---
title: WannaCry
year: 2017
where: 150 countries; worst in the UK's National Health Service
actor: Lazarus Group — North Korea
sector: Healthcare, manufacturing, telecoms
cost: Around £92m to the NHS; over 19,000 appointments cancelled
kind: Ransomware worm
terms: [Ransomware, Worm, N-day, Patch, End-of-life, Kill switch, Critical infrastructure, Attribution, Vulnerability management]
sources:
  - title: "UK National Audit Office — investigation into WannaCry and the NHS"
    url: https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/
  - title: "US Department of Justice — charges against a Lazarus Group programmer"
    url: https://www.justice.gov/opa/press-release/file/1092091/dl
  - title: "Microsoft Security Response Center — MS17-010, the patch released two months before the outbreak"
    url: https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010
  - title: "UK Department of Health and Social Care — lessons learned review of WannaCry"
    url: https://www.gov.uk/government/publications/securing-cyber-resilience-in-health-and-care-october-2018-update
---

## What happened

On 12 May 2017 ransomware spread across the world in hours without anyone opening anything.
It encrypted machines and demanded $300 in bitcoin. In England it hit a third of NHS trusts:
ambulances diverted, operations cancelled, some hospitals reduced to paper. The ransom
collected almost nothing — the payment handling was so poor that even victims who paid often
could not be decrypted.

## How it worked

WannaCry was a worm, not an email campaign. It spread using EternalBlue, an exploit for
Windows file sharing developed by the NSA and leaked two months earlier by the Shadow
Brokers. Microsoft had patched it in March, two months before the outbreak.

So the vulnerability was known, the patch existed, and the attack still worked — because
patching a hospital estate means scheduling downtime on equipment that is in use, some of it
certified only against an operating system already out of support.

## How it was found

It announced itself. The more interesting moment came the same day: a researcher analysing
the sample found it querying an unregistered domain and registered it, for about ten
dollars. That was the kill switch — the malware checked whether the domain resolved and
stopped if it did. The global spread halted that afternoon, by accident and for the price
of a domain name.

Attribution to North Korea came later, from code shared with earlier Lazarus tooling,
infrastructure reuse and intelligence, and was formally stated by the US and UK in
December 2017.

## What changed

It is the clearest available demonstration that patch management is a patient safety issue,
not an IT housekeeping one. The NHS review that followed drove funded remediation and
central monitoring. It also raised a question governments still have not settled: the
exploit was stockpiled by a state and then lost, and the damage was done with the state's
own tool.
