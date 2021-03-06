from flask import Blueprint
from flask_restplus import Api

from .resource import StudentAPI

student_blueprint = Blueprint('student', __name__)
api = Api(student_blueprint)

routes = [
    '/add',
    '/get/<int:student_id>',
    '/get',
    '/delete/<int:student_id>',
    '/edit/<int:student_id>'
]

api.add_resource(StudentAPI, *routes)

