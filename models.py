from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)
    
    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')
    
    serialize_rules = ('-appearances.episode',)

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')
    
    serialize_rules = ('-appearances.guest',)

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    
    __table_args__ = (
        db.CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )
    
    serialize_rules = ('-episode.appearances', '-guest.appearances')
    
    @validates('rating')
    def validate_rating(self, key, rating):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating