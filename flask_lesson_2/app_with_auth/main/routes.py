from flask_restful import Resource
from utils import check_login


class Main(Resource):
    method_decorators = [check_login]  # add decorator check_login to all methods from Main

    def get(self):
        return "Hello from main page"
