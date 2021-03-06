# 'pass' se utiliza para clases o metodos vacios
import self as self


class Persona:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} Edad: {self.edad}')

    @property
    def nombre(self):  # getter
        return self._nombre

    @property
    def apellido(self):  # getter
        return self._apellido

    @property
    def edad(self):  # getter
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')