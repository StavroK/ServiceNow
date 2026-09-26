# Solution Architecture

## Design objective

The architecture separates the **system of engagement and record** (ServiceNow) from the **AI decision service** so models can be governed, tested, versioned, monitored, and rolled back independently.

## Logical flow

1. An incident is created or materially updated in ServiceNow.
2. A workflow sends an approved subset of ticket data to the AI service.
3. The AI service enriches the request with permitted context such as CMDB attributes or historical taxonomy mappings.
4. ML components predict category, subcategory, assignment group, and optionally priority.
5. GenAI components may summarize the incident or retrieve approved knowledge.
6. A policy layer evaluates confidence and business risk.
7. ServiceNow receives recommendations or approved automated updates.
8. Recommendation, model version, confidence, human action, and final outcome are logged for audit and improvement.

## AWS reference deployment

- **Amazon API Gateway** — secured ingress
- **AWS Lambda or ECS/Fargate** — inference/orchestration service
- **Amazon Bedrock** — optional GenAI summarization and RAG
- **Amazon S3** — approved artifacts and evaluation datasets
- **AWS Secrets Manager** — integration secrets
- **Amazon CloudWatch** — logs, metrics, alarms
- **AWS KMS** — encryption controls
- **VPC endpoints/private networking** — where required by enterprise security architecture

## ServiceNow touchpoints

- Incident table for controlled read/update operations
- CMDB context where data quality permits
- Flow Designer / IntegrationHub for orchestration patterns
- Performance Analytics or equivalent reporting for operational KPIs
- SPM for program-level investment, milestone, risk, and value tracking where appropriate

## Non-functional requirements

### Security
- OAuth or enterprise-approved authentication
- Least privilege
- Encryption in transit and at rest
- No secrets in source control
- PII minimization

### Reliability
- Timeouts and retry policy
- Circuit breaker / graceful degradation
- Manual workflow fallback
- Versioned model endpoints

### Observability
- Request volume and latency
- Prediction distribution
- Confidence distribution
- Error rates
- Human override rate
- Routing accuracy
- Drift indicators

## Architecture principle

AI failure must not become ITSM failure. If the AI service is unavailable or insufficiently confident, the standard ServiceNow process remains available.
