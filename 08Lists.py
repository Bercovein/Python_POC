condicion = True

while condicion:
    print('Ejecutando ciclo')
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
