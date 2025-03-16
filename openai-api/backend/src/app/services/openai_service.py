import os
from openai import OpenAI
from openai import AsyncOpenAI

class OpenAIService:
    def __init__(self) -> None:
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("ERROR: OpenAI API key is not set")
        
        self.client = OpenAI(api_key=self.api_key)
        self.async_client = AsyncOpenAI(api_key=self.api_key)

    def get_client(self) -> OpenAI:
        return self.client

    def get_async_client(self) -> AsyncOpenAI:
        return self.async_client
