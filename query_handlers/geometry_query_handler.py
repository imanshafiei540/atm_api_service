from app import db
from models.base_geometry import BaseGeometry
from manager_classes.geometry_manager import GeometryManager


class GeometryQueryHandler:
    def __init__(self) -> None:
        pass

    def insert(self, *args, **kwargs):
        coordinates = kwargs.get("geometry_args").get("coordinates")
        type = kwargs.get("geometry_args").get("type")
        new_geometry = BaseGeometry(
            type=type,
            coordinates=coordinates,
            geometry_coordinates=GeometryManager().convert_list_to_geoalchemy_type(
                type, coordinates
            ),
        )
        db.session.add(new_geometry)
        db.session.commit()

        return new_geometry.as_dict()
    
    def find_one(self, id):
        return BaseGeometry.query.filter_by(id=id).one().as_dict()
