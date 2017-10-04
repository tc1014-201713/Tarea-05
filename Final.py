#encoding: UTF-8
#Autor: Aaron Villanueva
#Este programa hace muchas cosas.
import pygame

anchoVentana = 800
altoVentana = 800
BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

def iniciarPygame():
    pygame.init()
    ventana = pygame.display.set_mode((anchoVentana, altoVentana))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
    pygame.display.flip()
    reloj.tick(40)
        
def dibujarCuadrosCirculos():
    iniciarpygame()
        for diferencia in range(0,400,10):
            pygame.draw.circle(ventana, NEGRO, (anchoVentana // 2, altoVentana // 2), 400-diferencia, 2)
        for cambio in range(0,400,10):
            pygame.draw.rect(ventana, NEGRO, (cambio, cambio, anchoVentana-(2*cambio), altoVentana-(2*cambio)), 1)
    pygame.quit()

def dibujarLaberinto():
    iniciarpygame()
        for diferencia in range(0,100,10):
            pygame.draw.lines(ventana, NEGRO, True, (400+cambio,400-cambio),1)
    pygame.quit()
    
def dibujarCirculos():
    iniciarpygame()
        for X in range(0,100,10)
            pygame.draw.circle(ventana, NEGRO, (x,y), 150, 1)
    
def aproximarPi(intentos):
    x = 0
    for i in range(1, intentos):
        x = x + (1 / (i ** 2))
    x = x * 6
    x = x ** .5
    return(x)

def encontrarNumerosDivisiblesEntre29():
    x=0
    for i in range(1000,9999):
        y=i%29
        if y==0:
            x=x+1
        else:
            x=x
    return(x)

def piramidesNumeros():
    piramide = 1
    for factor in range(1, 10):
        resultado = piramide * 8 + factor
        print(piramide, "X 8 +", factor, "=", resultado)
        piramide = (piramide * 10) + (factor + 1)
    print("")
    numeros = 1
    for i in range(10):
        resultadocuadrado = numeros * numeros
        print(numeros, "X", numeros, "=", resultadocuadrado)
        numeros = (numeros * 10) + 1
def menu():
    print("Tarea 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar espiral")
    print("3. Dibujar círculos")
    print("4. Dibujar parabolas")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 29")
    print("7. Imprimir piramides de números")
    print("0. Salir")
    conclusion=int(input("¿Qué desea hacer?"))
    return(conclusion)
def retorno():
    print("")
    print("1. Si")
    print("2. No")
    retornocondicional=int(input(("¿Desea regresar al menu principal?")))
    print("")
    return(retornocondicional)
    
def Main():
    eleccion=menu()
    respuesta=True
    while respuesta==True:
        if eleccion==0:
            print("saliendo")
            respuesta=False
        elif eleccion==1:
            dibujarCuadrosCirculos()
        elif eleccion==2:
            dibujarEspiral()
        elif eleccion==3:
            dibujarCirculos()
        elif eleccion==4:
            dibujarParabolas()
            solucion=retorno()
            if solucion==1:
              menu()
            else:
                break
        elif eleccion==5:
            final=int(input("Ingrese un número entero para determinar Pi. Entre mayor sea, más exacto el resultado"))
            print("La aproximación de Pi con", final,"intentos es de:",aproximarPi(final))
            solucion=retorno()
            if solucion==1:
              menu()
            else:
              break
        elif eleccion==6:
            print("El número de números de cuatro digitos divisibles entre 29 es:",encontrarNumerosDivisiblesEntre29())
            solucion=retorno()
            if solucion==1:
              menu()
            else:
              break
        elif eleccion==7:
            print(piramidesNumeros())
            solucion=retorno()
            if solucion==1:
              menu()
            else:
              break
        else:
            print("error. Número no localizado")
