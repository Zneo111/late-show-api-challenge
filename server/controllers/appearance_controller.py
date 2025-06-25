from flask import Blueprint, request, jsonify
from ..models.appearance import Appearance
from ..models.guest import Guest
from ..models.episode import Episode
from ..app import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    rating = data.get('rating')
    if not all([guest_id, episode_id, rating]):
        return jsonify({"error": "guest_id, episode_id, and rating required"}), 400
    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)
    if not guest or not episode:
        return jsonify({"error": "Guest or Episode not found"}), 404
    try:
        appearance = Appearance(guest_id=guest_id, episode_id=episode_id, rating=rating)
        db.session.add(appearance)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    return jsonify({
        "id": appearance.id,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id,
        "rating": appearance.rating
    }), 201
