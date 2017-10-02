#encoding: UTF-8
#Autor: Aaron Villanueva
#Este programa hace muchas cosas.
import pygame
#Espirales
#Calculos
#Pi
def encontrarNumerosDivisiblesEntre29():
  x=0
  for i in range(1000,9999):
    y=i%29
    if y==0:
      x=x+1
    else:
      x=x
  return(x)

#1000-9999
#29


def Main():
  
  if eleccion==1:
    
  elif eleccion==2:
    
    
  elif eleccion==4:
    print(encontrarNumerosDivisiblesEntre29())
  
  
Main()
