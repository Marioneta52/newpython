palabra = 'python'
lista = []
for letra in palabra:
        lista.append(letra)
print(lista)

#aplicando mejoras a la lista
lista = [letra for letra in palabra]
print(lista)

#if en lista mejorada
lista = [n if n * 2 > 10 else 'no' for n in  range(0,21,2) ]
print(lista)

pies = [10,20,30,40,50]
metros = [p* 3.281 for p in pies]
print(metros)