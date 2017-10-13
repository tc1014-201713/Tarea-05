# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González A01745998
# Descripción: Menú que da opciones para distintas funciones

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)


def dibujarCuadrosYCirculos():
    # círculo & cuadrado
    x = ANCHO // 2
    y = ALTO // 2
    r = 10
    l = r * 2
    xC = ANCHO // 2 - r
    yC = ALTO // 2 - r

    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        # Borrar pantalla
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras
        for factor in range (1,ANCHO//20):
            pygame.draw.circle(ventana, NEGRO, (x, y), r * factor, 1)

        for factor in range (0,ANCHO//20):
            pygame.draw.rect(ventana, NEGRO,(xC - r*factor, yC - r*factor, l + 2*r*factor, l + 2*r*factor), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()

def main():
    dibujarCuadrosYCirculos()

main()