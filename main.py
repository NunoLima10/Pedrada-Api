from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from routes.user import Users
from routes.login import Login
from routes.community import Communities
from  routes.posts import Posts
from routes.interaction import Interaction


app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)

class Pedrada(Resource):
    def get(self):
        
        return "Pedrada Flask RestFull API"
    
class PedradaRestAPI():
    @staticmethod
    def start() -> None:
        api.add_resource(Pedrada, '/')
        api.add_resource(Login, "/login","/login/valid/<string:token>")
        api.add_resource(Users, "/users")
        #require token
        api.add_resource(Posts,"/posts","/posts/<string:public_id>")
        api.add_resource(Communities,"/communities")
        api.add_resource(Interaction,"/interaction/<string:post_public_id>","/interaction" )

        app.run(debug=True)

if __name__ == "__main__":
    PedradaRestAPI.start()

 