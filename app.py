from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from apis import api
api.init_app(app)

# Run the server with flask run command and not python app.py
# TODO: Fix circular import error when running python app.py command
if "__main__" == __name__:
    app.run()
