from HerencyM.Rectangle import Rectangle
from Square import Square

print('Creación Objeto Cuadrado'.center(50, '-'))
square1 = Square(side=5, colour='rojo')

print(f'Cálculo area cuadrado: {square1.calculate_area()}')

# MRO - Method Resolution Order
print(Square.mro()) # muestra el orden en el que se accede a las clases

print(square1)

print('Creación Objeto Rectangulo'.center(50, '-'))
rectangle1 = Rectangle(width=3, height=8, colour='Verde')

print(rectangle1.calculate_area())

print(Square.mro())