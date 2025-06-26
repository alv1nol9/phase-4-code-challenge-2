from server.models import db
from sqlalchemy import CheckConstraint

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    # Add table-level constraint for rating validation
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_between_1_and_5'),
    )

    # Relationship to Guest
    guest = db.relationship('Guest', back_populates='appearances')
    
    # Relationship to Episode
    episode = db.relationship('Episode', back_populates='appearances')

    def __repr__(self):
        return f'<Appearance {self.id} - Rating: {self.rating}>'
