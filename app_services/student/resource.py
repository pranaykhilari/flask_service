from flask import jsonify
from flask_api import status
from flask_restful import reqparse, Resource

from app import db
from models.student import Student
from .serializer import student_schema

parser = reqparse.RequestParser()

parser.add_argument('name', type=str, required=True, help='name of employee')
parser.add_argument('email', type=str, required=True, help='email of employee')
parser.add_argument('phone_num', type=int, help='phone number of employee')


class StudentAPI(Resource):

    def post(self):

        args = parser.parse_args()

        student = Student(**args)

        db.session.add(student)
        db.session.commit()

        data = student_schema.dump(student)

        return jsonify(result=data, status=status.HTTP_201_CREATED)
