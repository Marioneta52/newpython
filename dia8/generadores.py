"""Tipo especial de funcion, en vez de entregar un valor terminado lo genera poco a poco
ejemplo si pido una lista con los numeros del 1 al 5, no se generan de una para ahorrar memoria

Nota envez de decirle a la funcion que retorne con return lo cambiamos por yield"""

def mi_funcion():
    lista = []
    for x in range(1,10):
        lista.append(x * 10)
    return lista

def mi_generador():
    for x in range(1,10):
        yield x * 10

print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))




