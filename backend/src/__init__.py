from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.rest_api.routes import api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


def create_app():
    db.init_app(app)
    app.app_context().push()

    with app.app_context():
        db.create_all()

    app.register_blueprint(api)
    return app
