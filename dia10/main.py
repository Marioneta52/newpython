import pygame


#inicializa pygame
pygame.init()

#Crea Pantalla
pantalla = pygame.display.set_mode((800, 600))

#titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

#Jugador
img_jugador = pygame.image.load('nave.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0

#funcion Jugador
def jugardor(x,y):
    pantalla.blit(img_jugador, (x,y))

#loop del Juego
se_ejecuta = True
while se_ejecuta:
    #rgb
    pantalla.fill((71, 148, 124))

    #Iterar Evento
    for event in pygame.event.get():
        #Cerrar Venta
         if event.type == pygame.QUIT:
             se_ejecuta = False
        #Movimiento con teclado
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                 jugador_x_cambio = -0.3
             if event.key == pygame.K_RIGHT:
                 jugador_x_cambio = 0.3
        #si se deja de presionar la tecla se queda quieto
         if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 jugador_x_cambio = 0

    #Modificar Ubicacion
    jugador_x += jugador_x_cambio
    #Mantener dentro de los bordes
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 736:
        jugador_x = 736

    jugardor(jugador_x,jugador_y)

    #Actualizar
    pygame.display.update()




