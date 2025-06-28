from flask import Blueprint, request, jsonify
from models.episode import Episode
from app import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode', __name__)

# ...existing code for episode routes...
