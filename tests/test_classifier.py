from src.classifier import classify_incident


def test_sap_incident_is_routed_to_finance_support() -> None:
    result = classify_incident("SAP invoice posting error", "Finance user cannot post invoice", "SAP-FIN-PROD")
    assert result.category == "Enterprise Applications"
    assert result.assignment_group == "SAP Finance Support"
    assert result.confidence >= 0.90


def test_unknown_incident_falls_back_safely() -> None:
    result = classify_incident("Unexpected application behavior")
    assert result.assignment_group == "Service Desk"
    assert result.confidence < 0.70
