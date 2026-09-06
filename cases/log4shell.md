---
title: Log4Shell
year: 2021
where: Everywhere Java is deployed
actor: Everyone, within hours — from state actors to cryptominers
sector: All
kind: Vulnerability in a ubiquitous dependency
cost: Unquantifiable; years of remediation still running
terms: [CVE / CVSS, Dependency, SBOM, SCA, Zero-day, Vulnerability management, Supply chain attack, Injection, KEV, Technical debt]
sources:
  - title: "CISA — Apache Log4j vulnerability guidance"
    url: https://www.cisa.gov/news-events/news/apache-log4j-vulnerability-guidance
  - title: "Cyber Safety Review Board — review of the Log4j event"
    url: https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf
  - title: "Apache Software Foundation — CVE-2021-44228 advisory and remediation guidance"
    url: https://logging.apache.org/log4j/2.x/security.html
  - title: "Google Open Source Insights — measurement of how deep in dependency trees the affected versions sat"
    url: https://opensource.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html
---

## What happened

In December 2021 it emerged that Log4j — a logging library present in an enormous share of
Java applications — would, on being asked to log a specially crafted string, go and fetch
and execute code from a server named in that string. Anything that wrote a user-supplied
value to a log was exploitable, which meant almost everything.

Proof of concept was trivial. Exploitation was global within hours.

## How it worked

The library supported a lookup syntax inside log messages. One of those lookups could
resolve over JNDI, which could point at a remote directory, which could return a Java class
that would then be loaded and run. Each of those features was reasonable in isolation and
had been there for years.

The severity came from where it sat: not in a product anyone had bought, but in a dependency
of a dependency, maintained by a handful of unpaid volunteers, and present in software whose
owners did not know they were using it.

## How it was found

Reported responsibly to Apache by a security engineer at Alibaba. What followed exposed the
real problem — most organisations could not answer whether they were affected, because
nothing told them what their software contained. The remediation effort was mostly an
inventory exercise, and for many it took months.

## What changed

It made software bills of materials a requirement rather than an aspiration, and gave
composition analysis tooling its business case. The US Cyber Safety Review Board's report
concluded that Log4Shell would be exploited for a decade and framed the deeper issue:
critical infrastructure resting on unfunded volunteer maintenance. Open source funding
initiatives that exist today were argued for on the back of this event.
