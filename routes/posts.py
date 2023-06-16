from flask import Response
from flask_restful import Resource, reqparse
from controllers.posts import PostController

new_posts_args = reqparse.RequestParser()
new_posts_args.add_argument("token", type=str, required=True, help="login token is required.")
new_posts_args.add_argument("identified_public_id", type=str, help="identified_public_id is required.")
new_posts_args.add_argument("community_public_id", type=str, help="community_public_id is required.")
new_posts_args.add_argument("post_description", type=str, required=True, help="post_description is required.")
new_posts_args.add_argument("post_type", type=str, required=True, help="post_type is required.")

post_controller = PostController()

class Posts(Resource):
    def options(self):
        print("chegouu")
        
    def get(self, public_id: str = None) -> Response:
        return post_controller.get_post(public_id)

    def post(self) -> Response:
        args = new_posts_args.parse_args()
        return post_controller.create_post(args)