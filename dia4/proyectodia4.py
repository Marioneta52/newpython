from random import randint


numero_secreto = randint(1, 100)
intentos_maximos = 8
intentos = 0

nombre = input('Introduce un nombre para iniciar Juego: ')

print(f"{nombre} ¡Bienvenido al Juego de Adivinanza! 🎯")
print(f"Tienes {intentos_maximos} intentos para adivinar el número secreto (1-100)")
print("-" * 50)

while intentos < intentos_maximos:
    try:
        # Mostrar intentos restantes
        intentos_restantes = intentos_maximos - intentos
        print(f"Intentos restantes: {intentos_restantes}")

        # Pedir número al usuario
        numero_usuario = int(input("Ingresa tu número: "))
        intentos += 1

        # Usar match-case para comparar
        match numero_usuario:
            case n if n == numero_secreto:
                print(f"🎉 ¡Felicidades! ¡Encontraste el número {numero_secreto}!")
                print(f"Lo lograste en {intentos} intento(s)")
                break
            case n if n > numero_secreto:
                print("📈 El número ingresado es MAYOR que el número secreto")
            case n if n < numero_secreto:
                print("📉 El número ingresado es MENOR que el número secreto")

        # Pista adicional
        diferencia = abs(numero_usuario - numero_secreto)
        if diferencia <= 5:
            print("💡 ¡Estás muy cerca!")
        elif diferencia <= 15:
            print("🔍 Estás cerca...")
        else:
            print("🌎 Estás lejos")

        print("-" * 30)

    except ValueError:
        print("❌ Error: Debes ingresar un número válido")
        print("-" * 30)

# Si se agotaron los intentos
if intentos >= intentos_maximos and numero_usuario != numero_secreto:
    print(f"😢 ¡Se agotaron los intentos! El número secreto era: {numero_secreto}")