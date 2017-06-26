from flask import request, g, Blueprint
from flask_restplus import Resource, Namespace
from werkzeug.security import check_password_hash

from app import db, cache
from app.mod_auth.controllers import user_m, user_m_expect, password_reset_m
from app.mod_core.models import User
from app.utils import abort_if_none, fill_object, msg


# Define the blueprint: 'auth', set its url prefix: app.url/core
mod_core = Blueprint('core', __name__, url_prefix='/core')
ns = Namespace('core', 'Operations related to core')


@ns.route('/user/<int:id>')
@ns.response(403, 'User is not logged or not have permission')
@ns.response(400, 'ID is not int')
@ns.response(404, 'Not Found')
@ns.header('Authorization', 'The authorization token')
class UserController(Resource):
    @ns.marshal_with(user_m)
    @ns.response(200, 'Returns the user model on the body of the response')
    def get(self, id):
        """Get an user by ID"""
        us = User.query \
            .filter(User.disabled == 0) \
            .filter(User.id_user == id) \
            .first()
        abort_if_none(us, 404, 'not found')
        return us

    @ns.response(200, 'User updated')
    @ns.expect(user_m_expect)
    def put(self, id):
        """Update an user by ID"""
        us = User.query\
            .filter(User.disabled == 0)\
            .filter(User.id_user == id)\
            .first()
        abort_if_none(us, 404, 'not found')

        fill_object(us, request.json)
        db.session.commit()

        return msg('success!')

    @ns.response(200, 'User disabled on db')
    def delete(self, id):
        """Delete an user by ID"""
        us = User.query.filter(User.disabled == 0)\
            .filter(User.id_user == id)\
            .first()
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
        """Get an list of users"""
        return User.query.filter(User.disabled == 0).all()

    @ns.response(400, 'The model is malformed')
    @ns.response(200, 'User inserted')
    @ns.expect(user_m_expect)
    def post(self):
        """Create a new user"""
        us = User()
        fill_object(us, request.json)
        db.session.add(us)
        db.session.commit()
        return msg(us.id_user, 'id')


@ns.route('/user/resetpassword/')
@ns.response(403, 'User is not logged, not have permission or the password is incorrect')
@ns.response(400, 'The input is wrong')
@ns.response(404, 'User not Found')
@ns.response(200, 'The password is successfully altered. Obs: You need login again, to receive new token.')
@ns.header('Authorization', 'The authorization token')
class PasswordController(Resource):

    @ns.expect(password_reset_m)
    def put(self):
        """Change the password"""
        us = User.query \
            .filter(User.disabled == 0) \
            .filter(User.id_user == g.current_user) \
            .first()
        abort_if_none(us, 404, 'User not found')

        if not check_password_hash(us.password, request.json['old_password']):
            return msg('Old password incorrect'), 403

        us.password = request.json['password']
        db.session.commit()
        cache.blacklisted_tokens.append(request.headers['Authorization'])

        return msg('success!')
