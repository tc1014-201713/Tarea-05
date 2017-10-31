
import pygame
import random
import math

ANCHO=800
ALTO=800

#Colores
Rojo=(255,0,0)
Blanco=(255,255,255)
Negro=(0,0,0)
Verde=(0, 122, 0)

def dibujarParabola():
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
        ventana.fill(Negro)

        for i in range(1, 400, 10):
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i, ALTO / 2), (ANCHO / 2, i + ALTO / 2))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i, ALTO / 2), (ANCHO / 2, -i + ALTO / 2))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (ANCHO - i, ALTO / 2), (ANCHO / 2, ALTO / 2 + i))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(ANCHO - i, ALTO / 2), (ANCHO / 2, ALTO / 2 - i))

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

def dibujarEspiral():
        pygame.init()
        ventana = pygame.display.set_mode((ANCHO, ALTO))
        reloj = pygame.time.Clock()
        termina = False

        while not termina:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    termina = True

            ventana.fill(Blanco)

            for i in range(1, 400, 10):  # Va 1, 11, 21, 31...
                pygame.draw.line(ventana, Negro, (i, ALTO - i), (ANCHO - i, ALTO - i))
                pygame.draw.line(ventana, Negro, (i, i), (i, ALTO - i))
                pygame.draw.line(ventana, Negro, (ANCHO - (10 + i), i), (ANCHO - (10 + i), ALTO - (10 + i)))
                pygame.draw.line(ventana, Negro, (i, i), (ANCHO - (10 + i), (i)))

            pygame.display.flip()
            reloj.tick(40)

def calcularNumeros():
    n=0
    for k in range(1000,100000):
        if k%29==0:
            n+=1
    return k
def calcularPi(n):
    suma=0
    for valor in range (1,n+1):
        resultado= 1/n**2
        total=suma+resultado
    aproximacion=total
    raiz=math.pi**2/6
    return raiz, aproximacion

def dibujarCC():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(Blanco)

        for n in range(1, 400, 10): # Va 1, 11, 21, 31...
            pygame.draw.line(ventana,Rojo, (n,ALTO-n),(ANCHO-n,ALTO-n))
            pygame.draw.line(ventana, Rojo, (n, n), (n, ALTO - n))
            pygame.draw.line(ventana, Rojo, (ANCHO - (10 + n), n), (ANCHO - (10 + n), ALTO - (10 + n)))
            pygame.draw.line(ventana, Rojo, (n, n), (ANCHO - (10 +n), (n)))
            pygame.draw.circle(ventana, Rojo, (ANCHO // 2, ALTO // 2), 400-n, 1)

        pygame.display.flip()
        reloj.tick(40)





def main():

    print("""
    0. Salir
    1. Parabola
   2. Crear espiral
   3. Números divisibles entre 29
   4. Aproximación de PI
   5. Cuadros y círculos
   
   """)

    print("")
    seleccion = int(input("¿Qué desea hacer?:"))


    while seleccion >= 0:
        if seleccion == 1:
            dibujarParabola()
            seleccion = int(input("¿Qué desea hacer?:"))

        elif seleccion == 2:
            dibujarEspiral()
            seleccion = int(input("¿Qué desea hacer?:"))

        elif seleccion == 3:
            print(calcularNumeros())

            seleccion = int(input("¿Qué desea hacer?:"))


        elif seleccion == 4:
            n = int(input("¿Cual es el valor que quieres usar:"))
            print(calcularPi(n))
            seleccion = int(input("¿Qué desea hacer?:"))
        elif seleccion == 5:
            dibujarCC()
            seleccion = int(input("¿Qué desea hacer?:"))

        elif seleccion == 0:
            print("Adios!")
            break


main()