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


@ns.route('/<int:id>')
@ns.doc(params={'id': 'Event ID'})
class EventController(Resource):
    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Id não é do tipo int',
                       404: 'Não foi encontrado o evento com a id especificada',
                       200: 'Retorna o modelo evento no corpo da request'})
    def get(self, id):
        return {'id': id, 'nome': 'evento padrão'}

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Id não é do tipo int ou o modelo está errado',
                       404: 'Não foi encontrado o evento com a id especificada',
                       200: 'Retorna o modelo evento no corpo da request'})
    def put(self, id):
        return {'msg': 'nada no put'}

    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'Id não é do tipo int',
                       404: 'Não foi encontrado o evento com a id especificada',
                       200: 'O evento foi desabilitado no db'})
    def delete(self, id):
        return {'msg': 'nada no delete'}


@ns.route('/')
class EventPostController(Resource):
    @ns.doc(responses={403: 'Usuario não está logado ou não tem permissão',
                       400: 'O modelo está com partes faltando ou com tipos diferentes',
                       200: 'Retorna o id do evento no corpo da request'})
    def post(self):
        return {'msg': 'nada no post'}