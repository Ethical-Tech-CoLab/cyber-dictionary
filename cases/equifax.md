---
title: Equifax
year: 2017
where: United States, UK, Canada
actor: Attributed by the US to four members of China's PLA
sector: Credit reporting
kind: Data breach
cost: 147m people's records; about $1.4bn in settlements and remediation
terms: [Vulnerability management, Patch, N-day, Exfiltration, Certificate, Encryption in transit, Personally identifiable information, Sensitive PII, Breach notification, Data minimisation]
sources:
  - title: "US House Oversight Committee — report on the Equifax data breach"
    url: https://oversight.house.gov/wp-content/uploads/2018/12/Equifax-Report.pdf
  - title: "FTC — Equifax settlement"
    url: https://www.ftc.gov/enforcement/refunds/equifax-data-breach-settlement
  - title: "US Government Accountability Office — Data Protection: Actions Taken by Equifax and Federal Agencies"
    url: https://www.gao.gov/products/gao-18-559
  - title: "US Department of Justice — indictment of four members of the PLA"
    url: https://www.justice.gov/opa/pr/chinese-military-personnel-charged-computer-fraud-economic-espionage-and-wire-fraud-hacking
---

## What happened

Attackers took the personal records of 147 million people — names, dates of birth, national
identity numbers, addresses, and for some, driving licence and card numbers. The victims
were not Equifax's customers. They were the subjects of files compiled about them without
their involvement, and they had no way to opt out or to take their data elsewhere.

## How it worked

The entry point was a known vulnerability in Apache Struts, disclosed and patched two months
earlier. The organisation had a patching process; it did not have an accurate inventory, so
the instruction to patch never reached the affected server.

The attackers then stayed for 76 days. Two failures kept them invisible. Internal network
traffic was inspected for anomalies, but the certificate on the inspection system had
expired ten months earlier, so nothing was being read. And the internal network was flat
enough to reach dozens of databases from the initial foothold. When the certificate was
renewed, the exfiltration became visible immediately.

## How it was found

By renewing an expired certificate. The moment inspection resumed, the traffic leaving the
network was obvious. That is the whole story of the detection.

## What changed

It became the reference case for regulators on accountability: a chief executive resigned,
Congress reported, and the settlement created a consumer fund. Its technical lessons are
unglamorous and universal — you cannot patch what you have not inventoried, a lapsed
monitoring certificate is a blind spot rather than a warning, and flat internal networks
convert one server into everything. It also sharpened the argument for data minimisation:
much of what was taken had no operational reason to still be there.
