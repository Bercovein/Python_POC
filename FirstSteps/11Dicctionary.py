# diccionario (key value)


diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)

# largo
print(len(diccionario))

# acceder a un elemento (key)
print(diccionario['IDE'])

# otra forma de recuperar un elemento
print(diccionario.get('OOP'))

# modificar elementos
diccionario['IDE'] = 'integrated development enviroment'

print(diccionario)

# recorrer elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# comprobar existencia de algun elemento
print('IDE' in diccionario)

# agregar elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento
diccionario.pop('DBMS')

# limpiar
diccionario.clear()
print(diccionario)

# eliminar diccionario
del diccionario
print(diccionario)


