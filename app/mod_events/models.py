"""
Model classes to access persistence. Such classes
are gonna provide data to controller layer.

TODO: maybe these constructors are bad designed (do they need
      explicit/manual None values if such fields don't exist in database?)
"""
# pylint: disable = C0111, R0903, C0103

from app import db
from app.mod_core.models import Base


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

    def __init__(self, title=None, description=None, date_start=None, date_end=None,
                 location=None, url=None, need_help=None):
        self.title = title
        self.description = description
        self.date_start = date_start
        self.date_end = date_end
        self.location = location
        self.url = url
        self.need_help = need_help


class EventType(Base):
    id_event_type = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description
