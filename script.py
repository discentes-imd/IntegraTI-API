from app.mod_events.models import *
from app import db

me = User('rodrigo', 'rodrigondec@gmail.com', '1', '2', '3', None, None, None)

db.session.add(me)
db.session.commit()