from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

wellness = Blueprint("wellness", __name__)

mongo = None


def init_wellness(database):
    global mongo
    mongo = database


@wellness.route("/", methods=["GET"])
@jwt_required()
def get_wellness():

    email = get_jwt_identity()

    assessment = mongo.db.assessments.find_one(
        {"user_email": email},
        sort=[("_id", -1)]
    )

    if not assessment:
        return jsonify({
            "message": "No health assessment found."
        }), 404

    recommendations = []

    bmi = assessment.get("bmi", 0)

    if bmi < 18.5:
        recommendations.append("Increase calorie intake with healthy foods.")
    elif bmi > 25:
        recommendations.append("Follow a balanced diet and exercise regularly.")
    else:
        recommendations.append("Maintain your current healthy lifestyle.")

    glucose = assessment.get("blood_glucose_level", 0)

    if glucose > 140:
        recommendations.append("Reduce sugar intake.")
    else:
        recommendations.append("Maintain normal sugar consumption.")

    recommendations.append("Drink 2–3 liters of water daily.")
    recommendations.append("Exercise for at least 30 minutes every day.")
    recommendations.append("Sleep 7–8 hours every night.")
    recommendations.append("Avoid smoking and excessive alcohol consumption.")

    return jsonify({
        "message": "Wellness recommendations generated successfully.",
        "recommendations": recommendations
    })