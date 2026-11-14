# Red Team Leadership — A Methodology Case Study

**Abdullah Batuhan Yilmaz** · Red Team Lead · Nine years in cybersecurity

> **Evidence and confidentiality statement:** This is a professional **methodology case study**, not an account of a specific client engagement. It does not invent incidents, customers, team sizes, exploitation results, financial impact, or success percentages. The representative scenario below is explicitly hypothetical. Non-public operational details and organizational identifiers have been excluded.

## Executive summary

My approach to Red Team leadership is to connect offensive testing with decisions an organization can take: define a measurable objective, identify the trust boundary that matters, assess potential consequences, capture defensible evidence and produce remediation the owner can verify.

Nine years of cybersecurity work and Red Team team leadership have shaped my interest in a recurring engineering problem: **a successful technical test is useful only when its evidence leads to a safer system**. That is also the perspective I bring to AI agent security research, where model intent and actual host-side authorization must be evaluated separately.

This document presents a repeatable leadership framework, a hypothetical walkthrough and explicit standards for what cannot be claimed without engagement evidence.

## 1 — Define mission and authorization

Before testing, an engagement should record the asset owner, business objective, in-scope systems, authorized accounts, testing windows, safety constraints, contacts and escalation rules. A test of whether access boundaries can be crossed should state **which boundary** and **what observation would count as crossing it**.

A useful hypothesis has a clear negative case. For example, an authorized ordinary user should be unable to read an unrelated tenant's object or exercise an administrative action. If the system rejects that action, the result is a tested control—not an attack success. If the action is blocked only at a later gateway, the report should distinguish the attempted authorization bypass from the absence of a side effect.

## 2 — Plan for evidence, not demonstrations

A responsible test records:

- The precondition and permission level of the test identity.
- The observed request and response or relevant configuration, while masking secrets.
- The specific boundary crossed or upheld.
- Independent evidence from application, identity, gateway and audit sources when available.
- Reproducibility and constraints: what was checked, what was not, and why.

A proposed access path, an overly broad permission and **an executed privilege escalation** are not interchangeable. Automated tools can identify candidates; the analyst determines whether the evidence supports an actual result.

## 3 — Model the defensive interpretation

For each candidate finding, identify what control should have stopped it. In web applications this may be object-level authorization. In Active Directory it may be the effective permissions on a protected object rather than the presence of a single Allow ACE. In Kubernetes it may be actual RBAC role bindings plus admission and network policy enforcement. In AI agents it may be a host capability gate rather than the instruction text shown to a model.

A useful report includes a detection question: *Would the defender be able to observe the attempted action?* This anchors the finding in telemetry and allows defenders to validate detection and response.

## 4 — Hypothetical engagement vignette (NOT a past engagement)

**Scenario:** A service retrieves external documents to assist with internal workflow summaries. The assistant can also request simulated internal note changes and email actions.

**Authorized user goal:** Summarize a release note. The user has not granted permission to send it outside the environment.

**Test question:** If the retrieved document contains instructions to forward the release note, will the agent request the unauthorized action—and will the host prevent its execution?

**Method:** Compare a general prompt, explicit source-trust instruction, host-side exact-target authorization and their combination. Observe attempted and executed actions separately. Include approved controls to verify the tool is still usable.

**Evidence:** Decision JSON, authorization verdict, simulated side-effect result, parsing errors, and exact experiment configuration.

**Interpretation:** An attempted action stopped by the host is evidence for that particular control. It is not evidence that the model resisted the injection. A system that rejects every response is not a useful security success.

This vignette illustrates the analytical method and connects to the public [AI Agent Security Lab](https://github.com/abyilmaz-BatuhanYILMAZ/AI-Agent-Security-Lab). It is **not** a description of a client engagement or a claim that the scenario was tested against a production system.

## 5 — Deliver findings and validate remediation

A report should enable an asset owner to take action without relying on the tester's private notes. For each significant finding:

1. Record the affected asset and minimum precondition.
2. Identify the expected boundary and the observed result.
3. Rate impact according to the affected service and realistic privileges, not a generic exploit label.
4. Recommend changes at the correct enforcement layer.
5. Define a retest that can be run without reproducing unnecessary harm.
6. Record residual risk and gaps.

Leadership is demonstrated through clarity, prioritization, review discipline and coordination—not through a count of tools executed.

## Public engineering examples

| Project | What it demonstrates | What it does **not** establish |
| --- | --- | --- |
| [AI Agent Security Lab](https://github.com/abyilmaz-BatuhanYILMAZ/AI-Agent-Security-Lab) | Prompt-injection evaluation, host controls, honest denominators | Production-grade AI agent security |
| [KubeGuard](https://github.com/abyilmaz-BatuhanYILMAZ/KubeGuard) | Static and live Kubernetes configuration review, RBAC relationships | Every possible runtime escalation path |
| [AD-HealthAudit](https://github.com/abyilmaz-BatuhanYILMAZ/AD-HealtAudit) | Read-only AD configuration and preliminary privilege graph analysis | Verified effectiveness against a real enterprise domain |
| [Publications](../README.md) | Two separately published Android malware ML papers | Reproduction of published model training |

## Metrics that may be included **only if verified**

The following are **not supplied or claimed** here: direct-report team size, number of assessments led, critical vulnerabilities verified, average time to remediation, detection engineering outcomes, customer sector, clearance, certifications and confidential operational achievements.

Before submitting a tailored application or CV, include only verified, shareable numbers and roles, using evidence that could be explained under interview questioning.

## My research direction

I am interested in building repeatable evaluations for AI agents and their surrounding infrastructure, where a strong security claim requires both a measurable test and a well-defined scope. My work on offensive assessment and defensive validation makes **the trust boundary between a model's proposed action and a system's authorized operation** a natural research focus.

---

*This page is for a public portfolio. It deliberately excludes private engagement records, organization identifiers, exploit steps against third parties, credentials and unverified achievements.*
