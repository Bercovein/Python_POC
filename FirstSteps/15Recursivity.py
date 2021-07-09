# funcion recursiva, ejemplo con factorial

def factorial(numero):
    if numero == 1:
        return 1
    return numero * factorial(numero - 1)


print('Factorial de 5:', factorial(5))


# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
# Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
# 5 4 3 2 1
# Si se pasa el valor de 3, debe imprimir:
# 3 2 1
# Si se pasan valores negativos no imprime nada

def printNumeros(numero):

    if numero >= 1:
        print(numero)
        printNumeros(numero - 1)


printNumeros(5)
printNumeros(1)
printNumeros(-5)
