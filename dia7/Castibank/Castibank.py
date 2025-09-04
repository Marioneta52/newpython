class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, cuenta, saldo):
        self.cuenta = cuenta
        self.saldo = saldo

    def __str__(self):
        return f'Cliente: {self.cuenta} con saldo: {self.saldo}'

class Consignar(Cliente):
    def __init__(self, cuenta, saldo, nombre):
        self.cuenta = cuenta
        self.saldo = saldo
        self.nombre = nombre

        Saldo_Cliente =  self.saldo
        self.saldo = Saldo_Cliente + self.saldo


    def __str__(self):
        return f'Cliente: {self.nombre} consigno: {self.saldo} actualmente tiene un saldo de: {self.saldo + self.saldo} '

nombre = input('Bienvenido a CastiBank: Ingrese su nombre para iniciar:')
print(f'Buenos días {nombre} ingrese una opcion para iniciar')
opcion = int(input('Opción 1: Consignar \nOpción 2: Consignar \nOpción 3:Salir \n'))

saldo = 0

while True:
    print("\n" + "=" * 30)
    print("       SISTEMA BANCARIO")
    print("=" * 30)
    print(f"Saldo actual: ${saldo:,.2f}")
    print("1. Consignar")
    print("2. Retirar")
    print("3. Salir")
    print("=" * 30)

    try:
        opcion = int(input("Seleccione una opción (1-3): "))
    except ValueError:
        print("Error: Por favor ingrese un número válido")
        continue

    match opcion:
        case 1:
            try:
                monto = float(input("Ingrese el monto a consignar: $"))
                if monto <= 0:
                    print("Error: El monto debe ser mayor a cero")
                else:
                    saldo += monto
                    print(f"✅ Consignación exitosa. Nuevo saldo: ${saldo:,.2f}")
            except ValueError:
                print("Error: Ingrese un monto válido")

        case 2:
            try:
                monto = float(input("Ingrese el monto a retirar: $"))
                if monto <= 0:
                    print("Error: El monto debe ser mayor a cero")
                elif monto > saldo:
                    print("❌ Fondos insuficientes")
                else:
                    saldo -= monto
                    print(f"✅ Retiro exitoso. Nuevo saldo: ${saldo:,.2f}")
            except ValueError:
                print("Error: Ingrese un monto válido")

        case 3:
            print("¡Gracias por usar nuestro sistema bancario!")
            print(f"Saldo final: ${saldo:,.2f}")
            break

        case _:
            print("Opción no válida. Por favor seleccione 1, 2 o 3")

cliente1 = Cliente(cuenta='Cliente1', saldo=1000)
consignar = Consignar(cuenta=19293847, saldo=1000, nombre= 'Emilio')

print(consignar)