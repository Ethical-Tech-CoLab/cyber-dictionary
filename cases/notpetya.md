---
title: NotPetya
year: 2017
where: Ukraine, then everywhere
actor: Sandworm — Russian military intelligence, GRU Unit 74455
sector: Logistics, pharmaceuticals, food, government
kind: Destructive attack
cost: Around $10bn in global damage; roughly $300m each at Maersk and Merck
terms: [Sandworm, Wiper, Supply chain attack, Compromised update, Ransomware, Attribution, Cyber warfare, Proportional response]
sources:
  - title: "US Department of Justice indictment of six GRU officers (2020)"
    url: https://www.justice.gov/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and
  - title: "UK National Cyber Security Centre attribution statement (2018)"
    url: https://www.ncsc.gov.uk/news/russian-military-almost-certainly-responsible-destructive-2017-cyber-attack
---

## What happened

On 27 June 2017 a piece of malware disguised as ransomware spread out of Ukraine and kept
going. It reached Maersk, which moves close to a fifth of the world's container freight,
and stopped it. It reached Merck, Mondelez, FedEx's European arm, and the radiation
monitoring at Chernobyl. It did not stop at the border because nothing told it to.

The ransom note was a lie. There was no working decryption, and money was never the point:
the malware was built to destroy, and dressed as crime to muddy who had done it.

## How it worked

The delivery was a supply chain attack on M.E.Doc, Ukrainian tax accounting software that
almost every company doing business in the country has to run. Its update server was
compromised, so the malware arrived correctly signed, through a channel every victim had
deliberately trusted.

Once inside a network it spread on its own using EternalBlue — a leaked NSA exploit for
Windows file sharing — and, where machines were patched, by harvesting credentials from
memory and using legitimate administration tools to move on. Patching alone did not save
you if an unpatched neighbour had your administrator password in memory.

## How it was found

Attribution took a year and did not come from the malware. Investigators had the code
lineage back to earlier Sandworm tooling used against Ukraine's power grid, the choice of
targets, the timing on Ukraine's Constitution Day, and the fake ransom mechanism that could
never have collected. Governments then added intelligence they did not publish. The United
States, United Kingdom and others attributed it to the GRU in 2018; the indictment naming
six officers followed in 2020.

## What changed

It ended the argument about whether a cyber attack could cause physical, global, economic
damage. Insurers invoked war exclusions to refuse payment, and the litigation that followed
— Merck's in particular — reshaped how cyber insurance is written. For defenders it made
three points concrete: an update channel is an attack surface, a flat network turns one
compromise into all of them, and recovery capability matters more than prevention. Maersk
rebuilt its directory from a single surviving copy in Ghana that had been offline through
a power cut.
