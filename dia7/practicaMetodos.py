class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
