# brain/slot_extractor.py

class SlotExtractor:
    def extract(self, text: str, required_slots: list[str]) -> dict:
        """
        Extract slot values from text.
        Returns only slots it is confident about.
        """

        extracted = {}

        # TODO 1: very naive rule-based extraction for now
        # Example:
        # if "btech" in text.lower(): extracted["course"] = "BTech"

        # TODO 2 (later): replace with LLM-based JSON extraction

        return extracted
