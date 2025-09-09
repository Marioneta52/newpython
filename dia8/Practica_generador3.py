"""Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:
"Te quedan 3 vidas"
"Te quedan 2 vidas"
"Te queda 1 vida"
"Game Over"
Almacena el generador en la variable perder_vida"""


def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x
perder_vida = mensaje()



def perder_vidas():
    vida = [3,2,1]
    for n in vida:
        yield n



perder_vida = perder_vidas()

try:
   print(f'te quedan {next(perder_vida)} vidas')
   print(f'te quedan {next(perder_vida)} vidas')
   print(f'te quedan {next(perder_vida)} vidas')
   print(f'te quedan {next(perder_vida)} vidas')
except:
    print('game over')
