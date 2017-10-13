#Javier Pascal Flores
#Encding: UTF-8

import pygame
from math import *
from random import *

def Dibujar_CirculosC():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    NEGRO= (0,0,0)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(BLANCO)

        for i in range(10,400,10):
            pygame.draw.circle(ventana, NEGRO,((400),(400)),i,1 )

            pygame.draw.rect(ventana, NEGRO,(i,i,800-2*i,800-2*i),1)





        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()

def Dibujar_Circulos():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    NEGRO= (0,0,0)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(BLANCO)

        x=0
        radio=150
        angulo=0

        for i in range (1,13):
            angulo+= pi/6
            x=int(150*(cos(angulo)))
            y=int(150*(sin(angulo)))
            pygame.draw.circle(ventana, NEGRO,(x+400, y+400), radio, 1 )




        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()

def Dibujar_Espiral():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    NEGRO= (0,0,0)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(BLANCO)

        x=400
        y=400
        for i in range (0,159):
            a = i % 4
            counter = (((i % 2) + i) // 2) * 10
            if a == 1:
                pygame.draw.line(ventana,NEGRO,(x,y),(x+counter,y+0),1)
                x+=counter
            elif a==2:
                pygame.draw.line(ventana, NEGRO, (x, y), (x +0, y - counter), 1)
                y-=counter
            elif a==3:
                pygame.draw.line(ventana, NEGRO, (x, y), (x -counter, y +0), 1)
                x-=counter
            else:
                pygame.draw.line(ventana, NEGRO, (x, y), (x + 0, y + counter), 1)
                y+=counter


        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()

def dibujar_Estrella():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(BLANCO)
            for y in range(0, 400, 10):
                pygame.draw.line (ventana,(randint(0,255), randint(0,255), randint(0,255)) ,(400, y), (400 + y, 400),
                                 1)

                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, y), (400 - y, 400),1)

                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, 800 - y),(400 + y, 400), 1)

                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, 800 - y),(400 - y, 400), 1)

            pygame.display.flip()
            reloj.tick(40)
    pygame.quit()

def Ejercicio_Pi(n):
    pi_cuadrada = 0
    for i in range(1,n+1):
        pi_cuadrada+=(1/(i**2))
    pi=sqrt((pi_cuadrada*6))

    return pi

def dividir_29():
    numero=0
    for i in range (1000,10000):
        if i % 29==0:
            numero += 1
    return (numero)

def Hacer_Piramides():
    cuenta=0
    for i in range(1,10,1):
        for x in range (i+1,1,-1):
            cuenta+=(10**x)//100
        print("%d * 8 +%d = %d" % (cuenta, i, cuenta*8+i))
    print("\n")


    for i in range(0, 10, 1):
        factor=0
        for j in range(1, i + 1, 1):
            factor += 10 ** j
        factor+=1
        print("%d * %d = %d" %(factor, factor, factor * factor))



def main():

    print("Tarea 5. Seleccione que quiere hacer" 
          "\n" 
          " 1. Dibujar cuadros y círculos "
          "\n"
          " 2. Dibujar espiral "
          "\n" 
          " 3. Dibujar círculos"
            "\n" 
          " 4. Dibujar parábolas "
            "\n" 
          " 5. Aproximar PI "
          "\n" 
          " 6. Contar divisibles entre 29 "
            "\n"    
          " 7. Imprimir pirámides de números"
          "\n"
          " 0. Salir "
          "\n")
    seleccion=int(input(" ¿Qué desea hacer? "))

    salir = False
    while not salir:
        if seleccion == 0:
            salir=True
            quit()


        if seleccion > 0 and seleccion <= 7:

            if seleccion == 1:
                Dibujar_CirculosC()
            elif seleccion ==2:
                Dibujar_Espiral()
            elif seleccion ==3:
                Dibujar_Circulos()
            elif seleccion ==4:
                dibujar_Estrella()
            elif seleccion ==5:
                ultimo_denominador = int(input("Dame un valor numerico: "))
                pi = Ejercicio_Pi(ultimo_denominador)
                print(pi)
            elif seleccion ==6:
                numero = dividir_29()
                print(numero)
            elif seleccion ==7:
                Hacer_Piramides()


        else:
            print("numero invalido")
        seleccion=int(input(" ¿Qué desea hacer? "))







main()