#metodo open puede recibir varios argumentos ('archivo.txt', r-w)
# 'r' solo lectura,
# 'w' si ya existe el archivo se vacia, si no lo crea
# 'a' Si el archivo no existe lo crea, de lo contrario se posiciona al final y guarda lo que ya existe
archivo = open('file02.txt','w')
lista=['Hola','Mundo','aqui','estoy']

for p in lista:
    archivo.write(p+ '\n')

archivo.close()

archivo = open('file02.txt', 'a')
lista = ['Hola', 'Mundo2', 'aqui', 'estoy']
for p in lista:
   archivo.write(p + '\n')

archivo.close()
