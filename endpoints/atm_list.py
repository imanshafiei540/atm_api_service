from flask_restful import Resource
from request_parsers.atm_parser import ATMRequestParser
from request_parsers.geometry_parser import GeometryParser
from manager_classes.atm_manager import ATMManager
from constants import HTTP_STATUS_CREATED


atm_parser = ATMRequestParser().get_parser()
geometry_parser = GeometryParser().get_parser()
class ATMListEndpoint(Resource):
    def get(self):
        pass
    
    def post(self):
        atm_args = atm_parser.parse_args()
        geometry_args = geometry_parser.parse_args(req=atm_args)
        new_atm = ATMManager().create_atm(atm_args, geometry_args)

        return new_atm, HTTP_STATUS_CREATED