from constants import GEOMETRY_POINT_TYPE


class GeometryManager:
    def __init__(self) -> None:
        pass

    def convert_list_to_geoalchemy_type(self, type, coordinates):
        if type == GEOMETRY_POINT_TYPE:
            return f"{GEOMETRY_POINT_TYPE}({' '.join([str(x) for x in coordinates])})"