# brain/controller.py

from brain.fsm import FSM_TRANSITIONS
from brain.slot_extractor import SlotExtractor
from brain.answer_generator import AnswerGenerator
from knowledge.loader import KnowledgeLoader


class BrainController:
    def __init__(self):
        self.slot_extractor = SlotExtractor()
        self.answer_generator = AnswerGenerator()
        self.knowledge = KnowledgeLoader()

    def handle(self, text: str, session) -> str:
        """
        Main brain entry point.
        """

        # TODO 1: detect intent from text
        intent = self.detect_intent(text)

        # TODO 2: FSM transition
        session.state = self.next_state(session.state, intent)

        # TODO 3: get required slots for this state
        required_slots = self.required_slots(session.state)

        # TODO 4: extract slots
        extracted = self.slot_extractor.extract(text, required_slots)
        session.slots.update(extracted)

        # TODO 5: check missing slots
        missing = [s for s in required_slots if s not in session.slots]

        if missing:
            return self.ask_for_slot(missing[0])

        # TODO 6: load knowledge
        knowledge = self.load_knowledge_for_state(session.state)

        # TODO 7: generate answer
        return self.answer_generator.generate(
            session.state, session.slots, knowledge
        )
