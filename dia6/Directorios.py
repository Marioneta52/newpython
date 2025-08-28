#Nota import objeto os se utiliza principalmente en sistemas Windows para linux se utiliza Path
import os
ruta = os.chdir('/home/elitebook/Documentos')

archivo = open('PUNTACANA2.txt')

print(archivo.read())

#rutas en sistemas linux y mac
from pathlib import Path
carpeta = Path('/home/elitebook/Documentos')
archivo2 = carpeta / 'PUNTACANA2.txt'
mi_archivo = open(archivo2)
print(mi_archivo.read())