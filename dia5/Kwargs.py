# **kwargs recibe elementos de forma de diccionarios
def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave}  = {valor}')
        total += valor
suma(x=3,y=4,z=5)


def prueba(num1,num2,*args,**kwargs):
    print(f'el primer valor es: {num1}')
    print(f'el primer valor es: {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave}  = {valor}')

args = [234,3,234,2,23,342,345,654]
kwargs = {'x':'uno','y':'dos'}
prueba(10,24,*args,**kwargs )