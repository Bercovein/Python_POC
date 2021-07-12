from Persona import Persona

# puede ser utilizado para condicionar llamados
# muestra el nombre del modulo en donde se está trabajando
if __name__ == '__main__':
    print(__name__)

# destructor de pbjetos
print('Creación de objetos'.center(30, '-'))
persona1 = Persona('Ging', 'Freecss', 40)
persona1.mostrar_detalle()

print('Eliminación de objetos'.center(30, '-'))
# el garbage collector elinina las variables automaticamente, asi que no se suele utilizar
del persona1
