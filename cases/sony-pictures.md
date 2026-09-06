---
title: Sony Pictures
year: 2014
where: Culver City, California
actor: Guardians of Peace — attributed by the FBI to North Korea
sector: Film and entertainment
kind: Destructive attack and coercive leak
cost: Around $35m in IT remediation; unreleased films, salaries and private mail published
terms: [Wiper, Exfiltration, Double extortion, Attribution, Hacktivist, Insider threat, Data classification, Business continuity, Cyber warfare]
sources:
  - title: "FBI — update on Sony Pictures Entertainment investigation"
    url: https://www.fbi.gov/news/press-releases/update-on-sony-investigation
  - title: "US Department of Justice — complaint against a North Korean programmer"
    url: https://www.justice.gov/opa/press-release/file/1092091/dl
  - title: "US Department of the Treasury — sanctions on North Korea in response to the attack"
    url: https://home.treasury.gov/news/press-releases/jl9733
  - title: "Schneier on Security — contemporaneous critique of the attribution evidence"
    url: https://www.schneier.com/blog/archives/2015/01/attributing_the.html
---

## What happened

In November 2014 Sony Pictures employees arrived to find skulls on their screens and their
computers wiped. Thousands of machines were destroyed. Over the following weeks the
attackers published what they had taken first: unreleased films, executive salaries, medical
records, and years of internal email, in instalments timed for maximum press attention.

The demand, when it came, was that Sony withdraw *The Interview*, a comedy about the
assassination of Kim Jong-un. After threats against cinemas, Sony pulled the theatrical
release, then reversed and released it online.

## How it worked

Technically the destruction was straightforward: credentials were harvested, the network
was traversed, and a wiper overwrote the master boot records of every machine it reached.
Sony's network was flat, its recovery capability was limited, and the malware ran with
administrative rights.

The novel part was the strategy. Destruction alone would have been a costly outage. What
made this coercive was publishing — the slow release of embarrassing material kept the
story alive for a month, and turned a company's private communications into a lever.

## How it was found

Impossible to miss. Attribution was the contested part, and unusually the FBI stated it
publicly within weeks: code overlaps with malware previously used against South Korean
targets, reused infrastructure, and North Korean addresses appearing in the operation.
Sceptics argued the evidence shown was thin, and the case became an early public argument
about how much a government must disclose to make an attribution credible.

## What changed

It established the pattern now standard in ransomware — steal first, destroy second, publish
as leverage — years before double extortion had a name. It also raised a question companies
had not asked: not what happens if our data is stolen, but what happens if all of it is
published, including the mail nobody wrote for an audience.
