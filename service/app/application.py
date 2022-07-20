import flask
from service.app.swagger import api
from service.api.models.base import db, migrate
from service.api.handlers.user import api_service


def create_app():
    app = flask.Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    api.add_namespace(api_service)

    return app

