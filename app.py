import os
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList



app = Flask(__name__)
# The Postgres database link was added as an environment varianle in Heroku. sqlite is in the second position of the get and would be the deafault value
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #take off resource to track modifications
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity) # jwt creates endpoint /.auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# We only want to run the flask app if we run the file from terminal, not if we import the file
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug = True)