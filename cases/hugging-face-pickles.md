---
title: Hugging Face model pickles
year: 2024
where: Hugging Face's shared AI infrastructure
actor: Wiz security researchers, in coordinated disclosure
sector: AI platforms and model distribution
kind: Platform vulnerability found by research, not exploited
cost: No known malicious exploitation; the industry's model of model distribution had to change
terms: [Sandbox escape, Pickle deserialisation, Safetensors, Model registry, Untrusted model, Multi-tenancy, Cross-tenant access, Container escape, Supply chain attack, Deserialisation vulnerability, Model weights, Malicious package]
sources:
  - title: "Wiz Research — Wiz and Hugging Face address risks to AI infrastructure"
    url: https://www.wiz.io/blog/wiz-and-hugging-face-address-risks-to-ai-infrastructure
  - title: "Hugging Face — pickle scanning and model security documentation"
    url: https://huggingface.co/docs/hub/security-pickle
  - title: "JFrog Security Research — malicious models found published on the Hugging Face hub"
    url: https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/
  - title: "Hugging Face — the safetensors format and its rationale"
    url: https://huggingface.co/docs/safetensors/index
---

## What happened

In 2024, researchers at Wiz showed that they could upload a model to Hugging Face, have the
platform's own inference service load it, and end up running code inside that service — then
reach across to infrastructure shared with other customers. Hugging Face hosts the models a
very large share of the industry builds on, so the finding was not about one company's
configuration. It was about the assumption underneath the whole distribution model.

It was found by researchers and fixed in coordinated disclosure. There is no evidence anyone
malicious got there first, which is the only comfortable sentence in the case.

## How it worked

The root of it is a decision made long before anyone thought about AI security: most models
are distributed as Python pickles, and a pickle is not data. It is a set of instructions for
reconstructing an object, and reconstruction can call arbitrary code. Loading someone else's
model in that format is running their program. Every scanner, licence check and download
count around it addresses a different question.

So a model uploaded to the hub, and then loaded by the platform's inference service to serve
predictions, executed the researchers' code inside that service. From there the problem
became an ordinary cloud one: the inference environment was shared, the isolation between
tenants was weaker than assumed, and credentials and network reach inside the cluster
allowed movement toward other customers' workloads — including, in principle, the ability to
tamper with models other people would then download.

Related work found the same shape elsewhere on the platform: container escapes from the
Spaces application sandbox, and malicious models already published to the hub by others.

## How it was found

By people looking for it, deliberately, and telling the vendor. The interesting question is
why it had not been found earlier, and the answer is that AI infrastructure was being built
and adopted faster than it was being reviewed. The pickle risk was documented and widely
known among practitioners; what was new was following it through the platform into
multi-tenant infrastructure and asking what a compromised inference worker could reach.

## What changed

It moved model distribution into the software supply chain, where it belongs. Safetensors —
a format that stores tensors and cannot execute anything on load — went from an option to
the default expectation, and platforms added pickle scanning, provenance and stricter
isolation of inference workloads.

The general lesson outruns the specific one. A model is an artefact you download from a
stranger and execute, which makes a model hub a package registry, and everything the
software world learned about package registries the hard way now applies: signing,
provenance, scanning, pinned versions, and the assumption that anything you did not build is
untrusted until handled otherwise. Sandboxing is the control of last resort, and this case
is a reminder that a sandbox is only a boundary until someone tests it.
