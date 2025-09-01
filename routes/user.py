from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from database import db
from models import User

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@user_bp.route("/me", methods=["PUT", "PATCH"])
@jwt_required()
def update_me():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    data = request.get_json(silent=True) or {}
    updated = False

    if "name" in data and isinstance(data["name"], str) and data["name"].strip():
        user.name = data["name"].strip()
        updated = True

    if "password" in data and isinstance(data["password"], str) and len(data["password"]) >= 6:
        # optional: hash here if using werkzeug; handled in auth normally
        from werkzeug.security import generate_password_hash
        user.password_hash = generate_password_hash(data["password"])
        updated = True

    if not updated:
        return jsonify({"error": "nothing to update or invalid inputs"}), 400

    db.session.commit()
    return jsonify({"message": "updated", "user": user.to_dict()}), 200

@user_bp.route("/me", methods=["DELETE"])
@jwt_required()
def delete_me():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "account deleted"}), 200
