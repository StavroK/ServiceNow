# Enterprise Delivery Roadmap

## Phase 1 — Discovery and baseline

**Objectives**
- Map current incident lifecycle and assignment logic.
- Assess data quality, taxonomy stability, CMDB coverage, integrations, and security constraints.
- Establish operational baselines.

**Exit evidence**
- approved use case;
- data assessment;
- KPI baseline;
- architecture decision record;
- initial risk register.

## Phase 2 — Offline MVP

**Objectives**
- Train or configure baseline classifier.
- Measure precision, recall, F1, class-level performance, and calibration.
- Define human-in-the-loop thresholds.

**Exit evidence**
- reproducible evaluation;
- documented model card;
- acceptance criteria;
- failure-mode review.

## Phase 3 — ServiceNow sandbox integration

**Objectives**
- Expose a secured inference API.
- Integrate with a non-production ServiceNow instance.
- Validate identity, authorization, field mappings, latency, and error handling.

## Phase 4 — Human-in-the-loop pilot

AI recommendations are visible to analysts but automation is limited. Track acceptance, override reasons, routing accuracy, time saved, and incidents where AI should not be used.

## Phase 5 — Controlled production

Automation is introduced only where evidence supports it. Use change control, rollback, monitoring, and support ownership.

## Phase 6 — GenAI augmentation

Add incident summarization, knowledge retrieval, and resolution assistance using approved sources and explicit citation/grounding controls.

## Phase 7 — Continuous improvement

- monitor drift;
- retrain or recalibrate;
- update taxonomy mappings;
- review overrides;
- measure realized value;
- revalidate governance controls.

## Example portfolio governance cadence

| Cadence | Forum | Focus |
|---|---|---|
| Weekly | Delivery team | blockers, risks, quality, sprint outcomes |
| Biweekly | Product / service owners | adoption, workflow feedback, backlog |
| Monthly | Steering committee | value, risk, milestones, funding decisions |
| Quarterly | Model governance | drift, controls, revalidation, retirement |
