#Asignacion
myVariable = 10

#Reasignacion
myVariable = myVariable + 1
#Igual forma pero reducido (funciona para el resto de los operadores ya vistos)
myVariable += 1

#Operadores de comparacion
a = 4
b = 3

# Igualdad: ==
resultado = a == b

# Desigualdad: !=
resultado = a != b

# Mayor / Menor:  < >
resultado = a < b

# Mayor  / Menor o igual:  <=  >=
resultado = a <= b


# Verificar si es par o impar

numero = int(input('Por favor ingrese un numero: '))

if numero % 2 == 0:
    print(f'{numero} es un numero par')
else:
    print(f'{numero} es un numero impar')
