# Import flask dependencies
from flask import Blueprint, request, flash, g, session, redirect, url_for

from flask_restplus import Namespace, Resource, fields, reqparse
from datetime import datetime

# Import password / encryption helper tools
#from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.mod_events.models import EventType
from app.mod_events.models import Event
from app.mod_events.models import Tag

from app.mod_events.controllers import mod_event, ns
from flask import request
from app.utils import update_object
from app.utils import abort_if_none
from app.utils import msg
# Define the blueprint: 'event', set its url prefix: app.url/event
# mod_event = Blueprint('event', __name__, url_prefix='/event')

# ns = Namespace('event', description='Operations related to events')

tag_m = ns.model('tag', {
    'name': fields.String,
    'slug': fields.String
})

event = ns.model('event', {
    'id_event': fields.Integer,
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'date_start': fields.DateTime(required=True),
    'date_end': fields.DateTime(required=True),
    'location': fields.String(required=True),
    'url': fields.String(required=True),
    'need_help': fields.Boolean(required=True),
    'id_event_type': fields.Integer,
    'tags': fields.List(fields.Nested(tag_m)),
    'files': fields.List(fields.Integer)
})

event_type = ns.model('event_type', {
    'id_event_type': fields.Integer,
    'name': fields.String,
    'description': fields.String
})


# TODO: Fazer parte referentes a upload de arquivos
# TODO: Definir como será o json do query
@ns.route('/<int:id>')
@ns.doc(params={'id': 'Event ID'})
@ns.response(403, 'User is not logged or not have permission')
@ns.response(400, 'ID is not int')
@ns.response(404, 'Not Found')
class EventController(Resource):
    @ns.response(200, 'Returns the event model on the body of the response', event)
    @ns.marshal_with(event)
    def get(self, id):
        '''Get an event by ID'''
        ev = Event.query.filter(Event.disabled == 0).filter(Event.id_event == id).first()
        abort_if_none(ev, 404, 'Not Found')
        return ev

    @ns.response(200, 'Successfully updated', event)
    @ns.expect(event)
    def put(self, id):
        '''Update an event by ID'''
        ev = Event.query.filter(Event.disabled == 0).filter(Event.id_event == id).first()
        abort_if_none(ev, 404, 'Not Found')
        update_object(ev, request.json)
        db.session.commit()
        return msg('success!')

    @ns.response(200, 'Disabled on db')
    def delete(self, id):
        '''Delete an event by ID'''
        ev = Event.query.filter(Event.disabled == 0).filter(Event.id_event == id).first()
        abort_if_none(ev, 404, 'Not Found')
        ev.disabled = 1
        db.session.commit()
        return msg('disabled')


@ns.route('/')
@ns.response(403, 'User is not logged or not have permission')
class EventPostController(Resource):
    @ns.response(400, 'The query json is wrong')
    @ns.response(200, 'Return an event list that matched criteria', event)
    @ns.marshal_with(event)
    def get(self):
        '''Get an event list'''
        return Event.query.all()

    @ns.response(400, 'The model is malformed')
    @ns.response(200, 'Added', event)
    @ns.expect(event)
    def post(self):
        '''Create a new event'''
        ev = Event()
        # copy the tags dict
        tags_model = request.json['tags'][:]
        del request.json['tags']
        update_object(ev, request.json)
        for tm in tags_model:
            t = Tag.query.filter(Tag.name == tm['name']).first()
            if t is not None:
                ev.tags.append(t)
                continue
            tag = Tag()
            update_object(tag, tm)
            ev.tags.append(tag)
        # submit objects to db
        db.session.add(ev)
        db.session.commit()
        return msg(ev.id_event, 'id')


@ns.route('/type/<int:id>')
@ns.doc(params={'id': 'Event Type ID'})
@ns.response(403, 'User is not logged or not have permission')
@ns.response(400, 'ID is not int')
@ns.response(404, 'Not Found')
class EventTypeController(Resource):

    @ns.response(200, 'Returns the event model on the body of the response', event_type)
    @ns.marshal_with(event_type)
    def get(self, id):
        '''Get an event_type by ID'''
        et = EventType.query.filter(EventType.disabled == 0).filter(EventType.id_event_type == id)
        et = et.first()
        abort_if_none(et, 404, 'Not Found')
        return et

    @ns.response(200, 'Event altered')
    @ns.expect(event_type)
    def put(self, id):
        '''Update an event_type by ID'''
        et = EventType.query.filter(EventType.disabled == 0).filter(EventType.id_event_type == id)
        et = et.first()
        abort_if_none(et, 404, 'Not Found')
        update_object(et, request.json)
        db.session.commit()
        return msg('altered')

    @ns.response(200, 'Event disabled')
    def delete(self, id):
        '''Delete an event_type by ID'''
        et = EventType.query.filter(EventType.disabled == 0).filter(EventType.id_event_type == id)
        et = et.first()
        abort_if_none(et, 404, 'Not Found')
        et.disabled = 1
        db.session.commit()
        return msg('disabled')


@ns.route('/type')
@ns.response(403, 'User is not logged or not have permission')
class EventTypePostController(Resource):

    @ns.response(400, 'One of the arguments is malformed')
    @ns.response(200, 'Return an list of events that matched criteria', event_type)
    @ns.marshal_with(event_type)
    def get(self):
        '''Get a event_type list'''
        return EventType.query.filter(EventType.disabled == 0).all()

    @ns.response(400, 'The model is malformed')
    @ns.response(200, 'Event inserted')
    @ns.expect(event_type)
    def post(self):
        '''Create a new event_type'''
        et = EventType(request.json['name'], request.json['description'], 1, 1)
        db.session.add(et)
        db.session.commit()
        return msg(et.id_event_type, 'id')
