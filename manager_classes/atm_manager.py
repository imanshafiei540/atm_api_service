from query_handlers.geometry_query_handler import GeometryQueryHandler
from query_handlers.atm_query_handler import ATMQueryHandler


class ATMManager:
    def __init__(self) -> None:
        pass

    def create_atm(self, atm_args, geometry_args):
        new_geometry = GeometryQueryHandler().insert(geometry_args=geometry_args)
        atm_args["geometry_id"] = new_geometry.get("id")
        new_atm = ATMQueryHandler().insert(atm_args=atm_args)
        new_atm["geometry"] = new_geometry
        del new_atm["geometry"]["geometry_coordinates"]
        del new_atm["geometry_id"]
        return new_atm

    def find_all(self, *args, **kwargs):
        all_atm_devices = ATMQueryHandler().find_all(page=kwargs.get("page"))
        for item in all_atm_devices["results"]:
            item["geometry"] = GeometryQueryHandler().find_one(item.get("geometry_id"))
            del item["geometry"]["geometry_coordinates"]
            del item["geometry_id"]
        return all_atm_devices
