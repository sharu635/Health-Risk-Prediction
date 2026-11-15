from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo

from config import Config

# Import Routes
from routes.auth import auth, init_auth
from routes.assessment import assessment, init_assessment
from routes.prediction import prediction, init_prediction
from routes.recommendation import recommendation, init_recommendation
from routes.history import history, init_history
from routes.wellness import wellness, init_wellness
from routes.dashboard import dashboard, init_dashboard
from routes.profile import profile, init_profile

app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize JWT
JWTManager(app)

# Initialize MongoDB
mongo = PyMongo(app)

# Initialize Routes
init_auth(mongo)
init_assessment(mongo)
init_prediction(mongo)
init_recommendation(mongo)
init_history(mongo)
init_wellness(mongo)
init_dashboard(mongo)
init_profile(mongo)

# Register Blueprints
app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(assessment, url_prefix="/api/assessment")
app.register_blueprint(prediction, url_prefix="/api/prediction")
app.register_blueprint(
    recommendation,
    url_prefix="/api/recommendation"
)
app.register_blueprint(history, url_prefix="/api/history")
app.register_blueprint(wellness, url_prefix="/api/wellness")
app.register_blueprint(dashboard, url_prefix="/api/dashboard")
app.register_blueprint(profile, url_prefix="/api/profile")

@app.route("/")
def home():
    return {
        "message": "AI-Powered Health Risk Prediction API",
        "status": "Running Successfully",
        "database": "MongoDB Connected"
    }


# Print all available routes (for debugging)
print(app.url_map)


if __name__ == "__main__":
    app.run(debug=True)