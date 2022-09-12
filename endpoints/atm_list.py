from flask_restful import Resource
from request_parsers.atm_parser import ATMRequestParser
from request_parsers.geometry_parser import GeometryParser


atm_parser = ATMRequestParser().get_parser()
geometry_parser = GeometryParser().get_parser()
class ATMListEndpoint(Resource):
    def get(self):
        pass
    
    def post(self):
        atm_args = atm_parser.parse_args()
        geometry_args = atm_parser.parse_args(req=atm_args)
        