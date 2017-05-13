"""
Class models to access data for any event controller.

TODO: implement foreign keys
TODO: maybe these constructors are bad designed (do they need
      explicit/manual None values if such fields don't exist in database?)
"""

from sqlalchemy import Column, Integer, Boolean, String, DateTime, Model


class User(Model):
    id_user = Column(Integer, primary_key=True)
    name = Column(String(80))
    sigaa_registration_number = Column(Integer, unique=True)
    sigaa_user_name = Column(Integer, unique=True)
    password = Column(String(64))
    id_photo_file = Column(Integer)

    def __init__(self, id_user, name, sigaa_registration_number, sigaa_user_name,
                 password, id_photo_file):
        self.id_user = id_user
        self.name = name
        self.sigaa_registration_number = sigaa_registration_number
        self.sigaa_user_name = sigaa_user_name
        self.password = password
        self.id_photo_file = id_photo_file



class Event(Model):
    id_event = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(2000))
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    location = Column(String(50))
    url = Column(String(2000))
    need_help = Column(Boolean)

    def __init__(self, id_event, title, description, date_start, date_end,
                 location, url, need_help):
        self.id_event = id_event
        self.title = title
        self.description = description
        self.date_start = date_start
        self.date_end = date_end
        self.location = location
        self.url = url
        self.need_help = need_help



class Tag(Model):
    id_tag = Column(Integer, primary_key=True)
    name = Column(String(25), unique=True)
    slug = Column(String(50), unique=True)

    def __init__(self, id_tag, name, slug):
        self.id_tag = id_tag
        self.name = name
        self.slug = slug



class File(Model):
    id_file = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(1000))
    path = Column(String(2000), unique=True)

    def __init__(self, id_file, name, description, path):
        self.id_file = id_file
        self.name = name
        self.description = description
        self.path = path



class EventType(Model):
    id_event_type = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(1000))

    def __init__(self, id_event_type, name, description):
        self.id_event_type = id_event_type
        self.name = name
        self.description = description



class ParticipationStatus(Model):
    id_participation_status = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, id_participation_status, name):
        self.id_participation_status = id_participation_status
        self.name = name



class Participation(Model):
    id_participation = Column(Integer, primary_key=True)
    id_participation_status = Column(Integer)
    id_user = Column(Integer)
    id_event = Column(Integer)

    def __init__(self, id_participation, id_participation_status, id_user, id_event):
        self.id_participation = id_participation
        self.id_participation_status = id_participation_status
        self.id_user = id_user
        self.id_event = id_event

