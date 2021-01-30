from flask_sqlalchemy import SQLAlchemy
from main import app
import os.path

db = SQLAlchemy(app)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score_value = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Score (score = {score}, user_id ={user_id})"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    clientGuid = db.Column(db.String(30), nullable = False)
    userGuid = db.Column(db.String(28), nullable = False)
    score_list = db.relationship('Score',backref='user',lazy=True)

    def __repr__(self):
        return f"Score (user id = {id},username={name})"


if os.path.isfile('database.db'):
    print("Database exist")
else: 
    db.create_all()
    print("Create new Database")