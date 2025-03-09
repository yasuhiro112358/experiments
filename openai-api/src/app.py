from src.openai_client import OpenAIClient
from src.memory_db import MemoryDB
from src.persona import Persona

def run_chat() -> None:
    openai_client = OpenAIClient()
    memory_db = MemoryDB()

    user1 = Persona("Alice", "あなたは関東出身の日本人男性です。", openai_client, memory_db)
    user2 = Persona("Bob", "あなたは関西弁の日本人男性です。", openai_client, memory_db)

    # Testing on console
    conversation_id = "test_conversation_1"
    user_input = input("あなた: ")
    response = user1.chat(conversation_id, user_input)
    print(user1.name, ":\n", response)
    print("\n")

    conversation_id = "test_conversation_2"
    user_input = input("あなた: ")
    response = user2.chat(conversation_id, user_input)
    print(user2.name, ":\n", response)
    print("\n")