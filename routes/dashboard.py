from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

dashboard = Blueprint("dashboard", __name__)

mongo = None


def init_dashboard(database):
    global mongo
    mongo = database


@dashboard.route("/", methods=["GET"])
@jwt_required()
def get_dashboard():

    email = get_jwt_identity()

    # Get user info
    user = mongo.db.users.find_one(
        {"email": email},
        {"_id": 0, "password": 0}
    )

    # Get latest assessment
    latest_assessment = mongo.db.assessments.find_one(
        {"user_email": email},
        {"_id": 0},
        sort=[("_id", -1)]
    )

    # Get latest prediction
    latest_prediction = mongo.db.predictions.find_one(
        {"user_email": email},
        {"_id": 0},
        sort=[("_id", -1)]
    )

    # Get counts
    total_assessments = mongo.db.assessments.count_documents(
        {"user_email": email}
    )
    total_predictions = mongo.db.predictions.count_documents(
        {"user_email": email}
    )

    # Build response
    dashboard_data = {
        "user": {
            "name": user.get("name", "User") if user else "User",
            "email": email
        },
        "latest_assessment": None,
        "latest_prediction": None,
        "total_assessments": total_assessments,
        "total_predictions": total_predictions
    }

    if latest_assessment:
        dashboard_data["latest_assessment"] = {
            "bmi": latest_assessment.get("bmi"),
            "bmi_category": latest_assessment.get("bmi_category"),
            "health_score": latest_assessment.get("health_score"),
            "age": latest_assessment.get("age"),
            "blood_glucose_level": latest_assessment.get("blood_glucose_level"),
            "HbA1c_level": latest_assessment.get("HbA1c_level")
        }

    if latest_prediction:
        dashboard_data["latest_prediction"] = {
            "diabetes_prediction": latest_prediction.get("diabetes_prediction"),
            "diabetes_probability": latest_prediction.get("diabetes_probability"),
            "overall_risk": latest_prediction.get("overall_risk")
        }

    return jsonify(dashboard_data)
