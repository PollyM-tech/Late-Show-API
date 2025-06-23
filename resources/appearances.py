from flask_restful import Resource
from flask import request
from models import db, Appearance, Episode, Guest
from sqlalchemy.exc import IntegrityError

class AppearancesResource(Resource):
    def post(self):
        data = request.get_json()

        required = ['rating', 'episode_id', 'guest_id']
        if not all(field in data for field in required):
            return {'errors': ['Missing required fields']}, 400

        episode = Episode.query.get(data['episode_id'])
        guest = Guest.query.get(data['guest_id'])

        if not episode:
            return {'errors': ['Episode not found']}, 404
        if not guest:
            return {'errors': ['Guest not found']}, 404

        try:
            appearance = Appearance(
                rating=data['rating'],
                episode_id=data['episode_id'],
                guest_id=data['guest_id']
            )
            db.session.add(appearance)
            db.session.commit()
            return appearance.to_dict(), 201

        except ValueError as e:
            return {'errors': [str(e)]}, 422
        except IntegrityError:
            db.session.rollback()
            return {'errors': ['Database integrity error']}, 400
        except Exception:
            db.session.rollback()
            return {'errors': ['Internal server error']}, 500


class AppearanceByIdResource(Resource):
    def get(self, id):
        appearance = Appearance.query.get(id)
        if not appearance:
            return {'error': 'Appearance not found'}, 404
        return appearance.to_dict(), 200

    def patch(self, id):
        appearance = Appearance.query.get(id)
        if not appearance:
            return {'error': 'Appearance not found'}, 404

        data = request.get_json()
        rating = data.get('rating')

        if rating is not None:
            try:
                appearance.rating = rating
                db.session.commit()
            except ValueError as e:
                return {'errors': [str(e)]}, 422

        return appearance.to_dict(), 200

    def delete(self, id):
        appearance = Appearance.query.get(id)
        if not appearance:
            return {'error': 'Appearance not found'}, 404
        db.session.delete(appearance)
        db.session.commit()
        return {'message': 'Appearance deleted'}, 200
