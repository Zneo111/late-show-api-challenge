from flask import Blueprint, request, jsonify
from models.guest import Guest
from app import db

guest_bp = Blueprint('guest', __name__)

# ...existing code for guest routes...
