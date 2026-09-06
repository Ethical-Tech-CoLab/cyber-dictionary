---
title: Mirai
year: 2016
where: Global; worst felt in the eastern United States and Liberia
actor: Three US college students, later cooperating witnesses
sector: Internet infrastructure, hosting, DNS
kind: Botnet and record-breaking denial of service
cost: Dyn outage took down much of the US consumer internet for a day
terms: [Botnet, IoT, DoS / DDoS, Amplification attack, Reflection attack, Default credentials, DNS, Zombie, Script kiddie]
sources:
  - title: "US Department of Justice — Mirai botnet guilty pleas"
    url: https://www.justice.gov/opa/pr/justice-department-announces-charges-and-guilty-pleas-three-computer-crime-cases-involving
  - title: "Cloudflare — inside the infamous Mirai IoT botnet"
    url: https://blog.cloudflare.com/inside-mirai-the-infamous-iot-botnet-a-retrospective-analysis/
---

## What happened

In October 2016 an attack on Dyn, a DNS provider, made Twitter, Spotify, Reddit, Netflix and
much else unreachable across the United States. None of those services were attacked. Their
names simply stopped resolving. The traffic came from hundreds of thousands of cameras,
routers and video recorders in people's homes.

## How it worked

Mirai's technique was almost insultingly simple: scan the internet, try around sixty
default username and password pairs, and take whatever answers. No exploit, no
vulnerability — just devices shipped with credentials the owner was never told to change,
and often could not.

The resulting botnet was large enough to produce floods over a terabit per second, at the
time unprecedented. The source code was then published, which is why Mirai variants are
still doing this.

## How it was found

The scale drew immediate attention, and the operators were not careful. They advertised,
argued in forums, and rented the botnet out. Investigators followed the boasting, the
infrastructure and the money. The three pleaded guilty in 2017; one had written Mirai partly
to gain advantage in a Minecraft server protection racket.

## What changed

It put device security into law. California's SB-327 and the UK's Product Security and
Telecommunications Infrastructure Act both ban universal default passwords on consumer
connected devices, and both trace directly to Mirai. It also made a structural point the
industry had been avoiding: the security of the internet depends on equipment whose owners
have no way to patch it and no reason to care, and whose manufacturers had no obligation
to either.
