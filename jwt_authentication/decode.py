import datetime
import jwt_authentication

from app import app


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt_authentication.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt_authentication.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt_authentication.InvalidTokenError:
        return 'Invalid token. Please log in again.'
