from dataclasses import dataclass


@dataclass(frozen=True)
class Prediction:
    category: str
    subcategory: str
    assignment_group: str
    priority: int
    confidence: float


def classify_incident(short_description: str, description: str = "", cmdb_ci: str | None = None) -> Prediction:
    """Deterministic portfolio scaffold.

    Production implementations should replace these rules with a validated model,
    calibrated probabilities, ServiceNow taxonomy mapping, and monitored inference.
    """
    text = f"{short_description} {description} {cmdb_ci or ''}".lower()

    if any(token in text for token in ("sap", "invoice", "finance")):
        return Prediction("Enterprise Applications", "SAP", "SAP Finance Support", 2, 0.91)
    if any(token in text for token in ("password", "login", "locked")):
        return Prediction("Access", "Authentication", "Service Desk", 3, 0.88)
    if any(token in text for token in ("network", "vpn", "latency", "wifi")):
        return Prediction("Infrastructure", "Network", "Network Operations", 2, 0.86)

    return Prediction("General", "Unclassified", "Service Desk", 3, 0.62)
