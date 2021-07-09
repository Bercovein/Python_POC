def listarTerminos(**kwargs):  # kwargs: keyword arguments
    for llave, valor in kwargs.items():
        print(f'{llave}, {valor}')

listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Tomas', 'Lucas', 'Seba','Ailu']

desplegarNombres(nombres)
desplegarNombres('Carlos') # Lo toma como string, no funciona con otro tipo de variable



