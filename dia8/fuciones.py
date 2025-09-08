"""Se crea una funcion dentro de otra, funcion principal cambiar_letras dentro de esta se crean otras dos
funciones, mayuscula y minuscula se valida un parametro y se retorna segun la validacion"""

def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())


    def minuscula(texto):
        print(texto.lower())


    if tipo=="may":
        return mayuscula
    elif tipo=="min":
        return minuscula


operacion = cambiar_letras('min')
operacion('palabra')