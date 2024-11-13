from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model): #defines layout for objects
    id = db.Column(db.Integer, primary_key=True) #unique identifier that represents object
    data = db.Column(db.String(10000)) #the note itself
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #date and time of note 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #references an ID to a column of a different database

class User(db.Model, UserMixin): #defines layout for objects
    id = db.Column(db.Integer, primary_key=True) #unique identifier that represents object
    email = db.Column(db.String(150), unique=True) #says no user can have the same email as another user
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    role = db.Column(db.String(150))
    notes = db.relationship('Note') 