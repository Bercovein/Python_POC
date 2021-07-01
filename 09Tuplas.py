# una tupla es inmutable, no se puede modificar

# definir tupla
# (si tiene un solo elemento debe declararse: frutas = ('Naranja',)
frutas = ('Naranja','Banana','Manzana')

print(len(frutas))

print(frutas)

# acceder a un elemento
print(frutas[1])

# navegacion inversa
print(frutas[-1])

# acceder a un rango de valores
print(frutas[0:1]) # sin incluir el ultimo indice

# recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')

# cambiar valor de tupla
# no se puede de esta forma: frutas[0] = 'Anana'
frutaLista = list(frutas)
frutaLista [0] = 'Anana'
frutas = tuple(frutaLista)
print('\n',frutas)


# Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for:

tupla = (13, 1, 8, 3, 2, 5, 8)

list = []
for t in tupla:
    if t < 5:
        list.append(t)
print(list)