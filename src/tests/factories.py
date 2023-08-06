import factory

from src.core.plateau import Plateau
from src.core.rover import Rover


class PlateauFactory(factory.Factory):
    class Meta:
        model = Plateau

    width = 5
    height = 5


class RoverFactory(factory.Factory):
    class Meta:
        model = Rover

    x = 1
    y = 2
    orientation = "N"
    plateau = factory.SubFactory(PlateauFactory)
