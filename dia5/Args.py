#Pasa N argumentos a una funcion

def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(3,4,5,4,3))

#simplificado
def sumatoria(*args):
    return sum(args)

print(sumatoria(3,4,5,4,3,300,343,234))

