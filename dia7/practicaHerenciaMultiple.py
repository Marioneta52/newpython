class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class Hija(Padre, Madre):
    def trabajar(self):
        print("Trabajando en la Fiscalía")


Hija.trabajar('Fiscalia')
Hija.reir('Fiscalia')
