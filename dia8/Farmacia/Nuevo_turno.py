from turnos import generar_turno
import os

def inicio():

    while True:

        print("\n" + "=" * 30)
        print("       SISTEMA DE TURNOS")
        print("=" * 30)
        print("1. Medicamento")
        print("2. Cosmetica")
        print("3. Otros")
        print("4. Salir")
        print("=" * 30)

        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            os.system('cls')
        except ValueError:
            print("Error: Por favor ingrese un número válido")
            os.system('cls')
            continue

        match opcion:
            case 1:
                try:
                    nuevo_turno = generar_turno('Medicamento')
                    print(next(nuevo_turno))

                except ValueError:
                    print("Error: Error generando turno")

            case 2:
                try:
                    nuevo_turno = generar_turno('Cosmetica')
                    print(next(nuevo_turno))
                    print(next(nuevo_turno))
                except ValueError:
                    print("Error: Error generando turno")
            case 3:
                nuevo_turno = generar_turno('Otros')
                print(next(nuevo_turno))
                print(next(nuevo_turno))
            case 4:
                print("¡Gracias por usar Sistema de Turnos!")

                break

            case _:
                print("Opción no válida. Por favor seleccione 1, 2 , 3 o 4")

inicio()



