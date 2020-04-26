from app import app
from models import User, Rol, UsersRol,db, RolsFunctionality, Functionality
from flask import jsonify, request
from utils import to_dict, exists
@app.route("/")
def index():
    return 'Hola mundo desde aqui'

@app.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    user = User.query.filter_by(**body)
    if exists(user):
        data = {**to_dict(user.first(), ['password'])}
        return jsonify({"status": True, "data": data})
    return jsonify({"status": False})

@app.route("/rols/<user_id>", methods=["GET"])
def rols(user_id):
    query = db.session.query(User, Rol, UsersRol).filter(
        User.id == UsersRol.user_id).filter(
        Rol.id == UsersRol.rols_id).filter(User.id == user_id)
    data = []
    for user, rol, userol in query.all():
        data.append({**to_dict(rol)})
    return jsonify({"status": True, "data": data})

@app.route("/permissions/<user_id>", methods=["GET"])
def permissions(user_id):
    query = db.session.query(User, Rol, UsersRol, RolsFunctionality, Functionality).filter(
        User.id == UsersRol.user_id).filter(Rol.id == UsersRol.rols_id).filter(
        User.id == user_id).filter(Functionality.id == RolsFunctionality.functionality_id).filter(
        RolsFunctionality.rol_id == UsersRol.rols_id)
    data = []
    for user, rl, userrol, rolfunc, func in query.all():
        data.append({**to_dict(func, ['view_id'])})
    return jsonify({"status": True, "data": data})
        
    