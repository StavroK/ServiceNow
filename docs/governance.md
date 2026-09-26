# AI Governance and Risk Controls

## Control objective

AI recommendations must be **traceable, bounded, reversible, and measurable**.

## Human-in-the-loop policy

Illustrative portfolio policy:

- **confidence >= 0.90:** eligible for approved low-risk automation;
- **0.70-0.89:** analyst confirmation required;
- **< 0.70:** standard manual triage.

Confidence alone is not sufficient for production automation. Business impact, service criticality, security classification, data sensitivity, and class-specific error cost must also be considered.

## Key risks and controls

| Risk | Example control |
|---|---|
| Misrouting | thresholding, class-level evaluation, manual fallback |
| Model drift | distribution monitoring, scheduled revalidation |
| PII exposure | field allowlist, minimization, retention policy |
| Unauthorized update | scoped ServiceNow role and OAuth token |
| GenAI hallucination | grounding, approved corpus, analyst confirmation |
| Prompt injection | isolate untrusted text, tool restrictions, output validation |
| Taxonomy change | versioned mappings and change management |
| Vendor/model change | regression suite and version pinning |
| Silent failure | observability, alerts, circuit breaker |

## Audit record

For each AI-assisted action, retain as policy permits:

- incident identifier;
- model/prompt version;
- timestamp;
- input feature references or approved hashes;
- prediction/recommendation;
- confidence;
- policy decision;
- analyst acceptance/override;
- final assignment/outcome.

## Production gates

No production automation should be enabled without:

1. security review;
2. privacy/data review;
3. offline quality acceptance;
4. sandbox integration test;
5. pilot evidence;
6. rollback plan;
7. monitoring dashboard;
8. named service owner.
