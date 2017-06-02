from app import db
from sqlalchemy.ext.declarative import declared_attr
from app.cache import get_current_user



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


class File(Base):
    id_file = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    path = db.Column(db.String(255), unique=True)

    def __init__(self, name, description, path):
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