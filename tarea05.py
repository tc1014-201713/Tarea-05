#encoding: UTF-8

#Oscar Zuñiga Lara

#A01654827

import math
from random import randint

import pygame

ANCHO = 800
ALTO = 800
BLANCO = (255,255,255)
Negro = (0, 0, 0)
tamano =400
def dibujarA():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
#//////////////////////////////////////
        ventana.fill(BLANCO)
#///////DIBUJOS/////////////////////
        tamano = 20
        for tamano in range(0,400,20):
            pygame.draw.rect(ventana, Negro, ((ANCHO - tamano) // 2, (ALTO - tamano) // 2, tamano, tamano), 1)
        for tamano in range(0,190,10):
            pygame.draw.circle(ventana, Negro, (ANCHO // 2, ALTO // 2), 190 - tamano, 1)
        #/////////////////////////////////////
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def dibujarD():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
#///////////////////////////////////////////////////////////////////////
        ventana.fill(BLANCO)
#///////DIBUJOS/////////////////////////////////////////////////////////
        ubicacion = 1
        for angulo in range(0,361,30):
            a = 0
            x = ANCHO//2
            y = ALTO//2
            for a in range(0,360,30):
                radian = a * math.pi // 180
                x = int(60 * math.cos(radian))
                y = int(60 * math.sin(radian))
                print(x)
                print(y)
                pygame.draw.circle(ventana, Negro, (200 + x , 200 + y ),60, 1)
                #////////////////////////////////////////////////////////////////////////
        pygame.display.flip()
        reloj.tick(30)
    pygame.quit()

def dibujarB():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
                # //////////////////////////////////////
        ventana.fill(BLANCO)
        # ///////DIBUJOS/////////////////////
        for lineasX in range(0, (ALTO // 2) + 1, 10):
            colorAleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, colorAleatorio, (lineasX, ALTO // 2), (ANCHO // 2, ALTO // 2 + lineasX))
            pygame.draw.line(ventana, colorAleatorio, (ANCHO - lineasX, ALTO // 2),(ANCHO // 2, ALTO // 2 + lineasX))
            pygame.draw.line(ventana, colorAleatorio, (ANCHO - lineasX, ALTO // 2),(ANCHO // 2, ALTO // 2 - lineasX))
            pygame.draw.line(ventana, colorAleatorio, (lineasX, ALTO // 2), (ANCHO // 2, ALTO // 2 - lineasX))
            # /////////////////////////////////////
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def dibujarC():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
                # //////////////////////////////////////
        ventana.fill(BLANCO)
        # ///////DIBUJOS/////////////////////
        for a in range(5, 400, 10):
            pygame.draw.line(ventana, Negro, (ANCHO // 2 + 5 + a, ALTO // 2 - a), (ANCHO // 2 + 5 - a, ALTO // 2 - a))
            pygame.draw.line(ventana, Negro, (ANCHO // 2 + 5 - a, ALTO // 2 - a),
                             (ANCHO // 2 + 5 - a, ALTO // 2 - 5 + a))
            pygame.draw.line(ventana, Negro, (ANCHO // 2 + 5 - a, ALTO // 2 - 5 + a),
                             (ANCHO // 2 - 5 + a, ALTO // 2 - 5 + a))
            pygame.draw.line(ventana, Negro, (ANCHO // 2 - 5 + a, ALTO // 2 - 5 + a),
                             (ANCHO // 2 - 5 + a, ALTO // 2 + 10 - a))
        # /////////////////////////////////////
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def calcular3():
    a = 1015
    x = 0
    for a in range(1000,9999,19):
        x = x + 1
    print(x)

def ejercicio4():

    b = 0

    e = 1

    f = 0

    e = 0

    r = 4

    for d in range(1,10,1):

        e = e * 10 + d

        r = e * 8  + d

        print("%d * 8 + %d = %d"%(e,d,r))

    for a in range(0,10,1):

        b = 10 ** a + b

        c = b * b

        print(b, "*", b ,"=" , c)

def calcularPI():
    serie = 1
    for divisor in range(2,1000,1):
        serie = 1/(divisor**2) + serie
        pi = (6 *serie)**.5
    print(pi)

def main():
    aas = True
    while aas == True:
        print((" Tarea 5. Seleccione qué quiere hacer."))
        print("1. Dibujar cuadros y círculos")
        print("2. Dibujar espiral ")
        print("3. Dibujar círculos")
        print("5. Aproximar PI")
        print("6. Contar divisibles entre 19 ")
        print("7. Imprimir pirámides de números")
        print("0. Salir ")
        usuario = int(input("Inserte el ejercicio que quiere ejecutar: "))
        if usuario == 1:
            dibujarA()
        elif usuario == 2:
            dibujarC()
        elif usuario == 3:
            dibujarD()
        elif usuario == 4:
            dibujarB()
        elif usuario == 5:
            calcularPI()
        elif usuario == 6:
            calcular3()
        elif usuario == 7:
            ejercicio4()
        elif usuario == 0:
            aas = False
        else:
            print("Inserte opcion valida")



main()