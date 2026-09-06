---
title: Stuxnet
year: 2010
where: Natanz, Iran
actor: Widely attributed to the United States and Israel; never officially claimed
sector: Nuclear enrichment, industrial control
kind: Sabotage of physical infrastructure
cost: Around 1,000 centrifuges destroyed; Iran's enrichment programme set back
terms: [OT / ICS, SCADA, Air gap, Zero-day, Code signing abuse, Sabotage, Cyber warfare, Attribution, Critical infrastructure]
sources:
  - title: "Symantec — W32.Stuxnet Dossier"
    url: https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
  - title: "IAEA safeguards reports on Iran, 2009–2011"
    url: https://www.iaea.org/newscenter/focus/iran/iaea-and-iran-iaea-reports
---

## What happened

Between 2009 and 2010 centrifuges at Iran's Natanz enrichment plant began failing at an
unusual rate. The plant's own monitoring said everything was normal. It was not equipment
failure: software was spinning the centrifuges outside their tolerances while replaying
recorded normal readings to the operators watching the screens.

## How it worked

Stuxnet crossed an air gap — the plant's control network was not connected to the internet,
so the malware travelled on removable media. It used four Windows zero-days, an
extraordinary expenditure, and drivers signed with certificates stolen from two legitimate
Taiwanese hardware companies, so Windows accepted them without complaint.

It was also extremely specific. It looked for a particular Siemens controller configuration,
driving a particular number of frequency converters, running in a particular frequency
range. On anything else it did nothing. Having found its target it altered the rotor speeds
and, critically, fed the monitoring systems the readings they expected to see.

## How it was found

It was found by accident, and outside Iran. The malware spread further than intended, and
in June 2010 a small Belarusian antivirus firm investigating machines that kept rebooting
in Iran isolated the sample. Researchers at Symantec, Kaspersky and Langner then spent
months reverse-engineering it. Langner identified the target as centrifuge control. Nobody
was ever charged; attribution rests on journalism, leaks and the sheer cost of the operation.

## What changed

It is the first widely accepted case of code destroying physical equipment, and it ended
two comfortable assumptions: that an air gap is a boundary, and that industrial control
systems are too obscure to attack. Every subsequent framework for critical infrastructure
security cites it. It also set a precedent that its likely authors now live with — the
techniques were studied, adapted and eventually used against Western infrastructure.
