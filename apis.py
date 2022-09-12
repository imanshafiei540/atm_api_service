from app import app
from flask_restful import Api
from endpoints.atm_list import ATMListEndpoint


api = Api(app)

api.add_resource(ATMListEndpoint, "/atm/")