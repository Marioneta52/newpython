import os
import shutil
#Saber en que directorio me encuentro
print(os.getcwd())


#Crear archivo
archivo = open('curso.txt','w')
#archivo.write('Texto Prueba')
archivo.close()

print(os.listdir())

#Shutil me permite mover
#shutil.move('curso.txt','/home/elitebook/Escritorio')

#Eliminar archivos OS.UN elimina archivo de una ruta OS.RM elimina carpeta vacia
#shutil.rmt eliminar todo dentro de una ruta

ruta    ='/home/elitebook/Documentos/Python_Workspace/python/dia8'


for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta {ruta}')
    print(f'En la subdirs {subcarpeta}')
    for sub in  subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:

        if arch.startswith('Practica'):
            print(f'\t{arch}')
    print('/n')