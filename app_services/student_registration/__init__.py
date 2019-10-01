from flask import Blueprint
from flask_restplus import Api

from .resource import UserRegistration, UserLogin

student_registration = Blueprint('registration', 'registration')
registration_api = Api(student_registration)

registration_routes = [
    '/create'
]

login_routes = [
    '/login'
]

registration_api.add_resource(UserRegistration, *registration_routes)
registration_api.add_resource(UserLogin, *login_routes)
