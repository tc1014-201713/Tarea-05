# encoding: UTF-8
# Autor: Iván Alejandro Dumas Martínez
# Descripción: Este programa genera un menu con varias opciones de funciones

# Librerias
import pygame,math,random

# Constantes
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
NEGRO = (0, 0, 0)
RANDCOLOR = random.sample((range(0,255)), 3)

def dibujarCuadrosCirculos():
    pygame.init()  # Inicializa pygam
    window = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        window.fill(BLANCO)

        for i in range(1,ANCHO//2,10):
            pygame.draw.circle(window,NEGRO, (ANCHO//2,ALTO//2), (i),1)
            pygame.draw.polygon(window,NEGRO,[(ANCHO//2+i,ALTO//2+i),(ANCHO//2-i,ALTO//2+i),(ANCHO//2-i,ALTO//2-i),(ANCHO//2+i,ALTO//2-i)],1)

        pygame.display.flip()
        reloj.tick(60)


    pygame.quit()


def dibujarParabolas():
    pygame.init()  # Inicializa pygam
    window = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
            window.fill(BLANCO)

            for i in range(0, ANCHO // 2, 10):
                RANDCOLOR = random.sample((range(0, 255)), 3)
                pygame.draw.line(window, RANDCOLOR, (ANCHO // 2, i), (ANCHO // 2 + i, ALTO // 2), 1)
                pygame.draw.line(window, RANDCOLOR, (ANCHO // 2, i), (ANCHO // 2 - i, ALTO // 2), 1)
                pygame.draw.line(window, RANDCOLOR, (ANCHO // 2, ALTO - i), (ANCHO // 2 + i, ALTO // 2), 1)
                pygame.draw.line(window, RANDCOLOR, (ANCHO // 2, ALTO - i), (ANCHO // 2 - i, ALTO // 2), 1)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


def dibujarCirculos():
    PI = math.pi
    rad = 0
    RADIO = 150

    pygame.init()  # Inicializa pygam
    window = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución


    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        window.fill(BLANCO)

        # Ciclo que primero calcula las coordenadas en un circulo unitario y posteriormente dibuja un circulo en dichas coordenadas
        for i in range (12):
            rad += PI / 6
            xVal = int(math.sin(rad)*RADIO) # coordenada en x
            yVal = int(math.cos(rad)*RADIO) # coordenada en y
            pygame.draw.circle(window, NEGRO, (ANCHO//2 + xVal, ALTO // 2 + yVal), RADIO, 1)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


def dibujarEspiral():
    DX= +10

    listCoordenadas =[(ANCHO//2,ALTO//2),(ANCHO//2 + DX//2,ALTO//2)]
    for i in range (10,ANCHO//2,DX):
        listCoordenadas.append((ANCHO//2 - DX//2  + i, ALTO//2 - i))
        listCoordenadas.append((ANCHO//2 - i, ALTO//2 - i))
        listCoordenadas.append((ANCHO//2 - i,ALTO//2 + i))
        listCoordenadas.append((ANCHO//2 + DX//2 + i, ALTO//2 +i))

    print (listCoordenadas)

    pygame.init()  # Inicializa pygame
    window = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        window.fill(BLANCO)
        #[(ANCHO - 10, ALTO - 10), (10, ALTO - 10), (10, 10), (ANCHO - 10, 10), (790,780)]
        pygame.draw.lines(window,NEGRO,False,listCoordenadas,1)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


def aproximarPi(num):
    pi = 0
    for i in range (1,num+1):
        pi += (1/(i*i))

    result = (pi*6)**0.5
    return result


def contarDivisibles29():
    counter = 0
    for i in range (1000, 9999):
        if i%29 == 0:
            counter += 1
    return counter


def imprimirPiramides():
    pir1 = 0
    pir2 = 0
    for i in range (1,10):
        pir1 = pir1 * 10 + i
        num1 = pir1 * 8 + i
        print ("%d * 8 + %d = %d" % (pir1,i,num1))

    for i in range (9):
        pir2 = (pir2 * 10) + 1
        num2 = pir2 * pir2
        print ("%d * %d = %d" % (pir2,pir2,num2))


def main():
    print("Tarea 5. Seleccione qué quiere hacer.")
    menu = """––––––––––––––––––––––––––––––––
1. Dibujar cuadros y círculos
2. Dibujar espiral
3. Dibujar círculos
4. Dibujar parábolas
5. Aproximar PI
6. Contar divisibles entre 29
7. Imprimir pirámides de números 
0. Salir
¿Qué desea hacer?
––––––––––––––––––––––––––––––––
"""
    accion = int(input(menu))
    while 1:
        if accion >= 0 and accion <= 7:
            if accion == 0:
                print ("    ADIOS :)    ")
                break
            elif accion == 1:
                dibujarCuadrosCirculos()
            elif accion == 2:
                dibujarEspiral()
            elif accion == 3:
                dibujarCirculos()
            elif accion == 4:
                dibujarParabolas()
            elif accion == 5:
                num = int(input("Por cuanto quieres aproximar el valor de Pi?\n"))
                pi = aproximarPi(num)
                print("El valor aproximado de Pi es: ", pi)
            elif accion == 6:
                divisores = contarDivisibles29()
                print ("Hay %d números de 4 digitos divisibles entre 29" % (divisores))
            elif accion == 7:
                imprimirPiramides()
        else:
            print("""
            
    ERROR: EL VALOR INGRESADO ES INVÁLIDO
    
    """)
        accion = int(input(menu))


main()