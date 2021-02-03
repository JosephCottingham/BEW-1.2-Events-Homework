"""Create database models to represent tables."""
import enum
from events_app import db
from sqlalchemy.orm import backref


class Guest(db.Model):

    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone = db.Column(db.String(12))
    events_attending = db.relationship('Event', back_populates="guests", secondary='guest_event_table')



class EVENT_TYPE_ENUM(enum.Enum):
    Party = 0
    Study = 1
    Networking = 2   
    etc = 3  

class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(64))
    date_and_time = db.Column(db.DateTime())
    event_type = db.Column(db.Enum(EVENT_TYPE_ENUM))
    guests = db.relationship('Guest', back_populates="events_attending", secondary='guest_event_table')

class guest_event_table(db.Model):

    __tablename__ = 'guest_event_table'

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), primary_key=True)
