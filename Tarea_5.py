#encoding: UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
# Programa que aloja un menu y de acuerdo a la respuesta del usuario realiza lo que el usuario pida.

#Importar librerias y estableciendo constantes
import pygame
from random import randint
import sys
import math
ANCHO = 800
ALTO = 800
NEGRO = (0,0,0)
BLANCO = (255,255,255)

#Función que dibuja cuadrados y circulos intersectandose
def dibujarcuadrosycirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        #Dibujando los cuadrados y circulos
        for x in range(0,ANCHO//2 + 1,10):
            pygame.draw.rect(ventana,NEGRO,(ANCHO//2-x,ALTO//2-x,2*x,2*x),1)
        for x in range(10,ANCHO//2 + 1,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),x,1)




        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()

#Funcion que dibuja parabolas multicolor
def dibujarparabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibujando los cuadrados y circulos
        for x in range(0, ANCHO//2 +1, 10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO,(ANCHO//2, 0 + x), (ANCHO//2 + x,ALTO//2), 1)
            pygame.draw.line(ventana, ALEATORIO,(ANCHO//2, ALTO - x), (ANCHO//2 + x,ALTO//2), 1)
            pygame.draw.line(ventana, ALEATORIO, (ANCHO//2, 0 + x), (ANCHO//2 - x,ALTO//2), 1)
            pygame.draw.line(ventana, ALEATORIO, (ANCHO//2, ALTO - x), (ANCHO//2 - x,ALTO//2), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()

#Funcion que dibuja un espiral cuadrangular
def dibujarespiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibujando los cuadrados y circulos
        for x in range(0, ANCHO//2 +1, 10):
            pygame.draw.line(ventana, NEGRO, (ANCHO//2 - x, ALTO//2 + x), (ANCHO//2 + 5 + x, ALTO//2 + x))
            pygame.draw.line(ventana, NEGRO, (ANCHO//2 - 10 - x, ALTO//2 - 10 - x), (ANCHO//2 + 5 + x, ALTO//2 - 10 - x))
            pygame.draw.line(ventana, NEGRO, (ANCHO//2 + 5 + x, ALTO//2 - 10 - x), (ANCHO//2 + 5 + x,  ALTO//2 + x))
            pygame.draw.line(ventana, NEGRO, (ANCHO//2 - x,  ALTO//2 - x), (ANCHO//2 - x,  ALTO//2 + x))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()

#Funcion que dibuja circulos intersectados
def dibujarcirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibujando los cuadrados y circulos
        for x in range(0, 360, 30):
            coseno = ((math.cos(x*math.pi/180)))
            seno = ((math.sin(x*math.pi/180)))
            pygame.draw.circle(ventana,NEGRO,(int(ANCHO/2+ (150*coseno)),int(ALTO/2 + (150*seno))),150,1)



        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()

#Funcion que aproxima al valor de pi de acuerdo al número que indique el usuario
def calcularpi(limite):
    serie = 0
    for x in range (1,limite+1):
        serie= serie+(1/x**2)
    pi = (6*(serie))**(1/2)
    return pi

#Funcion que calcula todos los números de 4 digitos divisibles entre 29
def calculardivisibles29():
    ndivisibles = 0
    for x in range (1000,10000,1):
        if x % 29 == 0:
            ndivisibles += 1
    return ndivisibles

#Funcion que calcula e imprime piramaides de multiplicaciones
def calcularpiramides():
    piramides = "\n"
    escalera = 0
    for factor in range(1,10):
        escalera = int("1"*factor) + escalera
        resultado = escalera * 8 + factor
        piramides = piramides + ("%d * 8 + %d = %d\n" % (escalera,factor,resultado))
    piramides = piramides + "\n"
    for factor in range(1,10):
        escalera = int("1" * factor)
        resultado = escalera * escalera
        piramides = piramides + ("%d * %d = %d\n" % (escalera, escalera, resultado))

    return piramides

#Funcion principal que dirige al programa
def main():
    termina = True
    while termina:
        print("""Seleccione que quiere hacer:
            1) Cuadros y circulos
            2) Parabolas multicolor
            3) Espiral cuadrado
            4) Circulos intersectados
            5) Aproximación de pi
            6) Contar divisibles entre 29
            7) Imprimir piramides de numeros enteros
            0) Salir """)
        eleccion = input("¿Qué programa desea utilizar? inserte el número:")
        if eleccion == "1":
            dibujarcuadrosycirculos()
            print("")
        elif eleccion == "2":
            dibujarparabolas()
            print("")
        elif eleccion == "3":
            dibujarespiral()
            print("")
        elif eleccion == "4":
            dibujarcirculos()
            print("")
        elif eleccion == "5":
            limite = int(input("Dame el limite de la serie para aproxima pi: "))
            print("Pi vale aproximadamente %.4f " % calcularpi(limite))
            print("")
        elif eleccion == "6":
            print(" Los numeros de 4 digitos divisibles entre 29 son: ", calculardivisibles29())
            print("")
        elif eleccion == "7":
            print(calcularpiramides())
            print("")
        elif eleccion == "0":
            sys.exit()
        else:
            print("El termino que uso no es válido")
            sys.exit()

main()