#alojar archivo
mi_archivo =open('file01.txt')
#print(mi_archivo.read())

una_limea =  mi_archivo.readline()
print(una_limea.upper())

una_limea = mi_archivo.readline()
print(una_limea)

una_limea = mi_archivo.readline()
print(una_limea)

#loop con archivos
for l in mi_archivo:
    print(f'Aqui dice: ' + l.upper())

mi_archivo.close()