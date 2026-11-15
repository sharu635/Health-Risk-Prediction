from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.prediction_service import generate_prediction

prediction = Blueprint("prediction", __name__)

mongo = None


def init_prediction(database):
    global mongo
    mongo = database


@prediction.route("/", methods=["GET"])
@jwt_required()
def get_prediction():

    email = get_jwt_identity()

    assessment = mongo.db.assessments.find_one(
        {"user_email": email},
        sort=[("_id", -1)]
    )

    if not assessment:
        return jsonify({
            "message": "No health assessment found."
        }), 404

    # AI Prediction using the trained ML model
    result = generate_prediction(assessment)

    # Save prediction to MongoDB
    mongo.db.predictions.insert_one({
        "user_email": email,
        **result
    })

    return jsonify({
        "message": "Prediction generated successfully",
        "prediction": result
    }), 200