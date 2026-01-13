import asyncio
from models.llm_ollama import OllamaLLM


async def main():
    llm = OllamaLLM(model="mistral")
    response = await llm.generate("Say hello in one short sentence.")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
