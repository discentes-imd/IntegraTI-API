# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from flask_restplus import Api


# Define the WSGI application object
app = Flask(__name__)

# Define Api application object
api = Api(app, version='1.0', title='IntegraTI-API',
    description='API do IntegraTI',)

# Configurations
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return 'Error: 404'

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_events.controllers import mod_event as event_module, ns as ns_event

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(event_module)
api.add_namespace(ns_event)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
