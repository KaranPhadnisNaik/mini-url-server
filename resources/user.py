import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    """
    UserRegister: Resource that enables for user registration
    UserRegister.post() a username and password stored in users table

    Required Arguments:
    + username (str)
    + password (str)
    """

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field can not be left blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field can not be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A User with that name already exists!"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        
        return {"message": "User created successfully."}, 201
