from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from server.models import db

class Appearance(db.Model, SerializerMixin):
    __tablename__ = "appearances"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"))
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"))

    @validates("rating")
    def validate_rating(self, key, rating):
        if 1 <= rating <= 5:
            return rating
        raise ValueError("Rating must be between 1 and 5.")
