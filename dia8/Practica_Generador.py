"""Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números,
iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next."""

def generador_num():
    num = 1
    while True:
        yield num
        num += 1




generador = generador_num()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))






