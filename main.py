from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from database.db_connector import SQLite_Connector

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
        app.run(debug=True)

if __name__ == "__main__":
    PedradaRestAPI.start()