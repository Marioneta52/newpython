#metodo open puede recibir varios argumentos ('archivo.txt', r-w)
# 'r' solo lectura,
# 'w' si ya existe el archivo se vacia, si no lo crea
# 'a' Si el archivo no existe lo crea, de lo contrario se posiciona al final y guarda lo que ya existe

archivo = open('file01.txt','w')
archivo.write('soy el nuevo texto')
archivo.close()