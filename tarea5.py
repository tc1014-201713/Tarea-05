# encoding: UTF-8
# Autor: Jaime Orlando López Ramos, A01374696
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla, mas ejercicios for y uso del menú

import pygame
from random import randint
from math import cos
from math import sin
from math import radians

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)


def dibujarParabola():
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

        for i in range (0, ALTO//2 +1, 10):
            pygame.draw.line(ventana, ((randint(0, 255)), (randint(0, 255)), randint(0,255)), (i, ALTO//2), (ANCHO//2, ALTO//2 + i))
            pygame.draw.line(ventana, ((randint(0, 255)), (randint(0, 255)), randint(0, 255)),(ANCHO-i, ALTO//2), (ANCHO//2, ALTO//2 + i))
            pygame.draw.line(ventana, ((randint(0, 255)), (randint(0, 255)), randint(0, 255)), (ANCHO-i, ALTO // 2), (ANCHO // 2, ALTO//2 - i))
            pygame.draw.line(ventana, ((randint(0, 255)), (randint(0, 255)), randint(0, 255)), (i, ALTO // 2), (ANCHO // 2, ALTO // 2 - i))


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

def dibujarCuadradoCirc():
        # Ejemplo del uso de pygame
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
        for i in range (0, 401, 10):
#Líneas derecha
            pygame.draw.line(ventana, (50, 50, 50), (0 + i, 0 +i), (0 + i, ALTO - i), 1)
        for i in range (0, 401, 10):
            pygame.draw.line(ventana, (50, 50, 50), (ANCHO-i, ALTO-i), (ANCHO-i, 0+i), 1)
        for i in range (0, 401, 10):
            pygame.draw.line(ventana, (50, 50, 50), (0+i, 0+i), (ANCHO-i, 0 + i), 1)
        for i in range (0, 401, 10):
            pygame.draw.line(ventana, (50, 50, 50), (0+i, ALTO - i), (ANCHO-i, ALTO-i))
        for i in range (1, 402, 10):
            pygame.draw.circle(ventana, (50, 50, 50), (ANCHO//2, ALTO//2), i, 1)


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps


    pygame.quit()   # 'termina pygame'

def numero29():
    x=0
    for i in range (1000, 10000, 1):
        if i%29 == 0:
            x+= 1
            #print(i)
    print(x, "números son divisibles entre 29")

def calcularPi():
    r = 0
    num= int(input("Ingrese un número para aproximar pi: "))
    for i in range (1,num+1, 1):
        eq= (1/(i)**2)
        r = eq + r

    pi = (r*6)**0.5
    print("%.4f" % (pi))

def dibujarLaberinto():
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
        xi = 400
        yi = 400
        xf = 410
        yf = 400
        counter = 20

        # Dibujar, aquí haces todos los trazos que requieras
        for i in range(0, 401, 10):
            pygame.draw.line(ventana, NEGRO, (xi, yi), (xf, yf), 1)
            xi = xf
            yi = yf
            xf = xi
            yf = yi - counter
            counter += 5
            pygame.draw.line(ventana, NEGRO, (xi, yi), (xf, yf), 1)
            xi = xf
            yi = yf
            xf = xi - counter
            yf = yi
            counter += 5

            pygame.draw.line(ventana, NEGRO, (xi, yi), (xf, yf), 1)
            xi = xf
            yi = yf
            xf = xi
            yf = yi + counter
            counter += 5

            pygame.draw.line(ventana, NEGRO, (xi, yi), (xf, yf), 1)
            xi = xf
            yi = yf
            xf = xi + counter
            yf = yi
            counter += 5

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

def dibujarCirculos():
    # Ejemplo del uso de pygame
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
        for i in range (0, 360, 30):
            pygame.draw.circle(ventana, NEGRO, (int(400 + 150*cos(radians(i))), int(400-150*sin(radians(i)))), 150, 1)






        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

def crearPiramide():
    n = 1
    p = 1
    print("""
    Pirámide 1: """)
    for i in range(9):
            print (n, "* 8 +", p, "=", (n * 8 + p) )
            p = p + 1
            n = n * 10 + p

    x = 1
    print("""
    Pirámide 2: """)
    for i in range(9):
        print(x, "*", x, "=", x*x)
        x = x * 10 +1

def main():
    a= 1
    while (a > 0):

        a = int(input("""
        1. dibujar cuadros y círculos
        2. Dibujar espiral
        3. Dibujar círculos
        4. Dibujar parábolas
        5. Aproximar Pi
        6. Contar divisibles entre 19
        7. Imprimir pirámides de números
        0. Salir
        Teclee el número deseado: """))
        if a == 1:
            dibujarCuadradoCirc()
        elif a == 2:
            dibujarLaberinto()
        elif a == 3:
            dibujarCirculos()
        elif a == 4:
            dibujarParabola()
        elif a == 5:
            calcularPi()
        elif a == 6:
            numero29()
        elif a == 7:
            crearPiramide()
        elif (a>7):
            print ("Número no válido, vuelva a intentar.")

    print ("Programa termidado")

main()