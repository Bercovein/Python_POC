condicion = True

while condicion:
    print('Ejecutando ciclo')
    condicion = False
else:
    print('Fin de ciclo')

cadena = 'hola'

for letra in cadena:
    print(letra)
    if letra == 'a':
        break
else:
    print('Fin ciclo for')

# imprimir solo nros pares
# continue interrumple la interacion y avanza a la siguiente
for i in range(10):
    if i % 2 == 0:
        continue
    print(f'Valor: {i}')

# Listas
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']

print(nombres[2])  # Ricardo
print(nombres[-1])  # Maria, accede de forma inversa
print(nombres[0:2])  # 0 y 1, sin contemplar la pocision 2
print(nombres[:2])  # lo mismo pero desde el principio
print(nombres[0:])  # lo mismo pero  hasta el final

#size de una lista
print(len(nombres))

#agregar elemento
nombres.append('Jorge')
print(nombres)

#insertar elemento en indice especifico
nombres.insert(1,'Hernan')
print(nombres)

#remove elemento
nombres.remove('Hernan')
print(nombres)

#remover ultimo valor agregado
nombres.pop()
print(nombres)

#eliminar en un indice indicado
del nombres[0]
print(nombres)

#limiar la lista completa
nombres.clear()
print(nombres)

#borrar lista por completo
del nombres
# print(nombres)

#iterar rango de 0 a 10 e imprimir solo los numeros divisibles por 3
for i in range(10):
    if(i % 3 == 0):
        print(i)
