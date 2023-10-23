from phobos.io.base import Representation
from phobos.io.smurf_reflection import SmurfBase


class CuttingPlane(Representation, SmurfBase):
    class_variables = {}
    type_dict = {}

    def __init__(self, **kwargs):
        SmurfBase.__init__(self, **kwargs)

    def __str__(self):
        return self.name
