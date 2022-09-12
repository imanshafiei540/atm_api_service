from flask_restful import reqparse
from constants import GEOMETRY_TYPE_CHOICES


class GeometryParser:
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        # TODO: Add a function could handle both POINT and POLYGON type
        self.parser.add_argument(
            "coordinates",
            type=float,
            action="append",
            nullable=False,
            location=("geometry",),
        )
        self.parser.add_argument(
            "type",
            type=str,
            trim=True,
            nullable=False,
            choices=GEOMETRY_TYPE_CHOICES,
            location=("geometry",),
        )
    
    def get_parser(self):
        return self.parser
