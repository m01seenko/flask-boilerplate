import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config_map

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    tier = os.environ.get("ENV", "development").lower()
    app.config.from_object(config_map[tier])
    app.config.from_pyfile("config.py", silent=True)

    db.init_app(app)
    migrate.init_app(app, db)

    return app
