from flask import Response,request
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
        name = request.args.get("name")
        public_id = request.args.get("public_id")

        if name:
            return community_controller.get_community(filter=name, filter_type="community_name")
        
        if public_id:
            return community_controller.get_community(filter=public_id, filter_type="public_id")
        
        return community_controller.get_community(filter=None, filter_type=None)

    def post(self) -> Response:
        args = new_community_args.parse_args()
        return community_controller.create_community(args)

     
