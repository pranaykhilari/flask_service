from flask_restful import Resource


class TodoItem(Resource):

    def get(self):
        return {'task': "Hello, World!"}