import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///:memory:")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config_map = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
