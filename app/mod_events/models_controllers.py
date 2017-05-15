# Import flask dependencies
from flask import Blueprint, request, flash, g, session, redirect, url_for

from flask_restplus import Namespace, Resource, fields, reqparse
from datetime import datetime

# Import password / encryption helper tools
#from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
# from app.mod_event.models import User

from app.mod_events.controllers import mod_event, ns
# Define the blueprint: 'event', set its url prefix: app.url/event
# mod_event = Blueprint('event', __name__, url_prefix='/event')

# ns = Namespace('event', description='Operations related to events')

event = ns.model('event', {
    'id_event': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'date_event_start': fields.DateTime,
    'date_event_end': fields.DateTime,
    'location': fields.String,
    'url': fields.String,
    'help': fields.Boolean,
    'event_type_id': fields.Integer,
    'tags': fields.List(fields.String, required=False)
})

event_type = ns.model('event_type', {
    'id_event_type': fields.Integer,
    'name': fields.String,
    'description': fields.String
})

event_file = ns.model('event_file', {
    'id_event_file': fields.Integer,
    'id_event': fields.Integer,
    'id_file': fields.Integer
})

event_tag = ns.model('event_tag', {
    'id_tag': fields.Integer,
    'id_event': fields.Integer,
    'id_event_tag': fields.Integer
})


@ns.route('/<int:id>')
@ns.doc(params={'id': 'Event ID'})
class EventController(Resource):

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Id não é do tipo int',
                       404: 'Não foi encontrado o evento com a id especificada',
                       200: 'Retorna o modelo evento no corpo da request'})
    @ns.marshal_with(event)
    def get(self, id):
        '''Get an event by ID'''
        return {
                    'id_event': id,
                    'title': 'fgggffg',
                    'description': 'fgfggfgf',
                    'date_event_start': datetime(2017, 12, 24),
                    'date_event_end': datetime(2017, 12, 24),
                    'location': 'fgfgfdggf',
                    'url': 'rgfgffggf',
                    'help': True,
                    'event_type_id': 123,
                    'tags': ['tag1', 'tag2', 'tag3']
                }, 200

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Id não é do tipo int ou o modelo está errado',
                       404: 'Não foi encontrado o evento com a id especificada',
                       200: 'Retorna o modelo evento no corpo da request'})
    @ns.expect(event)
    def put(self, id):
        '''Update an event by ID'''
        return {'msg': 'nada no put'}

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Id não é do tipo int',
                       404: 'Não foi encontrado o evento com a id especificada',
                       200: 'O evento foi desabilitado no db'})
    def delete(self, id):
        '''Delete an event by ID'''
        return {'msg': 'nada no delete'}


@ns.route('/')
class EventPostController(Resource):
    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Algum dos argumentos está errado',
                       200: 'Retorna no corpo da request uma lista de eventos encontrados'})
    @ns.marshal_with(event)
    def get(self):
        '''Get an event list'''
        return {'msg': 'nada aqui'}

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'O modelo está com partes faltando ou com tipos diferentes',
                       200: 'Retorna o id do evento no corpo da request'})
    @ns.expect(event)
    def post(self):
        '''Create a new event'''
        return {'msg': 'nada no post'}


@ns.route('/type/<int:id>')
@ns.doc(params={'id': 'Event Type ID'})
class EventTypeController(Resource):

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Id não é do tipo int',
                       404: 'Não foi encontrado o tipo de evento com a id especificada',
                       200: 'Retorna o modelo tipo de evento no corpo da request'})
    @ns.marshal_with(event_type)
    def get(self, id):
        '''Get an event_type by ID'''
        return {'msg': 'nada ainda aqui'}

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Id não é do tipo int ou o modelo está errado',
                       404: 'Não foi encontrado o evento com a id especificada',
                       200: 'O tipo foi alterado'})
    @ns.expect(event)
    def put(self, id):
        '''Update an event_type by ID'''
        return {'msg': 'nada no put'}

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Id não é do tipo int',
                       404: 'Não foi encontrado o evento com a id especificada',
                       200: 'O tipo de evento foi desabilitado no db'})
    def delete(self, id):
        '''Delete an event_type by ID'''
        return {'msg': 'nada no delete'}


@ns.route('/type')
class EventTypePostController(Resource):
    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Algum dos argumentos está errado',
                       200: 'Retorna no corpo da request uma lista de tipo de eventos encontrado'})
    @ns.marshal_with(event_type)
    def get(self):
        '''Get a event_type list'''
        return {'msg': 'nada aqui'}

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'O modelo está com partes faltando ou com tipos diferentes',
                       200: 'Retorna o id do tipo de evento no corpo da request'})
    @ns.expect(event)
    def post(self):
        '''Create a new event_type'''
        return {'msg': 'nada no post'}