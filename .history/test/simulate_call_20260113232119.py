from brain.controller import BrainController
from runtime.session import CallSession
import uuid


def simulate():
    brain = BrainController()

    # Each simulation represents one call
    session = CallSession(call_id=str(uuid.uuid4()))

    print("📞 Admission Voice Agent (type 'exit' to quit)")
    print("---------------------------------------------")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("📴 Call ended.")
            break

        response = brain.handle(user_input, session)

        print(f"Agent: {response}")
        print(f"[DEBUG] CallID={session.call_id}")
        print(f"[DEBUG] State={session.state}, Slots={session.slots}")
        print()


if __name__ == "__main__":
    simulate()
