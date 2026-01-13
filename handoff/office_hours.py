# handoff/office_hours.py

import json
from datetime import datetime
from pathlib import Path
import pytz


def office_hours() -> bool:
    """
    Returns True if current time is within office hours,
    otherwise False.
    """
    config_path = Path(__file__).parent / "office_hours.json"

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    tz = pytz.timezone(config["timezone"])
    now = datetime.now(tz)

    current_day = now.strftime("%A")
    current_time = now.strftime("%H:%M")

    if current_day not in config["working_days"]:
        return False

    start = config["working_hours"]["start"]
    end = config["working_hours"]["end"]

    return start <= current_time <= end
