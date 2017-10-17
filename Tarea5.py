# Autor: Mónica Monserrat Palacios Rodríguez, A01375137
# UTF-8
# Tarea 5

import pygame
import math
from random import randint

#Se establecen las variables constantes
ANCHO = 800
ALTO = 800

NEGRO = (0,0,0)
BLANCO = (255, 255, 255)
opcion = 1

#Primera función, dibuja cuadros y círculos crecientes
def dibujarCuadrosYCirculos():
    pygame.init () #Se inicia pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina: #While para que no se cierre hasta que se indique
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        v1 = 400 #se establecen estas variables para las coordenadas
        v2 = 0

        for i in range(0, 40, 1):
            v1 = v1-10 #Se acumula el valor en las variables i veces
            v2 = v2+(2*10)
            pygame.draw.rect(ventana, NEGRO, (v1, v1, v2, v2), 1) #Se dibuja el cuadrado con las variables que usamos

        for i in range(10, 400, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), i, 1) #Se dibuja el círculo
        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

#Segunda función, se dibujan líneas para cada cuadrante con un for y crea una parábola
def dibujarParabola():
    pygame.init() #Se inicia Pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina: #Ciclo while para que siga corriendo hasta que se indique lo contrario

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

            ventana.fill(BLANCO)

        for i in range (0, 400, 10): #Se dibujan las líneas para cada cuadrante
            random = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, random, (ANCHO // 2 + i, ALTO // 2), (ALTO // 2, i), 1)
            pygame.draw.line(ventana, random, (ANCHO // 2 - i, ALTO // 2), (ALTO // 2, i), 1)
            pygame.draw.line(ventana, random, (ANCHO // 2, ALTO - i), (ANCHO // 2 - i, ALTO // 2), 1)
            pygame.draw.line(ventana, random, (ANCHO // 2, ALTO - i), (ANCHO // 2 + i, ALTO // 2), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

#Tercer función, se dibuja un espiral con líneas divididas
def dibujarEspiral():
    pygame.init() #Se inicia pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina: #Ciclo while para que siga corriendo hasta que se indique lo contrario

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina=True

            ventana.fill(BLANCO)
        finx1 = 400 #Inicio de la línea
        finy1 = 400

        for i in range (0,40,1):
            contadorA = 5+(i*20)
            contadorB = 10+(i*20)
            contadorC = 15+(i*20)
            contadorD = 20+(i*20)


            inicioax = finx1
            inicioay = finy1
            finax = finx1 + contadorA
            finay = finy1
            pygame.draw.line(ventana, NEGRO, (inicioax, inicioay), (finax, finay), 1)

            iniciobx = finax
            inicioby = finay
            finbx = finax
            finby = finay-contadorB
            pygame.draw.line(ventana, NEGRO, (iniciobx, inicioby), (finbx, finby), 1)

            iniciocx = finbx
            iniciocy = finby
            fincx = finbx-contadorC
            fincy = finby
            pygame.draw.line(ventana, NEGRO, (iniciocx, iniciocy), (fincx, fincy), 1)

            iniciodx = fincx
            iniciody = fincy
            findx = fincx
            findy = fincy + contadorD
            pygame.draw.line(ventana, NEGRO, (iniciodx, iniciody), (findx, findy), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

# Cuarta función, dibuja 12 círculos a partir de un for para teta
def dibujarCirculos():
    pygame.init() #Se inicia pygame
    ventana = pygame.display.set_mode((ALTO, ANCHO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina: #Ciclo while para que siga corriendo hasta que se indique lo contrario
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)


        r = 150 #Radio

        for teta in range(0, 360, 30):
            anguloRadianes = teta*(math.pi/180) #de grados a radianes
            x = int(r * math.cos(anguloRadianes))
            y = int(r * math.sin(anguloRadianes))

            pygame.draw.circle(ventana, NEGRO, (400 + x, 400 + y), r, 1) #Se dibujan los círculos

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

#Quinta función, calcula la aproximación de Pi
def aproximarPi(n):
    suma = 0 #Se establece la suma
    for i in range(1, n + 1):
        suma = suma + (1 / i ** 2)
        pi = (6 * (suma)) ** (1 / 2)

    return pi #regresa pi

#Sexta función, calcula cuántos números de 4 dígitos hay divisibles entre 19
def calcularNumerosDivisibles():
    num_divisibles = 0
    for i in range(1000, 10000): #Para los cuatro dígitos
        if (i % 19) == 0:
            num_divisibles += 1

    return num_divisibles

#Séptima función, realiza una pirámide con números a partir de un for
def calcularPiramides():
    piramide = "\n"
    incremento = 0
    resultado = 0

    for i in range(1, 10, 1):
        incremento = int("1" * i) + incremento
        resultado = (resultado * 8) + i
        piramide = piramide + ("%d * 8 + %d = %d\n" % (incremento, i, resultado))


    for i in range(1, 10, 1):
        incremento = int("1" * i)
        resultado = incremento * incremento
        piramide = piramide + ("%d * %d = %d\n" % (incremento, incremento, resultado))

    return piramide #Regresa las pirámides


def main(): #Menú
  print ("""
  
  Tarea 5. Seleccione qué quiere hacer.
  1. Dibujar cuadros y círculos
  2. Dibujar espiral
  3. Dibujar círculos
  4. Dibujar parábolas
  5. Aproximar Pi
  6. Contar divisibles entre 19
  7. Imprimir pirámides de números
  0. Salir
  """)
  #While para que siga preguntando las opciones
  opcion = 1
  while opcion!= 0:
        print(" ")
        opcion = int(input("¿Qué desea hacer? : "), )
        if opcion < 0 or opcion > 7:
             print("El número %d no es una opción válida. " % opcion)
        elif opcion == 0:
             print("¡Adiós!")
        else:
             if opcion == 1:
                dibujarCuadrosYCirculos()
             if opcion == 2:
                dibujarEspiral()
             if opcion == 3:
                dibujarCirculos()
             if opcion == 4:
                dibujarParabola()
             if opcion == 5:
                num = aproximarPi(int(input("Ingresa un número : ")))
                print("La aproximación es: %.8f" % num)
             if opcion == 6:
                num = calcularNumerosDivisibles()
                print("Hay %d números de 4 dígitos divisibles entre 19." % num)
             if opcion == 7:
                piramides = calcularPiramides()
                print(piramides)
             if opcion == 0:
                print("¡Adiós!")

main()