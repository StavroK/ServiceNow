# ServiceNow AI Incident Intelligence

Enterprise reference implementation for **AI-assisted incident triage in ServiceNow**.

This portfolio project demonstrates how machine learning and generative AI can augment ITSM workflows through incident classification, routing recommendations, summarization, knowledge retrieval, confidence-based automation, governance, and operational measurement.

> **Portfolio focus:** enterprise AI delivery, ServiceNow integration, solution architecture, AI governance, AWS deployment patterns, and measurable ITSM outcomes.

## What this repository demonstrates

### Enterprise AI delivery
- Business-to-technology problem framing
- MVP-to-production delivery roadmap
- Human-in-the-loop operating model
- Risk, governance, and KPI design
- Production-readiness thinking

### ServiceNow
- Incident Management / ITSM workflow integration
- CMDB context as an input to AI decisions
- REST-based integration patterns
- Flow Designer / workflow orchestration concepts
- Performance and service-management KPI design
- Extension paths for SPM, APM, ITOM, and SecOps use cases

### AI / ML / GenAI
- NLP incident classification
- Confidence-based routing decisions
- Model evaluation and monitoring
- GenAI summarization and knowledge-assist patterns
- Retrieval-augmented resolution recommendations

### Cloud & engineering
- AWS reference architecture
- Python service layer
- REST API
- CI checks and automated tests
- Observability and secure configuration patterns

---

## Business problem

Enterprise service desks receive incidents with inconsistent descriptions, categories, priorities, and assignment decisions. Manual triage can increase assignment time, reassignment rates, analyst effort, and ultimately mean time to resolution.

This project treats AI as an **operational decision-support capability**, not a standalone model.

The target workflow is:

```text
ServiceNow incident
        |
        v
Context enrichment (ticket + CMDB + history)
        |
        v
AI Incident Intelligence
  - classification
  - assignment recommendation
  - priority recommendation
  - summary
  - similar incidents / knowledge
        |
        v
Confidence policy
  >= 0.90  -> automated action where approved
  0.70-0.89 -> analyst confirmation
  < 0.70   -> manual triage
        |
        v
ServiceNow update + audit trail + KPI monitoring
```

The thresholds above are **illustrative portfolio defaults**, not production recommendations. They should be calibrated with business risk, class imbalance, cost of misrouting, and observed model performance.

---

## Target operating outcomes

The project is designed around measurable ITSM outcomes.

| KPI | Example target | Why it matters |
|---|---:|---|
| Routing accuracy | > 85% | Fewer incorrect assignments |
| Classification accuracy | > 90% | More consistent incident data |
| Mean time to assign | < 2 min | Faster ownership |
| Reassignment rate | < 8% | Less queue bouncing |
| Analyst triage effort | -30% | More analyst capacity |
| MTTR | -20% | Faster restoration of service |
| AI recommendation acceptance | > 80% | Measures usefulness to analysts |

These are **illustrative targets** for a portfolio reference architecture and must be replaced with baseline-driven targets in a real implementation.

---

## Reference architecture

```text
+---------------------------+
|         ServiceNow        |
| ITSM | CMDB | PA | SPM    |
+-------------+-------------+
              |
              | REST / IntegrationHub
              v
+---------------------------+
|       API Gateway         |
+-------------+-------------+
              |
              v
+---------------------------+
| AI Incident Orchestrator  |
| Lambda / Container        |
+-------+-----------+-------+
        |           |
        |           +--------------------+
        v                                v
+---------------+              +-------------------+
| ML classifier |              | Amazon Bedrock   |
| routing /     |              | summary / RAG    |
| categorization|              | knowledge assist |
+-------+-------+              +---------+---------+
        |                                |
        +---------------+----------------+
                        |
                        v
                +---------------+
                | Monitoring &  |
                | audit evidence|
                +---------------+
```

See [docs/architecture.md](docs/architecture.md) for the detailed component model and [docs/servicenow-integration.md](docs/servicenow-integration.md) for the ServiceNow interaction pattern.

---

## Repository structure

```text
.
├── README.md
├── ServiceNow_Incident_Classifier.ipynb   # original ML experiment
├── api/
│   └── app.py                             # lightweight inference API
├── src/
│   ├── classifier.py
│   ├── inference.py
│   └── servicenow_client.py
├── tests/
│   ├── test_classifier.py
│   └── test_inference.py
├── docs/
│   ├── architecture.md
│   ├── business-case.md
│   ├── delivery-roadmap.md
│   ├── governance.md
│   ├── model-card.md
│   └── servicenow-integration.md
└── .github/workflows/
    └── ci.yml
```

The original notebook is retained as historical experimental evidence. The surrounding project structure turns the experiment into a more complete enterprise solution narrative.

---

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
uvicorn api.app:app --reload
```

Example request:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "short_description": "SAP users cannot post invoices",
    "description": "Finance users receive a timeout during invoice posting",
    "cmdb_ci": "SAP-FIN-PROD"
  }'
```

Illustrative response:

```json
{
  "category": "Enterprise Applications",
  "subcategory": "SAP",
  "assignment_group": "SAP Finance Support",
  "priority": 2,
  "confidence": 0.91,
  "decision": "auto_route_candidate"
}
```

The included Python implementation is intentionally lightweight and deterministic so the repository can be cloned and tested without proprietary data or cloud credentials. It is a reference scaffold for the production integration described in the documentation.

---

## Enterprise delivery approach

The recommended delivery sequence is:

1. **Discovery & baseline** — process mapping, data quality, taxonomy, CMDB coverage, security, KPI baseline.
2. **Offline MVP** — classifier, evaluation, explainability, threshold policy.
3. **Sandbox integration** — REST service + ServiceNow non-production instance.
4. **Human-in-the-loop pilot** — recommendations only, controlled traffic, analyst feedback.
5. **Production rollout** — guarded automation, monitoring, rollback, support model.
6. **GenAI augmentation** — summarization, knowledge retrieval, resolution recommendations.
7. **Continuous improvement** — drift detection, taxonomy changes, model retraining, value tracking.

See [docs/delivery-roadmap.md](docs/delivery-roadmap.md).

---

## Governance principles

This portfolio treats governance as part of the architecture:

- Human review for uncertain or high-impact decisions
- Explicit confidence thresholds
- No credentials committed to source control
- PII minimization and data-retention controls
- RBAC and least-privilege integration users
- Audit logging of AI recommendations and human overrides
- Model/version traceability
- Drift and performance monitoring
- Fallback to standard ServiceNow workflow
- Change-management and production rollback procedures

See [docs/governance.md](docs/governance.md).

---

## ML case study notebook

The original 2021 Colab experiment has been rebuilt as a focused, reproducible enterprise ML case study:

- [ServiceNow_Incident_Classifier.ipynb](ServiceNow_Incident_Classifier.ipynb)

The notebook now demonstrates privacy-conscious data handling, class-imbalance analysis, a majority-class baseline, multilingual word + character TF-IDF features, logistic-regression classification, stratified evaluation, macro/weighted F1, confusion analysis, confidence-based human-in-the-loop policy, error analysis, and model metadata export.

If a private ServiceNow dataset is not available locally, the notebook generates synthetic incidents so reviewers can execute the workflow without proprietary data.

---

## Next evolution

Potential extensions include:

- Replace the deterministic reference classifier with a trained model artifact
- Add Bedrock-based incident summarization
- Add RAG over approved knowledge articles
- Add ServiceNow OAuth integration
- Add CMDB / service context
- Add CloudWatch/OpenTelemetry monitoring
- Add model drift dashboards
- Add infrastructure as code
- Add synthetic performance and security tests
- Add a demo ServiceNow Flow Designer configuration

---

## Disclaimer

This is an independent portfolio/reference implementation. It is not an official ServiceNow or AWS product, and no proprietary customer data, credentials, or confidential implementation artifacts should be committed to this repository.
