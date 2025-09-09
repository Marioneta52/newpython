import os
import shutil


#Saber en que directorio me encuentro
print(os.getcwd())


#Crear archivo
archivo = open('curso.txt','w')
archivo.write('Texto Prueba')
archivo.close()

print(os.listdir())

#Shutil me permite mover
shutil.move('curso.txt','/home/elitebook/Escritorio')

#Eliminar archivos OS.UN elimina archivo de una ruta OS.RM elimina carpeta vacia
#shutil.rmt eliminar todo dentro de una ruta

send2trash.send2trash('curso.txt')

