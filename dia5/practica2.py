'''Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.'''

def suma_menores(lista):
    suma = 0
    for n in lista:
        if n in range(0,1001):
            suma = suma + n
    return suma

lista_numeros= [10,20,84,-58,-18]
print(suma_menores(lista_numeros))