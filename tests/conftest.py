import pytest
from flask import Flask
from flask_app import create_app, db


@pytest.fixture(scope="function")
def app() -> Flask:
    app = create_app()
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
