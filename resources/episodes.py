from flask import jsonify, make_response
from flask_restful import Resource
from models import Episode

class EpisodesResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return jsonify([episode.to_dict() for episode in episodes])

class EpisodeByIdResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return make_response(jsonify({"error": "Episode not found"})), 404
        return jsonify(episode.to_dict(only=('id', 'date', 'number', 'appearances')))