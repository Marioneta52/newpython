from random import randint
def lanzar_moneda():
    moneda = randint(0, 1)
    caramoneda = ''
    if moneda == 1:
         caramoneda = 'Cruz'
    else:
         caramoneda = 'Cara'
    return caramoneda

def probar_suerte(suerte, lista):
    if suerte == 'Cara':
        return []
        print("La lista se autodestruirá")
    else:
        print("La lista fue salvada")

    return  lista

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]