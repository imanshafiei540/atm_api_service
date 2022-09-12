import imp
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

from models.atm_device import ATMDevice
from models.base_geometry import BaseGeometry
migrate = Migrate(app, db)

from apis import api
api.init_app(app)

if "__main__" == __name__:
    app.run()
