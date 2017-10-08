# encoding: UTF-8
# Autor: Carlos Pano Hernández
# Este programa crea diversos patrones de dibujo.

import pygame

import math

import random


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]. Paleta de colores.
NEGRO = (0,0,0)

def dibujarEspiral():

    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps. Se debe bajar para reducir la sobrecarga a la computadora.
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        for a in range(0,400,10):

            #Líneas horizontales abajo:
            pygame.draw.line(ventana, NEGRO, (ANCHO-a, ALTO-a),(0+a, ALTO-a), 1)

            #Vertical Izquierda:
            pygame.draw.line(ventana,NEGRO,(0+a, ALTO-a),(0+a,10+a),1)

            #Horizontal Arriba
            pygame.draw.line(ventana, NEGRO, (0+a,10+a), (ANCHO-(a+10), 10 + a), 1)

            #Vertical derecha arriba
            pygame.draw.line(ventana, NEGRO, (ANCHO-a, ALTO-a), (ANCHO-a, 10 + a-10),1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(30)          # 40 fps

    pygame.quit()   # termina pygame

def dibujarParabola():

    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps. Se debe bajar para reducir la sobrecarga a la computadora.
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        #Cambio de color:
        RANDOM = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        #Dibujo de parábolas:
        for p in range(0, 400, 10):#Separación de 10 pixeles. 40 línes generadas
            RANDOM = (random.randint(0, 255), random.randint(0, 255), random.randint(0,255))

            #Cuadrante 1=
            pygame.draw.line(ventana, RANDOM, (ANCHO // 2 + p, ALTO // 2), (ALTO // 2, p), 1)
            #Cuadrante 2
            pygame.draw.line(ventana, RANDOM, (ANCHO//2 - p, ALTO//2),(ALTO//2,p),1)
            # Cuadrante 3
            pygame.draw.line(ventana, RANDOM, (ANCHO // 2, ALTO - p), (ANCHO // 2 - p, ALTO // 2), 1)
            #Cuadrante 4
            pygame.draw.line(ventana, RANDOM, (ANCHO//2, ALTO-p), (ANCHO//2+p, ALTO//2), 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(30)          # 40 fps

    pygame.quit()   # termina pygame

def dibujarCirculosEntrelazados():

    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps. Se debe bajar para reducir la sobrecarga a la computadora.
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        #Dibujar patrón de círculos.
        for r in range(0, 330, 32):#El ángulo máximo es 330. 360 ya está contado en el (0,0). Queremos 12 círculos: 360/11= 32.72
            pygame.draw.circle(ventana, NEGRO, (int((math.cos(r) * 150) + ANCHO//2), int((math.sin(r) * 150) + ALTO//2)), (150), 1)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(60)          # 40 fps

    pygame.quit()   # termina pygame

def dibujarCirculoCuadrado():

        pygame.init()  # Inicializa pygame
        ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
        reloj = pygame.time.Clock()  # Para limitar los fps. Se debe bajar para reducir la sobrecarga a la computadora.
        termina = False  # Bandera para saber si termina la ejecución

        while not termina:
            # Procesa los eventos que recibe
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                    termina = True

            # Borrar pantalla
            ventana.fill(BLANCO)

            for y in range(1, 400, 10):
                # DibujarCírculo
                pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), y, 1)
                # DibujarCuadrado
                pygame.draw.rect(ventana, NEGRO, (y, y, ANCHO - y * 2, ALTO - y * 2), 1)

            pygame.display.flip()  # Actualiza trazos
            reloj.tick(60)  # 40 fps

        pygame.quit()  # termina pygame


def imprimirPiramide():
    pass

def calcularNumerosDivisibles():
    pass

def aproximarPI():
    pass


def main():

    print("Tarea 5. Seleccione qué quiere hacer:")

    print("""
    1. Dibujar cuadros y círculos
    2. Dibujar espiral
    3. Dibujar círculos
    4. Dibujar parábolas
    5. Aproximar PI
    6. Contar divisibles entre 29
    7. Imprimir pirámides de números
    0. Salir""")

    print("")
    seleccion=int(input("¿Qué desea hacer?:"))
    print("---------------------------------")

    if seleccion==1:
        dibujarCirculoCuadrado()

    elif seleccion == 2:
        dibujarEspiral()

    elif seleccion==3:
        dibujarCirculosEntrelazados()

    elif seleccion == 4:
        dibujarParabola()

    elif seleccion==7:
        imprimirPiramide()

    elif seleccion==6:
        calcularNumerosDivisibles()

    elif seleccion==5:
        aproximarPI()

    elif seleccion==0:
        pass

    else:
        print("No se puede realizar esta acción. Seleccione un número del 1-7 o bien 0 para salir.")


main()