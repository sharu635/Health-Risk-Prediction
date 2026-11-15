from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

history = Blueprint("history", __name__)

mongo = None


def init_history(database):
    global mongo
    mongo = database


@history.route("/", methods=["GET"])
@jwt_required()
def get_history():

    email = get_jwt_identity()

    assessments = list(
        mongo.db.assessments.find(
            {"user_email": email},
            {"_id": 0}
        )
    )

    predictions = list(
        mongo.db.predictions.find(
            {"user_email": email},
            {"_id": 0}
        )
    )

    return jsonify({
        "total_assessments": len(assessments),
        "total_predictions": len(predictions),
        "assessments": assessments,
        "predictions": predictions
    })