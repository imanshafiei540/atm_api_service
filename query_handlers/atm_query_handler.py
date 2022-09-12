from app import db
from models.atm_device import ATMDevice
from constants import GLOBAL_PAGINATION_PER_PAGE_NUMBER


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

    def find_all(self, page=1, per_page=GLOBAL_PAGINATION_PER_PAGE_NUMBER):
        pagination_object = ATMDevice.query.paginate(page=page, per_page=per_page)
        return {
            "has_next": pagination_object.has_next,
            "has_prev": pagination_object.has_prev,
            "results": [x.as_dict() for x in pagination_object.items],
        }
