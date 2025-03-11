from src.openai_client import OpenAIClient
from src.memory_db import MemoryDB
from src.persona import Persona
from src.conversation_manager import ConversationManager

def run_chat() -> None:
    openai_client = OpenAIClient()
    memory_db = MemoryDB()

    Alice = Persona("Alice", "あなたは関東出身の日本人女性です。", openai_client, memory_db)
    Bob = Persona("Bob", "あなたは関西弁の日本人男性です。議論が大好きです。", openai_client, memory_db)

    conversation_id: str = "test_conversation_1"

    chat0: str = "そういえば、さっき教えてくれたレストランなんだっけ？"
    print(f"{Alice.name}: {chat0}")
    chat1: str = Bob.speak(conversation_id, "Alice", chat0)
    print(f"{Bob.name}: {chat1}")
    chat2: str = Alice.speak(conversation_id, "Bob", chat1)
    print(f"{Alice.name}: {chat2}")
    chat3: str = Bob.speak(conversation_id, "Alice", chat2)
    print(f"{Bob.name}: {chat3}")
    chat4: str = Alice.speak(conversation_id, "Bob", chat3)
    print(f"{Alice.name}: {chat4}")
    chat5: str = Bob.speak(conversation_id, "Alice", chat4)
    print(f"{Bob.name}: {chat5}")