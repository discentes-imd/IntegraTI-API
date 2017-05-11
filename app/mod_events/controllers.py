# Import flask dependencies
from flask import Blueprint, request, flash, g, session, redirect, url_for

from flask_restplus import Namespace, Resource, fields

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
# from app.mod_event.models import User

# Define the blueprint: 'event', set its url prefix: app.url/event
mod_event = Blueprint('event', __name__, url_prefix='/event')

ns = Namespace('event', description='Operations related to events')

@ns.route('/event/<int:id>', endpoint='event')
@ns.doc(params={'id': 'An ID'})
class Event_controller(Resource):
    def get(self, id):
        return {'id': id, 'nome': 'evento padrão'}

    @ns.doc(responses={403: 'Not Authorized'})
    def post(self, id):
        ns.abort(403)