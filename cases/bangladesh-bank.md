---
title: The Bangladesh Bank heist
year: 2016
where: Dhaka, New York, Manila
actor: Lazarus Group — North Korea
sector: Central banking, international payments
kind: Payment fraud
cost: $81m stolen; $851m more attempted and stopped by a spelling mistake
terms: [SWIFT, Payment fraud, Malware, Persistence, Lazarus Group, Money mule, Cash-out, Segregation of duties, Audit trail, Insider threat]
sources:
  - title: "US Department of Justice — complaint against Park Jin Hyok"
    url: https://www.justice.gov/opa/press-release/file/1092091/dl
  - title: "SWIFT — customer security programme, established after the 2016 attacks"
    url: https://www.swift.com/myswift/customer-security-programme-csp
---

## What happened

Over a weekend in February 2016, thirty-five payment instructions went out from Bangladesh
Bank's account at the Federal Reserve Bank of New York, asking for nearly $1bn to be moved
to accounts in the Philippines and Sri Lanka. Five succeeded. Eighty-one million dollars
went into Manila casinos and largely vanished.

The rest were stopped because one instruction spelled the recipient "Shalika Fandation"
instead of Foundation, which prompted a routine query, which prompted a look at the others.

## How it worked

The attackers were inside the bank's network for weeks first, quietly learning how its
payments actually worked. They then used legitimate SWIFT credentials to submit genuine,
correctly formatted instructions. Nothing about the messages was malformed; from New York's
side, the customer had asked.

The sophistication was in hiding the evidence. Custom malware interfered with the bank's
SWIFT software so the confirmations would not appear, and manipulated the printer that
produced the paper audit trail — the copies staff would have read on Monday morning. The
timing exploited the weekend gap between Bangladeshi, American and Philippine banking
calendars, buying days before anyone could reconcile.

## How it was found

By the typing error, then by reconciliation. Once queried, the bank discovered its own
records were being suppressed. Recovery of the money largely failed: it moved through
casinos, which at the time sat outside Philippine anti-money-laundering rules.

Attribution to North Korea came from code shared with earlier Lazarus operations, and the
2018 US complaint against Park Jin Hyok laid out the same infrastructure connecting this,
Sony and WannaCry.

## What changed

It ended the assumption that the interbank messaging network was safe because its members
were. SWIFT's Customer Security Programme, with mandatory controls and annual attestation,
exists because of this attack. It also demonstrated a category of fraud where nothing is
technically forged — the credentials, the format and the authorisation are all real, and the
attack is against the process rather than the protocol.
