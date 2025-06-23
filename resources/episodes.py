from flask_restful import Resource
from flask import request
from models import db, Episode

class EpisodesResource(Resource):
    def get(self):
        episodes = Episode.query.order_by(Episode.number).all()
        return [episode.to_dict() for episode in episodes], 200

    def post(self):
        data = request.get_json()
        try:
            episode = Episode(
                date=data['date'],
                number=data['number']
            )
            db.session.add(episode)
            db.session.commit()
            return episode.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400


class EpisodeByIdResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {'error': 'Episode not found'}, 404
        return episode.to_dict_with_appearances(), 200

    def patch(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {'error': 'Episode not found'}, 404
        data = request.get_json()
        episode.date = data.get('date', episode.date)
        episode.number = data.get('number', episode.number)
        db.session.commit()
        return episode.to_dict(), 200

    def delete(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {'error': 'Episode not found'}, 404
        db.session.delete(episode)
        db.session.commit()
        return {'message': 'Episode deleted'}, 200
