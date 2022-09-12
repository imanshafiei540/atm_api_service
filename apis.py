from flask_restful import Api
from endpoints.atm_list import ATMListEndpoint


api = Api()
api.add_resource(ATMListEndpoint, "/atm/")