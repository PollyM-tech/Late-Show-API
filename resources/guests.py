from flask_restful import Resource
from flask import request
from models import db, Guest

class GuestsResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict() for guest in guests], 200

    def post(self):
        data = request.get_json()
        try:
            guest = Guest(
                name=data['name'],
                occupation=data['occupation']
            )
            db.session.add(guest)
            db.session.commit()
            return guest.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400


class GuestByIdResource(Resource):
    def get(self, id):
        guest = Guest.query.get(id)
        if not guest:
            return {'error': 'Guest not found'}, 404
        return guest.to_dict(), 200

    def patch(self, id):
        guest = Guest.query.get(id)
        if not guest:
            return {'error': 'Guest not found'}, 404
        data = request.get_json()
        guest.name = data.get('name', guest.name)
        guest.occupation = data.get('occupation', guest.occupation)
        db.session.commit()
        return guest.to_dict(), 200

    def delete(self, id):
        guest = Guest.query.get(id)
        if not guest:
            return {'error': 'Guest not found'}, 404
        db.session.delete(guest)
        db.session.commit()
        return {'message': 'Guest deleted'}, 200
