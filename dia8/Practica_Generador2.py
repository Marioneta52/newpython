"""Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7,
iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...)"""

def generador_multiplos():
    num = 0
    while True:
        num += 7
        yield num

generador = generador_multiplos()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


