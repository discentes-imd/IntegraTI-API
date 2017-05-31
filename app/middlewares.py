from flask import Response, request
from app.utils import msg
from app.routes_need_login_config import routes
from werkzeug.security import generate_password_hash
import jwt
import config


def verify_route(response):
    """
    Verify if the route is in a list of routes that need have the authorization header
    """
    for route in routes:
        if route[0] == str(request.url_rule) and request.method in route[1] and 'Authorization' not in request.headers:
            return Response(str(msg('Authorization header missing!')), 400)
    return response


# TODO: Implementar a função verify token
# TODO: Depois de decodificar o token adicionar o id_user ao objeto request
# TODO: Implementar blacklist para tokens (logout por ex.)
# TODO: Implementar a validação dos modelos de entrada

def clear_user():
    config.current_user = 1


def verify_token(response):
    """
    Verify if the token is valid, not expired and not blacklisted
    """
    if 'Authorization' not in request.headers:
        return response

    try:
        payload = jwt.decode(request.headers['Authorization'], config.SECRET_KEY)
        config.curent_user = payload['id_user']
    except jwt.ExpiredSignatureError:
        return Response(str(msg('Error: token expired')), 403)
    except jwt.DecodeError:
        return Response(str(msg('Error: invalid token')), 403)
    return response


def encrypt_password(response):
    """
    Verify if the route is for login or user create, then encrypts the password.
    :param response: flask.Response
    :return: response: flask.Response
    """
    if request.url_rule in ['/auth/login/', '/user/create/'] \
            and request.method == 'POST' and request.json['password'] != '':
        request.json['password'] = generate_password_hash(request.json['password'])
    return response
