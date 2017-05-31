# Import flask dependencies
from flask import Blueprint, request

# Import password / encryption helper tools
import jwt

# Import the database object from the main app module
from app import db

from flask_restplus import Namespace, Resource, fields, reqparse

# Import module models (i.e. User)
from app.mod_auth.models import User

# Import utils
from app.utils import abort_if_none, msg, update_object
from app import app

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
ns = Namespace('auth', 'Operations related to authentication and user')

msg_m = ns.model('msg', {
    'msg': fields.String
})

token_m = ns.model('token', {
    'token': fields.String
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
    'id_photo_file': fields.Integer
})


# TODO: Implementar encriptação do password no db
# TODO: Implementar permissões de usuário


# Define the authentication controller. POST is for login and DELETE for logout.
@ns.route('/login/')
@ns.response(403, 'Login or logout failed')
@ns.response(400, 'The username or user pass is malformed')
@ns.header('Authorization', 'The authorization token')
class AuthController(Resource):
    @ns.expect(user_auth_m)
    @ns.marshal_with(token_m)
    def post(self):
        'Login the user'
        username = request.json['username']
        password = request.json['password']
        us = User.query.filter(User.disabled == 0).filter(User.sigaa_user_name == username).filter(User.password == password)
        us = us.first()
        abort_if_none(us, 403, 'Username or password incorrect')
        token = jwt.encode(
            {'id_user': us.id_user},
            app.secret_key,
            algorithm='HS256'
        )
        return msg(token, 'token')

    @ns.marshal_with(msg_m)
    def delete(self):
        'Logout the user'
        pass


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
