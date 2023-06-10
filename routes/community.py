from flask import Response
from flask_restful import Resource, reqparse
from controllers.community import CommunityController

new_community_args = reqparse.RequestParser()
new_community_args.add_argument("token", type=str, required=True, help="login token is required.")
new_community_args.add_argument("community_name", type=str, required=True, help="community_name is required.")
# new_community_args.add_argument("founder_id", type=str, required=True, help="founder_id is required.")
new_community_args.add_argument("community_description", type=str, required=True, help="community_description is required.")

community_controller = CommunityController()

class Communities(Resource):
    def get(self) -> Response:
        return community_controller.get_community()
        
    def post(self) -> Response:
        args = new_community_args.parse_args()
        return community_controller.create_community(args)

class Community(Resource): 
    def get(self, name: str)-> Response:
        return community_controller.get_community(name)

    def put(self, public_id: str)-> Response:
        pass

    def delete(self, public_id: str)-> Response:
        pass

