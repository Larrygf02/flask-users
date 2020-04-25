from app import app
from models import User
from flask import jsonify, request
from utils import to_dict, exists
@app.route("/")
def index():
    return 'Hola mundo desde aqui'

@app.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    print(body)
    user = User.query.filter_by(**body)
    if exists(user):
        return jsonify({"status": True})
    #data = []
    """ for user in users:
        data.append({**to_dict(user, ['password'])}) """
    return jsonify({"status": False})