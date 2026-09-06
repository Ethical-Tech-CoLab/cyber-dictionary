---
title: The Polish energy attacks
year: 2025
where: Poland — 30 renewable energy sites and two combined heat and power plants
actor: Unattributed
sector: Energy generation and district heating
kind: Purely destructive attack on operational technology
cost: Turbine and water treatment shutdown at a plant heating 50,000 residents; no loss of supply to customers
terms: [Destructive OT attack, OT / ICS, SCADA, PLC, Private APN, Client isolation, VPN concentrator, Perimeter device, Multi-factor authentication, Default credentials, Lateral movement, Jumping, S7 protocol, Modbus, Variable frequency drive, Anti-forensics, Log loss, Unexplained failure, Critical infrastructure, Network segmentation, Reconnaissance]
sources:
  - title: "CERT Polska — report on the December 2025 attacks against the Polish energy sector (30 January 2026)"
    url: https://cert.pl/en/
  - title: "CERT Polska — supplementary report on the combined heat and power plant incident (August 2026)"
    url: https://cert.pl/en/posts/
  - title: "Marcin Dudek, CERT Polska — presentation of the findings at DEF CON, Las Vegas (August 2026)"
    url: https://defcon.org/
  - title: "Industrial Cyber — CERT Polska exposes multi-stage cyberattack on energy infrastructure"
    url: https://industrialcyber.co/
---

## What happened

On 29 December 2025, thirty renewable energy facilities and a large combined heat and power
plant in Poland were attacked in a coordinated, purely destructive operation. A smaller CHP
plant supplying heat to 50,000 people was hit the same day, and took three months longer to
investigate — which is why it was disclosed separately, in August 2026.

At that smaller plant the attacker stopped the steam turbine and the water treatment system
producing process water, halting cogeneration. Operators responded fast enough that the
outage was short and no customer lost heat or electricity.

The plant's first assumption was that maintenance contractors had made a mistake. It
reported the event for information only. CERT Polska, aware of the other incidents, opened
it as a possible attack anyway.

## How it worked

The route in is the reason this case matters, and it had not been seen before.

The attacker reached a FortiGate at a wind farm substation, acting as both firewall and VPN
concentrator, exposed to the internet and accepting password authentication with no second
factor. With administrative rights on it they obtained a VPN account with access to every
network segment — the VLANs existed, and the credentials crossed them.

Inside, they found a Teltonika cellular router, reached its web interface, then its SSH
service, and tunnelled from there into the **private APN** — the carrier-provided mobile
network the distribution operator uses to reach its remote sites. That network was scanned
for over a week, looking for VNC, HTTP, and the industrial protocols S7 and Modbus.

On it sat a WAGO PFC200 controller with its web administration interface exposed on the WAN
side and the default password on the admin account. The attacker logged in, used the web
interface to enable SSH, and tunnelled again — this time into the operational network of the
CHP plant, which the WAGO could reach because it spoke to both the SCADA systems and the
industrial segments.

A week of reconnaissance followed: probing remote desktop services on 22 December, then on
Christmas Day connecting to three Siemens PLCs over S7. On the 29th, between about 05:30 and
10:10, they acted — compromising the SCADA server, switching an S7-300, S7-1200 and S7-1500
into STOP mode and setting passwords on them to lock operators out, and reconfiguring seven
Moxa serial servers and three switches to factory state with changed passwords and IP
addresses set to 127.0.0.1, deliberately to slow recovery. The timing of those requests shows
the reconfiguration was automated. Recovery began at 07:30, while the attacker was still in
the network.

Then they covered their tracks. The WAGO controller they had tunnelled through was destroyed
by corrupting its partition table — a factory reset could not repair it and no logs survived.
The Teltonika router was factory-reset, its password changed and its address set to 127.0.0.1.
Finally the FortiGate they had entered by was reset, losing its logs too.

## How it was found

Backwards, from the effects, with most of the evidence deliberately destroyed. The device the
attacker worked from was identified from logs elsewhere, but the device itself was bricked
and yielded nothing in laboratory forensics. Investigators tested hypotheses instead: the
first, that the controller had been accidentally exposed to the internet, was ruled out by
analysing Polish address space for that device type in the relevant period. Only on learning
the controller held a SIM on the operator's private APN did the sequence become
reconstructable.

The plant's own successful recovery removed evidence as well: restoring the PLCs from backup
minimised downtime and permanently erased their operational logs, which Siemens confirmed
could not be recovered.

## What changed

CERT Polska's central recommendation is a reframing: **a private APN is not a private
network.** Treat it as untrusted with respect to the operational environment, with
segmentation and traffic control at least equal to a corporate WAN link — and where the
organisation cannot verify how the carrier has configured it, treat it as the internet.

Concretely: enable client isolation between devices on the APN so one compromised unit
cannot reach the others; allowlist only the connections the plant actually needs across the
APN gateway and monitor for deviations; expose no administrative services — web, SSH, Telnet
— on APN-facing interfaces; change every default credential; log centrally, off the device;
and bring the APN and its gateways into penetration tests and red-team scope, which is
exactly where they had never been.

Two lessons sit outside the technical list. An attack against an industrial network launched
from a PLC is not a scenario most OT defenders had modelled. And this case was only ever
opened because someone treated an unexplained failure as possibly hostile — the plant itself
had filed it as contractor error.
