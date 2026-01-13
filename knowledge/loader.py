# knowledge/loader.py

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

def load_json(filename):
    with open(BASE_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)

knowledge = {
    "courses": load_json("courses.json"),
    "eligibility": load_json("eligibility.json"),
    "fees": load_json("fees.json"),
    "deadlines": load_json("deadlines.json"),
    "documents": load_json("documents.json"),
    "process": load_json("process.json"),
}
