archivo = open('mi_archivo.txt', 'w')
archivo.write("Nuevo texto")

archivo.close()

archivo = open('mi_archivo.txt', 'r')
linea = archivo.readline()
print(linea)


'''Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar. '''
archivo = open('file02.txt','a')
archivo.write('\n''Nuevo inicio de sesión')
archivo = open('file02.txt','r')
print(archivo.read())
archivo.close
