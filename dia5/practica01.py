def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return  False
        else:
            pass
    return True


lista_numeros = [1, 10, 58, 30, 48, 87]
print(todos_positivos(lista_numeros))