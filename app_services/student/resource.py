from flask import jsonify
from flask_api import status
from flask_restplus import reqparse, Resource

from app import db
from models.student import Student
from .serializer import student_schema, students_schema

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

    def get(self, student_id=None):

        if student_id:
            student = Student.query.filter(Student.id == student_id).first()
            data = student_schema.dump(student)
            if not data:
                return jsonify(result=data, status=status.HTTP_404_NOT_FOUND)
        else:
            student = Student.query.all()
            data = students_schema.dump(student)
        return jsonify(result=data, status=status.HTTP_200_OK)

    def delete(self, student_id):

        student = Student.query.filter(Student.id == student_id).first()

        if not student:
            return jsonify(result='Record not available with this ID', status=status.HTTP_404_NOT_FOUND)

        db.session.delete(student)
        db.session.commit()

        return jsonify(result='Record deleted successfully', status=status.HTTP_202_ACCEPTED)

    def put(self, student_id):

        student = Student.query.filter(Student.id == student_id).first()

        if not student:
            return jsonify(result='Record not available with this ID', status=status.HTTP_404_NOT_FOUND)

        args = parser.parse_args()
        student.name = args.get('name')
        student.email = args.get('email')
        student.phone_num = args.get('phone_num')
        db.session.commit()

        return jsonify(result=student_schema.dump(student), status=status.HTTP_202_ACCEPTED)