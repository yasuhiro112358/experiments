from src.openai_client import OpenAIClient
from src.memory_db import MemoryDB
from src.persona import Persona
from src.conversation_manager import ConversationManager

def run_chat() -> None:
    openai_client = OpenAIClient()
    memory_db = MemoryDB()

    # alice = Persona("Alice", "あなたは関東出身の日本人女性です。", openai_client, memory_db)
    # alice.save()

    alice = Persona.load("9d7c6cb2-331d-42c5-a3df-93c899f8bdfd", openai_client, memory_db)
    if alice:
        print(f"Loaded Persona: {alice.name}, {alice.personality}")

    # bob = Persona("Bob", "あなたは関西弁の日本人男性です。議論が大好きです。", openai_client, memory_db)
    # bob.save()

    bob = Persona.load("bbbdd292-accf-4ebb-b38d-8dc991d32065", openai_client, memory_db)
    if bob:
        print(f"Loaded Persona: {bob.name}, {bob.personality}")


    conversation_id: str = "test_conversation_1"

    chat0: str = "音楽について話しましょう！"
    print(f"{alice.name}: {chat0}")
    chat1: str = bob.speak(conversation_id, alice.id, chat0)
    print(f"{bob.name}: {chat1}")
    chat2: str = alice.speak(conversation_id, bob.id, chat1)
    print(f"{alice.name}: {chat2}")
    chat3: str = bob.speak(conversation_id, alice.id, chat2)
    print(f"{bob.name}: {chat3}")
    chat4: str = alice.speak(conversation_id, bob.id, chat3)
    print(f"{alice.name}: {chat4}")
    chat5: str = bob.speak(conversation_id, alice.id, chat4)
    print(f"{bob.name}: {chat5}")