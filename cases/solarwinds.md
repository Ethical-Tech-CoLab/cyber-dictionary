---
title: SolarWinds
year: 2020
where: United States, then allied governments and industry
actor: APT29 / Cozy Bear — Russia's foreign intelligence service, the SVR
sector: Government, technology, consulting
kind: Supply chain espionage
cost: Around 18,000 organisations received the backdoor; roughly 100 were actively exploited
terms: [Supply chain attack, Compromised update, Code signing abuse, APT, Backdoor, Golden SAML, Dwell time, Persistence, Attribution, SBOM]
sources:
  - title: "CISA — Emergency Directive 21-01"
    url: https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise
  - title: "Mandiant — Highly evasive attacker leverages SolarWinds supply chain"
    url: https://cloud.google.com/blog/topics/threat-intelligence/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor
---

## What happened

Attackers got into the build system of SolarWinds Orion, a network management product, and
added a backdoor to the source before it was compiled. The result was signed by SolarWinds
and shipped through its update channel to some 18,000 customers, including US federal
departments. From that pool the attackers picked roughly a hundred worth pursuing and left
the rest alone.

The first breach happened in 2019. It was found in December 2020.

## How it worked

The tradecraft was patient and quiet. The backdoor slept for up to two weeks before calling
home. It checked whether it was in an analysis environment. It used domain names generated
to look like ordinary Orion traffic. Where it did act, the attackers frequently forged SAML
tokens with stolen signing keys — *Golden SAML* — to mint their own access to cloud
services, so credentials could be reset and multi-factor enforced without dislodging them.

They also took care not to reuse infrastructure between victims, which is precisely what
makes indicator-based detection fail.

## How it was found

Not by any government monitoring, and not by SolarWinds. FireEye, itself a victim, noticed
that an employee had registered a second phone for multi-factor authentication. That single
anomalous enrolment led to its own breach, then to the Orion backdoor, then to everything
else. A helpdesk-level detail unravelled a two-year intelligence operation.

## What changed

It made software supply chain security a policy matter. The US executive order that
followed required software bills of materials and secure development attestations from
federal suppliers. It also settled an argument about dwell time: fourteen months, against
some of the most heavily monitored networks in the world. And it demonstrated that
identity, not the network, is where a modern intrusion actually lives — forged tokens
survived every credential reset aimed at them.
