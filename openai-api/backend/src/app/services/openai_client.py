import os
from dotenv import load_dotenv
from openai import OpenAI
from openai import AsyncOpenAI

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../../../config/.env.dev'))

class OpenAIClient:
    def __init__(self) -> None:
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("ERROR: OpenAI APIキーが設定されていません")
        
        self.client = OpenAI(api_key=self.api_key)
        self.async_client = AsyncOpenAI(api_key=self.api_key)

    def get_client(self) -> OpenAI:
        return self.client

    def get_async_client(self) -> AsyncOpenAI:
        return self.async_client
    