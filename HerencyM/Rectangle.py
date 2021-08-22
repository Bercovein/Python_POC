from HerencyM.Colour import Colour
from HerencyM.GeometricFigure import GeometricFigure


class Rectangle(GeometricFigure, Colour):
    def __init__(self, width, height, colour):
        GeometricFigure.__init__(self, width, height)
        Colour.__init__(self, colour)

    def calculate_area(self):
        return self.width * self.height

    def __str__(self):
        return f'{GeometricFigure.__str__(self)}, {Colour.__str__(self)}'