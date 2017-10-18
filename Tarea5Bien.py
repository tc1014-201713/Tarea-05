#encoding: UTF-8
#Autor: Ana María López Soto
#Descripción: Realiza cuatro figuras con pygame y tres ejercicos extras

import pygame
from random import randint
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

#Color
BLANCO = (255, 255, 255)

def dibujarCiculoCuadrado():

    pygame.init() # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO)) # Crea la ventana
    reloj = pygame.time.Clock()# Limitar los fps.
    termina = False# Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        #Borrar pantalla
        ventana.fill(BLANCO)

        for y in range(1, 400, 10):
            #Genera el cambio de color
            COLORLOCO = (randint(0, 255), randint(0, 255), randint(0, 255))
            # DibujarCírculo
            pygame.draw.circle(ventana, COLORLOCO, (ANCHO // 2, ALTO // 2), y, 1)
            # DibujarCuadrado
            pygame.draw.rect(ventana, COLORLOCO, (y, y, ANCHO - y * 2, ALTO - y * 2), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(1)  #fps

    pygame.quit()  # termina pygame

def dibujarParabola():
    pygame.init()# Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana
    reloj = pygame.time.Clock() # Limitar los fps.
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

         # Borrar pantalla
        ventana.fill(BLANCO)

        for y in range(0, 400, 10):#Separación de 10 pixeles.
            # Genera el cambio de color
            COLORLOCO = (randint(0, 255), randint(0, 255), randint(0, 255))
            # Dibujar parábolas:
            pygame.draw.line(ventana, COLORLOCO, (ANCHO // 2 + y, ALTO // 2), (ALTO // 2, y), 1)
            pygame.draw.line(ventana, COLORLOCO, (ANCHO//2 - y, ALTO//2),(ALTO//2,y),1)
            pygame.draw.line(ventana, COLORLOCO, (ANCHO // 2, ALTO - y), (ANCHO // 2 - y, ALTO // 2), 1)
            pygame.draw.line(ventana, COLORLOCO, (ANCHO//2, ALTO-y), (ANCHO//2+y, ALTO//2), 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(1)          # fps
    pygame.quit()   # termina pygame

def dibujarLaberinto():
    pygame.init() # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO)) #Crea la ventana
    reloj = pygame.time.Clock()# Limitar los fps.
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        for cambio in range (0, 400, 10): #Separación de 10 pixeles.
            # Genera el cambio de color
            COLORLOCO = (randint(0, 255), randint(0, 255), randint(0, 255))
            # Dibuja laberinto
            pygame.draw.line(ventana, COLORLOCO, (400 - cambio, 400 + cambio), (400 + 10 + cambio, 400 + cambio))
            pygame.draw.line(ventana, COLORLOCO, (410 + cambio, 400 + cambio),(400 + 10 + cambio, 400 - 10 - cambio))
            pygame.draw.line(ventana, COLORLOCO, (390 - cambio, 390 - cambio),(390 - cambio, 410 + cambio))
            pygame.draw.line(ventana, COLORLOCO, (410 + cambio, 390 - cambio),(390 - cambio, 390 - cambio))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(1)  # fps
    pygame.quit()  # termina pygame

def dibujarCirculosEntrelazados():

    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
         # Procesa los eventos que recibe
         for evento in pygame.event.get():
             if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                 termina = True

         # Borrar pantalla
         ventana.fill(BLANCO)

         for circulo in range(1, 13): #Cantidad de circulos
             # Genera el cambio de color
             COLORLOCO = (randint(0, 255), randint(0, 255), randint(0, 255))
             radio = 150  # radio de los círculos
             radianes = math.pi / 6  # conversión de grados entre los círculos a radianes.
             angulo = radianes * circulo #  centro del círculo
             posicionX =int((math.cos(angulo)*radio)) # centro del círculo
             posiciónY = int((math.sin(angulo))*radio) # centro del círculo
             # Dibuja circulos
             pygame.draw.circle(ventana, COLORLOCO, (400+posicionX, 400+posiciónY), radio, 1)

         pygame.display.flip()  # Actualiza trazos
         reloj.tick(1)  # fps
    pygame.quit()  # termina pygame

def aproximarPI(n):
    adición = 0
    for x in range (1,n+1,):
        adición=adición+(1/x**2)#División más contador.
        pi=(adición*6)**(1/2)
        return pi

def calcularDivisibles():
    contador = 0
    for dividendo in range(29,10000): #Números de cuatro dígitos
        if dividendo % 29 == 0:
            contador += 1
    return contador

def dibijarPiramide():
    contador1 = 1
    for x in range(1, 10):
        resultado1 = contador1 * 8 + x
        print("%d * 8 + %d = " % (contador1, x), resultado1)
        contador1 = (10 * contador1) + (x + 1)

        contador2 = 1
    for z in range(1, 10):
        resultado2 = contador2 * contador2
        print("%d * %d = %d" % (contador2, contador2, resultado2))
        contador2 = (contador2 * 10) + 1

def main():
    print("Tarea 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar espiral")
    print("3. Dibujar círculos")
    print("4. Dibujar parábolas")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 29")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    opcion = int(input("¿Qué desea hacer?: "))

    terminar = False

    while not terminar:
        if opcion == 1:
            dibujarCiculoCuadrado()
            opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 2:
            dibujarLaberinto()
            opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 3:
            dibujarCirculosEntrelazados()
            opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 4:
            dibujarParabola()
            opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 5:
            n = int(input("Inserte el número de divisores: "))
            print("PI es igual a: ", aproximarPI(n))
            opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 6:
            print("La cantidad de números de cuatro dígitos divisibles por 29 es de:", calcularDivisibles())
            opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 7:
            dibijarPiramide()
            opcion = int(input("¿Qué desea hacer? "))
        elif opcion == 0:
            print("¡Hasta pronto!")
            terminar = True
            quit()
        else:
            print("Error. Seleccione una de las opciones dadas.")
            opcion = int(input("¿Qué desea hacer? "))

main()