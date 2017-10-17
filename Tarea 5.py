#encoding: UTF-8
#Luis Fernando Figueroa Rendon, A01746139
#Programa que realiza varios ejercicios.

#importamos las librerias requeridas
import pygame
from random import randint
import math

#Se dan los valores de la ventana y se dan colores.
ANCHO=800
ALTO=800
NEGRO=(0,0,0)
BLANCO=(255,255,255)

#Funcion en la cual se dibuja en pygame una serie de cuadrados, uno mas grande que otro, y circulos dentro de esos cuadrados.
def dibujarCuadradosconCirculos():
    pygame.init()
    ventana=pygame.display.set_mode((ANCHO,ALTO))
    reloj=pygame.time.Clock()
    termina=False
    while not termina:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                termina=True
        ventana.fill(BLANCO)
        #Se dibuja el cuadrado.
        for x in range(0,ANCHO//2 +1,10):
            pygame.draw.rect(ventana,NEGRO,(ANCHO//2-x,ALTO//2-x,2*x,2*x),1)
        #Se dibuja el circulo.
        for x in range(10,ANCHO//2+1,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),x,1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

#Es la funcion DibujarCuadradosconCirculos, pero en esta funcion los circulos aparecen y desaparecen.
def dibujarCuadrosconCirculosM():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        #Se dibuja el cuadrado.
        for x in range(0, ANCHO // 2 + 1, 10):
            aleatorio= (randint(0, 255), randint(0, 255), randint(0,255))
            pygame.draw.rect(ventana, aleatorio, (ANCHO // 2 - x, ALTO // 2 - x, 2 * x, 2 * x), 1)
        #Se dibuja el circulo.
        for x in range(10, ANCHO // 2 + 1, 10):
            aleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.circle(ventana, aleatorio, (ANCHO // 2, ALTO // 2), x, 1)

            pygame.display.flip()
            reloj.tick(20)
    pygame.quit()

#Funcion que dibuja con parabolas una estrella.
def dibujarParabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for x in range(0, ANCHO // 2 + 1, 10):
            aleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, aleatorio, (ANCHO // 2, 0 + x), (ANCHO // 2 + x, ALTO // 2), 1)
            pygame.draw.line(ventana, aleatorio, (ANCHO // 2, ALTO - x), (ANCHO // 2 + x, ALTO // 2), 1)
            pygame.draw.line(ventana, aleatorio, (ANCHO // 2, 0 + x), (ANCHO // 2 - x, ALTO // 2), 1)
            pygame.draw.line(ventana, aleatorio, (ANCHO // 2, ALTO - x), (ANCHO // 2 - x, ALTO // 2), 1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

#Funcion que dibuja con lineas crecientes un espiral.
def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for x in range(0, ANCHO // 2 + 1, 10):
            aleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, aleatorio, (ANCHO // 2 - x, ALTO // 2 + x), (ANCHO // 2 + 5 + x, ALTO // 2 + x))
            pygame.draw.line(ventana, aleatorio, (ANCHO // 2 - 10 - x, ALTO // 2 - 10 - x),
                             (ANCHO // 2 + 5 + x, ALTO // 2 - 10 - x))
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + 5 + x, ALTO // 2 - 10 - x),
                             (ANCHO // 2 + 5 + x, ALTO // 2 + x))
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 - x), (ANCHO // 2 - x, ALTO // 2 + x))
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


#Funcion que dibuja 12 circulos con radio de 150 los cuales se tocan en alguna parte de la circunferencia.
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for x in range(0, 360, 30):
            aleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
            coseno = ((math.cos(x * math.pi / 180)))
            seno = ((math.sin(x * math.pi / 180)))
            pygame.draw.circle(ventana, aleatorio, (int(ANCHO / 2 + (150 * coseno)), int(ALTO / 2 + (150 * seno))), 150, 1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

#Funcion que calcula el valor aproximado de PI
def sacarPi(valor):
    #Acumulador igual a cero (sumatoria)
    suma=0
    for i in range (1, valor + 1):
        suma= suma + (1/(i**2))
    sumatoria= (suma * 6)**(1/2)
    return  sumatoria

#Funcion que calcula todos los numero de 4 digitos que son divisibles entre 29
def calcularDivisibles():
    #Acumulador igual a cero (sumatoria)
    divisibles = 0
    for numeros in range (1000, 10000):
        if (numeros%29) == 0:
            divisibles += 1
    return divisibles

#Funcion que con sumatorias refleja dos piramides con patrones diferentes.
def calcularPiramides():
    piramide = "\n"
    #Acumulador a 0 (sumatoria)
    escalera = 0
    #Sumatoria para sacar la primera piramide(1 * 8 + 1 = 9, .... , 123456789 * 8 + 9 = 987654321)
    for sumatoria in range(1, 10):
        escalera = int("1" * sumatoria) + escalera
        resultado = escalera * 8 + sumatoria
        piramide = piramide + ("%d * 8 + %d = %d\n" % (escalera, sumatoria, resultado))
    piramide += ''

    #Sumatoria para sacar la segunda piramide(1 * 1 = 1, ..... ,  111111111 * 111111111 =12345678987654321)
    for numero in range(1, 10):
        escalera = int("1" * numero)
        resultado = escalera * escalera
        piramide = piramide + ("%d * %d = %d\n" % (escalera, escalera, resultado))

    return piramide



def main():
    ejercicio= 1       #Valor que hace que el while se repita hasta que el usuario teclee 0
    #Menu del programa
    while ejercicio == 1:
        print("Tarea 5. Seleccione qué quiere hacer.")
        print("1. Dibujar cuadros y círculos.")
        print("2. Dibujar espiral.")
        print("3. Dibujar círculos.")
        print("4. Dibujar parábolas. ")
        print("5. Aproximar PI.")
        print("6. Contar divisibles entre 29.")
        print("7. Imprimir pirámides de números.")
        print("0. Salir.")
        dato= int(input("¿Qué desea hacer?"))
# Se establece que es lo que hara el programa al recibir ciertos valores.
        if dato == 1:
            print("1. Movimiento")
            print("2. Estatico")
            opcion=int(input("Como quieres que se vea el dibujo: "))
            if opcion==1:
                dibujarCuadrosconCirculosM()
            elif opcion==2:
                dibujarCuadradosconCirculos()
            else:
                print("Intenta 1 o 2: ")
        elif dato==2:
            dibujarEspiral()
        elif dato == 3:
            dibujarCirculos()
        elif dato == 4:
            dibujarParabolas()
        elif dato == 5:
            valor= int(input("¿Hasta que número deseas calcular?"))
            if valor > 0:
                print("El valor aproximado de PI es: ", sacarPi(valor))
        elif dato == 6:
            print("Hay" ,calcularDivisibles(), "divisibles de 29")
        elif dato == 7:
            print(calcularPiramides())
        else:
            ejercicio=0
            print("Hasta luego!")


main()

