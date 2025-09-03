class Animal:
    def __init__(self,edad,color): #Atributos de la clase
        self.edad = edad
        self.color = color

    def nacer(self): #Metodo de la clase
        print(f'Este animal ha nacido de color {self.color} y ademas tiene {self.edad} edad')

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    def __init__(self,edad,color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")

#print(Pajaro.__bases__)
#print(Animal.__subclasses__())


piolin = Pajaro(2,'morado',60)
piolin.nacer()
piolin.hablar()
piolin.volar(100)

mi_animal = Animal(5, 'Rojo')
mi_animal.nacer()