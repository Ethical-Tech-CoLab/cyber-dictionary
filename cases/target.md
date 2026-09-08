---
title: Target
year: 2013
where: United States
actor: Criminal group using the BlackPOS point-of-sale malware
sector: Retail
kind: Payment card breach
cost: 40m card numbers and 70m customer records; about $292m gross, and the chief executive's job
terms: [Third-party risk, Network segmentation, Payment card data, PCI DSS, Alert fatigue, Supply chain attack, Exfiltration, Least privilege, Breach notification]
sources:
  - title: "US Senate Commerce Committee — a kill chain analysis of the 2013 Target data breach"
    url: https://www.commerce.senate.gov/services/files/24d3c229-4f2f-405d-b8db-a3a67f183883
  - title: "US Federal Trade Commission — the Target settlement with state attorneys general and its guidance for business"
    url: https://www.ftc.gov/
  - title: "Brian Krebs — reporting that first identified the HVAC contractor as the entry point"
    url: https://krebsonsecurity.com/tag/target-data-breach/
  - title: "Verizon — Data Breach Investigations Report series, for the retail intrusion pattern"
    url: https://www.verizon.com/business/resources/reports/dbir/
---

## What happened

Over the American Thanksgiving shopping weekend of 2013, malware sat on Target's checkout
tills reading card numbers out of memory as customers paid. Forty million cards were taken,
along with names and addresses for another seventy million people. The chief executive and
the chief information officer both left, and the case became the reference for board-level
accountability over a breach.

## How it worked

The way in was a heating and ventilation contractor. The firm had credentials to Target's
vendor portal for billing and project management, and its own security was what you would
expect of a small mechanical services company. Those credentials got the attackers a
foothold on Target's corporate network.

The network then did the rest of the work for them. Nothing meaningful separated the
corporate environment from the payment environment, so a supplier login for invoicing
eventually reached the tills. On the tills, BlackPOS scraped card data out of memory in the
brief moment it is decrypted for processing, staged it on an internal server, and pushed it
out to an external address.

## How it was found

Target's own tooling saw it. A newly installed detection product raised alerts on the
exfiltration, and a security team in Bangalore escalated them to Minneapolis. Nobody acted.
The breach was eventually confirmed after the US Department of Justice contacted Target,
having seen the cards for sale on carding forums.

The uncomfortable part of this case is that the technology worked and the process did not.

## What changed

It accelerated the United States' shift to chip cards, which removes the value of the data
this attack stole. For everyone else it made three arguments that are now standard:
suppliers inherit your risk and must be scoped and segmented accordingly, a payment
environment must be genuinely separated rather than nominally so, and an alert nobody acts
on is not a detection.
