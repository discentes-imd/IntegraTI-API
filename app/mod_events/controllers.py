# Import flask dependencies
from flask import Blueprint, request, flash, g, session, redirect, url_for

from flask_restplus import Namespace, Resource, fields, reqparse
from datetime import datetime

# Import password / encryption helper tools
#from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

mod_event = Blueprint('event', __name__, url_prefix='/event')

ns = Namespace('event', description='Operations related to events')

from app.mod_events import models_controllers

@ns.route('/<int:event_id>/tag/<int:tag_id>')
class EventTagDeleteController(Resource):
    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Algum dos ids não é do tipo int',
                       404: 'Não foi encontrado o evento ou tag com a id especificada',
                       200: 'A tag foi removida do evento'})
    def delete(self, event_id, tag_id):
        '''Remove a tag from an event'''
        return {'msg': 'Nada ainda'}, 200


@ns.route('/<int:event_id>/tag/')
class EventTagPostController(Resource):
    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'O id do evento não é do tipo int',
                       200: 'A tag foi foi adicionada ao evento'})
    def post(self, event_id):
        '''Add a tag to an event'''
        return {'msg': 'Nada ainda'}, 200