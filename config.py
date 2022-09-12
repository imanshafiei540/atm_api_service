import os


class Config:
    DEBUG = os.environ.get("DEBUG", True)
    FLASK_APP = os.environ.get("FLASK_APP")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_TRACK_MODIFICATIONS set to false because of flask_migrate alert message
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
