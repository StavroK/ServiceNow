from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.classifier import classify_incident
from src.inference import automation_decision

app = FastAPI(title="ServiceNow AI Incident Intelligence", version="0.1.0")


class IncidentRequest(BaseModel):
    short_description: str = Field(min_length=3)
    description: str = ""
    cmdb_ci: str | None = None


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict(incident: IncidentRequest) -> dict[str, object]:
    result = classify_incident(incident.short_description, incident.description, incident.cmdb_ci)
    return {
        "category": result.category,
        "subcategory": result.subcategory,
        "assignment_group": result.assignment_group,
        "priority": result.priority,
        "confidence": result.confidence,
        "decision": automation_decision(result),
    }
