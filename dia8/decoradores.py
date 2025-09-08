def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())

#otra forma de hacerlo seria se elimina el @decorar_saludo y
mayuscula_decorada = decorar_saludo(mayusculas)
mayuscula_decorada('Hola Mario')

# se incluye el @decorar saludo
#minusculas('Python')