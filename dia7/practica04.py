class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas  # atributo de instancia

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print(f"Flecha lanzada. Flechas restantes: {self.cantidad_flechas}")
        else:
            print("No quedan flechas para lanzar.")


# Ejemplo de uso
p1 = Personaje(5)
p1.lanzar_flecha()  # Flechas restantes: 4
p1.lanzar_flecha()  # Flechas restantes: 3
p1.lanzar_flecha()
p1.lanzar_flecha()
p1.lanzar_flecha()
p1.lanzar_flecha()