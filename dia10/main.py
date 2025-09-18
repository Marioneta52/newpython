import pygame
import random


#inicializa pygame
pygame.init()

#Crea Pantalla
pantalla = pygame.display.set_mode((800, 600))

#titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
mi_fondo = pygame.image.load('espacio.png')

#Variables del Jugador
img_jugador = pygame.image.load('nave.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0


#Variables del enemigo
img_enemigo = pygame.image.load('alien2.png')
enemigo_x = random.randint(0,536)
enemigo_y = random.randint(50,200)
enemigo_x_cambio = 1
enemigo_y_cambio = 50

#Variables de la Bala
img_bala= pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False



#funcion Jugador
def jugardor(x,y):
    pantalla.blit(img_jugador, (x,y))

# funcion Enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# funcion Disparar BAla
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

#loop del Juego
se_ejecuta = True
while se_ejecuta:
    #rgb
    #pantalla.fill((71, 148, 124))
    pantalla.blit(mi_fondo, (0, 0))

    #Iterar Evento
    for event in pygame.event.get():
        #Cerrar Venta
         if event.type == pygame.QUIT:
             se_ejecuta = False

        #Evento Presionar teclas
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                 jugador_x_cambio = -1
             if event.key == pygame.K_RIGHT:
                 jugador_x_cambio = 1
             if event.key == pygame.K_SPACE:
                 disparar_bala(jugador_x, bala_y)

        #Evento soltar teclas
         if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 jugador_x_cambio = 0

    #Modificar Ubicacion del jugador
    jugador_x += jugador_x_cambio

    #Mantener dentro de los bordes
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x  >= 736:
        jugador_x = 736

    # Modificar Ubicacion del Enemigo
    enemigo_x += enemigo_x_cambio

    # Mantener dentro de los bordes enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio= 1
        enemigo_y+= enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -1
        enemigo_y += enemigo_y_cambio

    #Movismiento Bala
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugardor(jugador_x,jugador_y)
    enemigo(enemigo_x,enemigo_y)

    #Actualizar
    pygame.display.update()




