# 'pass' se utiliza para clases o metodos vacios
class Persona:
    # def __init__(self):  # double underscore = dunder
    #    self.nombre = 'Juan'
    #    self.apellido = 'Perez'
    #    self.edad = '28'

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona = Persona('Juan', 'Perez', 28)
print(persona.nombre, persona.apellido)

# modificar variables de un objeto
persona.nombre = 'Pepe'
print(persona.nombre, persona.apellido)




