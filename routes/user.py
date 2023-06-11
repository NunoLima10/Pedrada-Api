from flask import Response
from flask_restful import Resource, reqparse

from controllers.user import UserController


add_new_args = reqparse.RequestParser()
add_new_args.add_argument("pseudonym", type=str, required=True, help="Pseudonym name is required.")
add_new_args.add_argument("email", type=str, required=True, help="Email is required.")
add_new_args.add_argument("user_password", type=str, required=True, help="Password name is required.")

user_controller = UserController()

class Users(Resource):

    def get(self) -> Response:
        return user_controller.get_user_by_id()

    def post(self) -> Response:
        args = add_new_args.parse_args()
        return user_controller.create_user(args)

class UserByID(Resource):

    def get(self, public_id: str)-> Response:
        return user_controller.get_user_by_id(public_id)

   
class UserByPseudonym(Resource):

    def get(self, pseudonym: str)-> Response:
        return user_controller.get_user_by_pseudonym(pseudonym)

   