import os
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, cuenta, saldo):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.saldo = saldo

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido} \nBalance de Cuenta  {self.cuenta}\nSaldo Disponible ${(self.saldo)}'

class Consignar(Cliente):
    def deposito(self,cuenta, saldo, saldo_actual ):
        self.cuenta = cuenta
        self.saldo = saldo
        self.saldoactual = saldo_actual
        return self.saldoactual + self.saldo

    def sacar(self,cuenta, saldo, saldo_actual):
        self.cuenta = cuenta
        self.saldo = saldo
        self.saldoactual = saldo_actual

        return self.saldoactual - self.saldo


def inicio():
    nomcli = input('Bienvenido a CastiBank:\nIngrese su Nombre:')
    apecli = input('Ingrese su Apellido:')
    cuenta = int(input("Ingrese una cuenta Bancaria: "))
    print(f'Buenos días {nomcli} {apecli} ingrese una opcion para iniciar')
    saldo = 0

    while True:

        print("\n" + "=" * 30)
        print("       SISTEMA BANCARIO")
        print("=" * 30)
        print(f"Su cuenta {cuenta} tiene un Saldo actual: ${saldo:,.2f}")
        print("1. Consignar")
        print("2. Retirar")
        print("3. Balance")
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
                    monto = float(input("Ingrese el monto a consignar: $"))
                    if monto <= 0:
                        print("Error: El monto debe ser mayor a cero")
                    else:
                        # saldo += monto
                        consignacion = Consignar(nomcli,apecli,cuenta, monto)
                        saldo = consignacion.deposito(cuenta, monto, saldo)
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
                        # saldo -= monto
                        Retiro = Consignar(nomcli,apecli,cuenta, monto)
                        saldo = Retiro.sacar(cuenta, monto, saldo)
                        print(f"✅ Retiro exitoso. Nuevo saldo: ${saldo:,.2f}")
                except ValueError:
                    print("Error: Ingrese un monto válido")
            case 3:
                balance = Cliente(nomcli,apecli,cuenta,monto)
                print(balance)
            case 4:
                print("¡Gracias por usar CastiBank sistema bancario!")
                print(f"Saldo final: ${saldo:,.2f}")
                break

            case _:
                print("Opción no válida. Por favor seleccione 1, 2 , 3 o 4")

inicio()