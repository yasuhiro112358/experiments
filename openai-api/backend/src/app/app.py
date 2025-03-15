from flask import Flask, request, jsonify, Response
from openai_client import OpenAIClient
from memory_db import MemoryDB
from persona import Persona
from conversation_manager import ConversationManager
import logging
import json

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_AS_ASCII'] = False

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

openai_client = OpenAIClient()
memory_db = MemoryDB()

@app.route('/health', methods=['GET'])
def health() -> Response:
    return jsonify({'status': 'OK', 'message': 'Server is running'})

@app.route('/chat', methods=['POST'])
def chat() -> Response:
    data = request.json
    conversation_id = data.get('conversation_id')
    speaker_id = data.get('speaker_id')
    listener_id = data.get('listener_id')
    message = data.get('message')

    speaker = Persona.load(speaker_id, openai_client, memory_db)
    listener = Persona.load(listener_id, openai_client, memory_db)

    if not speaker or not listener:
        return jsonify({'error': 'Speaker or listener not found'}), 404

    response = speaker.speak(conversation_id, listener_id, message)

    response_json = json.dumps({'speaker': speaker.name, 'message': response}, ensure_ascii=False, indent=4)

    return Response(response=response_json, content_type="application/json; charset=utf-8")

@app.route('/run-chat', methods=['GET'])
def run_chat() -> Response:
    alice = Persona.load("9d7c6cb2-331d-42c5-a3df-93c899f8bdfd", openai_client, memory_db)
    if alice:
        print(f"Loaded Persona: {alice.name}, {alice.personality}")
    else:
        alice = Persona("Alice", "あなたは関東出身の日本人女性です。", openai_client, memory_db)
        alice.save()

    bob = Persona.load("bbbdd292-accf-4ebb-b38d-8dc991d32065", openai_client, memory_db)
    if bob:
        print(f"Loaded Persona: {bob.name}, {bob.personality}")
    else:
        bob = Persona("Bob", "あなたは関西弁の日本人男性です。議論が大好きです。", openai_client, memory_db)
        bob.save()

    conversation_id: str = "test_conversation_1"

    chat0: str = "音楽について話しましょう！"
    # print(f"{alice.name}: {chat0}")
    chat1: str = bob.speak(conversation_id, alice.id, chat0)
    # print(f"{bob.name}: {chat1}")
    chat2: str = alice.speak(conversation_id, bob.id, chat1)
    # print(f"{alice.name}: {chat2}")

    result = {
        "conversation_id": conversation_id,
        "messages": [
            {"speaker": alice.name, "message": chat0},
            {"speaker": bob.name, "message": chat1},
            {"speaker": alice.name, "message": chat2},
        ]
    }
    response_json = json.dumps(result, ensure_ascii=False, indent=4)
    return Response(response=response_json, content_type="application/json; charset=utf-8")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
