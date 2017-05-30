from app import db
from sqlalchemy.ext.declarative import declared_attr


def get_id():
    return 2


class Base(db.Model):
    __abstract__ = True

    disabled = db.Column(db.Boolean, default=0)
    inserted_since = db.Column(db.DateTime, default=db.func.now())
    last_updated_since = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @declared_attr
    def inserted_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id_user'),
                         default=get_id())

    @declared_attr
    def last_updated_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id_user'),
                         default=get_id(), onupdate=get_id())


class File(Base):
    id_file = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    path = db.Column(db.String(255), unique=True)

    def __init__(self, name, description, path):
        self.name = name
        self.description = description
        self.path = path
