# models/stt_vosk.py

import json
from vosk import Model, KaldiRecognizer
from livekit.agents.stt import STT


class VoskSTT(STT):
    """
    Offline Speech-to-Text using Vosk.
    Compatible with LiveKit audio frames.
    """

    def __init__(self, model_path: str):
        capabilities = type(
            "Capabilities",
            (),
            {"streaming": False} 
        )()
        super().__init__(capabilities=capabilities)

        self.model = Model(model_path)

    async def _recognize_impl(self, audio_frame, **kwargs) -> str:
        """
        Called by LiveKit with an AudioFrame.
        """
        pcm_bytes = audio_frame.data.tobytes()
        recognizer = KaldiRecognizer(self.model, audio_frame.sample_ratl)

        recognizer.AcceptWaveform(pcm_bytes)
        result = recognizer.Result()

        text = json.loads(result).get("text", "")
        return text
