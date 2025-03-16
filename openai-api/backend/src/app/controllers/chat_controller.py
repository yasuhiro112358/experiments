from flask import Blueprint, request, jsonify, Response
import json
from models.persona import Persona
from bson import ObjectId

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/health', methods=['GET'])
def health() -> Response:
    return jsonify({'status': 'OK', 'message': 'Server is running'})

@chat_bp.route('/chat', methods=['POST'])
def chat() -> Response:
    data = request.json
    conversation_id = data.get('conversation_id')
    speaker_id = data.get('speaker_id')
    listener_id = data.get('listener_id')
    message = data.get('message')

    speaker = Persona.load(speaker_id)
    listener = Persona.load(listener_id)

    if not speaker or not listener:
        return jsonify({'error': 'Speaker or listener not found'}), 404

    response = speaker.speak(conversation_id, listener_id, message)

    response_json = json.dumps({'speaker': speaker.name, 'message': response}, ensure_ascii=False, indent=4)

    return Response(response=response_json, content_type="application/json; charset=utf-8")

@chat_bp.route('/run-chat', methods=['GET'])
def run_chat() -> Response:
    alice = Persona.load("67d5bdccc9b5719b96222c8b")
    if alice:
        print(f"Loaded Persona: {alice.name}, {alice.personality}")
    else:
        alice = Persona("Alice", "あなたは関東出身の日本人女性です。")
        alice.save()

    bob = Persona.load("67d5bdccc9b5719b96222c8e")
    if bob:
        print(f"Loaded Persona: {bob.name}, {bob.personality}")
    else:
        bob = Persona("Bob", "あなたは関西弁の日本人男性です。議論が大好きです。")
        bob.save()

    conversation_id = ObjectId()
    # conversation_id = ObjectId("xxxx")

    chat0: str = "音楽について話しましょう！"
    chat1: str = bob.speak(conversation_id, alice.id, chat0)
    chat2: str = alice.speak(conversation_id, bob.id, chat1)

    result = {
        "conversationId": str(conversation_id),
        "messages": [
            {"speaker": alice.name, "message": chat0},
            {"speaker": bob.name, "message": chat1},
            {"speaker": alice.name, "message": chat2},
        ]
    }
    response_json = json.dumps(result, ensure_ascii=False, indent=4)
    return Response(response=response_json, content_type="application/json; charset=utf-8")