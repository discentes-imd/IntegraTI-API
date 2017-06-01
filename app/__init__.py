# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restplus import Api
import logging
from logging.handlers import RotatingFileHandler
import pymysql
from app.middlewares import verify_route, verify_token, encrypt_password, reset_current_user, set_cors_header

pymysql.install_as_MySQLdb()

# Define the WSGI application object
app = Flask(__name__)

# Register middlewares
# before request
app.before_request(verify_route)
app.before_request(verify_token)
app.before_request(encrypt_password)
# after request
app.after_request(reset_current_user)
app.after_request(set_cors_header)

# Define Api application object
api = Api(app, version='0.5a', title='IntegraTI-API',
    description='API do IntegraTI',)

# Configurations
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Add log handler
handler = RotatingFileHandler(app.config['LOGGING_LOCATION'], maxBytes=100000, backupCount=50)
formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    app.logger.error(error)
    return error

from app.mod_shared import models
from app.mod_auth import models
from app.mod_events import models


# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module, ns as ns_auth
from app.mod_events.controllers import mod_event as event_module, ns as ns_event

# Register blueprint(s)

app.register_blueprint(auth_module)
app.register_blueprint(event_module)
api.add_namespace(ns_event)
api.add_namespace(ns_auth)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
# db.drop_all()
db.create_all()
