from app import db


class ATMDevice(db.Model):
    __tablename__ = "atm_devices"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(450))
    provider = db.Column(db.String(50))
    geometry_id = db.Column(db.Integer, db.ForeignKey("base_geometries.id"))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}