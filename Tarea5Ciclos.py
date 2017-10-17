# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González A01745998
# Descripción: Menú que da opciones para distintas funciones

# Importaciones
import pygame
from random import randint
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
NEGRO = (0, 0, 0)

def dibujarCuadrosYCirculos():
    # círculo & cuadrado
    x = ANCHO // 2 # centro
    y = ALTO // 2 # centro
    r = 10 # radio
    l = r * 2 # longitud
    xC = ANCHO // 2 - r # x del cuadrado
    yC = ALTO // 2 - r # y del cuadrado

    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        # Borrar pantalla
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras
        for factor in range (1, ANCHO//20):
            pygame.draw.circle(ventana, NEGRO, (x, y), r * factor, 1)

        for factor in range (0, ANCHO//20):
            pygame.draw.rect(ventana, NEGRO,(xC - r*factor, yC - r*factor, l + 2*r*factor, l + 2*r*factor), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps
    pygame.quit()

def dibujarParabolas():
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
        for separacion in range (0,ALTO // 2,10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO, (ANCHO//2, separacion), ((ANCHO//2) - separacion, ALTO//2), 1)
        for separacion in range(0, ALTO // 2, 10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO, (ANCHO//2, separacion), ((ANCHO // 2) + separacion, ALTO // 2), 1)
        for separacion in range(0, ALTO // 2, 10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - separacion), ((ANCHO // 2) + separacion, ALTO // 2), 1)
        for separacion in range(0, ALTO // 2, 10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - separacion), ((ANCHO // 2) - separacion, ALTO // 2), 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps
    pygame.quit()   # termina pygame

def dibujarEspiral():
    x = ANCHO // 2 # centro
    y = ALTO // 2 # centro
    separacion = 10 # separacion entre paredes

    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        # Borrar pantalla
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras
        for d in range(0, x + 1, separacion):
            pygame.draw.line(ventana, NEGRO, (x - d, y + d), (x + separacion + d, y + d))
            pygame.draw.line(ventana, NEGRO, (x + separacion + d, y + d), (x + separacion + d, y - separacion - d))
            pygame.draw.line(ventana, NEGRO, (x - separacion - d, y - separacion - d), (x - separacion - d, y + separacion + d))
            pygame.draw.line(ventana, NEGRO, (x + separacion + d, y - separacion - d), (x - separacion - d, y - separacion - d))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps
    pygame.quit()  # termina pygame

def dibujar12Circulos():
    x = ANCHO // 2 # centro
    y = ALTO // 2 # centro
    radio = 150 # radio de los círculos
    radianes = math.pi/6 # transformación de los grados entre cada círculo y otro a radianes. En este caso pi/6 es igual a 30º

    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        # Borrar pantalla
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras
        for circulo in range(1, 13):
            angulo = radianes * circulo # ubicación del centro de un círculo
            xC = int((math.cos(angulo))*radio) # centro del círculo
            yC = int((math.sin(angulo))*radio) # centro del círculo
            pygame.draw.circle(ventana, NEGRO, (x+xC, y+yC), radio, 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps
    pygame.quit()  # termina pygame

def aproximarPI(n):
    suma = 0
    contador = 0
    for d in range(1,n+1):
        contador += 1
        suma = suma + 1/(d**2)
    return (6*suma)**0.5

def calcularDivisibilidad(n):
    contador = 0
    for dividendo in range(1000,10000): # Del mil al 9999; números de cuatro dígitos
        if dividendo % n == 0:
            contador += 1
    return contador

def imprimirPiramidesDeNumeros():
    acumulador = 1
    factor = 8 # para que la pirámide aparezca
    for nivel in range(1,10):
        resultado = (acumulador * factor) + nivel
        print("%d * %d + %d = %d" % (acumulador, acumulador, nivel, resultado))
        acumulador = (10 * acumulador) + (nivel + 1)

    print("---------------------------------------")

    acumulador = 1
    for nivel in range(1,10):
        resultado = acumulador * acumulador
        print("%d * %d = %d" % (acumulador, acumulador, resultado))
        acumulador = (acumulador * 10) + 1

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
    decision = int(input("¿Qué desea hacer? "))

    salir = False
    while not salir:
        if decision == 0:
            print("¡Hasta pronto!")
            salir = True
            quit()

        elif decision == 1:
            dibujarCuadrosYCirculos()

        elif decision == 2:
            dibujarEspiral()

        elif decision == 3:
            dibujar12Circulos()

        elif decision == 4:
            dibujarParabolas()

        elif decision == 5:
            n = int(input("Inserte el número de divisores para hacer la aproximación: "))
            print("PI es igual a: ", aproximarPI(n))

        elif decision == 6:
            print("La cantidad de números de cuatro dígitos divisibles por 29 es de:", calcularDivisibilidad(29))
            # cambiar argumento en caso de elegir otro divisor

        elif decision == 7:
            imprimirPiramidesDeNumeros()

        else:
            print("Error. Introduzca un número válido.")

        decision = int(input("¿Qué desea hacer? "))

main()