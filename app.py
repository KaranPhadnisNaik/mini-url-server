import os

from flask import Flask
from flask_restful import Api, reqparse
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.link import Links, InterpretHash, LinksList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'karan'
api = Api(app)
'''
@app.before_first_request
def create_tables():
    db.create_all()
'''

jwt = JWT(app, authenticate,identity) # creates a new endpoint /auth,
                                      # sends username and password to authnetiate function

api.add_resource(InterpretHash, '/<string:hash>') # localhost:9000/h4xD
api.add_resource(Links, '/link') # localhost:9000/link
api.add_resource(LinksList, '/all') # localhost:9000/all
api.add_resource(StoreList, '/stores') # localhost:9000/stores

api.add_resource(UserRegister, '/register') # localhost:9000/register

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=9000, debug=True)
