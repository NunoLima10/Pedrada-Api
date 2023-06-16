from flask import Response,request
from flask_restful import Resource, reqparse

from controllers.user import UserController


add_new_args = reqparse.RequestParser()
add_new_args.add_argument("pseudonym", type=str, required=True, help="Pseudonym name is required.")
add_new_args.add_argument("email", type=str, required=True, help="Email is required.")
add_new_args.add_argument("user_password", type=str, required=True, help="Password name is required.")

user_controller = UserController()

class Users(Resource):

    def options(self):
        print("chegouu")

    def get(self) -> Response:
        pseudonym = request.args.get("pseudonym")
        public_id = request.args.get("public_id")

        if pseudonym:
            return user_controller.get_user(filter=pseudonym,filter_type="pseudonym")
        
        if public_id:
            return user_controller.get_user(filter=public_id,filter_type="public_id")
        
        return user_controller.get_user(filter=None,filter_type=None)

    def post(self) -> Response:
        args = add_new_args.parse_args()
        return user_controller.create_user(args)



   