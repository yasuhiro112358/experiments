from typing import List, Dict
from src.openai_client import OpenAIClient
from src.memory_db import MemoryDB

class Persona:
    def __init__(self, name: str, personality: str, openai_client: OpenAIClient, memory_db: MemoryDB):
        self.name = name
        self.personality = personality
        self.memory_db = memory_db
        self.client = openai_client.get_client()

    def remember(self, conversation_id: str, listener_id: str, content: str) -> None:
        """会話履歴を記録する"""
        speaker_id: str = self.name
        self.memory_db.insert(conversation_id, speaker_id, listener_id, content)

    def speak(self, conversation_id: str, listener_id: str, new_message: str) -> str:
        """
        listener_id: 話しかける相手のID
        new_message: listenerから話しかけられた内容
        """
        # あとでIDに変更
        speaker_id: str = self.name

        # System messageを追加
        messages = [{"role": "system", "content": self.personality}]
        # 会話履歴を追加
        prev_messages: List[Dict[str, str]] = self.memory_db.get_messages(conversation_id)
        for prev_message in prev_messages:
            if prev_message["speaker_id"] == speaker_id and prev_message["listener_id"] == listener_id:
                messages.append({"role": "assistant", "content": prev_message["content"]})
            elif prev_message["speaker_id"] == listener_id and prev_message["listener_id"] == speaker_id:
                messages.append({"role": "user", "content": prev_message["content"]})
        # 新しいメッセージを追加
        messages.append({"role": "user", "content": new_message})

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
        self.remember(conversation_id, listener_id, reply)

        return reply