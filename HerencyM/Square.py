from GeometricFigure import GeometricFigure
from Colour import Colour

class Square(GeometricFigure, Colour): ## Herencia multiple, importa el orden
    def __init__(self, side, colour):
        #super().__init__(colour) no se utiliza porque genera confusion
        # como hereda de mas de una clase, depende de la cantidad de parametros
        # elige un constructor u otro
        GeometricFigure.__init__(self, side, side)
        Colour.__init__(self, colour)

    def calculate_area(self):
        return self._width * self._height

    def __str__(self):
        return f'{GeometricFigure.__str__(self)}, {Colour.__str__(self)}'