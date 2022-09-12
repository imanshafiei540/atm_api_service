from app import db


class ATMDevice(db.Model):
    __tablename__ = 'atm_devices'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(450))
    provider = db.Column(db.String(50))