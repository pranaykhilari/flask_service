from flask import Blueprint
from flask_restful import Api


def configure():
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)
    return api_bp, api
