# encoding: UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Creación de figuras con Pygame

import pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
NEGRO = (0,0,0)     # R,G,B en el rango [0,255]
BLANCO = (255,255,255)
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

def dibujar(numero):
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

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        def dibujarCuadrosCirculos():
            lado = ANCHO
            x = 0
            radio = 10
            for lado in range(ANCHO, 0, -20):
                pygame.draw.rect(ventana, NEGRO, (x, x, lado,lado), 2)
                x += 10
                pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 2)
                radio += 10

            pygame.display.flip()  # Actualiza trazos
            reloj.tick(40)  # 40 fps


        def dibujarEspiral():
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = ALTO
            x3 = ANCHO
            y3 = ALTO
            x4 = ANCHO
            y4 = 0
            for x1 in range (0, ANCHO//2, 10):
                pygame.draw.line(ventana, NEGRO, (x1,y1), (x2,y2), 2)
                x3 -= 10
                pygame.draw.line(ventana, NEGRO, (x2, y2), (x3, y3), 2)
                x4 -= 10
                y4 += 10
                pygame.draw.line(ventana, NEGRO, (x3, y3), (x4, y4), 2)
                x1 += 10
                y1 += 10
                pygame.draw.line(ventana, NEGRO, (x4, y4), (x1, y1), 2)
                x2 += 10
                y2 -= 10
                pygame.draw.line(ventana, NEGRO, (x1, y1), (x2, y2), 2)
                y3 -= 10


        def dibujarCirculos():
            angulo = 0
            radio = 150
            for angulo in range (0, 360, 30):
                x = int(ANCHO//2 + (math.cos(math.radians(angulo)) * radio))
                y = int(ALTO//2 - (math.sin(math.radians(angulo)) * radio))
                pygame.draw.circle(ventana, NEGRO, (x, y), radio, 2)

            pygame.display.flip()  # Actualiza trazos
            reloj.tick(40)  # 40 fps


        def dibujarParabolas():
            from random import randint
            # Parte superior
            x1 = ANCHO//2
            y1 = 0
            x2 = ANCHO//2
            y2 = ALTO//2
            x5 = ANCHO//2
            y5 = ALTO//2
            for y1 in range (0, ALTO//2, 10):
                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (x1, y1), (x2, y2), 2)
                x2 += 10
                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (x1, y1), (x5, y5), 2)
                x5 -= 10
            # Parte inferior
            x3 = ANCHO//2
            y3 = ALTO
            x4 = ANCHO // 2
            y4 = ALTO // 2
            x6 = ANCHO // 2
            y6 = ALTO // 2
            for y3 in range (ALTO, ALTO//2, -10):
                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (x3, y3), (x4, y4), 2)
                x4 += 10
                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (x3, y3), (x6, y6), 2)
                x6 -= 10


        if numero == 1:
            dibujarCuadrosCirculos()
        elif numero == 2:
            dibujarEspiral()
        elif numero == 3:
            dibujarCirculos()
        elif numero == 4:
            dibujarParabolas()


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def ejecutarOtrasFunciones(numero):


    def calcularPi(n):
        divisor = 1
        resultado = 0
        for divisor in range (1, n+1, 1):
            division = 1/(divisor**2)
            resultado = resultado + division
            divisor += 1
        return resultado


    def aproximarPi(resultado):
        n = int(input("Inserte el valor del último divisor: "))
        resultado = calcularPi(n)
        pi = (resultado*6)**0.5
        print("La aproximación es: %.4f" % pi)


    def esDivisible(k):
        return k % 29 == 0


    def contarDivisibles(k):
        counter = 0
        print("Números de 4 dígitos divisibles entre 29:")
        for k in range(1000, 10000, 1):
            if esDivisible(k):
                print(k)
                counter += 1
        print("La cantidad de números divisibles entre 29 es: %d" % counter)


    def primerPiramide():
        numero = 1
        adicion = 2
        for adicion in range(1, 10, 1):
            resultado = (numero * 8) + adicion
            print("%d * 8 + %d = %d" % (numero, adicion, resultado))
            adicion += 1
            numero = (numero * 10) + adicion


    def segundaPiramide():
        numero = 1
        for k in range(9):
            resultado = numero ** 2
            print("%d * %d = %d" % (numero, numero, resultado))
            numero = (numero * 10) + 1


    def imprimirPiramides(numero):
        primerPiramide()
        print("")
        segundaPiramide()


    if numero == 5:
        aproximarPi(numero)
    elif numero == 6:
        contarDivisibles(numero)
    elif numero == 7:
        imprimirPiramides(numero)
    else:
        return


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
    numero = int(input("¿Qué desea hacer? "))
    if (1 <= numero <= 4):
        dibujar(numero)
    else:
        ejecutarOtrasFunciones(numero)

main()
