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

    #Para columna del 8:
    incremento = 1
    for x in range(1,10,1):
        resultado = incremento * 8 + x #Primer resultado.
        print(incremento, "* 8 +", x, "=", resultado) #Imprime el primer resultado.

        incremento = (incremento * 10) + (x+1)#El valor del incremento cambia. Multiplicando la variable inicial X10 y sumando el facto más x para agregar el valor pasado.
    print("---------------------------------")

    #Para columna del 8:
    incremento2=1

    for y in range(1,10,1):
        resultado2 = incremento2*incremento2 #Primer resultado.
        print(incremento2,"*",incremento2, "=", resultado2) #Imprime el primer resultado.

        incremento2 = (incremento2 * 10) + (1)#El valor del incremento cambia. Multiplicando la variable inicial X10 y sumando el factor más 1 para agregar.

def calcularNumerosDivisibles():
        d = 0
        for x in range(1000, 10000, 1):

            if x % 29 == 0:
                d += 1

        return d

def aproximarPI(valor):
    incremento=0

    for x in range (1,valor+1):
        incremento=incremento+(1/x**2)

    pi=(incremento*6)**(1/2)

    return pi

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

    while seleccion>=0:
        if seleccion==1:
            dibujarCirculoCuadrado()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 2:
            dibujarEspiral()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion==3:
            dibujarCirculosEntrelazados()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 4:
            dibujarParabola()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion==7:
            imprimirPiramide()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion==6:
            print("Número de divisibles entre 29 es:", calcularNumerosDivisibles())
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion==5:
            pi = int(input("Ingresa el rango de pi:"))
            print("PI vale:", aproximarPI(pi))
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion>=8:
            print("Selecciones un número del 1 al 7.")
            print("")
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion==0:
            print("¡Hasta luego!")
            break

main()