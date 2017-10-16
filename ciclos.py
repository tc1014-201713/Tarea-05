#encoding:UTF-8
#Autor: José Antonio Gómez Mora
#El programa lee la ocpción que seleccione el usuario en el menú y la ejecuta.
import pygame
import math
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
NEGRO = (0,0,0)
COLORES=randint(0,255)

def dibujarCuadrosCirculos():
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
        for x in range (0,ANCHO+10,10):
        # Dibujar, aquí haces todos los trazos que requieras
            pygame.draw.rect(ventana, NEGRO, (ANCHO//2-x/2,ALTO//2-x/2,x,x), 1)
        for x in range (0,ANCHO//2,5):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),5+x,1)

            #pygame.draw.circle(ventana, NEGRO, (ANCHO//2-1, ALTO//2-1), x, 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(1)          # 40 fps

    pygame.quit()   # termina pygame

def dibujarParabolas():
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
        #for x in range(0, ANCHO + 10, 10):
            # Dibujar, aquí haces todos los trazos que requieras
        for x in range (ANCHO//80,ANCHO//2+ANCHO//80+ANCHO//80,ANCHO//80):
            pygame.draw.lines(ventana,NEGRO,False,((ANCHO//2,ANCHO//80+x),(ANCHO//2-x,ALTO//2),(ANCHO//2,ALTO+ANCHO//80-x),(ANCHO//2+x,ALTO//2),(ANCHO//2,ANCHO//80+x)),1)

            # pygame.draw.circle(ventana, NEGRO, (ANCHO//2-1, ALTO//2-1), x, 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(1)  # 40 fps

    pygame.quit()  # termina pygame

def dibujarPiramide():
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
        for x in range (ANCHO//80,ANCHO,ANCHO//80):
            pygame.draw.lines(ventana,NEGRO,False,((ANCHO//2+ANCHO//80-x,ALTO//2-ANCHO//80+x),(ANCHO//2+x,ALTO//2-ANCHO//80+x),(ANCHO//2+x,ALTO//2-x),(ANCHO//2-x,ALTO//2-x),(ANCHO//2-x,ALTO//2+x)),1)



        pygame.display.flip()  # Actualiza trazos
        reloj.tick(1)  # 40 fps

    pygame.quit()  # termina pygame

def dibujarCirculos():
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

        for x in range (1,13,1):
            #Sabemos las medidas del circulo unitario. Cada 30° es igual a pi/6. 360°=2pi. Por lo tanto varía el numerador.
            #Para el ciclo for lo establecemos que de 12 vueltas para cumplir 12/6pi=2pi.
            #Establecemos los puntos para dibujar los círculos con las funciones coseno para 'x' y seno para 'y'.
            #Sumamos +1 porque python redondea hacia abajo, por lo tanto perdemos -1.
            pygame.draw.circle(ventana,NEGRO,(int((math.cos(x*math.pi/6)*150)+1)+ANCHO//2,int((math.sin(x*math.pi/6)*150)+1)+ALTO//2),150,1)



        pygame.display.flip()  # Actualiza trazos
        reloj.tick(1)  # 40 fps

    pygame.quit()

def calcularPi(divisor):
    suma=0
    for k in range(1, divisor + 1):
        pi= 1 / k ** 2
        suma+=pi
    return (suma*6)**(1/2)

def calcularSeries():
    suma=0
    for x in range(1,10,1):
        suma+=1
        resultado=(suma)*8+x
        print("%d x 8 + %d = %d "%(suma,x,resultado))
        suma=(suma*10)+x
    suma=0
    for numero in range(1,10):
        suma+=1
        resultado=suma*suma
        print ("%d x %d = %d"%(suma,suma,resultado))
        suma=suma*10

def calcularDivisible():
    counter = 0
    for esDivisible in range (1000,10001):
        if esDivisible%29==0:
            counter+=1
    return counter

def main():

    menu=True

    if menu==True:
        print("""Tarea 5. Seleccione que desea hacer:

        1. Dibujar cuadrados y círculos
        2. Dibujar parábolas
        3. Dibujar pirámide
        4. Dibujar círculos entrelazados
        5. Aproximar Pi
        6. Contar divisibles entre 29
        7. Imprimir pirámides de números
        0. Salir""")

    while menu==True:

        seleccion=int(input("\n¿Qué desea hacer?: "))

        while seleccion>=8:
            print("La opción número %d no se encuentra en el menú."%seleccion)
            seleccion = int(input("\n¿Qué desea hacer?: "))

        while seleccion<=-1:
            print("Error. Escribe números positivos")
            seleccion = int(input("\n¿Qué desea hacer?: "))

        if seleccion==0:
            menu=False

        if seleccion==1:
            print("Ha seleccionado 'Dibujar cuadrados y círculos'.")
            print("Se abrirá una ventana nueva. Cierre para continuar.")
            dibujarCuadrosCirculos()

        if seleccion==2:
            print("Ha seleccionado 'Dibujar parábolas'.")
            print("Se abrirá una ventana nueva. Cierre para continuar.")
            dibujarParabolas()

        if seleccion == 3:
            print("Ha seleccionado 'Dibujar pirámide'.")
            print("Se abrirá una ventana nueva. Cierre para continuar.")
            dibujarPiramide()

        if seleccion == 4:
            print("Ha seleccionado 'Dibujar círculos entrelazados'.")
            print("Se abrirá una ventana nueva. Cierre para continuar.")
            dibujarCirculos()

        if seleccion == 5:
            print("Ha seleccionado 'Aproximación a Pi'.")
            print("\nEntre más grande sea el divisor, mayor será la aproximación.")
            divisor = int(input("Divisor: "))
            while divisor <=0:
                print("\nError. Escribe números que sean mayores que 0.")
                divisor = int(input("Divisor: "))
            if divisor>=1:
                print("\nAproxímación a Pi=",calcularPi(divisor))

        if seleccion == 6:
            print("Ha seleccionado 'Contar divisibles entre 29'.")
            print("\n%d números de más de 4 dígitos son divisibles entre 29."%calcularDivisible())

        if seleccion == 7:
            print("Ha seleccionado 'Imprimir pirámides de números'.\n")
            calcularSeries()

    if menu==False:
        print("\nGracias por su visita. Vuelva pronto.")

main()
