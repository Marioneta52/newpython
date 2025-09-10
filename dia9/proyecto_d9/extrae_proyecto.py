'''Modulo para extraer el contenido del proyecto'''
import zipfile

def descomprimir():
    proyecto = zipfile.ZipFile('C:\\Workspace\\newpython\\PythonDoc\\dia9\\Proyecto+Dia+9.zip','r')
    proyecto.extractall()
    abrir_instrucciones()


def abrir_instrucciones():
    print(open('instrucciones.txt').read())

descomprimir()

