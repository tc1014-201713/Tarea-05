# encoding: UTF-8
# Autor: Pedro Cortés Soberanes


import pygame
import random

######################################################################################################################################

#Graficos PyGame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)
        # Dibujar

        #1

def dibujarCuadrosyCirculos():
    x = ANCHO // 2
    y = ALTO // 2
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

        for z in range (10, 402,10):
            pygame.draw.rect(ventana,NEGRO,(z,z, (ANCHO)-2*z, (ALTO)-2*z),2)
            pygame.draw.circle(ventana, NEGRO, (x, y), z, 2)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


        #2

def dibujarParabolas():
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

        for a in range (0,401,10):
            pygame.draw.line(ventana, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (ANCHO//2, a), (ALTO//2-a, ANCHO//2), 1)
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(ANCHO // 2 + a, ANCHO//2),(ANCHO // 2, a) , 1)


            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (ANCHO // 2, ALTO - a), (ANCHO // 2 - a, ALTO // 2), 1)
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(ANCHO // 2, ALTO - a), (ANCHO // 2 + a, ALTO // 2), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame

        #3

def dibujarEspiral():
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

        for o in range(0, 401, 10):
            pygame.draw.line(ventana, NEGRO, (ANCHO//2, ALTO//2), ((ANCHO//2)+o,ALTO//2), 2)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 +o, ALTO // 2), (ANCHO // 2+o, ALTO // 2-o), 2)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2+o, ALTO // 2-o), ((ANCHO // 2) - o, ALTO // 2-o), 2)
            pygame.draw.line(ventana, NEGRO, ((ANCHO // 2) - o, ALTO // 2 - o), (ANCHO // 2 - o, ALTO // 2 + o), 2)


            pygame.draw.line(ventana, NEGRO, (ANCHO // 2-o, ALTO // 2+o), ((ANCHO // 2) + o, ALTO // 2-o), 2)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + o, ALTO // 2-o), (ANCHO // 2 - o, ALTO // 2 + o), 2)


            
            pygame.draw.line(ventana, NEGRO, (ANCHO//2 , o), (ANCHO , o), 2)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


        #4

def dibujarCirculos():
    radio = 150
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

        for c in range(1, 15, 8):
            pygame.draw.circle(ventana, NEGRO, ((ALTO//2), (ANCHO//2)), radio, 2)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


'''
  pygame.draw.rect(ventana, VERDE_BANDERA, (30, 30, ANCHO-60, ALTO-60) , 5 )
  pygame.draw.circle(ventana, ROJO, (ANCHO//2, ALTO//2), 200, 2)
  pygame.draw.line(ventana, VERDE_BANDERA,(0,ALTO),(ANCHO,0),10)
  '''
'''''
for y in range(0,ALTO,20):
    pygame.draw.line(ventana, ROJO, (0, y), (ANCHO, y), 2)

for x in range(0,ANCHO,20):
    pygame.draw.line(ventana, ROJO, (x, 0), (x, ALTO), 2)
'''

######################################################################################################################################

#PI

def aproximarPI(n):
    suma = 0
    for d in range(1,n+1):
        suma = suma + (1/(d**2))
    return (suma*6)**.5

######################################################################################################################################

#Divisibles entre 19

def calcularDividibles():
    cn = 0
    for i in range (1000,10000,1):
        if i%19== 0:
            cn += 1
    print("->", cn)


######################################################################################################################################

#Piramides

def imprimirPiramides():
    for i in range(1, 10):
        factor = i
        factor = factor* "1"
        resultado = (((10 ** i - 1) // 9) ** 2)
        print("%s * %s = %d" % (factor, factor, resultado))




######################################################################################################################################

#Función main y menu

def main():
    opcion = -1
    while opcion !=0:
        print ("1. Dibujar Cuadrados y Círculos ")
        print ("2. Dibujar Parabolas")
        print ("3. Dibujar Espiral")
        print ("4. Dibujar Círculos")
        print ("5. Aproximar PI")
        print ("6. Contar Divisibles entre 19")
        print ("7. Imprimir piramides de números")
        print ("0. Salir ")
        opcion = int (input("¿Que desea hacer?: "))
        if opcion == 1:
            dibujarCuadrosyCirculos()
        elif opcion == 2:
            dibujarParabolas()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
            n = int(input("¿Que valor quieres de denominador?"))
            aproximarPI(n)
        elif opcion == 6:
            calcularDividibles()
        elif opcion == 7:
            imprimirPiramides()
        elif opcion == 0:
            print ("Adios :)")













main()
