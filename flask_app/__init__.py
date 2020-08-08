import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config_map
from .routes.root import root_blueprint
from .routes.admin import admin_blueprint

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    tier = os.environ.get("ENV", "development").lower()
    app.config.from_object(config_map[tier])
    app.config.from_pyfile("config.py", silent=True)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(root_blueprint)
    app.register_blueprint(admin_blueprint)

    return app
