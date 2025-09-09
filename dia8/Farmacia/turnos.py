def addtexto(funcion):

    def decorador(*args, **kwargs):
        print('Buenos días su turno es:')
        resultado = funcion(*args, **kwargs)
        return resultado
    return decorador


def generar_turno(tipo_turno):
        lista_turno = range(0,100)
        while True:
            if tipo_turno == 'Medicamento':
                for n in lista_turno:
                    yield f"M - {n}"
            elif tipo_turno == 'Cosmetica':
                for n in lista_turno:
                    yield f"C - {n}"
            else:
                for n in lista_turno:
                    yield f"P - {n}"



