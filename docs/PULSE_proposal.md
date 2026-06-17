# PULSE — AI-Powered Lead Qualification & Capital Connection System

**NEWITY · Summer 2026 · Confidential Executive Proposal**

*An automated engine that identifies pre-qualified small businesses nationwide before they search — and delivers them, clean and ready, into NEWITY's pipeline.*

| 2x / week | $100K–$10M | 125K+ | 0 |
|---|---|---|---|
| Automated data refresh | Qualified revenue band | CRM loans training the model | Startups & trucking in pipeline |

---

## Executive Summary

NEWITY processes up to 10,000 applications a month, but a large share of that pipeline is wasted on businesses NEWITY cannot serve — primarily startups seeking loans NEWITY does not offer. At the same time, thousands of genuinely qualified businesses never reach NEWITY at all, because they are not actively searching and no competitor channel surfaces them.

PULSE is a single automated system that solves both problems from the supply side. It pulls national business data on a recurring schedule, scores every business against NEWITY's own CRM history, and isolates only those that meet NEWITY's exact qualification criteria. **Every lead PULSE produces is qualified by design — no startup, no trucking operation, and no business outside the serviceable revenue band ever enters the pipeline.**

The system runs in two branches. The primary branch finds qualified businesses in the data and routes them directly to NEWITY. The secondary branch uses the geographic pattern of those leads to activate Business Support Organizations (BSOs) that can surface the qualified businesses the data cannot see. One system, two complementary intake paths, built on three years of SBA-funded research that no competitor can replicate.

**The ask:** Approval to deploy PULSE as a recurring automated pipeline during the Summer 2026 pilot, with the goal of permanent implementation — built and operated at under $200 in pilot cost, with zero new infrastructure.

---

## 1. The Problem NEWITY Has Not Yet Solved

NEWITY's qualified borrower has two hard requirements: **at least two years in operation and at least $100,000 in annual revenue.** Any business that fails either test is disqualified immediately. NEWITY's marketing team confirmed that the single largest source of pipeline waste is inbound demand from businesses seeking startup loans — a product NEWITY does not offer — because the channels that feed NEWITY today are demand-driven and do not filter for qualification before a business arrives.

### Two Structural Gaps

| Gap 1 — Unqualified Inbound | Gap 2 — Invisible Qualified Demand |
|---|---|
| Startups, trucking operations, and businesses outside the serviceable revenue band flood the funnel. They consume call-center time, pipeline capacity, and marketing spend, then disqualify. | Qualified businesses that have stopped searching — or never started — are invisible to search ads and SBA Lender Match. The Federal Reserve's 2026 survey found 32% of Black-owned firms that needed capital did not apply, citing discouragement, not disqualification. |
| **PULSE answer:** filter on the supply side. Only businesses meeting every criterion are ever surfaced. | **PULSE answer:** find them in national data before they search, and use BSOs to reach the ones the data misses. |

---

## 2. How PULSE Works — One System, Two Branches

PULSE is a scheduled automated job. On every data refresh (once or twice weekly, depending on source update frequency), it pulls the national business dataset, scores it against NEWITY's CRM model, and applies NEWITY's qualification rules. The output drives two independent branches.

### Branch A — Direct Lead Engine (primary)

- **Pull:** On each refresh, PULSE ingests the national business dataset.
- **Score in two stages:** every business passes through Scoring System 1 (eligibility gates — pass/fail) and then Scoring System 2 (a propensity score that ranks the survivors).
- **Visualize:** A heatmap report shows the NEWITY team exactly where qualified businesses are concentrated — serving both as a lead dashboard and as the BSO targeting map for Branch B.
- **Reach out:** Qualified businesses receive direct, automated outreach, highest-propensity first. Interested businesses self-select into NEWITY's standard 10-minute application.

### Branch B — BSO Gap Network (secondary)

Branch B exists for a single, well-defined purpose: to reach qualified businesses that are *not present in the national data* — the ones deepest in under-resourced communities with no digital footprint. It does not duplicate Branch A; it covers the gap Branch A cannot reach by design.

The targeting logic is data-driven: where Branch A finds a dense cluster of qualified businesses, more qualified businesses very likely exist nearby that the data cannot see. PULSE identifies the BSOs closest to those high-density clusters and prioritizes them for partnership outreach, drawing on the QSII 209-organization BSO database built during the SBA research. Activated BSOs refer the invisible businesses directly into NEWITY's pipeline.

**Why this branch matters most where approval is rarest.** Research feedback was direct: businesses in these communities are almost never approved for an SBA loan. That is not a disqualification problem — it is a discouragement-and-barrier problem. The Federal Reserve's 2026 survey shows the same pattern nationally: 32% of Black-owned firms that needed capital never applied, citing discouragement rather than ineligibility.

Branch B applies the same eligibility gates as Branch A — no business is surfaced unless it qualifies — then reaches qualified owners through advisors they already trust and pairs them with NEWITY's 10-minute application.

> **The two branches share one output.** The same heatmap that tells the NEWITY team where qualified leads are also tells us which BSOs to activate. The data deploys the human layer precisely where it adds the most value.

---

## 3. The Two Scoring Systems

### Scoring System 1 — Eligibility Gates (pass / fail)

A business must pass **all** of these gates to be surfaced as a qualified lead.

| Gate | Rule | Signal / Field |
|---|---|---|
| Operating history | 2+ years in business. Construction businesses require 4+ years. | Registration / filing date; NAICS sector 23 flags the construction rule |
| Revenue floor | $100,000+ in annual revenue. Hard cutoff — below this, excluded. | Revenue field / modeled estimate |
| Revenue ceiling | Under $10,000,000 in annual revenue. Hard cutoff — above this, excluded. | Revenue field / modeled estimate |
| Trucking exclusion | Trucking businesses excluded entirely. | NAICS 484 — excluded |
| Entity type | For-profit businesses only. Nonprofits excluded. | Entity / organization type |

*Result: a qualified lead is a for-profit business, 2+ years old (4+ for construction), earning between $100K and $10M annually, that is not in trucking.*

### Scoring System 2 — Propensity & Fit Score (ranking)

- **Trained on outcomes NEWITY already owns.** The signals most associated with funded loans — rather than declined or incomplete ones — become the highest-weighted filters.
- **Tuned to observed trends.** Industry mix, revenue range, business age, and geographic patterns that historically convert are weighted up; patterns that historically stall are weighted down.
- **Output: a ranked list.** Every eligible business receives a fit score, so outreach and the NEWITY team always work the highest-propensity leads first.

---

## 4. Why This Cannot Be Copied

PULSE's scoring model is trained on NEWITY's full CRM history — not only funded loans, but declined and incomplete applications. This three-class training set lets the model recognize a qualified profile across the full readiness spectrum. No competitor can build it, because no competitor has NEWITY's 125,000-loan history.

The BSO branch rests on three years and $625,000 of SBA-funded primary research (Grant #SBAHQ23I0138): a 209-organization BSO database with full contact and location data, a peer-reviewed manuscript under review at the Journal of Business Venturing Insights, and a documented understanding of why qualified businesses in specific community contexts never reach capital.

---

## 5. Implementation, Compliance & Approval

### 10-Week Pilot Plan

| Weeks | Activities & Deliverables |
|---|---|
| 1–2 | Approval secured. Data access confirmed. Scoring model specified against the three-class CRM history. Qualification rules implemented and tested on a Chicago sample. |
| 3–4 | Branch A live: scoring job scheduled on the data refresh, qualified-lead output generated, heatmap report built. Automated outreach sequence drafted and human-reviewed. |
| 5–6 | First qualified leads flow to NEWITY. Branch B activated: BSOs nearest the densest qualified clusters contacted. Weekly KPI reporting begins. |
| 7–8 | Mid-point review with Uzziel Guzman. Model precision tuned on early results. Outreach and BSO targeting refined. Lead quality reviewed with the ops team. |
| 9–10 | Final KPI dashboard and a real qualified-lead list generated during the pilot. Handoff package and scale roadmap delivered. CEO presentation with permanent-implementation recommendation. |

### Compliance & Cost

| | |
|---|---|
| **Data privacy** | All identity and financial data is collected exclusively within NEWITY's existing SBA-compliant application pipeline. No new data store is created. |
| **AI governance** | Every outreach message is human-reviewed before sending. AI drafts and scores; a person approves. No autonomous deployment. |
| **Infrastructure** | Runs on existing tools and SOC 2-compliant SaaS. No new servers, no proprietary code, no capital expenditure. Pilot cost under $200. |

### Approval Request

Approval of this proposal authorizes, effective on sign-off:
- Deployment of the PULSE scoring job against the national business data and NEWITY CRM model.
- Generation of the qualified-lead output and heatmap reporting for the NEWITY team.
- Automated, human-reviewed outreach to qualified businesses (Branch A).
- BSO partnership outreach targeted to qualified-lead clusters (Branch B).
- Weekly KPI reporting to Uzziel Guzman beginning Week 5, leading to a Week 10 decision on permanent implementation.

---

## 6. Success Metrics — What Week 10 Will Prove

**Primary KPI:** a measurable increase in qualified businesses reaching NEWITY's application start versus the current channel baseline — counting only businesses that meet every qualification gate.

| Metric | 10-Week Target | How Measured |
|---|---|---|
| Qualified businesses identified (Branch A) | 50–200 real leads | Scoring job output |
| Qualified leads delivered to NEWITY pipeline | Track & report | Pipeline attribution |
| Direct-outreach response / self-select rate | Report delta | Outreach tracking |
| BSOs activated near qualified clusters (Branch B) | 8–12 partners | Partnership log |
| NEWITY applications started | Track & report | Internal pipeline data |
| Cost per qualified lead vs. current baseline | Report delta | Ops baseline data |

### Three Proof Points for Permanent Implementation

1. **A working output, not a concept.** A real list of qualified businesses — for-profit, 2+ years (4+ for construction), $100K–$10M, no trucking — generated by the system during the pilot.
2. **Measurable lift.** Evidence that PULSE moves a higher share of qualified businesses to application start than business-as-usual, at a lower cost per qualified lead.
3. **A hands-off path forward.** A scheduled job, a scored BSO targeting map, a reviewed outreach playbook, and a scale roadmap — everything needed for any NEWITY team member to run PULSE after summer.

---

> PULSE turns NEWITY's unique assets — a 125,000-loan CRM and three years of SBA-funded research — into a recurring, self-running source of pre-qualified borrowers. It costs under $200 to pilot and is designed to run permanently after summer.

---

*Rene De Sola Zumarraga · NEWITY Finance & Data Analyst Intern, Summer 2026 · Lead Quantitative Researcher, Loyola QSII · SBA Grant #SBAHQ23I0138 · Supervisor: Uzziel Guzman*
