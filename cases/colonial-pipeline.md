---
title: Colonial Pipeline
year: 2021
where: Eastern United States
actor: DarkSide, a ransomware-as-a-service operation
sector: Energy, fuel distribution
kind: Ransomware
cost: $4.4m ransom paid, $2.3m recovered; days of fuel shortages across the US east coast
terms: [Ransomware, Ransomware-as-a-service, VPN, Multi-factor authentication, Credential stuffing, Critical infrastructure, Blockchain analysis, Double extortion, Business continuity]
sources:
  - title: "US Department of Justice — recovery of the ransom payment"
    url: https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside
  - title: "CISA and FBI joint advisory on DarkSide ransomware"
    url: https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a
  - title: "US House Committee on Homeland Security — testimony of Colonial Pipeline's chief executive"
    url: https://homeland.house.gov/
  - title: "TSA — security directives for pipeline owners and operators issued after the attack"
    url: https://www.tsa.gov/news/press/releases/2021/07/20/dhs-announces-new-cybersecurity-requirements-critical-pipeline
---

## What happened

In May 2021 ransomware encrypted the business systems of the company operating the largest
fuel pipeline in the United States. The pipeline's control systems were not encrypted — the
company shut the pipeline down itself, because with billing systems offline it could not
measure what it was delivering or bill for it. Fuel shortages and panic buying followed
across the east coast, and the effect was national before any operational technology was
touched.

## How it worked

The way in was a single password. An old VPN account, no longer in use, still worked and
had no multi-factor authentication on it. The password appeared in a batch of leaked
credentials, suggesting reuse elsewhere. From there DarkSide's affiliates did the ordinary
thing: moved laterally, stole data for extortion leverage, and encrypted.

DarkSide itself did not run the attack. It rented the malware and the negotiation
infrastructure to affiliates for a share, the model that made ransomware an industry rather
than a craft.

## How it was found

The company knew within hours. The interesting investigation came after: the FBI followed
the bitcoin ransom across the public ledger to a specific wallet and seized most of it,
having obtained the private key. That recovery did more to change ransomware economics than
any advisory — it demonstrated publicly that the payment rail is the traceable part.

## What changed

It moved ransomware from an IT problem to a national security one. In the United States it
produced an executive order on cybersecurity, mandatory incident reporting for pipelines,
and TSA security directives for the sector. The operational lesson is narrower and harder:
one dormant account without MFA, and a billing system whose failure stops the physical
business, were enough.
