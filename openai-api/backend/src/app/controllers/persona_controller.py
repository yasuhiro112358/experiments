from flask import Blueprint, request, jsonify, Response
import json
from bson import ObjectId
from models.persona import Persona

persona_bp = Blueprint('persona', __name__)

@persona_bp.route('/personas', methods=['POST'])
def create_persona() -> Response:
    data = request.json

    # validate request
    if not data.get('name') or not data.get('personality'):
        return jsonify({'error': 'Name and personality are required'}), 400

    name = data.get('name')
    personality = data.get('personality')

    persona = Persona(name, personality)
    persona.save()

    response_json = json.dumps({'id': str(persona.id), 'name': persona.name, 'personality': persona.personality}, ensure_ascii=False, indent=4)

    return Response(response=response_json, status=201, content_type="application/json; charset=utf-8")

@persona_bp.route('/personas', methods=['GET'])
def get_all_personas() -> Response:
    personas = Persona.load_all()

    response_json = json.dumps([{'id': str(persona.id), 'name': persona.name, 'personality': persona.personality} for persona in personas], ensure_ascii=False, indent=4)

    return Response(response=response_json, status=200, content_type="application/json; charset=utf-8")

@persona_bp.route('/personas/<persona_id>', methods=['GET'])
def get_persona(persona_id: str) -> Response:
    persona = Persona.load(ObjectId(persona_id))

    if not persona:
        return jsonify({'error': 'Persona not found'}), 404
    
    response_json = json.dumps({'id': str(persona.id), 'name': persona.name, 'personality': persona.personality}, ensure_ascii=False, indent=4)

    return Response(response=response_json, status=200, content_type="application/json; charset=utf-8")

@persona_bp.route('/personas/<persona_id>', methods=['PUT'])
def update_persona(persona_id: str) -> Response:
    persona = Persona.load(ObjectId(persona_id))
    if not persona:
        return jsonify({'error': 'Persona not found'}), 404
    
    data = request.json
    persona.name = data.get('name', persona.name)
    persona.personality = data.get('personality', persona.personality)
    persona.save()

    response_json = json.dumps({'id': str(persona.id), 'name': persona.name, 'personality': persona.personality}, ensure_ascii=False, indent=4)

    return Response(response=response_json, status=200, content_type="application/json; charset=utf-8")

@persona_bp.route('/personas/<persona_id>', methods=['DELETE'])
def delete_persona(persona_id: str) -> Response:
    persona = Persona.load(ObjectId(persona_id))
    if not persona:
        return jsonify({'error': 'Persona not found'}), 404
    
    persona.delete()

    return jsonify({'message': 'Persona deleted'}), 200
    