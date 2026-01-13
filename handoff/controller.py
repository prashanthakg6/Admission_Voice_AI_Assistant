# handoff/controller.py

import json
from pathlib import Path
from .office_hours import office_hours


def controller(reason: str = "user_request") -> dict:
    """
    Handles human handoff decision.

    Returns:
        {
            "handoff": bool,
            "message": str,
            "action": "transfer" | "end_call"
        }
    """
    config_path = Path(__file__).parent / "office_hours.json"

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    if office_hours():
        return {
            "handoff": True,
            "message": "I will connect you to our admissions team now.",
            "action": "transfer"
        }

    return {
        "handoff": False,
        "message": config["fallback_message"],
        "action": "end_call"
    }
