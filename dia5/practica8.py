'''Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.'''

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

lanzamiento = lanzar_moneda()

listas =probar_suerte(lanzamiento, lista_numeros)
print(listas)






