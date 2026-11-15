from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.prediction_service import generate_prediction
from services.recommendation_service import generate_recommendations

recommendation = Blueprint("recommendation", __name__)

mongo = None


def init_recommendation(database):
    global mongo
    mongo = database


@recommendation.route("/", methods=["GET"])
@jwt_required()
def get_recommendation():

    email = get_jwt_identity()

    assessment = mongo.db.assessments.find_one(
        {"user_email": email},
        sort=[("_id", -1)]
    )

    if not assessment:
        return jsonify({
            "message": "No assessment found."
        }), 404

    prediction = generate_prediction(assessment)

    recommendations = generate_recommendations(
        assessment,
        prediction
    )

    return jsonify({
        "message": "Recommendations generated successfully",
        "prediction": prediction,
        "recommendations": recommendations
    })