# brain/controller.py

from brain.fsm import FSM_TRANSITIONS
from brain.slot_extractor import SlotExtractor
from brain.answer_generator import AnswerGenerator
from knowledge.loader import KnowledgeLoader
from brain.slots import REQUIRED_SLOTS, OPTIONAL_SLOTS


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
    

    def detect_intent(self, text): 
        """
        Dummy intent detection based on keywords.
        """

        text = text.lower()

        if "course" in text:
            return "COURSE_INFO"
        elif "fee" in text or "cost" in text:
            return "FEES_QUERY"
        elif "eligible" in text or "eligibility" in text:
            return "ELIGIBILITY_QUERY"
        elif "date" in text or "deadline" in text:
            return "DATES_QUERY"
        elif "document" in text or "paper" in text:
            return "DOCUMENTS_QUERY"
        elif "process" in text or "procedure" in text:
            return "PROCESS_QUERY"
        elif "human" in text or "representative" in text:
            return "CONTACT_HUMAN"
        else:
            return "UNKNOWN"
        
    def next_state(self, current_state, intent): ...

    def required_slots(self, state):
        if state in REQUIRED_SLOTS:
            return REQUIRED_SLOTS[state]
        return []
        


    def ask_for_slot(self, slot):
        questions = {
            "course_name": "Which course are you interested in?",
            "percentage": "What is your percentage?",
            "subjects": "Which subjects have you studied?",
            "exam_type": "What type of exam did you take?",
            "hostel_required": "Do you require hostel accommodation?",
        }
        return questions.get(slot, "Could you please provide more information?")
    
    
    def load_knowledge_for_state(self, state): ...
