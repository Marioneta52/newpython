import pygame


#inicializa pygame
pygame.init()
#Crea Pantalla
pantalla = pygame.display.set_mode((800, 600))

#titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

#loop del Juego
se_ejecuta = True

while se_ejecuta:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             se_ejecuta = False

     pantalla.fill((71,148,124))
     pygame.display.update()




