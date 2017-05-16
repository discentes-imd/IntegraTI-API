# Import flask dependencies
from flask import Blueprint, request, flash, g, session, redirect, url_for

from flask_restplus import Namespace, Resource, fields, reqparse
from datetime import datetime

# Import password / encryption helper tools
#from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db
from app.mod_events.models import EventType

# Import module models (i.e. User)
# from app.mod_event.models import User

from app.mod_events.controllers import mod_event, ns
from flask import request
from app.utils import update_object
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
    @ns.response(403, 'User is not logged or not have permission')
    @ns.response(400, 'ID is not int')
    @ns.response(404, 'Not Found')
    @ns.response(200, 'Returns the event model on the body of the request', event_type)
    @ns.marshal_with(event_type)
    def get(self, id):
        '''Get an event_type by ID'''
        et = EventType.query.filter(EventType.disabled != 1 and EventType.id_event_type == id)
        et = et.first()
        if et is None:
            ns.abort(404, 'Not Found')
        return et

    @ns.response(403, 'User is not logged or not have permission')
    @ns.response(400, 'ID is not int')
    @ns.response(404, 'Not Found')
    @ns.response(200, 'Event altered')
    @ns.expect(event_type)
    def put(self, id):
        '''Update an event_type by ID'''
        et = EventType.query.filter(EventType.disabled != 1 and EventType.id_event_type == id)
        et = et.first()
        if et is None:
            ns.abort(404, 'Not Found')
        update_object(et, request.json)
        db.session.commit()
        return {'msg': 'altered'}

    @ns.response(403, 'User is not logged or not have permission')
    @ns.response(400, 'ID is not int')
    @ns.response(404, 'Not Found')
    @ns.response(200, 'Event disabled')
    def delete(self, id):
        '''Delete an event_type by ID'''
        et = EventType.query.filter(EventType.disabled != 1 and EventType.id_event_type == id)
        et = et.first()
        if et is None:
            return {'msg': 'Not Found'}, 404
        et.disabled = 1
        db.session.commit()
        return {'msg': 'disabled'}


@ns.route('/type')
class EventTypePostController(Resource):
    @ns.response(403, 'User is not logged or not have permission')
    @ns.response(400, 'One of the arguments is malformed')
    @ns.response(200, 'Return an list of events that matched criteria', event_type)
    @ns.marshal_with(event_type)
    def get(self):
        '''Get a event_type list'''
        return EventType.query.filter(EventType.disabled != 1)

    @ns.response(403, 'User is not logged or not have permission')
    @ns.response(400, 'The model is malformed')
    @ns.response(404, 'Not Found')
    @ns.response(200, 'Event disabled')
    @ns.expect(event_type)
    def post(self):
        '''Create a new event_type'''
        et = EventType(request.json['name'], request.json['description'], 1, 1)
        db.session.add(et)
        db.session.commit()
        return {"id": et.id_event_type}
