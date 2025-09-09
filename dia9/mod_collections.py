#Counter Permite contar repetidos de alguna coleccion
from collections import Counter, defaultdict, namedtuple

#contar numeros repetidos
numeros = [8,6,4,8,8,3,6,0,9,5,3,8,4,5,1,1,0,6,4]
print(Counter(numeros))
#Tambien puede contar letras repetidas
print(Counter('mississippi'))

#split permite contar palabras repetias
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))

#el metodo most_common permite mostrar el que mas se repite en este caso se pudo los 3 mas repetidos
serie = Counter([1,1,1,1,5,3,3,3,3,4,5,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,6,7,8,4,4,4,4,8,9,7,9,9,6,4,5,4,4,4])
print(serie.most_common(3))
##Castear un counter a lista
print(list(serie))

#defaultdict(lambda : 'nada') muestra nada si buscamos en un diccionario una clave que no existe
mi_dic = defaultdict(lambda : 'nada')
mi_dic ['uno'] ='verde'
print(mi_dic['ocho'])

# namedtuple puedo accede a la tupo por el nombre
mi_tupla =(500,18,65)
print(mi_tupla[1])

Persona = namedtuple('persona',['nombre','altura','peso'])
individuo = Persona('JhonDoe',1.76, 79)
print(individuo[0])
