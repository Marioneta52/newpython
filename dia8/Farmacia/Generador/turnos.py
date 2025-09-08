def addtexto(funcion):

    def decorador(*args, **kwargs):
        print('Buenos días su turno es:')
        resultado = funcion(*args, **kwargs)
        print('Que tenga un buen día')
        return resultado
    return decorador

@addtexto
def generar_turno(tipo_turno):
        lista_turno = range(0,100)
        if tipo_turno == 'Medicamento':
            for n in lista_turno:
                yield n
        elif tipo_turno == 'Cosmetica':
            for n in lista_turno:
                yield n
        else:
            for n in lista_turno:
                yield n


turno = generar_turno('Cosmetica')
print(next(turno))
print(next(turno))
print(next(turno))
print(next(turno))
print(next(turno))
print(next(turno))
