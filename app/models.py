# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from app import db

class Functionality(db.Model):
    __tablename__ = 'functionalities'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Integer)
    view_id = db.Column(db.ForeignKey('views.id'), nullable=False)

    view = db.relationship('View', primaryjoin='Functionality.view_id == View.id', backref='functionalities')



class Rol(db.Model):
    __tablename__ = 'rols'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(100), unique=True)



class RolsFunctionality(db.Model):
    __tablename__ = 'rols_functionalities'
    __table_args__ = (
        db.UniqueConstraint('rol_id', 'functionality_id'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    rol_id = db.Column(db.ForeignKey('rols.id'), nullable=False)
    functionality_id = db.Column(db.ForeignKey('functionalities.id'), nullable=False)

    functionality = db.relationship('Functionality', primaryjoin='RolsFunctionality.functionality_id == Functionality.id', backref='rols_functionalities')
    rol = db.relationship('Rol', primaryjoin='RolsFunctionality.rol_id == Rol.id', backref='rols_functionalities')



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    username = db.Column(db.String(40))
    password = db.Column(db.String(100))
    name = db.Column(db.String(45))



class UsersRol(db.Model):
    __tablename__ = 'users_rol'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    rols_id = db.Column(db.ForeignKey('rols.id'), nullable=False)

    rols = db.relationship('Rol', primaryjoin='UsersRol.rols_id == Rol.id', backref='users_rols')
    user = db.relationship('User', primaryjoin='UsersRol.user_id == User.id', backref='users_rols')



class View(db.Model):
    __tablename__ = 'views'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    view_id = db.Column(db.ForeignKey('views.id'))
    name = db.Column(db.String(100))

    view = db.relationship('View', remote_side=[id], primaryjoin='View.view_id == View.id', backref='views')
