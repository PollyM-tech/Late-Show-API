from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from resources import all_resources
from seed import seed_database
import os



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///lateshow.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    api = Api(app)
    for resource, endpoint in all_resources:
        api.add_resource(resource, endpoint)

    return app

if __name__ == '__main__':
    app = create_app()

    app.run(port=5555, debug=True)
