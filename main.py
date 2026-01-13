from models.stt_vosk import VoskSTT
from models.llm_ollama import OllamaLLM
from models.tts_pyttsx3 import Pyttsx3TTS

stt = VoskSTT("models/vosk-model-small-en-us-0.15")
llm = OllamaLLM(model="mistral")
tts = Pyttsx3TTS()
