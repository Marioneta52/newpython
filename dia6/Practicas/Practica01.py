'''Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).'''
def abrir_leer(archivo):
    archivo = open(archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

print(abrir_leer('abrir_leer.txt'))
