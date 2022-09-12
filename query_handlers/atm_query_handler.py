from app import db, ATMDevice


class ATMQueryHandler:
    def __init__(self) -> None:
        pass

    def insert(self, *args, **kwargs):
        address = kwargs.get("atm_args").get("address")
        provider = kwargs.get("atm_args").get("provider")
        geometry_id = kwargs.get("atm_args").get("geometry_id")

        new_atm = ATMDevice(address=address, provider=provider, geometry_id=geometry_id)
        db.session.add(new_atm)
        db.session.commit()
        
        return new_atm.as_dict()