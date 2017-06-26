# Import flask dependencies
import random

# Import password / encryption helper tools
import jwt
from flask import Blueprint, request
from flask_restplus import Namespace, Resource, fields
# Import password utils
from werkzeug.security import check_password_hash

import config
from app import cache
# Import the database object from the main app module
# Import module models (i.e. User)
from app.mod_core.models import User
# Import utils
from app.utils import abort_if_none, msg

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
ns = Namespace('auth', 'Operations related to authentication and user')

# Models used in formatting input and response
user_auth_m = ns.model('user_auth', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})
user_m = ns.model('user', {
    'id_user': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'sigaa_registration_number': fields.String,
    'sigaa_user_name': fields.String,
    'id_photo_file': fields.Integer
})
user_m_expect = ns.model('user', {
    'name': fields.String,
    'email': fields.String,
    'sigaa_registration_number': fields.String,
    'sigaa_user_name': fields.String,
    'id_photo_file': fields.Integer,
    'password': fields.String
})
password_reset_m = ns.model('password_reset', {
    'old_password': fields.String,
    'password': fields.String
})

# TODO: Implementar permissões de usuário


# Define the authentication controller. POST is for login and DELETE for logout.
@ns.route('/login/')
@ns.response(403, 'Login or logout failed')
@ns.response(400, 'The username or user pass is malformed')
@ns.header('Authorization', 'The authorization token')
class AuthController(Resource):
    @ns.expect(user_auth_m)
    @ns.response(200, 'Login success')
    def post(self):
        """Login the user"""
        username = request.json['username']
        password = request.json['password']

        us = User.query\
            .filter(User.disabled is False)\
            .filter(User.sigaa_user_name == username)\
            .first()
        abort_if_none(us, 403, 'Username or password incorrect')

        if not check_password_hash(us.password, password):
            return msg('Username or password incorrect'), 403

        token = jwt.encode(
            {'id_user': us.id_user, 'tid': random.random()},
            config.SECRET_KEY,
            algorithm='HS256'
        ).decode('utf-8')

        return msg(token, 'token')

    @ns.response(200, 'Logout success')
    def delete(self):
        """Logout the user"""
        cache.blacklisted_tokens.append(request.headers['Authorization'])
        return msg('Logged out')
