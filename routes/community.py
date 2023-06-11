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
        return community_controller.get_community_by_name()
        
    def post(self) -> Response:
        args = new_community_args.parse_args()
        return community_controller.create_community(args)

class CommunityByID(Resource): 
    def get(self, public_id: str = None) -> Response:
        return community_controller.get_community_by_id(public_id)
class CommunityByName(Resource): 
    def get(self, name: str = None) -> Response:
        return community_controller.get_community_by_name(name)
        
     
