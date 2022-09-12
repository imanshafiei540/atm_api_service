import os


class Config:
    DEBUG = os.environ.get("DEBUG", True)
    FLASK_APP = os.environ.get("FLASK_APP")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
