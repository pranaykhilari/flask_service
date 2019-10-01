from flask import jsonify
from flask_api import status
from flask_restplus import Resource, reqparse
from sqlalchemy import and_

from app import db
from jwt_authentication.encode import encode_auth_token
from models.student_registration import User
from .serializer import student_schema

parser = reqparse.RequestParser()

parser.add_argument('email', type=str, required=True, help='email is required')
parser.add_argument('password', type=str, required=True, help='Password to create account')


class UserRegistration(Resource):

    def post(self):

        args = parser.parse_args()
        username = args.get('email')

        student = User.query.filter(User.email == username).first()

        if not student:
            user = User(**args)
            db.session.add(user)
            db.session.commit()

            student = student_schema.dump(user),

            return jsonify(result=student, status=status.HTTP_201_CREATED)
        return jsonify(result='User is already exist with this username', status=status.HTTP_409_CONFLICT)


class UserLogin(Resource):

    def post(self):
        args = parser.parse_args()
        email = args.get('email')
        password = args.get('password')

        student = User.query.filter(and_(User.email == email, User.password == password)).first()
        if student:
            auth_token = encode_auth_token(student.id)
            return jsonify(result=auth_token.decode(), status=status.HTTP_200_OK)
        return jsonify(result='Incorrect username and password', status=status.HTTP_401_UNAUTHORIZED)
