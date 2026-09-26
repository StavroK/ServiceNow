from src.classifier import Prediction
from src.inference import automation_decision


def test_high_confidence_candidate() -> None:
    p = Prediction("A", "B", "C", 3, 0.95)
    assert automation_decision(p) == "auto_route_candidate"


def test_medium_confidence_requires_confirmation() -> None:
    p = Prediction("A", "B", "C", 3, 0.80)
    assert automation_decision(p) == "analyst_confirmation"


def test_low_confidence_falls_back_to_manual() -> None:
    p = Prediction("A", "B", "C", 3, 0.50)
    assert automation_decision(p) == "manual_triage"
