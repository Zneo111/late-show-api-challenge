from flask import Blueprint, request, jsonify
from models.appearance import Appearance
from app import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    new_appearance = Appearance(
        episode_id=data['episode_id'],
        guest_id=data['guest_id'],
        notes=data.get('notes', '')
    )
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify({"message": "Appearance created", "appearance": new_appearance.serialize()}), 201

@appearance_bp.route('/appearances/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_appearance(id):
    appearance = Appearance.query.get_or_404(id)
    db.session.delete(appearance)
    db.session.commit()
    return jsonify({"message": "Appearance deleted"}), 200

@appearance_bp.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify({"appearances": [appearance.serialize() for appearance in appearances]}), 200

@appearance_bp.route('/appearances/<int:id>', methods=['GET'])
def get_appearance(id):
    appearance = Appearance.query.get_or_404(id)
    return jsonify({"appearance": appearance.serialize()}), 200