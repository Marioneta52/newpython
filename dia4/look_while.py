#rango no incluye el 5
lista = list(range(10,1001))
print(lista)
for numero in range(5):
        print(numero)
#
monedas = 5
while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas -= 1
else:print("No tengo más monedas")


respuesta = 's'
while respuesta == 's':
    respuesta= input("Ingresa una respuesta (s/n)")
else:
    print('Gracias')

#pass
respuesta2 = 'n'
while respuesta2 == 's':
    pass
print('Gracias2')


#break - continiu
nombre = input("Ingresa una nombre")
for letra in nombre:
    if letra == 'a':
        print(letra)
        break


