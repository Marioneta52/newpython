class Pajaro:
    alas =True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro ha volador {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')


    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'puso{cantidad} Huevos')


    @staticmethod
    def mirar():
        print('El pajaro mirar')



Pajaro.poner_huevos(50)
Pajaro.mirar()