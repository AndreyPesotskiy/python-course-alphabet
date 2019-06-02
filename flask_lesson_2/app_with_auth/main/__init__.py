from flask import Blueprint
from flask_restful import Api
from main.routes import Main

main = Blueprint("main", __name__)
api_main = Api(main)

api_main.add_resource(Main, "/main")
