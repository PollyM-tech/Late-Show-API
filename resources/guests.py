from flask import jsonify
from flask_restful import Resource
from models import Guest

class GuestsResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests])