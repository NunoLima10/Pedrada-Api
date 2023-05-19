from flask import Response
from flask_restful import Resource, reqparse
from controllers.login import LoginController

login_args = reqparse.RequestParser()
login_args.add_argument("pseudonym", type=str, required=True, help="Pseudonym name is required.")
login_args.add_argument("user_password", type=str, required=True, help="Password name is required.")

login_controller = LoginController()

class Login(Resource):
    def __init__(self) -> None:
        super().__init__()
    
    def get(self, token) -> None:
        return login_controller.validade_token(token)

    
    def post(self) -> Response:
        args = login_args.parse_args()
        return login_controller.validade_login(args)
    
