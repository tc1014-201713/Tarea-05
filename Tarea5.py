# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame
from random import randint
from math import *

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
NEGRO = (0, 122, 0)
ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))


def dibujarCuadradoCirulo():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)


        # Dibujar, aquí haces todos los trazos que requieras
        #pygame.draw.rect(ventana, BLANCO, (30, 30, ANCHO-60, ALTO-60), 5)

        for x in range(10,(ANCHO//2),10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            UX = ANCHO
            UY = ALTO
            UX -= x * 2
            UY -= x * 2
            pygame.draw.circle(ventana,ALEATORIO, (ANCHO//2,ALTO//2), x, 1)
            pygame.draw.rect(ventana, ALEATORIO, (x, x, UX, UY), 1)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def dibujarEstrella():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    UX = ANCHO // 2
    UY = ALTO// 2
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)


        # Dibujar, aquí haces todos los trazos que requieras
        for x in range(0,400,10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            UX=ANCHO//2
            UY=ALTO//2

            pygame.draw.line(ventana, ALEATORIO, (UX,UY+x), (800-x,UY), 1)
            pygame.draw.line(ventana, ALEATORIO, (UX, UY + x), (0+x, UY), 1)
            pygame.draw.line(ventana,ALEATORIO, (UX,UY-x), (0+x,UY), 1)
            pygame.draw.line(ventana,ALEATORIO, (UX,UY-x),(800-x,UY),1)



        pygame.display.flip()   # Actualiza trazos
        reloj.tick(60)          # 40 fps

    pygame.quit()   # termina pygame


def dibujarCirculos():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    x = 0
    radio = 150
    angulo = 0


    while not termina:
        # Procesa los eventos que recibe

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)


        for x in range(0,13,1):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            angulo = angulo + (2 * pi) / 12

            f = int(radio * sin(angulo)) + 400
            v = int(radio * cos(angulo)) + 400
            pygame.draw.circle(ventana, ALEATORIO, (v, f), radio, 1)

        reloj.tick(60)
        pygame.display.flip()


def dibujarEspiral():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    X=400
    Y=400

    while not termina:
        # Procesa los eventos que recibe

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)


        for i in range(0,400,10):
            pygame.draw.line(ventana,ALEATORIO,((X+5)-i,Y+i),((X+5)+i,Y+i),1)
            pygame.draw.line(ventana,ALEATORIO,((X+5)+i,Y+i),((X+5)+i,(Y-5)-i),1)
            pygame.draw.line(ventana,ALEATORIO,((X+5)+i,(Y-5)-i),((X-5)-i,(Y-5)-i),1)
            pygame.draw.line(ventana,ALEATORIO,((X-5)-i,(Y-5)-i),((X-5)-i,(Y+5)+i),1)



        reloj.tick(60)
        pygame.display.flip()


def calcularDivisibles():
    suma=0
    for x in range(1000,10000,1):
        if x%29==0:
            suma += 1

    return suma


def calcularPiramide():
    suma = 0
    for x in range(0, 9):
        suma = suma + (10 ** x)
        resultado = suma ** 2
        print("%d * %d=%d" % (suma, suma, resultado))

    numero = 0
    for i in range(1, 10):
        for f in range(0, i):
            numero += 10 ** f
        piramide = ((numero * 8) + i)
        print("%d * 8 + %d = %d" % (numero, f, piramide))


def calcularPi(numero):

    suma=0
    for x in range(1,numero+1,1):
        suma += 1/(x)**2

    pi= (suma*6)**0.5

    return pi



def main():
    print("¿Que figura o valor deseas ver?""\n"
          "1.- Cuadrados y circulos ""\n"
          "2.- Estrella""\n"
          "3.- Circulos""\n"
          "4.- Espiral ""\n"
          "5.- Números divisbles entre 29 de 4 dígitos ""\n"
          "6.- Piramide de números consecutivos""\n"
          "7.- Aproximación a Pi ""\n")
    opcion=1
    while opcion>0:
        opcion = int(input("Introducir opción"))
        if opcion==1:
            dibujarCuadradoCirulo()
        elif opcion==2:
            dibujarEstrella()
        elif  opcion==3:
            dibujarCirculos()
        elif opcion==4:
            dibujarEspiral()
        elif opcion==5:
            print("Hay: %d numeros divisibles entre 29 de 4 dígitos"%calcularDivisibles())
        elif opcion==6:
            calcularPiramide()
        elif opcion==7:
            numero = int(input("Introducir numero:"))
            calcularPi(numero)
            print("Pi= ", calcularPi(numero))
        else:
            print("error")



main()