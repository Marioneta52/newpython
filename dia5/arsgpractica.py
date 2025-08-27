#suma el cuadrado de una lista de argumentos
def suma_cuadrados(*args):
    suma = 0
    for n in args:
        suma = n**2 + suma
    return suma


#suma el absoluto
def suma_absolutos(*args):
    return sum(abs(num) for num in args)


def numeros_persona(nombre,*args):
    return (f"{nombre}, la suma de tus números es {sum(args)}")

print(numeros_persona('Emiro',1,4,6,54,3,5,676))
