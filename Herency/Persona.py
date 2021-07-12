# 'pass' se utiliza para clases o metodos vacios
import self as self


class Persona:

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} Edad: {self.edad}')

    @property
    def nombre(self):  # getter
        return self._nombre

    @property
    def edad(self):  # getter
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # def __del__(self):
    #    print(f'Persona: {self._nombre}')

    def __str__(self):
        return f'Persona: {self.nombre} {self.edad}'