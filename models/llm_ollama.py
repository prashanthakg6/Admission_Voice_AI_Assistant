# models/llm_ollama.py

import aiohttp


class OllamaLLM:
    """
    Lightweight async wrapper around Ollama REST API.
    """

    def __init__(self, model: str = "mistral", url: str = "http://localhost:11434"):
        self.model = model
        self.url = url.rstrip("/")

    async def generate(self, text: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": text}
            ]
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.url}/v1/chat/completions",
                json=payload,
                timeout=60
            ) as response:
                data = await response.json()
                return data["choices"][0]["message"]["content"]
