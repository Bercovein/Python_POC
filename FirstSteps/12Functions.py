###########################################
# Funciones

def miFuncion():
    print('Saludos')


miFuncion()


# con parametros
def miOtraFuncion(nombre, apellido):
    print('Saludos de nuevo, soy', nombre, apellido)


miOtraFuncion('Jose', 'Luis')


def sumar(a, b):
    return a + b


resultado = sumar(5, 3)

print(f'Resultado de la suma: {resultado}')


# parametros por default y referencia al tipo de dato que devuelve -> int
# def restar ( a:int = 0, b:int = 0) -> int:
def restar(a=0, b=0) -> int:
    return a - b


print(f'Resultado de resta: {restar()}')


# argumentos variables
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Tomy', 'Seba', 'Chris', 'Lucas')












