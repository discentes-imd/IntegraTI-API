from flask import Response, request
from app.utils import msg
from app.routes_need_login_config import routes

"""
Verify if the route is in a list of routes that need have the authorization header
"""
def verify_route(response):
    for route in routes:
        if route[0] == str(request.url_rule) and request.method in route[1] and not request.headers.has_key('Authorization'):
            return Response(str(msg('Authorization header missing!')), 400)
    return response


# TODO: Implementar a função verify token
# TODO: Depois de decodificar o token adicionar o id_user ao objeto request
"""
Verify if the token is valid, not expired and not blacklisted
"""
def verify_token(response):
    if not request.headers.has_key('Authorization'):
        return response

