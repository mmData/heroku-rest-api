import sqlite3
from db import db

class UserModel(db.Model):
    # This is an API, in that this is how the database communicate with the user
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True) #is is autoincrementing because it's a primary key
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        #self.id = _id
        self.username = username
        self.password = password
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() #username is the table name by which we are filtering
        

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        