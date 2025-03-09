from src.openai_client import OpenAIClient
from src.memory_db import MemoryDB

class Persona:
    # def __init__(self, name, personality, memory=None):
    def __init__(self, name, personality, memory_db: MemoryDB):
        self.name = name
        self.personality = personality
        self.memory_db = memory_db
        self.client = OpenAIClient().get_client()

    def remember(self, conversation_id, role, content):
        """会話履歴を記録する"""
        self.memory_db.insert(conversation_id, role, content)

    def chat(self, conversation_id, user_input) -> str:
        """ChatGPTを使って会話を行う"""
        messages = [{"role": "system", "content": self.personality}]
        messages += self.memory_db.get_messages(conversation_id)
        messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            # temperatureは0.0から1.0の間で設定できる
            # 0.0にすると、最も確信度の高い回答を返す
            # 1.0にすると、最も多様で創造的な回答を返す
            temperature=1.0,
        )
        reply = response.choices[0].message.content

        # 会話履歴に追加
        self.remember(conversation_id, "user", user_input)
        self.remember(conversation_id, "assistant", reply)

        return reply