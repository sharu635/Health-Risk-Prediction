from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import bcrypt

profile = Blueprint("profile", __name__)

mongo = None


def init_profile(database):
    global mongo
    mongo = database


@profile.route("/", methods=["GET"])
@jwt_required()
def get_profile():

    email = get_jwt_identity()

    user = mongo.db.users.find_one(
        {"email": email},
        {"_id": 0, "password": 0}
    )

    if not user:
        return jsonify({"message": "User not found"}), 404

    total_assessments = mongo.db.assessments.count_documents(
        {"user_email": email}
    )
    total_predictions = mongo.db.predictions.count_documents(
        {"user_email": email}
    )

    return jsonify({
        "name": user.get("name"),
        "email": email,
        "total_assessments": total_assessments,
        "total_predictions": total_predictions
    })


@profile.route("/", methods=["PUT"])
@jwt_required()
def update_profile():

    email = get_jwt_identity()
    data = request.get_json()

    update_data = {}

    if "name" in data and data["name"]:
        update_data["name"] = data["name"]

    if "password" in data and data["password"]:
        update_data["password"] = bcrypt.hashpw(
            data["password"].encode("utf-8"),
            bcrypt.gensalt()
        )

    if not update_data:
        return jsonify({"message": "No data to update"}), 400

    mongo.db.users.update_one(
        {"email": email},
        {"$set": update_data}
    )

    result = {"message": "Profile updated successfully"}

    if "name" in update_data:
        result["name"] = update_data["name"]

    return jsonify(result)
