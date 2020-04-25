from app import app
from models import User
from flask import jsonify, request

@app.route("/")
def index():
    return 'Hola mundo desde aqui'

@app.route("/login", methods=["GET"])
def login():
    users = User.query.all()
    data = []
    for user in users:
        data.append({"users": user.username})
    return jsonify({"status": True, "data": data})