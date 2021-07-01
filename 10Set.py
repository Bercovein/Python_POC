# set
planetas = {"Marte", "Venus", "Jupiter"}
print(planetas)

# largo
print(len(planetas))

# revisar si un elemento esta presente
print('Marte' in planetas)

# agregar mas elementos
planetas.add('Tierra')
print(planetas)

# No soporta elementos duplicados
planetas.add('Tierra')
print(planetas)

# eliminar elemento, si no lo encuentra devuelve KeyError
planetas.remove('Tierra')
print(planetas)

planetas.discard('Tierras') # esta funcion no devuelve error
print(planetas)

# eliminar todos los elementos
planetas.clear()
print(planetas)
