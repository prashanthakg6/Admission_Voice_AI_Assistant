# runtime/session.py

class CallSession:
    def __init__(self, call_id: str):
        self.call_id = call_id
        self.state = "GREETING"
        self.slots = {}
        self.clarification_attempts = 0
        self.last_intent = None

    def update_slot(self, key, value):
        if key not in self.slots:
            self.slots[key] = value

    def override_slot(self, key, value):
        self.slots[key] = value

    def merge_slots(self, extracted: dict):
        for key, value in extracted.items():
            if value in (None, "", []):
                continue
            self.override_slot(key, value)