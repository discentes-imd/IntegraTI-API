# Import the database object (db) from the main application module
from app import db
from app.mod_shared.models import Base

# Define a base model for other database tables to inherit
from app.mod_events.models import user_interest
from app.mod_events.models import event_participation


class User(Base):
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)
    sigaa_registration_number = db.Column(db.String(15), unique=True)
    sigaa_user_name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))

    id_photo_file = db.Column(db.Integer, db.ForeignKey('file.id_file'))
    event_participations = db.relationship(
        'Event',
        secondary=event_participation,
        backref=db.backref('participating_users', lazy='dynamic')
    )
    user_interests = db.relationship(
        'Tag',
        secondary=user_interest,
        backref=db.backref('interested_users', lazy='dynamic')
    )

    def __init__(self, name=None, email=None, sigaa_registration_number=None, sigaa_user_name=None,
                 password=None, id_photo_file=None):

        self.name = name
        self.email = email
        self.sigaa_registration_number = sigaa_registration_number
        self.sigaa_user_name = sigaa_user_name
        self.password = password
        self.id_photo_file = id_photo_file
