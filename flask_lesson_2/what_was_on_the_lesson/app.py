from functools import wraps

from flask import Flask, request
from errors import errors
from config import run_config
from flask_restful import Api, Resource, reqparse, fields, marshal_with

app = Flask(__name__)
api = Api(app, errors=errors)
app.config.from_object(run_config())


class HelloRest(Resource):
    def get(self):
        return {"key": "value"}, 200, {"custom_header": "value"}

    def post(self):
        return "post"


a = ["Apple", "Amazon", "Alphabet", "Microsoft"]

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('page', type=int, help="wrong page expecting int")
parser.add_argument('filter', type=int, help="wrong filter type")
parser_2 = parser.copy()
parser_2.add_argument('new_value')


def cache(f):
    @wraps(f)
    def cacher(*args, **kwargs):
        print("Hello")
        return f(*args, **kwargs)

    return cacher


class Companies(Resource):
    method_decorators = [cache]

    def get(self):
        parser.parse_args()

        print()
        response = dict()
        for i, elem in enumerate(a):
            response[i + 1] = elem
        return response

    def post(self, value):
        a.append(value)
        return "Successful"

    def put(self):
        import json
        data = json.loads(request.data)
        company = data.get("company")
        position = data.get("position") - 1

        a.remove(company)
        a.insert(position, company)
        return "Successful"

    def delete(self, value):
        a.remove(value)
        return "Successful"


a = ["Carp", "Dorado", " Steelhead"]


class Upper(fields.Raw):
    def format(self, value):
        return value.upper()


structure_family = {
    "father": fields.String,
    "mother": fields.String
}
structure_fish = {
    "name": Upper,
    "address": {
        "city": fields.List(fields.String),
        "street": fields.String
    },
    "family": fields.Nested(structure_family)
}


class City:
    def __init__(self, name, city, street):
        self.name = name
        self.city = city
        self.street = street
        self.family = {
            "father": "Nick",
            "mother": "Kate"
        }


class GetFish(Resource):

    @marshal_with(structure_fish)
    def get(self):
        fish = City("Nick", ["Kyiv", 1], "Khreshatick")
        return fish


api.add_resource(Companies, "/companies", "/companies/<value>")
api.add_resource(HelloRest, "/")
api.add_resource(GetFish, "/fish")

if __name__ == '__main__':
    app.run(debug=True)
