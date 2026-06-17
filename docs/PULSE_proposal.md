# PULSE: AI-Driven Lead Qualification and Capital Connection System

**NEWITY · Summer 2026**
**Submitted by:** Anoushka Maller · Max Karolyi · Taksh Goel · Rene De Sola

---

## 1. Executive Summary

NEWITY's current lead pipeline depends on a referral and broker network that charges a percentage fee per lead, a cost that compounds at scale and limits margin on every deal closed through that channel. At the same time, thousands of small businesses that meet NEWITY's qualification criteria, operating for two or more years and generating over $100,000 in annual revenue and eligible for an SBA loan, are never reached because no direct outbound channel exists to find them.

PULSE is a two-branch, AI-driven system that solves both problems. It identifies pre-qualified small businesses from national data before they search and delivers them directly into NEWITY's pipeline. Where direct data cannot reach, PULSE activates Business Support Organizations (BSOs) as referral partners, targeting only the geographic clusters where qualified businesses are most concentrated. The result is a self-improving lead engine that gets smarter with every outcome it processes.

---

## 2. Business Case

**Target Market**

PULSE targets for-profit small businesses that meet all of the following:
- In operation 2 or more years (4 or more years for construction businesses)
- Annual revenue of $100,000 or more
- Not classified under NAICS 484 (trucking)
- Structured as a for-profit entity

**How PULSE Generates Qualified Leads**

- Branch A (Direct): Ingests national business data from the SBA database and Livesight, runs every business through two scoring layers, and surfaces only those that pass all qualification gates. Qualified businesses receive direct, AI-assisted outreach, with the highest-propensity leads contacted first.
- Branch B (BSO Referral): Where Branch A identifies dense clusters of qualified businesses, PULSE activates the nearest BSOs as referral partners. These BSOs surface qualified businesses with no digital footprint that data alone cannot reach.

**Business Value**

| Dimension | Impact |
|-----------|--------|
| Revenue | More qualified leads in the pipeline means more funded loans without increasing referral fee spend |
| Efficiency | Every PULSE lead has already passed qualification gates, eliminating wasted time on ineligible businesses |
| Scalability | The system runs on a recurring weekly schedule and produces leads automatically without additional headcount |

**Key Assumptions**
- SBA business data is publicly accessible and scrapable
- Livesight data licensing is accessible within the project budget
- NEWITY's CRM history can be used to train the propensity scoring model
- Legal will confirm email outreach compliance upon deployment review

---

## 3. Description of the Initiative

**What Is Being Built**

PULSE has three components:

**1. Data Pipeline**
Automated ingestion of SBA business data and Livesight records, supplemented by Secretary of State registration data for founding date and entity type verification.

**2. Two-Layer Scoring System**

Scoring System 1 (SBA Hard Gates, Pass/Fail): Every business must pass all eligibility criteria before advancing. Any business that fails a single gate is excluded entirely.

Scoring System 2 (NEWITY Propensity Model, Ranking): Trained on NEWITY's CRM history, this model scores businesses based on the likelihood of them not defaulting and their probability of converting into a funded loan. Each lead marked closed, not closed, and the reason why feeds back into the model, making it more accurate over time.

**3. Flask Web Application**
A dashboard giving the NEWITY team a ranked lead list, geographic heatmap, filtering tools, and Python-powered data science queries in one interface.

**How Claude Is Used**

Claude is embedded throughout PULSE:
- Research and ideation: Analyzes data, identifies patterns, and refines scoring logic during the build phase
- Outreach drafting: Drafts personalized outreach emails to qualified businesses. Every message is human-reviewed before sending.
- Score explanation: Explains in plain language why a specific business scored the way it did
- Data analysis: Surfaces patterns in the qualified lead pool and assists with interpreting results

**Why This Approach Over Alternatives**

Buying a third-party lead list gives undifferentiated data any competitor can purchase. PULSE's scoring model is trained on NEWITY's own CRM, encompassing 125,000 or more loans spanning funded and declined applications. No competitor can replicate this. The referral and broker network currently feeding NEWITY's pipeline charges a percentage fee per lead. PULSE would ideally eliminate that referral fee on the leads it generates, improving overall margin, pending legal confirmation.

---

## 4. Implementation Plan

*(Executive Approval Required)*

| Phase | Weeks | Key Activities |
|-------|-------|----------------|
| Research and Proposal | 1-2 | Business case finalized, proposal submitted, executive approval secured |
| Initial Implementation | 3-4 | Data pipeline built; Scoring System 1 implemented and tested; Flask app scaffolded; Figma designs started; IT tracking set up |
| Optimization and Measurement | 5-8 | Scoring System 2 trained and deployed; Branch A outreach live (human-reviewed); Branch B BSO targeting activated; heatmap dashboard live; weekly KPI reporting; model refined on early results |
| Final Presentation | 10 | Full KPI dashboard delivered; qualified lead list generated; scale roadmap and handoff package presented to executive team |

**Dependencies and Constraints**
- IT to confirm database access and storage within NEWITY's existing systems
- Livesight licensing confirmation before data pipeline build begins
- Legal sign-off required before any outreach is deployed
- Team roles (Anoushka Maller, Max Karolyi, Taksh Goel, Rene De Sola) to be assigned upon executive approval

---

## 5. Budget and Resources

*Target spend: $1,500 with $500 held as contingency reserve*

| Item | Purpose | Estimated Cost |
|------|---------|----------------|
| Livesight data access | Business data for scoring pipeline | TBD, licensing to be confirmed |
| Figma | UI and dashboard design | ~$150 |
| Cloud hosting | Flask app deployment | ~$100 |
| SBA Small Business Search | Primary data source | Free |
| GitHub Education | Free dev tools and Copilot for interns | Free (pending application) |
| Flask and Python libraries | Backend framework and data science tools | Free (open source) |
| Contingency reserve | Unexpected tool or data costs | $500 |
| **Total** | | **~$1,500 + $500 reserve** |

**Internal Support Required**
- IT/Infrastructure: database provisioning, storage within NEWITY's existing environment
- Legal team: email compliance review prior to outreach deployment
- NEWITY operations: CRM data access for model training. We would also be working with Merve if we create a partnership with a BSO, community engagement center, or chamber of commerce.

---

## 6. Security and Compliance Considerations

*(Infrastructure and Compliance Approval Required)*

**Data Involved**

PULSE processes publicly available business data (SBA records, Secretary of State filings, Livesight) and NEWITY's internal CRM data for model training. No new personal financial data is collected outside of NEWITY's existing SBA-compliant application pipeline.

**CAN-SPAM Compliance**

All outreach emails will comply with CAN-SPAM requirements, including clear sender identification, physical address, and an unsubscribe mechanism in every message. No emails are sent autonomously; every message is human-reviewed and approved before delivery. During the pilot phase, no actual emails are sent. The system is built and validated in simulation mode first. Final legal sign-off will be obtained before any live outreach begins.

**Data Storage and AI Governance**

All data is stored within NEWITY's existing systems. No new servers or external databases are created. Claude drafts and scores; a person approves. No autonomous AI actions are taken without human review.

---

## 7. Success Metrics

**KPIs**

| Metric | Target by Week 10 |
|--------|------------------|
| Qualified businesses identified (Branch A) | 200+ qualified leads |
| Qualified leads delivered to NEWITY pipeline | Track and report |
| Direct outreach response rate | Report delta |
| BSOs activated near qualified clusters (Branch B) | 8-12 partners |
| NEWITY applications started from PULSE leads | Track and report |
| Referral fee spend avoided | Report delta vs. broker channel |

**Tracking Plan**

PULSE is a new initiative. No existing program of this type exists in NEWITY's system. The team will work with IT to establish pipeline attribution tracking so leads generated through PULSE can be distinguished from those coming through the referral and broker network, making the cost-per-qualified-lead comparison measurable and auditable.

**What Success Looks Like by End of Internship**

1. A real, working list of qualified leads generated by the PULSE system during the pilot.
2. A measurable lift in qualified applications at a lower effective cost per lead than the broker and referral channel.
3. A fully operational system designed to run at least once a week, with a scored BSO targeting map, a human-reviewed outreach playbook, and a scale roadmap that any NEWITY team member can operate after summer.

---

*Anoushka Maller · Max Karolyi · Taksh Goel · Rene De Sola*
*NEWITY Summer Internship 2026 · AI-Driven Lead Generation Initiative*
