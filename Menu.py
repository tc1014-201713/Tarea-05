



import pygame
from random import randint
import math

ANCHO=800
ALTO=800
BLANCO=(255,255,255)
NEGRO=(0,0,0)



def circuloycuadrado():

    pygame.init()
    ventana= pygame .display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)
        for Radio in range (0,410,10):
            if Radio==0:
                pygame.draw.circle(ventana,NEGRO, (400, 400), Radio,0)
            if Radio != 0 and Radio>0:
                pygame.draw.circle(ventana,NEGRO,(400, 400),Radio,1)
        x=400
        y=400
        for Lado in range (0,810,20):
            if Lado==0:
                x -=10
                y -=10
                pygame.draw.rect(ventana,NEGRO,(x,y,Lado,Lado),0)
            if Lado !=0 and Lado>0:
                pygame.draw.rect(ventana,NEGRO,(x,y,Lado,Lado),1)
                x -= 10
                y -= 10







        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps


    pygame.quit()  # termina pygame



def parabola():

    pygame.init()
    ventana= pygame .display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        x=0
        y=400
        x1=400
        y1=400
        ventana.fill(BLANCO)
        for lado in range(0,410,10):
            if lado !=0 and lado>0:
                x+=10
                y1-=10
                pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(x,y),(x1,y1),1)
        x2=800
        y2=400
        x3=400
        y3=400
        for lado in range(0,410,10):
            if lado !=0 and lado>0:
                x2-=10
                y3-=10

                pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(x2,y2),(x3,y3),1)
        x4=800
        y4=400
        x5=400
        y5=400

        for lado in range(0,410,10):
            if lado !=0 and lado>0:
                x4-=10
                y5+=10
                pygame.draw.line(ventana, (randint(0,255),randint(0,255),randint(0,255)), (x4,y4), (x5,y5), 1)
        x6=0
        y6=400
        x7=400
        y7=400

        for lado in range(0,410,10):
            if lado !=0 and lado>0:

                x6+=10
                y7+=10

                pygame.draw.line(ventana, (randint(0,255),randint(0,255),randint(0,255)), (x6,y6), (x7,y7), 1)






        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def cuadrado():

    pygame.init()
    ventana= pygame .display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)
        x1=400
        y2=400
        x2=410
        y1=390
        for Lado in range (0,810,20):
            #if Lado==0:
                #pygame.draw.rect(ventana,NEGRO,(x1,y2,Lado,Lado),0)
                #pygame.draw.rect(ventana, NEGRO, (x2, y1, Lado, Lado), 0)
                #x1-=10
                #y2-=10
                #x2 -= 10
                #y1 -= 10

            if Lado !=0 and Lado>0:
                pygame.draw.rect(ventana,NEGRO,(x1,y2,Lado,Lado),1)
                pygame.draw.rect(ventana, NEGRO, (x2, y1, Lado, Lado), 1)
                x1 -= 10
                y2 -= 10
                x2 -=10
                y1 -=10







        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps


    pygame.quit()  # termina pygame



def pi():
    n = int(input("dar valor"))
    sumatoria=0
    for n in range (1,n+1,1):
        sumatoria+= 1/n**2
        pis= math.sqrt(6*sumatoria)

def esVeintinueve():
    contador = 0
    for num in range (1000,10000,1):
        if num % 29 ==0:
            contador+=1


    print("los numeros que son divisibles entre 29 y de 4 digitos son",contador)
def piramideUno():
    sum=0
    n=1
    for sum in range(1,80,n*10+1):
        n=n*10+1
        m=n**2
        print(m)
    con=2
    n=1
    print(n*8+1)
    n=n+11
    for a in range(1,700,n*8+con):
        print(n * 8 + con)
        con += 1
        n = n*10+con

def main():
    print("1  Dibujar cuadrados y circulos")
    print("2  Dibujar  Espiral")
    print("3  Dubujar Circulos")
    print("4  Dibujar parabolas")
    print("5  Aproximar pi")
    print("6  Contar divisibles entre 29")
    print("7  Imprimir piramides de numeros")
    print("0  salir ")
    accion=int(input("¿Que desea hacer : "))
    if accion==1:
        circuloycuadrado()
    elif accion==2:
        cuadrado()
    elif accion==3:
        print("NONE")
    elif accion==4:
        parabola()
    elif accion==5:
        pi()
    elif accion==6:
        esVeintinueve()
    elif accion==7:
        piramideUno()
    elif accion ==0:
        print("NONE")


main()