# encoding: UTF-8
# Autor: Eduardo Roberto Müller Romero, A01745219
from asyncore import loop

import pygame
import math
import math
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL_MARINO = (23, 32, 42)
AMARILLO = (255, 195, 0)
NEGRO = (0, 0, 0)


def dibujarcirculoconcuadrado():
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
		ventana.fill(NEGRO)

		# Dibujar, aquí haces todos los trazos que requieras
		x = ANCHO
		y = ALTO

		for x in range(1, ANCHO):
			if x / 10 == x // 10:
				pygame.draw.rect(ventana, ROJO, (x, x, y - 2 * x, y - 2 * x), 1)
				pygame.draw.circle(ventana, ROJO, (400, 400), x, 1)

		pygame.display.flip()  # Actualiza trazos
		reloj.tick(40)  # 40 fps

	pygame.quit()  # termina pygame


def circulos():
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
		ventana.fill(NEGRO)

		# Dibujar, aquí haces todos los trazos que requieras
		for x in range(250, 551, 300):
			pygame.draw.circle(ventana, ROJO, (x, 400), 150, 1)
			pygame.draw.circle(ventana, ROJO, (400, x), 150, 1)

		pygame.display.flip()  # Actualiza trazos
		reloj.tick(40)  # 40 fps

	pygame.quit()  # termina pygame

def parabolas():

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
		ventana.fill(NEGRO)

		# Dibujar, aquí haces todos los trazos que requieras
		for x in range(0, 401, 10):
			pygame.draw.line(ventana, ROJO, (x, 400), (400, (400 + x)), 1)

		for x in range(0, 401, 10):
			pygame.draw.line(ventana, ROJO, (x, 400), (400, 400 - x), 1)

			pygame.draw.line(ventana, ROJO, (800 - x, 400), (400, (400 + x)), 1)

		for x in range(0, 401, 10):
			pygame.draw.line(ventana, ROJO, (800 - x, 400), (400, (400 - x)), 1)

		pygame.display.flip()  # Actualiza trazos
		reloj.tick(40)  # 40 fps

	pygame.quit()  # termina pygame

def maze():
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
		ventana.fill(NEGRO)

		# Dibujar, aquí haces todos los trazos que requieras
		for x in range(0, 391, 10):
			pygame.draw.line(ventana, ROJO, (0 + x, 0 + x), (780 - x, 0 + x), 1) #Arriba
		for x in range(0, 401, 10):
			pygame.draw.line(ventana, ROJO, (0 + x, 800 - x), (800 - x, 800 - x)) #Abajo
		for x in range(0, 391, 10):
			pygame.draw.line(ventana, ROJO, (0 + x, 0 + x), (0 + x, 800 - x), 1) #Izquierda
		for x in range(0, 401, 10):
			pygame.draw.line(ventana, ROJO, (780 - x, 0 + x), (790 - 10 - x, 780 - x), 1) #Derecha


		pygame.display.flip()  # Actualiza trazos
		reloj.tick(40)  # 40 fps

	pygame.quit()  # termina pygame



def main():
	print("Tarea 5: ")
	print("1. Cuadros y Círculos")
	print("2. Estrella")
	print("3. Espiral cuadrado")
	print("4. Circulos")
	print("5. Aproximación de Pi")
	print("6. Números divisibles entre 29 de cuatro dígitos")
	print("7. Piramides de operaciones")
	print("0. Salir")
	choice = 1
	while choice != 0:
		choice = int(input("Selecciona una opción: "))
		if choice == 1:
			dibujarcirculoconcuadrado()
		elif choice == 2:
			parabolas()
		elif choice == 3:
			maze()
		elif choice == 4:
			circulos()
		elif choice == 5:
			aproximarPi()
		elif choice == 6:
			dividir29()
		elif choice == 7:
			aumentacion1()
			aumentacion2()
		elif choice == 0:
			print("Adios ;-) ")




main()
