# encoding: UTF-8
# Autor: Luis Daniel Rivera Salinas  A01374997
# Descripcion: Menu con distintos ejemplos a mostrar

import pygame
import math
from random import randint

#Dimensiones de la Pantalla
ANCHO = 800
ALTO = 800

#Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)



def dibujarCuadrosYCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()
    termina = True

    while termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = False

        ventana.fill(BLANCO)

        ancho = 0 #Tambien sirve como alto del rectangulo
        for xy in range(400,0,-10): #Cuadrado
            pygame.draw.rect(ventana, NEGRO, (xy, xy, ancho, ancho),1)
            ancho += 20
        for radio in range(0,400,+10): #Circulo
            if radio == 0:
                pygame.draw.circle(ventana,NEGRO,(400, 400), radio, 0)
            else:
                pygame.draw.circle(ventana, NEGRO, (400, 400), radio, 1)

        pygame.display.flip()

    reloj.tick(40)
    pygame.quit()

def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()
    termina = True

    while termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = False

        ventana.fill(BLANCO)

        arriba = False
        abajo = False
        izquierda = True
        derecha = False
        xy1 = 790
        x2= 10
        xy2 = 10
        y1 = 790
        xy3 = 10
        y3 = 780
        xy4 = 780
        y4 = 10
        for cont in range(1,40):
            if izquierda == True:
                pygame.draw.line(ventana,NEGRO,(xy1,xy1),(x2,xy1),1)
                arriba = True
                abajo = False
                izquierda = False
                derecha = False
                xy1-=10
                x2 +=10

            if arriba == True:
                pygame.draw.line(ventana, NEGRO, (xy2,y1), (xy2, xy2), 1)
                arriba = False
                abajo = False
                izquierda = False
                derecha = True
                xy2 +=10
                y1 -= 10

            if derecha == True:
                pygame.draw.line(ventana, NEGRO, (xy3, xy3), (y3, xy3), 1)
                arriba = False
                abajo = True
                izquierda = False
                derecha = False
                xy3 +=10
                y3 -=10

            if abajo == True:
                pygame.draw.line(ventana, NEGRO, (xy4, y4), (xy4, xy4), 1)
                arriba = False
                abajo = False
                izquierda = True
                derecha = False
                xy4 -= 10
                y4 += 10





        pygame.display.flip()
    reloj.tick(40)
    pygame.quit()

def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()
    termina = True

    while termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = False

        ventana.fill(BLANCO)

        radio = 150
        posiciony = 400
        x = 400
        posicionx = int(400+radio)

        #Ejes rectos
        for angulo in range(0,390,30):
            pygame.draw.circle(ventana,NEGRO,(posicionx,posiciony),radio,1)
            posicionx = int(radio*math.cos(angulo) + x)
            posiciony = int(radio*math.sin(angulo) + x)




        pygame.display.flip()
    reloj.tick(40)
    pygame.quit()



def dibujarParabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()
    termina = True

    while termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = False

        ventana.fill(BLANCO)


        #Puntos iniciales y color
            #Cuadrante1
        y2Cuadrante1 = 0

            #Cuadrante2
        y2Cuadrante2 = 0

            #Cuadrante 3
        y2Cuadrante3 = 800

            #Cuadrante 4
        y2Cuadrante4 = 800



        #Cuadrante 1
        for x1Cuadrante1 in range(400,810,10):
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(x1Cuadrante1,400),(400,y2Cuadrante1))
            y2Cuadrante1 +=10

        #Cuadrante 2
        for x2Cuadrante2 in range(400,-10,-10):
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(x2Cuadrante2,400),(400,y2Cuadrante2))
            y2Cuadrante2 +=10

        #Cuadrante 3
        for x3Cuadrante3 in range(400,-10,-10):
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(x3Cuadrante3,400),(400,y2Cuadrante3))
            y2Cuadrante3 -= 10

        #Cuadrante 4
        for x4Cuadrante4 in range(400,810,10):
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(x4Cuadrante4,400),(400,y2Cuadrante4))
            y2Cuadrante4 -= 10


        pygame.display.flip()
    reloj.tick(40)
    pygame.quit()

def aproximarNumero():
    numero = int(input("Ingrese el numero de valores que vas a usar para aproximar a PI: "))
    for valor in range(0,numero+1):
        if valor == 0:
            formula = 0
            f2 = 0 + formula
        else:
            f1 = (1/(valor**2))
            f2 = f1 + f2
    resultado = (f2*6)**(.5)
    return(resultado)

def dividirEntre29():
    lista29 = []
    for numero in range(1000,10000):
        if numero%29 == 0:
           lista29.append(numero)
    longitud = len(lista29)
    return(longitud)

def imprimirPiramides():

    posicion1= 1
    constante = 8
    suma2 = 2
    for suma in range(1,10):
        print(posicion1,"*",constante,"+",suma,"=",((posicion1*constante)+suma))
        posicion1 = (posicion1*10)+suma2
        suma2 += 1

    print("           ")

    n = 1
    for multiplicadorDeUnos in range(1,10,):
        print(n,"*",n,"=",n*n)
        n = (n*10) + 1



def main():
    #Menu
    print("          Tarea 5. Seleccione que quiere hacer")
    print("          1. Dibujar cuadrados y círculos")
    print("          2. Dibujar espiral")
    print("          3. Dibujar círculos")
    print("          4. Dibujar parabolas")
    print("          5. Aproximar PI")
    print("          6. Contar divisibles entre 29")
    print("          7. Imprimir pirámides de números")
    print("          0. Salir")
    print("          ¿Que desea hacer? ")
    decision = int(input(": "))
    if decision > 7:
        print("Ingresa un numero que esté en las opciones de arriba")
    elif decision == 1:
        dibujarCuadrosYCirculos()
    elif decision == 2:
        dibujarEspiral()
    elif decision == 3:
        dibujarCirculos()
    elif decision == 4:
        dibujarParabolas()
    elif decision == 5:
        print("Este programa calcula la aproximacion de PI")
        print(" ")
        print("La aproximacion a Pi es de:",aproximarNumero())
    elif decision == 6:
        print("Este programa te imprime cuantos numeros de 4 digitos son divisibles entre 29")
        print(" ")
        print("Hay", dividirEntre29(), "numeros divisibles entre 29 de 4 digitos ")
    elif decision == 7:
        print("Este programa imprime 2 piramides de numeros")
        print(" ")
        imprimirPiramides()
    elif decision == 0:
        print("Gracias por usar el programa, ¡vuelva pronto!")


main()


