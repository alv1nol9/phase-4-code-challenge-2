from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import Appearance, db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify({
            'id': appearance.id,
            'rating': appearance.rating,
            'guest_id': appearance.guest_id,
            'episode_id': appearance.episode_id
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except KeyError:
        return jsonify({'error': 'Missing required fields'}), 400
