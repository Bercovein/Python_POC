# Crear una función para sumar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parámetro de la función y
# regresar como resultado la suma de todos los valores pasados como argumentos.

def sumarTodo(*sumandos:int):
    resultado = 0
    for sumando in sumandos:
        resultado += sumando
    return resultado

# Crear una función para multiplicar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parámetro de la función y
# regresar como resultado la multiplicación de todos los valores pasados como argumentos.

def multiplicarTodo(*multiplicandos:int):
    resultado = 1
    for multiplicando in multiplicandos:
        resultado *= multiplicando
    return resultado