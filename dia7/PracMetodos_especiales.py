class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return '"{titulo}", de {autor}'


 mi_libro = Libro('Mil Horas','Romeo Santos', 2601)


