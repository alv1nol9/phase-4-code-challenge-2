from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import Episode, Appearance, db

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number
    } for episode in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [{
        'id': app.id,
        'rating': app.rating,
        'guest': {
            'id': app.guest.id,
            'name': app.guest.name,
            'occupation': app.guest.occupation
        }
    } for app in episode.appearances]

    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': appearances
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted successfully'}), 200

