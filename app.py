from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///lateshow.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    
    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    api = Api(app)
    
    from resources.episodes import EpisodesResource, EpisodeByIdResource
    from resources.guests import GuestsResource
    from resources.appearances import AppearancesResource
    
    api.add_resource(EpisodesResource, '/episodes')
    api.add_resource(EpisodeByIdResource, '/episodes/<int:id>')
    api.add_resource(GuestsResource, '/guests')
    api.add_resource(AppearancesResource, '/appearances')
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555, debug=True)