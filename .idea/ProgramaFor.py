#encoding UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa realiza diversas ejercicios
import math
import pygame
from random import randint

#Colores
NEGRO=  (0,0,0)
BLANCO =(225,225,225)

def dibujarParabolas(): #Dibuja parábolas.
    #Medidas de pantalla
    ancho=800
    alto=800
    #Inicializa el programa
    pygame.init()
    ventana =pygame.display.set_mode((ancho,alto)) #Crea la pantalla
    reloj=pygame.time.Clock()#Para limitar los fps
    termina=False #Para saber si termina la ejecución

    while not termina:
        #Porcesa los eventos que recibe
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                termina=True
        #Borra pantalla
        ventana.fill(BLANCO)
        #Realiza los trazos
        y=0
        for x in range (0,410,10): #Realiza el primer cuadrante
            ALEATORIO = (randint(0, 225), randint(0, 225), randint(0, 225))
            pygame.draw.line(ventana, ALEATORIO, (400,y),(x+400,400),1)
            y+=10
        y=400
        for x in range (0,410,10): #Realiza el segundo cuadrante
            ALEATORIO = (randint(0, 225), randint(0, 225), randint(0, 225))
            pygame.draw.line(ventana, ALEATORIO, (x,400),(400,y),1)
            y-=10
        y=400
        for x in range (0,410,10): #Realiza el tercer cuadrante
            ALEATORIO = (randint(0, 225), randint(0, 225), randint(0, 225))
            pygame.draw.line(ventana, ALEATORIO, (x,400),(400,y) ,1)
            y+=10
        y=800
        for x in range (0,410,10): #Realiza el cuarto cuadrante
            ALEATORIO = (randint(0, 225), randint(0, 225), randint(0, 225))
            pygame.draw.line(ventana, ALEATORIO,(400,y),(x+400,400),1)
            y-=10
        pygame.display.flip() #Actualiza trazos
        reloj.tick(40) #40 fps
    pygame.quit()#Termina pygame


def dibujarEspiral():#Esta función dibuja un espiral
    #Medidas de pantalla
    ancho = 800
    alto = 800
    pygame.init() # Inicializa pygame
    ventana = pygame.display.set_mode((ancho, alto)) #Crea la ventana de dibujo
    reloj = pygame.time.Clock() #Limita los fps
    termina = False #Para saber si termina la ejecución

    while not termina:
        #Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #El usuario hizo click en botón salir
                termina = True
            # Color de la ventana
            ventana.fill(BLANCO)
            # Dibuja los trazos
            x = 800
            for y in range(0, 410, 10): #Dibuja las líneas necesarias para el espiral
                pygame.draw.line(ventana, NEGRO, (y, y), (800 - y, y), 1)
                pygame.draw.line(ventana, NEGRO, (y, y), (y, 800 - y + 10), 1)
                pygame.draw.line(ventana, NEGRO, (400 + y, 400 - y), (400 + y, 400 + y), 1)
                pygame.draw.line(ventana, NEGRO, (400 - y, 400 + y + 10), (400 + y + 10, 400 + y + 10), 1)

        pygame.display.flip()#Actualiza trazos
        reloj.tick(40)#40 fps
    pygame.quit() #Termina pygame


def dibujarCirculos(): #Esta función dibuja un mandala hecho a base de círculos

    ancho= 800
    alto=800
    #Uso de pygame
    pygame.init() #Inicia pygame
    ventana=pygame.display.set_mode((ancho,alto)) #Crea la pantalla de dibujo
    reloj=pygame.time.Clock() #Limita los fps
    termina= False#Para saber si termina la ejecución

    while not termina:
        #Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT: #El usuario hizo click en salir
                termina=True
        #Color de la ventana
        ventana.fill(BLANCO)

        #Dibuja los trazos
        for numero in range (0,13): #Dibuja los doce círculos

            angulo = (math.pi/6)*numero
            y=int (math.sin(angulo)*150)
            x= int(math.cos(angulo)*150)
            x = x + 400
            y = y + 400
            pygame.draw.circle(ventana, NEGRO, (x,y),150, 1 )




        pygame.display.flip()#Actualiza los trazos
        reloj.tick(40) #40 fps
    pygame.quit() #Termina pygame



def dibujarCuadrosyCirculos():#Esta función dibuja un diagrama hecho base de cuadrados y círculos.
    #Medidas de pantalla
    ancho = 800
    alto = 800
    #cuadro
    x= 0


    #Uso de pygame
    pygame.init()#Inicia el programa
    ventana=pygame.display.set_mode((ancho,alto))#Crea la pantalla para el programa
    reloj=pygame.time.Clock() #Limita los fps
    termina = False #Para saber si termina la ejecución

    while not termina:
        #procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:#El usuario hizo click en salir.
                termina= True
        #Borrar pantalla
        ventana.fill(BLANCO)
        #Medidas del cuadrado
        anchoCuadro = 800
        altoCuadro = 800
        #Dibuja los trazos

        for x in range(10,400,10): #Dibuja los cuadrados
            anchoCuadro = anchoCuadro - 20
            altoCuadro = altoCuadro - 20

            pygame.draw.rect(ventana, NEGRO,(x,x,  anchoCuadro,altoCuadro), 1)

        for radio in range(10,400,10):#Dibuja los círculos
            pygame.draw.circle(ventana, NEGRO, (400,400), radio,1)


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame

def calcularPI(ultimoDivisor): #Aproxima el valor de PI
    suma= 0
    for divisor in range (1,ultimoDivisor+1):
        suma = 1/(divisor**2)+suma
    return suma

def contarDivisores(): #Cuenta la cantidad de números de 4 dígitos divisibles entre 29.
    contador = 0
    for x in range(1000,10000):
        if x%29==0:
            contador= 1 + contador
    return contador

def realizarCadenasDeNumeros(): #Realiza las cadenas de números
    n=1 #Realiza la primera cadena
    for x in range(1,10):
        if x>= 2:
            multiplicador=10
            n = n * multiplicador+x
        else:
            multiplicador=1
            n = n * multiplicador
        resultado= n*8+x
        print(n," * 8 + ",x," = ",resultado)
    print()
    n = 1 #Realiza la segunda cadena.
    for x in range(1, 10):
        if x >= 2:
            multiplicador = 10
            n = n * multiplicador + 1
        else:
            multiplicador = 1
            n = n * multiplicador
        resultado = n*n
        print(n, " *  ", n, " = ", resultado)

def main():#Programa principal
    boton = 10
    print ("Tarea 5. Seleccione qué hacer")
    print ("1.Dibujar cuadros y círculos")
    print ("2.Dibujar espiral")
    print ("3.Dibujar círculos")
    print ("4.Dibujar parábolas" )
    print ("5. Aproximar PI")
    print ("6. Contar divisibles entre 29")
    print ("7. Imprimir pirámides de números")
    print ("0.Salir")
    while not ( boton== "0") :
        boton = input (str ("¿Qué deseas que haga el problema?: "))
        if boton == "1" :
            dibujarCuadrosyCirculos()
        if boton=="2":
            dibujarEspiral()
        if boton=="3":
            dibujarCirculos()
        if boton=="4":
            dibujarParabolas()
        if boton=="5":
            ultimoDivisor=int(input("Dame el valor del último divisor: "))
            print("El valor aproximado de PI es: ", (calcularPI(ultimoDivisor)))
        if boton=="6":
            print("La cantidad de números de 4 dígitos divisibles entre 29 es :", (contarDivisores()))
        if boton=="7":
            realizarCadenasDeNumeros()
        if boton=="0":
            print ("El programa termina")


main()