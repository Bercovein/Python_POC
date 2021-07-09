# Valor dentro de un rango
valor = int(input('Escribe el valor: '))
valorMin = 0

valorMax = 5

dentroRango = (valor >= valorMin) and (valor <= valorMax)
print(f'El valor se encuentra entre 0 y 5? {dentroRango}')

# otra forma igual
dentroRango = valorMin <= valor <= valorMax

print(f'El valor se encuentra entre 0 y 5? {dentroRango}')


# Solicitar al usuario dos valores:

#  numero1 (int)

#  numero2 (int)

#  Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):

#  Proporciona el numero1:
# Proporciona el numero2:
# El numero mayor es:<numeroMayor>

num1 = int(input('Proporciona el numero1: '))
num2 = int(input('Proporciona el numero2: '))

mayor = 'El numero mayor es:'

if num1 < num2:
    print(f'{mayor} {num2}')
elif num1 > num2:
    print(f'{mayor} {num1}')
else:
    print(f'Los numeros {num1} y {num2} son iguales')


# Triple comilla:

print(f'''
    
    Nombre: Jorge
    Apellido: Sarasa

''')
