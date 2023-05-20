import pygame

import time
import random


pygame.font.init()
ancho_pantalla = 1000
alto_pantalla = 700
fondo = pygame.transform.scale(pygame.image.load('Animacion2/img/fondo1.jpg'),(ancho_pantalla,alto_pantalla))
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Juego2") #nombre juego
fps = 60 #fps fotogramas por segundos
temporizador = pygame.time.Clock()

def main():

    iniciar_juego = True #variable Bandera para iniciar el juego
    nivel = 1
    vidas = 3 
    texto_pantalla = pygame.font.SysFont('italic', 40, True, False)

    def actualizar_ventana():
        ventana.blit(fondo, (0,0)) #adapta el fondo a la ventana 
        texto_vidas = texto_pantalla.render(f'vidas:{vidas}',True, (0,255,0))
        texto_nivel = texto_pantalla.render(f'nivel:{nivel}',True, (255,0,0))
        ventana.blit(texto_vidas, (10,10))
        ventana.blit(texto_nivel, (900,10))
        pygame.display.update()  
    while iniciar_juego:
        temporizador.tick(fps)
        actualizar_ventana()
        for evento in pygame.event.get(): #por cada evento
            if evento.type == pygame.QUIT:
                iniciar_juego = False


if __name__ == '__main__':  #es para llamar la función principal
    main()


pygame.quit()