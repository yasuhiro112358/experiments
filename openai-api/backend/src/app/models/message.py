from typing import Optional, List, Dict
from bson.objectid import ObjectId
from services.database_service import DatabaseService

class Message:
    def __init__(self, conversation_id: ObjectId, speaker_id: ObjectId, listener_id: ObjectId, message: str, message_id: Optional[ObjectId] = None) -> None:
        self.id = message_id if message_id else ObjectId()
        self.conversation_id = conversation_id
        self.speaker_id = speaker_id
        self.listener_id = listener_id
        self.message = message
        self.db = DatabaseService.get_app_database()

    def save(self) -> None:
        self.db.messages.insert_one({
            "_id": self.id,
            "conversationId": self.conversation_id,
            "speakerId": self.speaker_id,
            "listenerId": self.listener_id,
            "message": self.message
        })

    @classmethod
    def load(cls, message_id: ObjectId) -> Optional["Message"]:
        db = DatabaseService.get_app_database()
        data = db.messages.find_one({"_id": message_id})
        if data:
            return cls(data["conversationId"], data["speakerId"], data["listenerId"], data["message"], message_id)
        else:
            return None

    @classmethod
    def find_by_conversation(cls, conversation_id: ObjectId) -> List[Dict[str, str]]:
        db = DatabaseService.get_app_database()
        return list(db.messages.find({"conversationId": conversation_id}))