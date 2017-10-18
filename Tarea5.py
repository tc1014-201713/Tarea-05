#UTF-8
#Natalia Meraz Tostado
#Hacer la tarea 5

import sys
import pygame
from math import sin
from math import cos

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


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
# R,G,B en el rango [0,255]
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
NARANJA = (255, 128, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)


def dibujarCuadrosyCirculos():
        x = 10
        y = 10
        pygame.init()  # Inicializa pygame
        ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
        reloj = pygame.time.Clock()  # Para limitar los fps
        termina = False  # Bandera para saber si termina la ejecución

        while not termina:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                    termina = True

            ventana.fill(NEGRO)

            for x in range(10, (ANCHO // 2), 10):
                UX = ANCHO
                UY = ALTO
                UX -= x * 2
                UY -= x * 2
                pygame.draw.rect(ventana, AZUL, (x, x, UX, UY), 1)
                pygame.draw.circle(ventana, AZUL, (ANCHO // 2, ALTO // 2), x, 1)

            # pygame.draw.circle(ventana, ROJO, (ANCHO//2, ALTO//2), 200, 2)

            pygame.display.flip()  # Actualiza trazos
            reloj.tick(40)  # 40 fps

        pygame.quit()  # termina pygame


def dibujarEspiral():
        x = 10
        p = ANCHO // 2
        pygame.init()  # Inicializa pygame
        ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
        reloj = pygame.time.Clock()  # Para limitar los fps
        termina = False  # Bandera para saber si termina la ejecución

        while not termina:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                    termina = True

            ventana.fill(NEGRO)

            for x in range(0, ANCHO // 2, 10):
                pygame.draw.line(ventana, NARANJA, ((p + 5) - x, p + x), ((p + 5) + x, p + x), 1)
                pygame.draw.line(ventana, NARANJA, ((p + 5) + x, p + x), ((p + 5) + x, (p - 5) - x), 1)
                pygame.draw.line(ventana, NARANJA, ((p + 5) + x, (p - 5) - x), ((p - 5) - x, (p - 5) - x), 1)
                pygame.draw.line(ventana, NARANJA, ((p - 5) - x, (p - 5) - x), ((p - 5) - x, (p + 10) + x), 1)

            # pygame.draw.circle(ventana, ROJO, (ANCHO//2, ALTO//2), 200, 2)

            pygame.display.flip()  # Actualiza trazos
            reloj.tick(40)  # 40 fps

        pygame.quit()  # termina pygame


def dibujarCirculos():
        radio = 150
        pi = 3.1416
        pygame.init()  # Inicializa pygame
        ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
        reloj = pygame.time.Clock()  # Para limitar los fps
        termina = False  # Bandera para saber si termina la ejecución

        angulo = 0
        while not termina:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                    termina = True

            ventana.fill(NEGRO)

            for x in range(0, 13, 1):
                angulo = angulo + (2 * pi) / 12

                x = int(radio * sin(angulo)) + 400
                y = int(radio * cos(angulo)) + 400

                pygame.draw.circle(ventana, AZUL, (x, y), radio, 1)

            # pygame.draw.circle(ventana, ROJO, (ANCHO//2, ALTO//2), 200, 2)

            pygame.display.flip()  # Actualiza trazos
            reloj.tick(40)  # 40 fps

        pygame.quit()  # termina pygame


def dibujarEstrella():
        p = ANCHO // 2
        pygame.init()  # Inicializa pygame
        ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
        reloj = pygame.time.Clock()  # Para limitar los fps
        termina = False  # Bandera para saber si termina la ejecución

        while not termina:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                    termina = True

            ventana.fill(NEGRO)

            for x in range(0, ANCHO // 2, 10):
                pygame.draw.line(ventana, NARANJA, ((p + 5) - x, p + x), ((p + 5) + x, p + x), 1)
                pygame.draw.line(ventana, NARANJA, ((p + 5) + x, p + x), ((p + 5) + x, (p - 5) - x), 1)
                pygame.draw.line(ventana, NARANJA, ((p + 5) + x, (p - 5) - x), ((p - 5) - x, (p - 5) - x), 1)
                pygame.draw.line(ventana, NARANJA, ((p - 5) - x, (p - 5) - x), ((p - 5) - x, (p + 10) + x), 1)

            # pygame.draw.circle(ventana, ROJO, (ANCHO//2, ALTO//2), 200, 2)

            pygame.display.flip()  # Actualiza trazos
            reloj.tick(40)  # 40 fps

        pygame.quit()  # termina pygame


def calcularPI(n):
        suma = 0
        contador = 0
        for d in range(1, (n + 1) ** 2, 2):
            contador += 1
            if contador % 2 == 0:
                suma -= (1 / d)
            else:
                suma += (1 / d)

        return 4 * suma


def calcularNumero():
        numero = 0
        for n in range(1000, 10000, 1):

            if n % 29 == 0:
                numero += 1

        return numero


def crearPiramide():
        numero = 0
        for n in range(0, 9, 1):
            numero = numero + (10 ** n)
            resultado = numero ** 2
            print(numero, "*", numero, "=", resultado)

        valor = 0
        for x in range(1, 10, 1):
            for y in range(0, x, 1):
                valor += (10 ** y)
            piramide = ((valor * 8) + x)
            print(valor, "*", y, "=", piramide)

if opcion == 1:
    dibujarCuadrosyCirculos()

elif opcion == 2:
    dibujarEspiral()

elif opcion == 3:
    dibujarCirculos()

elif opcion == 4:
    dibujarEstrella()

elif opcion == 5:
    print(calcularPI(895))

elif opcion == 6:
    print(calcularNumero())

elif opcion == 7:
    print(crearPiramide())

elif opcion == 0:
    sys.exit


def main():
    dibujarCuadrosyCirculos()
    dibujarEspiral()
    dibujarCirculos()
    dibujarEstrella()
    calcularPI(895)
    calcularNumero()
    crearPiramide()

main()