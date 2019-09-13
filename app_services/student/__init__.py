from flask import Blueprint
from flask_restful import Api

from .resource import StudentAPI

student_blueprint = Blueprint('student', __name__)
api = Api(student_blueprint)

api.add_resource(StudentAPI, '/add')
