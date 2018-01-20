from app import db
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils.types.password import PasswordType
from flask import g


def get_current_user():
    # return None
    return g.current_user


class Base(db.Model):
    __abstract__ = True
    disabled = db.Column(db.Boolean, default=0)
    inserted_since = db.Column(db.DateTime, default=db.func.now())
    last_updated_since = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @declared_attr
    def inserted_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id_user'),
                         default=get_current_user)

    @declared_attr
    def last_updated_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id_user'),
                         default=get_current_user, onupdate=get_current_user)


from app.mod_events.models import event_participation, user_interest


class User(Base):
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)
    sigaa_registration_number = db.Column(db.String(15), unique=True)
    sigaa_user_name = db.Column(db.String(50), unique=True)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],

        deprecated=['md5_crypt']
    ))

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


class File(Base):
    id_file = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    path = db.Column(db.String(255), unique=True)

    def __init__(self, name=None, description=None, path=None):
        self.name = name
        self.description = description
        self.path = path


class Tag(Base):
    id_tag = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    slug = db.Column(db.String(50), unique=True)

    def __init__(self, name=None, slug=None):
        self.name = name
        self.slug = slug
