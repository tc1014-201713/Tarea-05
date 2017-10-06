# encoding: UTF_8
# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
#Juntar todos los ejercicios para que el usuario pueda ver lo que quiera

#imports

import pygame
import random
import math

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

#Ventana
ventana = (ANCHO, ALTO)

#colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

#dibuja el primer patron a)
def a():
    pygame.init() #inicia pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO)) #tamaño de ventana
    reloj = pygame.time.Clock() #reloj
    termina = False #ciclo para cuando termine
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(negro) # pone en negro el fondo
        #dibujo
        for distancia in range(10, 400, 10):
            pygame.draw.circle(ventana, blanco, (400, 400), (distancia), 1)   # dubuja el circulo
            pygame.draw.rect(ventana, blanco,((distancia), (distancia), (800 - (distancia * 2)), (800 - (distancia * 2))), 1) #dibuja el cuadrado
        pygame.display.flip()
        reloj.tick(1) #temporisador
    pygame.quit() #cierra pygame

#dibuja el 2 patron b)
def b():
    pygame.init() #inicia pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO)) #tamaño de ventana
    reloj = pygame.time.Clock() #reloj
    termina = False  #ciclo para cuando termine
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(negro) #pone en negro el fondo
        for distancia in range(0, 405, 5):
            # color (se pone aqui ya que si la ponemos en colores no se actualiza)
            RANDOM = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #este colo tiene que ir aqui apra que se actualice y cambie cada vez que se pida
            #dibujo
            pygame.draw.line(ventana, RANDOM, (400 - distancia, 400), (400, 0 + distancia))  # dibuja lineas en distinto plano carteciano
            pygame.draw.line(ventana, RANDOM, (400 + distancia, 400), (400, 0 + distancia))
            pygame.draw.line(ventana, RANDOM, (400 + distancia, 400), (400, 800 - distancia))
            pygame.draw.line(ventana, RANDOM, (400 - distancia, 400), (400, 800 - distancia))

        pygame.display.flip()
        reloj.tick(1) #temporisador
    pygame.quit() #cierra pygame
#dubuja el 3 patron c)
def c():
    pygame.init() #inicia pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO)) #tamaño de ventana
    reloj = pygame.time.Clock() #reloj
    termina = False  #ciclo para cuando termine
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(negro) #pone en negro el fondo
        #dibujo
        for d in range(0, 400, 10):
            pygame.draw.line(ventana, blanco, (405 - d, 400 + d), (405 + d, 400 + d)) # dibuja lineas a distinta distancia
            pygame.draw.line(ventana, blanco, (405 + d, 400 + d), (405 + d, 395 - d))
            pygame.draw.line(ventana, blanco, (405 + d, 395 - d), (395 - d, 395 - d))
            pygame.draw.line(ventana, blanco, (395 - d, 395 - d), (395 - d, 410 + d))
        pygame.display.flip()
        reloj.tick(1) #temporisador
    pygame.quit() #cierra pygame
#dibuja el 4 patron d)
def d():
    pygame.init() #inicia pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO)) #tamaño de ventana
    reloj = pygame.time.Clock() #reloj
    termina = False #ciclo para cuando termie
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(negro) #pone en negro la pantalla
        for d in range(0, 330, (int(360 / 11))): #hace 12 ángulos, 360 / 12
            pygame.draw.circle(ventana, blanco, (int((math.cos(d) * 150) + 400), int((math.sin(d) * 150) + 400)), (150), 1) #dibuja el circulo
        pygame.display.flip()
        reloj.tick(1) #temporisador
    pygame.quit() #cierra pygame
#funcion de pi
def calcularpi():
    x = 0
    for i in range(1, 1000000000): #cambia i, empezando por uno hasta un valor para asemejarse a i
        x += (1/(i**2)) #suma el valor que resulta de 1/i^2
    x = (x * 6) ** (1/2) #hace la operacion para convertir en pi
    return(x)
#numeros de 4 dijitos divisibles entre 29
def dividir():
    x = 0
    for i in range(1000, 10000): #usa los numeros del 1000 al 9999 que son todos los que son de 4 dijitos
        if (i % 29) == 0: #ve si es divisible
            x += 1  #si se cumple suma 1
    return(x) #regresa x
#escribir numero
def imprimirNumero(): # imprime la serie de numeros que piden
    for n in range(1,10):
        print((str(numero(n))) + " * 8 + " + (str(n)) + " = " + (str((int(numero(n))) * 8 + n))) #serie de 123456789
    for n in range(1,10):
        print(((str(1)) * n) + " * " + ((str(1)) * n) + " = " + (str((int((str(1)) * n)) * (int((str(1)) * n))))) #serie 1111111...
def numero(n): # hace el numero: 123456789
    x = ""
    for i in range(1, (n +1)):
        x = str(x) + (str(i)) # junta el numero donde esta n al anterior
    return(x)
# funcion main
def main(): #funcion main
    jugar = 1 #ciclo para jugar
    while jugar == 1:
        accion = int(input(""" Tarea 5. Seleccione qué quiere hacer.
        1. Dibujar cuadros y círculos
        2. Dibujar espiral
        3. Dibujar círculos
        4. Dibujar parábolas
        5. Aproximar PI
        6. Contar divisibles entre 29
        7. Imprimir pirámides de números
        0. Salir
        ¿Qué desea hacer?""")) #escribe todo esto
        #selecciona la accion que tu dices
        if accion == 0:
            jugar = 0
        elif accion == 1:
            a()
        elif accion == 2:
            b()
        elif accion == 3:
            c()
        elif accion == 4:
            d()
        elif accion == 5:
            print("""si su computadora es lenta, puede que esto tarde si es asi, entre al codigo y cambie en la linea 104 el valor de 1000000000 a"
un valor con menos 0, esto hara que se aleje de pi pero tardara menos""") #por si tienes una compu de poco rendimiento
            print(calcularpi())
        elif accion == 6:
            print(dividir())
        elif accion == 7:
            print(imprimirNumero())
        else:
            print("Debes de escribir un número válido")  #por si no pones un número válido
main()