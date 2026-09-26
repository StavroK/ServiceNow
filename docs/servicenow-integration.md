# ServiceNow Integration Pattern

## Trigger

A ServiceNow flow or approved integration trigger invokes the AI service when an incident is created or when relevant fields change.

## Minimal request

```json
{
  "short_description": "SAP users cannot post invoices",
  "description": "Finance users receive a timeout during invoice posting",
  "cmdb_ci": "SAP-FIN-PROD"
}
```

## AI response

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

## Recommended ServiceNow behavior

The integration should not blindly overwrite analyst work. It should validate incident state, model version, confidence policy, and whether target fields have already been manually changed.

Potential implementation patterns:

- recommendation fields visible to the analyst;
- work note recording the AI recommendation;
- Flow Designer branch based on confidence and service criticality;
- assignment update only for approved categories;
- event emission for monitoring and audit.

## Authentication

Use an enterprise-approved OAuth pattern and a least-privilege integration identity. Do not use hard-coded credentials or personal accounts.

## Error handling

On API timeout, model error, invalid response, or policy failure:

1. do not block incident creation;
2. preserve the standard ServiceNow workflow;
3. log the integration failure;
4. expose operational alerts when thresholds are exceeded.

## Example client

See `src/servicenow_client.py`. It deliberately reads the instance URL and bearer token from environment variables.
