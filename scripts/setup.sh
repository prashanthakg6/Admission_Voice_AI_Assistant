#!/bin/bash

set -e

echo "📁 Creating project: $PROJECT_NAME"


# Root files
touch .env .gitignore README.md requirements.txt
touch main.py server.py agent.py

# Core folders
mkdir -p brain runtime knowledge handoff analytics models scripts

# Init files
touch brain/__init__.py runtime/__init__.py knowledge/__init__.py
touch handoff/__init__.py analytics/__init__.py models/__init__.py

# Brain
touch brain/fsm.py
touch brain/intents.py
touch brain/slots.py
touch brain/slot_extractor.py
touch brain/controller.py
touch brain/llm_slot_prompt.py
touch brain/answer_generator.py

# Runtime
touch runtime/session.py

# Knowledge
touch knowledge/loader.py
touch knowledge/courses.json
touch knowledge/eligibility.json
touch knowledge/fees.json
touch knowledge/deadlines.json
touch knowledge/documents.json
touch knowledge/process.json

# Handoff
touch handoff/office_hours.py
touch handoff/controller.py
touch handoff/office_hours.json

# Analytics
touch analytics/logger.py

# Models
touch models/stt_vosk.py
touch models/llm_ollama.py
touch models/tts_pyttsx3.py

echo "✅ Project structure created successfully!"
echo "👉 Next steps:"
echo "   1. Fill .env with LiveKit credentials"
echo "   2. Install dependencies: pip install -r requirements.txt"
echo "   3. Run: python main.py console"
