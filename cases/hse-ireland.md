---
title: The Irish health service
year: 2021
where: Ireland, nationally
actor: Conti — a Russian-speaking ransomware operation
sector: Public healthcare
kind: Ransomware
cost: Over €100m in response and recovery; months of disruption to cancer and diagnostic services
terms: [Ransomware, Phishing, Lateral movement, Dwell time, Business continuity, Disaster recovery, Endpoint, Legacy system, Critical infrastructure, Double extortion]
sources:
  - title: "PwC — independent post-incident review for the Irish Health Service Executive"
    url: https://www.hse.ie/eng/services/publications/conti-cyber-attack-on-the-hse-full-report.pdf
  - title: "Ireland's National Cyber Security Centre"
    url: https://www.ncsc.gov.ie/
---

## What happened

On 14 May 2021 ransomware encrypted the systems of Ireland's Health Service Executive, the
body that runs the country's public hospitals. Radiology, laboratories, maternity records
and cancer treatment scheduling went down together. Staff reverted to paper for months.
Chemotherapy and radiotherapy appointments were delayed. The HSE did not pay.

## How it worked

The entry was a malicious Excel attachment opened on a single workstation on 18 March —
eight weeks before the encryption. From there the attackers spent two months moving through
the network, gaining domain administrator rights, and reaching six other hospital networks
along the way.

The published review is unusually frank about why nobody stopped them. Alerts fired
repeatedly and were not investigated. Antivirus detections were treated as resolved when a
file was quarantined, not as evidence of an actor. Much of the estate ran unsupported
Windows. There was no single security operations function with authority over the whole
health service, and no reliable inventory of what it consisted of.

## How it was found

When it encrypted. The eight-week dwell time is the finding: this was not a fast, quiet
operation, and every stage generated signals in tools the organisation already owned.

The recovery is worth the same attention. Conti provided a decryption key without payment —
most likely to reduce the political heat — but it was slow and partial, and rebuilding
still took months. The HSE also obtained a High Court injunction against publication of the
stolen patient data.

## What changed

It is the case that forces health systems to reckon with cyber risk as clinical risk, not
administrative risk. The review's recommendations — a proper security function, executive
ownership, an accurate asset inventory, tested recovery, retirement of unsupported systems
— became the template other national health bodies were measured against. It also showed
that not paying is survivable, and expensive.
