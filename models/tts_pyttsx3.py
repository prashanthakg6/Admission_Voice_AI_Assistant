# models/tts_pyttsx3.py

import tempfile
import pyttsx3


class Pyttsx3TTS:
    """
    Offline Text-to-Speech using pyttsx3.
    Produces WAV audio bytes.
    """

    def __init__(self, rate: int = 170):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)

    async def speak(self, text: str) -> bytes:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            self.engine.save_to_file(text, tmp.name)
            self.engine.runAndWait()
            tmp.seek(0)
            audio_bytes = tmp.read()

        return audio_bytes
