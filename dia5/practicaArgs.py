def cantidad_atributos(**kwargs):
    cantidad = 1
    for clave, valor in kwargs.items():

        print(f'clave {clave} ,valor {valor} cantidad: {cantidad}')
        cantidad += 1
    return clave

kwargs = {'a':'Fiesta','b':'camaro'}
cantidad_atributos(**kwargs)