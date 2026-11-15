from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import bcrypt

auth = Blueprint("auth", __name__)

mongo = None

def init_auth(database):
    global mongo
    mongo = database


@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    existing_user = mongo.db.users.find_one({"email": email})

    if existing_user:
        return jsonify({"message": "Email already exists"}), 400

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    mongo.db.users.insert_one({
        "name": name,
        "email": email,
        "password": hashed_password
    })

    return jsonify({"message": "User registered successfully"}), 201


@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = mongo.db.users.find_one({"email": email})

    if not user:
        return jsonify({"message": "Invalid email or password"}), 401

    if not bcrypt.checkpw(
        password.encode("utf-8"),
        user["password"]
    ):
        return jsonify({"message": "Invalid email or password"}), 401

    token = create_access_token(identity=email)

    return jsonify({
        "message": "Login Successful",
        "token": token,
        "name": user["name"]
    })