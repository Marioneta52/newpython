from collections import *
import send2trash

mi_diccionario = defaultdict(lambda : "Valor no hallado")
mi_diccionario ['edad'] = '44'



# Crear la deque con los elementos iniciales
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

print("Deque inicial:")
print(lista_ciudades)
# Output: deque(['Londres', 'Berlin', 'París', 'Madrid', 'Roma', 'Moscú'])