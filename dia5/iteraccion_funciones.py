#Juego encuentra el palito
from random import shuffle

#Crear lista inicial
palitos = ['-','--','---','----']

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedir intento
def probar_suerte():
    intento=''
    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')
    return int(intento)

#Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento -1] == '-':
        print('Has peridod')
    else:
        print('Esta vez te has salvado')

    print(f"Te ha tocado{lista[intento -1]}")

palitos_mezclado = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclado,seleccion)