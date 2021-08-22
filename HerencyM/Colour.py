class Colour :
    def __init__(self, colour):
        self._colour = colour

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour):
        self._colour = colour

    def __str__(self):
        return f'Colour: [Colour: {self._colour}]'

