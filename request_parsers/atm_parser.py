from flask_restful import reqparse


class ATMRequestParser:
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("address", type=str, trim=True, nullable=False)
        self.parser.add_argument("provider", type=str, trim=True, nullable=False)
        self.parser.add_argument("geometry", type=dict, nullable=False)
    
    def get_parser(self):
        return self.parser
