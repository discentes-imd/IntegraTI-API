# Import flask dependencies
from flask import Blueprint, request

# Import password / encryption helper tools
import jwt

# Import the database object from the main app module
from app import db

from flask_restplus import Namespace, Resource, fields, reqparse

# Import module models (i.e. User)
from app.mod_auth.models import User

# Import password utils
from werkzeug.security import check_password_hash

# Import utils
from app.utils import abort_if_none, msg, update_object

import config

from app import cache

import random

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
ns = Namespace('auth', 'Operations related to authentication and user')

# Models used in formatting input and response
msg_m = ns.model('msg', {
    'message': fields.String
})
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
        'Login the user'
        username = request.json['username']
        password = request.json['password']
        us = User.query.filter(User.disabled == 0).filter(User.sigaa_user_name == username)
        us = us.first()
        abort_if_none(us, 403, 'Username or password incorrect')
        if not check_password_hash(us.password, password):
            return msg('Username or password incorrect'), 403
        token = jwt.encode(
            {'id_user': us.id_user,
             'tid': random.random()},
            config.SECRET_KEY,
            algorithm='HS256'
        )
        return msg(token.decode('utf-8'), 'token')

    @ns.marshal_with(msg_m)
    @ns.response(200, 'Logout success')
    def delete(self):
        'Logout the user'
        pass


@ns.route('/user/resetpassword/')
@ns.response(403, 'User is not logged, not have permission or the password is incorrect')
@ns.response(400, 'The input is wrong')
@ns.response(404, 'User not Found')
@ns.response(200, 'The password is successfully altered. Obs: You need login again, to receive new token.')
@ns.header('Authorization', 'The authorization token')
class PasswordController(Resource):
    @ns.expect(password_reset_m)
    def put(self):
        password = request.json['password']
        us = User.query.filter(User.disabled == 0).filter(User.id_user == cache.current_user)
        us = us.first()
        abort_if_none(us, 404, 'User not found')
        if not check_password_hash(us.password, request.json['old_password']):
            return msg('Old password incorrect'), 403
        us.password = password
        db.session.commit()
        cache.blacklisted_tokens.append(request.headers['Authorization'])
        return msg('success!')


@ns.route('/user/<int:id>')
@ns.response(403, 'User is not logged or not have permission')
@ns.response(400, 'ID is not int')
@ns.response(404, 'Not Found')
@ns.header('Authorization', 'The authorization token')
class UserController(Resource):
    @ns.marshal_with(user_m)
    @ns.response(200, 'Returns the user model on the body of the response')
    def get(self, id):
        'Get an user by ID'
        us = User.query.filter(User.disabled == 0).filter(User.id_user == id).first()
        abort_if_none(us, 404, 'not found')
        return us

    @ns.response(200, 'User updated', msg_m)
    @ns.expect(user_m_expect)
    def put(self, id):
        'Update an user by ID'
        us = User.query.filter(User.disabled == 0).filter(User.id_user == id).first()
        abort_if_none(us, 404, 'not found')
        update_object(us, request.json)
        db.session.commit()
        return msg('success!')

    @ns.response(200, 'User disabled on db', msg_m)
    def delete(self, id):
        'Delete an user by ID'
        us = User.query.filter(User.disabled == 0).filter(User.id_user == id).first()
        abort_if_none(us, 404, 'not found')
        us.disabled = 1
        db.session.commit()
        return msg('disabled on db')


@ns.route('/user/')
@ns.response(403, 'User is not logged or not have permission')
@ns.header('Authorization', 'The authorization token')
class UserPostController(Resource):
    @ns.response(400, 'One of the arguments is malformed')
    @ns.response(200, 'Return an list of users that matched criteria', user_m)
    @ns.marshal_with(user_m)
    def get(self):
        'Get an list of users'
        return User.query.filter(User.disabled == 0).all()

    @ns.response(400, 'The model is malformed')
    @ns.response(200, 'User inserted', msg_m)
    @ns.expect(user_m_expect)
    def post(self):
        'Create a new user'
        us = User()
        update_object(us, request.json)
        db.session.add(us)
        db.session.commit()
        return msg(us.id_user, 'id')
