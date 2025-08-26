'''Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.'''
def cantidad_pares(lista):
    par =0
    for n in lista:
        if n % 2 ==0:
            par +=1
    return par

lista  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(cantidad_pares(lista))