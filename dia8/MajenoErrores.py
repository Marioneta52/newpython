def suma():
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))

    print("El resultado es: ", num1 + num2)
    print("Gracias por sumar" + num2)




try:
    suma()

except TypeError:
    print("Esta intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    print("Todo OK")
finally:
    print("Eso Fue Todo")


def pedir_numero():
     while True:
         try:
             numero = int(input("Ingresa un numero: "))
         except:
             print("Ese no es un numero")
         else:
             print(f"El resultado es: {numero}")
             break
     print("Gracias")

pedir_numero()
