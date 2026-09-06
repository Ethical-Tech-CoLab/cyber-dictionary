---
title: Conti against Costa Rica
year: 2022
where: Costa Rica, nationally
actor: Conti, then Hive
sector: National government — finance, customs, health, payroll
kind: Ransomware against a state
cost: Estimates around $30m a day at the peak; a national emergency declared
terms: [Ransomware, Ransomware-as-a-service, Double extortion, Critical infrastructure, Cyber warfare, Attribution, Business continuity, Threat actor, Initial access broker]
sources:
  - title: "US Department of State — Rewards for Justice offer on Conti"
    url: https://rewardsforjustice.net/rewards/conti/
  - title: "CISA — Conti ransomware advisory"
    url: https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-265a
---

## What happened

In April 2022 Conti encrypted the Costa Rican Ministry of Finance, then spread across
government. Customs stopped, so trade backed up at the borders. Tax collection stopped.
Public sector payroll stopped. In May the newly inaugurated president declared a national
state of emergency over a cyber attack — the first time any country had done so.

Conti demanded $10m, then $20m, and publicly called for the government to be overthrown.
Weeks later Hive ransomware hit the country's health service.

## How it worked

The intrusion itself was ordinary: stolen credentials and a foothold in one ministry, then
lateral movement across a government estate with little separation between departments and
no central security operations capability. Nothing about the technique was novel.

The significance is structural. Conti was a ransomware-as-a-service business with an
affiliate model, revenue, and internal management — and it took on a sovereign state as a
commercial target. The public rhetoric about overthrowing the government also served a
purpose: Conti was, at that moment, badly damaged by the leak of its own internal chats
after declaring support for Russia's invasion of Ukraine, and the Costa Rica operation was
partly cover for winding the brand down and dispersing into successor groups.

## How it was found

Immediately, and publicly — the point was visibility. The interesting investigation was into
Conti itself: the leaked chat logs gave researchers and governments an unprecedented view of
a ransomware business from the inside, including salaries, hiring, and management
complaints.

## What changed

It moved ransomware from an economic crime to a question of national resilience. A criminal
group, with no state direction, disrupted a country's government for months. It also
sharpened the deterrence problem: nobody could be extradited, sanctions bit only lightly,
and the brand simply dissolved and reformed. Rewards for Justice put up $10m for information
on Conti's leadership, which is what a state does when its usual instruments do not reach.
