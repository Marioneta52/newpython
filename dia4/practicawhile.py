lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)

numero = 10
while numero >= 0:
    print(numero)
    numero -=1


#Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:
# Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)
# Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).
numero2 = 50
while numero2 >= 0:
        if numero2 % 5 == 0:
            print(numero2)
        numero2 -= 1