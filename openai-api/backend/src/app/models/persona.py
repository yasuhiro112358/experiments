from typing import Optional, Dict, List
from bson.objectid import ObjectId
from services.openai_service import OpenAIService
from services.database_service import DatabaseService
from models.message import Message

class Persona:
    def __init__(self, name: str, personality: str, persona_id: Optional[ObjectId] = None) -> None:
        self.id = persona_id if persona_id else ObjectId()
        self.name = name
        self.personality = personality
        self.openai_client = OpenAIService().get_client()
        self.db = DatabaseService.get_app_database()

    def save(self) -> None:
        self.db.personas.insert_one({
            "_id": self.id,
            "name": self.name,
            "personality": self.personality
        })

    @classmethod
    def load(cls, persona_id: ObjectId) -> Optional["Persona"]:
        db = DatabaseService.get_app_database()
        data = db.personas.find_one({"_id": persona_id})
        if data:
            return cls(data["name"], data["personality"], persona_id)
        else:
            return None

    def generate_message(self, conversation_id: ObjectId, listener_id: ObjectId, received_message: str) -> str:
        # prev_messages = list(self.db.messages.find({"conversationId": conversation_id}))
        prev_messages = Message.find_by_conversation(conversation_id)

        messages: List[Dict[str, str]] = []
        # システムメッセージを追加
        messages.append({"role": "system", "content": self.personality})
        # 会話履歴を追加
        for prev_message in prev_messages:
            if prev_message["speakerId"] == self.id and prev_message["listenerId"] == listener_id:
                messages.append({"role": "assistant", "content": prev_message["message"]})
            elif prev_message["speakerId"] == listener_id and prev_message["listenerId"] == self.id:
                messages.append({"role": "user", "content": prev_message["message"]})
        # 受け取ったメッセージを追加
        messages.append({"role": "user", "content": received_message})

        # OpenAI APIを呼び出して返信メッセージを生成
        response = self.openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=1.0,
        )
        replying_message = response.choices[0].message.content

        return replying_message

    def remember_message(self, conversation_id: ObjectId, listener_id: ObjectId, message: str) -> None:
        # self.db.messages.insert_one({
        #     "conversationId": conversation_id,
        #     "speakerId": self.id,
        #     "listenerId": listener_id,
        #     "message": message
        # })
        new_message = Message(conversation_id, self.id, listener_id, message)
        new_message.save()

        return None

    def speak(self, conversation_id: ObjectId, listener_id: ObjectId, received_msg: str) -> str:
        replying_msg = self.generate_message(conversation_id, listener_id, received_msg)
        self.remember_message(conversation_id, listener_id, replying_msg)
        return replying_msg