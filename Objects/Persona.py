# 'pass' se utiliza para clases o metodos vacios
import self as self


class Persona:
    # def __init__(self):  # double underscore = dunder
    #    self.nombre = 'Juan'
    #    self.apellido = 'Perez'
    #    self.edad = '28'

    def __init__(self, nombre, apellido, edad, *valores,
                 **terminos):  # podemos pasarle tuplas (*args) y diccionarios (**kwargs)
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._terminos = terminos  # underscore determina que el atributo es privado, aunque se puede acceder desde fuera pero es mala practica
        self.__valores = valores  # doble underscore, no se puede acceder desde fuera

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} Edad: {self.edad}')
        print(f'Tupla: {self.__valores}, Diccionario: {self._terminos}')

    @property  # decorador que hace que referenciemos este getter como si llamaramos a una variable
    def terminos(self):  # getter
        return self._terminos

    def valores(self):  # getter
        return self.__valores

    @terminos.setter # debe estar definido luego del getter, antes no reconoce el @terminos
    def terminos(self, **terminos):
        self.terminos = terminos


persona = Persona('Juan', 'Perez', 28, '12145124', 2, 3, 4, 5, m='manzana', p='pera')
persona.mostrar_detalle()

# modificar variables de un objeto
persona.nombre = 'Pepe'
persona.mostrar_detalle()

# mostrar_detalle es estatico por default
Persona.mostrar_detalle(persona)

# se puede acceder un nuevo atributo fuera de la clase, a nivel objeto
# el atributo no se reconoce en otros objetos hermanos, solo al modificado
persona.telefono = 123456789

# accediendo a getters
print(persona.valores())
# llamado diferente al anterior por la notacion @property
print(persona.terminos)
