#ABC = Abstract Base Class
from abc import ABC, abstractmethod

class GeometricFigure(ABC): # clase abstracta
    def __init__(self, height, width):
        if self._validate_value(width): #Validacion de variables
            self._width = width
        else:
            self._width = 0
        if self._validate_value(height):
            self._height = height
        else:
            self._height = 0

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        if self._validate_value(width):
            self._width = width

    @height.setter
    def height(self, height):
        if self._validate_value(height):
            self._height = height

    def __str__(self):
        return f'Geometric Figure: [Width: {self._width}, Height: {self._height}]'

    def _validate_value(self, value):
        return True if 0 < value < 10 else False

    @abstractmethod
    def calculate_area(self):
        pass