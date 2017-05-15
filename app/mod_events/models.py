"""
Model classes to access persistence. Such classes
are gonna provide data to controller layer.

TODO: maybe these constructors are bad designed (do they need
      explicit/manual None values if such fields don't exist in database?)
"""
# pylint: disable = C0111, R0903, C0103

from app import db
from sqlalchemy.ext.declarative import declared_attr


# Many-to-many helper tables (for public access, use models only) -----------

user_interest = db.Table(
    'user_interest',
    db.Column(
        'id_user',
        db.Integer,
        db.ForeignKey('user.id_user')
    ),
    db.Column(
        'id_tag',
        db.Integer,
        db.ForeignKey('tag.id_tag')
    )
)

event_file = db.Table(
    'event_file',
    db.Column(
        'id_event',
        db.Integer,
        db.ForeignKey('event.id_event')
    ),
    db.Column(
        'id_file',
        db.Integer,
        db.ForeignKey('file.id_file')
    )
)

event_tag = db.Table(
    'event_tag',
    db.Column(
        'id_event',
        db.Integer,
        db.ForeignKey('event.id_event')
    ),
    db.Column(
        'id_tag',
        db.Integer,
        db.ForeignKey('tag.id_tag')
    )
)

event_participation = db.Table(
    'event_participation',
    db.Column(
        'id_user',
        db.Integer,
        db.ForeignKey('user.id_user')
    ),
    db.Column(
        'id_event',
        db.Integer,
        db.ForeignKey('event.id_event')
    )
)


# Models and their simple relantionships -------------------------------------

class Base(db.Model):
    __abstract__ = True

    disabled = db.Column(db.Boolean)
    inserted_since = db.Column(db.DateTime, default=db.func.now())
    @declared_attr
    def inserted_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id_user'))
    # inserted_by = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    last_updated_since = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    @declared_attr
    def last_updated_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id_user'))
    # last_updated_by = db.Column(db.Integer, db.ForeignKey('user.id_user'))

class User(Base):
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)
    sigaa_registration_number = db.Column(db.String(15), unique=True)
    sigaa_user_name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(64))
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

    def __init__(self, id_user, name, sigaa_registration_number, sigaa_user_name,
                 password, id_photo_file,
                 disabled, inserted_since, inserted_by, last_updated_since, last_updated_by):
        self.disabled = disabled
        self.inserted_since = inserted_since
        self.inserted_by = inserted_by
        self.last_updated_since = last_updated_since
        self.last_updated_by = last_updated_by

        self.id_user = id_user
        self.name = name
        self.sigaa_registration_number = sigaa_registration_number
        self.sigaa_user_name = sigaa_user_name
        self.password = password
        self.id_photo_file = id_photo_file



class Event(Base):
    id_event = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(255))
    date_start = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)
    location = db.Column(db.String(50))
    url = db.Column(db.String(255))
    need_help = db.Column(db.Boolean)
    id_event_type = db.Column(db.Integer, db.ForeignKey('event_type.id_event_type'))
    participations = db.relationship('Participation', backref='event', lazy='dynamic')
    files = db.relationship(
        'File',
        secondary=event_file,
        backref=db.backref('events', lazy='dynamic')
    )
    tags = db.relationship(
        'Tag',
        secondary=event_tag,
        backref=db.backref('events', lazy='dynamic')
    )

    def __init__(self, id_event, title, description, date_start, date_end,
                 location, url, need_help,
                 disabled, inserted_since, inserted_by, last_updated_since, last_updated_by):
        self.disabled = disabled
        self.inserted_since = inserted_since
        self.inserted_by = inserted_by
        self.last_updated_since = last_updated_since
        self.last_updated_by = last_updated_by

        self.id_event = id_event
        self.title = title
        self.description = description
        self.date_start = date_start
        self.date_end = date_end
        self.location = location
        self.url = url
        self.need_help = need_help



class Tag(Base):
    id_tag = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    slug = db.Column(db.String(50), unique=True)

    def __init__(self, id_tag, name, slug):
        self.id_tag = id_tag
        self.name = name
        self.slug = slug



class File(Base):
    id_file = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    path = db.Column(db.String(255), unique=True)

    def __init__(self, id_file, name, description, path,
                 disabled, inserted_since, inserted_by, last_updated_since, last_updated_by):
        self.disabled = disabled
        self.inserted_since = inserted_since
        self.inserted_by = inserted_by
        self.last_updated_since = last_updated_since
        self.last_updated_by = last_updated_by

        self.id_file = id_file
        self.name = name
        self.description = description
        self.path = path



class EventType(Base):
    id_event_type = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, id_event_type, name, description,
                 disabled, inserted_since, inserted_by, last_updated_since, last_updated_by):
        self.disabled = disabled
        self.inserted_since = inserted_since
        self.inserted_by = inserted_by
        self.last_updated_since = last_updated_since
        self.last_updated_by = last_updated_by

        self.id_event_type = id_event_type
        self.name = name
        self.description = description
