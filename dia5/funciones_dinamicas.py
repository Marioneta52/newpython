#Funcion valida si un numero de la lista tiene 3 cifras
def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras


resultado = chequear_3_cifras([10,90,340,987])
print(resultado)

