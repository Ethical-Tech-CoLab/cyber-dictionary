---
title: The British Library
year: 2023
where: London
actor: Rhysida — a ransomware-as-a-service operation
sector: National library, cultural heritage
kind: Ransomware and data leak
cost: Around £6–7m in rebuilding; core services degraded for well over a year
terms: [Ransomware, Multi-factor authentication, Legacy system, Terminal server, Exfiltration, Double extortion, Business continuity, Disaster recovery, Technical debt, Personally identifiable information]
sources:
  - title: "British Library — Learning Lessons from the Cyber-Attack (2024)"
    url: https://www.bl.uk/home/british-library-cyber-incident-review-8-march-2024.pdf
  - title: "UK National Cyber Security Centre — ransomware guidance"
    url: https://www.ncsc.gov.uk/ransomware/home
  - title: "British Library — cyber incident updates and service restoration record"
    url: https://www.bl.uk/cyber-incident/
  - title: "UK Parliament, Culture Media and Sport Committee — evidence on the attack and its funding consequences"
    url: https://committees.parliament.uk/
---

## What happened

In October 2023 Rhysida encrypted the British Library's systems and stole around 600GB of
data, including staff personal information. The Library refused to pay. The data was
auctioned, then dumped. The catalogue — the record of a national collection built over
centuries — was unavailable for months, and full service restoration ran years, not weeks.

## How it worked

The attackers entered through a terminal services server, installed for supplier and
partner access, that did not require multi-factor authentication. Once in, they escalated
to domain administrator, spent days copying data out, and then encrypted and destroyed
servers on their way out — including some of the infrastructure needed to rebuild.

What made recovery so long was not the encryption but the estate. The Library ran a large
amount of ageing, deeply interdependent, in some cases unsupported software, much of it
customised over decades. Restoring it as it was would have meant restoring the
vulnerabilities. Rebuilding meant a modernisation programme nobody had budgeted for,
executed under emergency conditions.

## How it was found

The attack announced itself. What distinguishes this case is what the institution did next:
it published a detailed, self-critical review naming its own failures — the missing
multi-factor authentication, the historic underinvestment, the absence of a full network
diagram, the reliance on legacy systems — and released it for other organisations to learn
from.

## What changed

The published review is the artefact. Very few victims describe their own shortcomings in
public with that specificity, and it has become required reading in the cultural and public
sectors. Its central lesson is about technical debt: the incident was ordinary, and the
consequences were extraordinary because of what had been deferred for twenty years. The
recovery cost is not what the attack did — it is what the estate made unavoidable.
