"""Permite comprimir archivos"""
import zipfile
import shutil

#comprimir con zipfile
def comprimir():
    mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')
    mi_zip.write('mi_texto_A.txt')
    mi_zip.write('mi_texto_B.txt')
    mi_zip.close()

def descomprimir():
    zip_open = zipfile.ZipFile('archivo_comprimido.zip','r')
    zip_open.extractall()

#Tambien se puede comprimir utilizando shutil
def shutil_zip():
    carpeta_origen = '/home/elitebook/Documentos/mi_archivo'
    archivo_destino = 'todo_comprimido2'
    shutil.make_archive(archivo_destino,'zip', carpeta_origen)

#Otra forma de comprimir

#comprimir()
#descomprimir()
shutil_zip()

