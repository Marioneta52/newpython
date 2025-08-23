from random import * #importacion de librerias, nota el archivo no se puede llamar igual a la liqbreria

aleatorio = randint(1,50)
print(aleatorio)

#uniform Genera aleatorio con decimales, se utilizo round para eliminar decimales y solo dejar 1
aleatorio = round(uniform(1,5),1)
print(aleatorio)

#random genera un aleatorio, puede ser decimal o entero
aleatorio = random()
print(aleatorio)

#choice genera un aleatorio de la lista
colores =["azul","rojo","verde","morado","amarillo"]
aleatorio = choice(colores)
print(aleatorio)

#shuffle
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
