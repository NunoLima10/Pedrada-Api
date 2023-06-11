from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from routes.user import Users
from routes.user import UserByID
from routes.user import UserByPseudonym
from routes.login import Login
from routes.community import CommunityByID
from routes.community import CommunityByName
from routes.community import Communities
from  routes.posts import Posts

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
        api.add_resource(UserByID, "/user/id/<string:public_id>")
        api.add_resource(UserByPseudonym, "/user/pseudonym/<string:pseudonym>")
        #require token
        api.add_resource(Communities,"/communities")
        api.add_resource(Posts,"/posts","/post/<string:public_id>")
        # to do
        api.add_resource(CommunityByID,"/community/id/<string:public_id>")
        api.add_resource(CommunityByName,"/community/name/<string:name>")



        app.run(debug=True)

if __name__ == "__main__":
    PedradaRestAPI.start()

 