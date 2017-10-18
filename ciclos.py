#encoding: UTF-8
#Anaid Fernanda Labat González
#A01746289
#Descripción el programa dibuja diversos patrones

#Importa librerías
import pygame
from random import randint
import math
import sys

#Dimensiones de la pantalla
ANCHO= 800
ALTO= 800

#Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)

#Dibuja círculos y cuadros
def dibujarCirculoCuadro():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

 #Dibuja los cuadrados y círculos.

        for c in range(0,ANCHO//2 + 1,10):
            pygame.draw.rect(ventana,NEGRO,(ANCHO//2-c,ALTO//2-c,2*c,2*c),1)
        for c in range(10,ANCHO//2 + 1,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),c,1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(30)  # 40 fps
    pygame.quit()  # finaliza

#Dibuja parábolas en color aleatorio
def dibujarParabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibuja parabolas
        for p in range(0, ANCHO//2 +1, 10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO,(ANCHO//2, 0 + p), (ANCHO//2 + p,ALTO//2), 1)
            pygame.draw.line(ventana, ALEATORIO,(ANCHO//2, ALTO -p), (ANCHO//2 + p,ALTO//2), 1)
            pygame.draw.line(ventana, ALEATORIO, (ANCHO//2, 0 + p), (ANCHO//2 -p,ALTO//2), 1)
            pygame.draw.line(ventana, ALEATORIO, (ANCHO//2, ALTO -p), (ANCHO//2 -p,ALTO//2), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(30)  # 40 fps
    pygame.quit() #finaliza

#Dibuja un espiral cuadrado
def dibujarEspiralCuadrado():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibuja espiral
        for e in range(0, ANCHO//2 +1, 10):
            pygame.draw.line(ventana, NEGRO, (ANCHO//2 - e, ALTO//2 + e), (ANCHO//2 + 5 +e, ALTO//2 + e))
            pygame.draw.line(ventana, NEGRO, (ANCHO//2 - 10 -e, ALTO//2 - 10 - e), (ANCHO//2 + 5 + e, ALTO//2 - 10 - e))
            pygame.draw.line(ventana, NEGRO, (ANCHO//2 + 5 +e, ALTO//2 - 10 - e), (ANCHO//2 + 5 + e,  ALTO//2 + e))
            pygame.draw.line(ventana, NEGRO, (ANCHO//2 - e,  ALTO//2 -e), (ANCHO//2 - e,  ALTO//2 + e))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(30)  # 40 fps
    pygame.quit() #finaliza

#Dibuja 12 círculos
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibuja círculos
        for d in range(0, 360, 30):
            coseno = ((math.cos(d*math.pi/180)))
            seno = ((math.sin(d*math.pi/180)))
            pygame.draw.circle(ventana,NEGRO,(int(ANCHO/2+ (150*coseno)),int(ALTO/2 + (150*seno))),150,1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps
    pygame.quit() #finaliza

#Calcula una aproximación del valor de Pi
def aproximarPI(valor):
    r=0 #Contador

    for i in range (1,valor+1):
        r=r+(1/i**2)

    pi=(r*6)**(1/2)
    return pi #regresa el valor de Pi

#Calcula todos los números de 4 digitos divisibles entre 29
def calcularNumerosDivisibles():
        di = 0
        for n in range(1000, 10000, 1):
            if n % 29 == 0:
                di += 1
        return di

#Calcula e imprime operaciones de números enteros
def calcularOperaciones():
    operaciones = "\n"
    escalera = 0
    for o in range(1,10):
        escalera = int("1"*o) + escalera
        total = escalera * 8 + o
        operaciones = operaciones + ("%d * 8 + %d = %d\n" % (escalera,o,total))
    operaciones = operaciones + "\n"
    for o in range(1,10):
        escalera = int("1" * o)
        total = escalera * escalera
        operaciones = operaciones + ("%d * %d = %d\n" % (escalera, escalera,total))
    return operaciones #regresa las operaciones que realiza el programa

#Funcion principal que dirige al programa y pregunta al usuario qué acción quiere realizar
def main():
    termina = True
    while termina:
        print(""" ---------------------------- MENÚ ----------------------------
            1) Círculos y cuadrados
            2) Parábolas en color aleatorio
            3) Espiral cuadrado
            4) 12 círculos
            5) Aproximación de pi
            6) Números divisibles entre 29
            7) Imprimir operaciones de números enteros
            0) Salir """)
        eleccion = int(input("Seleccione qué quiere hacer:"))
        if eleccion == 1:
            dibujarCirculoCuadro()
            print("")
        elif eleccion == 2:
            dibujarParabolas()
            print("")
        elif eleccion == 3:
            dibujarEspiralCuadrado()
            print("")
        elif eleccion == 4:
            dibujarCirculos()
            print("")
        elif eleccion == "5":
            valor = int(input("Dame el límite para aproximar pi: "))
            print("Pi vale aproximadamente %.4f " %aproximarPI(valor))
        elif eleccion == "6":
            print(" Los números de 4 dígitos divisibles entre 29 son: ", calcularNumerosDivisibles())
        elif eleccion == "7":
            print(calcularOperaciones())
        elif eleccion == "0":
            sys.exit()
        else:
            print("El término que uso no es válido")
            sys.exit()
main()


