'''Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.
Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].'''
def reducir_lista(lista):
    """
    Reduce una lista eliminando duplicados y el valor más alto.
    """
    lista_unica = list(set(lista))
    if lista_unica:
        lista_unica.remove(max(lista_unica))
    return lista_unica

# Variable lista_numeros
lista_numeros = [1, 2, 15, 7, 2]


def promedio(lista):
    return sum(lista) / len(lista)

# Probando la función
print(reducir_lista(lista_numeros))  # Output: [1, 2, 7]
