#enumerador
lista=['a','b','c','d','e','f']

for indice,item in enumerate(lista):
    print(indice,item)

#tuples y enumerate

mis_tuples = list(enumerate(lista))
print(mis_tuples)
