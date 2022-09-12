from app import db
from sqlalchemy.dialects.postgresql import ARRAY
from geoalchemy2 import Geometry


class BaseGeometry(db.Model):
    __tablename__ = "base_geometries"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    coordinates = db.Column(ARRAY(db.Float))
    geometry_coordinates = db.Column(Geometry(geometry_type="GEOMETRY", srid=4326))
    atm_device = db.relationship("ATMDevice", backref="base_geometries", uselist=False)
