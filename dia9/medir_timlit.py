''' timeit mide el tiempo de ejecucion cuando el proceso se ejecuta muy rapido
'''

import timeit

declaracion ='''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista =[]
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, number=100000000)
print(duracion)

delaracion2 ='''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
    lista =[]
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion2 = timeit.timeit(declaracion, number=100000000)
print(duracion2)