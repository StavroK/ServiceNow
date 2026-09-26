from src.classifier import Prediction


def automation_decision(prediction: Prediction) -> str:
    """Map confidence to an illustrative human-in-the-loop decision policy."""
    if prediction.confidence >= 0.90:
        return "auto_route_candidate"
    if prediction.confidence >= 0.70:
        return "analyst_confirmation"
    return "manual_triage"
