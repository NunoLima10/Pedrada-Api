from flask import Response
from flask_restful import Resource, reqparse


class Communities(Resource):
    def get(self) -> Response:
        pass
        
    def post(self) -> Response:
        # args = add_new_args.parse_args()
        # return user_controller.create_user(args)
        pass

class Community(Resource): 
    def get(self, public_id: str)-> Response:
        pass

    def put(self, public_id: str)-> Response:
        pass

    def delete(self, public_id: str)-> Response:
        pass

