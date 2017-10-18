#Yerish Valdes Bernes A01375755
# encoding: UTF-8
# con este programa se puede seleccionar de un menu la funcion que se desea ejecutar la cual esta dentro de un ciclo que se corre hasta que se le indica que termine

import pygame
import math
from random import randint
ANCHO = 800
ALTO = 800
BLANCO = (255,255,255)
NEGRO = (000,000,000)
def dibujar_CuadradosYCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)


        for x in range(0,ANCHO,10):
            pygame.draw.rect(ventana,NEGRO,(ANCHO//2-x,ALTO//2-x,2*x,2*x),1)
        for y in range(1,ALTO//2,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),y,1)


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def Espiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)


        for i in range(0,ANCHO,10):
            pygame.draw.line(ventana, NEGRO,(ANCHO//2-i,ALTO//2+i),(ANCHO//2+10+i,ALTO//2+i))
            pygame.draw.line(ventana, NEGRO,(ANCHO//2-i,ALTO//2-i),(ANCHO//2-i,ALTO//2+i))
            pygame.draw.line(ventana, NEGRO,(ANCHO//2-10-i,ALTO//2-10-i),(ANCHO//2+10+i,ALTO//2-10-i))
            pygame.draw.line(ventana, NEGRO,(ANCHO//2+10+i,ALTO//2-10-i),(ANCHO//2+10+i,ALTO//2+i))


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def Circulos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)


        for i in range(0,330,32):

            pygame.draw.circle(ventana,NEGRO,(int((ANCHO//2+(math.cos(i)*150))),(int(ALTO//2+math.sin(i)*150))),150,1)


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def Parabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)


        for x in range(0,ANCHO,10):
            pygame.draw.rect(ventana,NEGRO,(ANCHO//2-x,ALTO//2-x,2*x,2*x),1)
        for y in range(1,ALTO//2,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),y,1)


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def Pi():
    pass


def divisibles():
    total = 0
    for i in range(1000, 9999):
        num = i / 29

        if num.is_integer():
            total = total + 1
    print(total)

    pass

def piramides():
    num = 0
    cons = 8
    for i in range(1, 10):
        if num < 1:
            total1 = i * 8 + i
            print("1*8+1=", total1)
            num = i
        else:
            total = num * 10 + i
            final = total * cons + i
            print("%i*%i+%i=%i" % (total, cons, i, final))
            num = total
    pass

def main():
    opcion = 8
    while opcion != 0:
        print ("\nTarea 5. Seleccione qué quiere hacer.\n 1. Dibujar cuadros y círculos\n 2. Dibujar espiral\n 3. Dibujar círculos\n 4. Dibujar parábolas\n 5. Aproximar PI\n 6. Contar divisibles entre 19\n 7. Imprimir pirámides de números\n 0. Salir\n")
        opcion = int(input("¿Qué desea hacer? "))
        if opcion == 1:
            dibujar_CuadradosYCirculos()
        elif opcion == 2:
            Espiral()
        elif opcion == 3:
            Circulos()
        elif opcion == 4:
            Parabolas()
        elif opcion == 5:
            Pi()
        elif opcion == 6:
            divisibles()
        elif opcion == 7:
            piramides()
        elif opcion == 0:
            print("FIN")
        else:
            print("numero na valido")
main()