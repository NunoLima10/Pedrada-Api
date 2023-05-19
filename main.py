from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from routes.user import Users
from routes.user import User
from routes.login import Login

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
        api.add_resource(Users, "/users")
        api.add_resource(User, "/user/<string:public_id>")
        api.add_resource(Login, "/login","/login/valid/<string:token>")
        app.run(debug=True)

if __name__ == "__main__":
    PedradaRestAPI.start()

 