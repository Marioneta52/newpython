numero = int(input("Ingresa un numero: "))
match numero:
    case n if numero %2 == 0:
        print("El numero es par")
    case n if numero % 2 == 1:
        print("El numero es impar")