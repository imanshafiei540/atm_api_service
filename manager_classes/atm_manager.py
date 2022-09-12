from query_handlers.geometry_query_handler import GeometryQueryHandler
from query_handlers.atm_query_handler import ATMQueryHandler


class ATMManager:
    def __init__(self) -> None:
        pass

    def create_atm(self, atm_args, geometry_args):
        new_geometry = GeometryQueryHandler().insert(geometry_args=geometry_args)
        atm_args["geometry_id"] = new_geometry.get("id")
        new_atm = ATMQueryHandler().insert(atm_args=atm_args)