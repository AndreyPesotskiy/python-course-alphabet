from flask_restful import Resource


class Main(Resource):
    def get(self):
        return 'hello from main'
