from flask import Response
from flask_restful import Resource, reqparse
from controllers.interaction import InteractionController

new_interaction_args = reqparse.RequestParser()
new_interaction_args.add_argument("token", type=str, required=True, help="login token is required.")
new_interaction_args.add_argument("post_id", type=str, required=True, help="post_id is required.")
new_interaction_args.add_argument("interaction", type=str, required=True, help="interaction is required.")

interaction_controller = InteractionController()

class Interaction(Resource):
    def get(self, post_public_id) -> Response:
        print(post_public_id)
        return interaction_controller.get_interaction(post_public_id)
        
    def post(self) -> Response:
        args = new_interaction_args.parse_args()
        return interaction_controller.create_post_interaction(args)
