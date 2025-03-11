from src.persona import Persona

class ConversationManager:
    def __init__(self, conversation_id: str) -> None:
        self.conversation_id = conversation_id
        self.personas = {}  # Personaの辞書を作成

    def add_persona(self, persona: Persona):
        """AIキャラクターを登録"""
        # ID管理にしたい
        self.personas[persona.name] = persona

    def talk(self, speaker_name: str, listener_name: str, message: str) -> str:
        """AI同士の会話を管理"""
        if speaker_name not in self.personas or listener_name not in self.personas:
            return "会話できるAIが見つかりません"

        listener: Persona = self.personas[listener_name]

        print(f"{speaker_name}: {message}")

        response: str = listener.chat(self.conversation_id, message)
        print(f"{listener_name}: {response}")

        return response
