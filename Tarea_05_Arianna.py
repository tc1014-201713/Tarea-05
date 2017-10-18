# encoding: UTF-8
# Autor: Arianna Sinai Soriano Vega
# Tarea 5: Ciclos

import pygame
import random
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
y = ALTO//2
x=ANCHO//2
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)

def CirCua():
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




        for radio in range(1,(ANCHO//2),(10-1)):
            pygame.draw.circle(ventana,NEGRO, (ANCHO//2,ALTO//2),radio,1)
            pygame.draw.rect(ventana, NEGRO, (ANCHO//2 - (radio), ANCHO//2 -(radio), 2*radio, 2*radio), 1)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fpsç

    pygame.quit()   # termina pygame

def Para():
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
        pygame.draw.line(ventana, VERDE_BANDERA, (x, ALTO), (x, -ALTO), 1)
        #pygame.draw.line(ventana, NEGRO, (ANCHO, y), (-ANCHO, y), 1)


        for i in range (10,x,10):
            C1 = random.randint(0, 255)
            C2 = random.randint(0, 255)
            C3 = random.randint(0, 255)
            pygame.draw.line(ventana, (C1,C2,C3), (x, ALTO), (x, -ALTO), 1)
            # Cuandrante 1 abajo
            pygame.draw.line(ventana, (C1,C2,C3), (ANCHO - i, y), (x, y - i), 1)
            #Cuadrante 2 abajo
            pygame.draw.line(ventana, (C1,C2,C3), (0+i, x), (x, y - i), 1)
            # Cuandrante 3 arriba
            pygame.draw.line(ventana, (C1,C2,C3), (0+i, x), (x, y + i), 1)
            # Cuandrante 4 arriba
            pygame.draw.line(ventana, (C1,C2,C3), (ANCHO-i, y), (x, y + i), 1)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fpsç

    pygame.quit()   # termina pygame

def Esp():
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





        for j in range (0,y-10,10):
            pygame.draw.line(ventana, NEGRO, (x+5+j, y + 10+j), (x +5+ j, y-j ), 1)
            pygame.draw.line(ventana, NEGRO, (x+5+j,y-j),(x -10-j, y-j ), 1)
            pygame.draw.line(ventana, NEGRO, (x-10-j, y-j), (x - 10-j, y+20+j ), 1)
            pygame.draw.line(ventana, NEGRO, (x - j, y + 10 + j), (x + 5 + j, y + 10 + j), 1)

        '''
        pygame.draw.line(ventana, NEGRO,(x,y+10),(x+5,y+10),1)
        pygame.draw.line(ventana, NEGRO, (x+5, y + 10), (x + 5, y ), 1)
        pygame.draw.line(ventana, NEGRO, (x+5,y), (x -10, y ), 1)
        pygame.draw.line(ventana, NEGRO, (x-10, y), (x - 10, y+15 ), 1)
        '''

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fpsç

    pygame.quit()   # termina pygame

def Flor():
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


            pygame.draw.circle(ventana, NEGRO, (x, y - 150), 150, 1)
            pygame.draw.circle(ventana, NEGRO, (x - 75, y - 130), 150, 1)
            pygame.draw.circle(ventana, NEGRO, (x + 75, y - 130), 150, 1)

            pygame.draw.circle(ventana, NEGRO, (x, y + 150), 150, 1)
            pygame.draw.circle(ventana, NEGRO, (x + 75, y + 130), 150, 1)
            pygame.draw.circle(ventana, NEGRO, (x - 75, y + 130), 150, 1)

            pygame.draw.circle(ventana, NEGRO, (x - 150, y), 150, 1)
            pygame.draw.circle(ventana, NEGRO, (x - 130, y - 75), 150, 1)
            pygame.draw.circle(ventana, NEGRO, (x - 130, y + 75), 150, 1)

            pygame.draw.circle(ventana, NEGRO, (x + 150, y), 150, 1)
            pygame.draw.circle(ventana, NEGRO, (x + 130, y - 75), 150, 1)
            pygame.draw.circle(ventana, NEGRO, (x + 130, y + 75), 150, 1)

            pygame.display.flip()  # Actualiza trazos
            reloj.tick(40)  # 40 fpsç

        pygame.quit()  # termina pygame

def piramides():
    actual=0
    anterior = 0

    result=0

    for i in range (0,10):
        anterior=(result*10)
        actual=anterior+1
        result=actual
        holi=result*result

        print(result, "*", result, "=",holi)


'''
1*8+1=9
12 * 8 + 2 = 98
123 * 8 + 3 = 987
1234 * 8 + 4 = 9876
12345 * 8 + 5 = 98765
123456 * 8 + 6 = 987654
1234567 * 8 + 7 = 9876543
12345678 * 8 + 8 = 98765432
123456789 * 8 + 9 = 987654321
'''
def piramide2():
    actual=0
    anterior = 0

    result=0

    for i in range (1,10):
        anterior=result*10+i

        result=anterior
        actual = result* 8 + i

        print(result, "* 8 +", i,"=",actual)

def Pira():
    piramide2()
    print("")
    piramides()

def Divisor():

    print("Los números de 4 dígitos divisibles entre 29 son: ")
    for i in range (1000,10000,1):

        if i%29==0:
            print(i)
def pi(y):
    ant=0
    act=0
    sum=0


    for i in range (1,(y+1)):
        ant=sum
        actual=ant+1/(i**2)
        sum=actual



        nessi = (6 * sum) ** (.5)
        if i==(y):
            print("1/(",i,"^2) = (π^2)/6")
        else:
            print("1/(",i,"^2) +")


    print("π =",nessi)


def menu():

    print("Tarea 05. Seleccione una opción:")
    print("1. Dibujar cuadrados y círculos ")
    print("2. Dibujar espiral ")
    print("3. Dibujar parábolas ")
    print("4. Dibujar círculos")
    print("5. Aproximar a PI ")
    print("6. Contar divisibles entre 29 ")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    print("")
    opcion = int(input("Teclea tu opción: "))

    while opcion !=0:


        if opcion==1:
            CirCua()
            print(" ")
            menu()
        if opcion ==2:
            Esp()
            print("")
            menu()
        if opcion==3:
            Para()
            print(" ")
            menu()
        if opcion == 4:
            Flor()
            print(" ")
            menu()
        if opcion==5:
            y = int(input("Escoge el número que deseas: "))
            pi(y)
            print(" ")
            menu()
        if opcion == 6:
            Divisor()
            print("")
            menu()
        if opcion==7:
            piramides()
            print("")
            piramide2()
            print("")
            menu()
    if opcion==0:
        print("Adiós!")
        exit()


def main():
    print("Tarea 05. Seleccione una opción:")
    print("1. Dibujar cuadrados y círculos ")
    print("2. Dibujar espiral ")
    print("3. Dibujar parábolas ")
    print("4. Dibujar círculos")
    print("5. Aproximar a PI ")
    print("6. Contar divisibles entre 29 ")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    print("")
    opcion = int(input("Teclea tu opción: "))

    while opcion !=0:


        if opcion==1:
            CirCua()
            print("")
            menu()
        if opcion == 2:
            Esp()
            print("")
            menu()
        if opcion==3:
            Para()
            print("")
            menu()
        if opcion == 4:
            Flor()
            print("!")
            menu()
        if opcion==5:
            x = int(input("Escoge el número que deseas: "))
            pi(x)
            print("")
            menu()
        if opcion == 6:
            Divisor()
            print("")
            menu()
        if opcion==7:
            piramides()
            print("")
            piramide2()
            print("")
            menu()
            print("")
    if opcion==0:
        print("Adiós!")
        exit()







main()

