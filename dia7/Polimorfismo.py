#El polimormismo es capaz de ejecutar dos metodos del mismo nombre en diferentes casos
class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' Dice Muu')

class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' Dice beee')

vaca1 = Vaca('Ramona')
oveja1 = Oveja('Julia')

vaca1.hablar()
oveja1.hablar()

#Polimorfismo
animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()

#otra forma de polimorfismo
def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
#animal_hablar(oveja1)