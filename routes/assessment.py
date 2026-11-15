from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.health_service import generate_health_score

assessment = Blueprint("assessment", __name__)

mongo = None


def init_assessment(database):
    global mongo
    mongo = database


@assessment.route("/", methods=["POST"])
@jwt_required()
def create_assessment():

    data = request.get_json()

    required_fields = [
        "age",
        "gender",
        "height",
        "weight",
        "hypertension",
        "heart_disease",
        "smoking_history",
        "HbA1c_level",
        "blood_glucose_level",
        "cholesterol",
        "alcohol",
        "exercise",
        "family_history"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    # Calculate BMI
    height_in_meters = data["height"] / 100
    bmi = round(data["weight"] / (height_in_meters ** 2), 2)

    data["bmi"] = bmi

    # Generate Health Score
    result = generate_health_score({
        "weight": data["weight"],
        "height": data["height"],
        "blood_pressure": 140 if data["hypertension"] else 120,
        "blood_sugar": data["blood_glucose_level"],
        "cholesterol": data["cholesterol"]
    })

    assessment_data = {
        "user_email": get_jwt_identity(),
        **data,
        **result
    }

    mongo.db.assessments.insert_one(assessment_data)

    return jsonify({
        "message": "Health assessment saved successfully",
        "assessment": assessment_data
    }), 201