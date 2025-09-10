import os
import shutil
import send2trash


#Saber en que directorio me encuentro
print(os.getcwd())


#Crear archivo
archivo = open('curso.txt','w')
archivo.write('Texto Prueba')
archivo.close()

print(os.listdir())

#Shutil me permite mover
shutil.move('curso.txt','C:\\Users\\003672661\\OneDrive - IBM\\Documents')

#Eliminar archivos OS.UN elimina archivo de una ruta OS.RM elimina carpeta vacia
#shutil.rmt

#Borra en la papelera de reciclaje
send2trash.send2trash('curso.txt')

