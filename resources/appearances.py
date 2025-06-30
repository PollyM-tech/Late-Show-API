from flask import request, jsonify, make_response
from flask_restful import Resource
from models import db, Appearance
from sqlalchemy.exc import IntegrityError

class AppearancesResource(Resource):
    def post(self):
        data = request.get_json()
        try:
            appearance = Appearance(
                rating=data['rating'],
                episode_id=data['episode_id'],
                guest_id=data['guest_id']
            )
            db.session.add(appearance)
            db.session.commit()
            return jsonify(appearance.to_dict())
        except (IntegrityError, ValueError) as e:
            db.session.rollback()
            return make_response(jsonify({"errors": ["validation errors"]}), 400)