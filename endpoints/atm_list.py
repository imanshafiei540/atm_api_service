from flask_restful import Resource
from request_parsers.atm_parser import ATMRequestParser, ATMListParser
from request_parsers.geometry_parser import GeometryParser
from manager_classes.atm_manager import ATMManager
from constants import HTTP_STATUS_CREATED


atm_parser = ATMRequestParser().get_parser()
geometry_parser = GeometryParser().get_parser()
atm_list_parser = ATMListParser().get_parser()


class ATMListEndpoint(Resource):
    def get(self):
        atm_list_args = atm_list_parser.parse_args()
        all_atm_devices = ATMManager().find_all(page=atm_list_args.get("page", 1))
        return all_atm_devices

    def post(self):
        atm_args = atm_parser.parse_args()
        geometry_args = geometry_parser.parse_args(req=atm_args)
        new_atm = ATMManager().create_atm(atm_args, geometry_args)
        return new_atm, HTTP_STATUS_CREATED
