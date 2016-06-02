#importación de la librería
import turtle 
import time #permite pausar la aplicación al final por un timpo determinado

#definir las características de la ventana
vent=turtle.Screen()
vent.bgcolor('brown') # color de fondo de la ventana
vent.title('Tablero de Ajedrez') #titulo de la aplicación

greg=turtle.Turtle()
greg.speed(20) #velocidad con la que dibuja en el tablero

#dibujar y llenar un cuadro
def cuadro(tamaño,alternar,color):
	greg.color(color)
	greg.begin_fill()
	for i in range(4):
		greg.fd(tamaño)
		greg.lt(90)
	greg.end_fill()
	greg.fd(tamaño)

#dibujar una fila de cuadrados
def fila(tamaño,alternar,color1,color2):
	for i in range(4):
		if(alternar==True):
			cuadro(tamaño,alternar,color1)
			cuadro(tamaño,alternar,color2)
		else:
			cuadro(tamaño,alternar,color2)
			cuadro(tamaño,alternar,color1)
			
#Dibujar el tablero completo
def tablero(tamaño,alternar,color1,color2):
	greg.pu()
	greg.goto(-(tamaño*4),(tamaño*4))
	for i in range(8):
		fila(tamaño,alternar,color1,color2)
		greg.bk(tamaño*8)
		greg.rt(90)
		greg.fd(tamaño)
		greg.lt(90)
		if(alternar==True):
			alternar=False
		else:
			alternar=True

tablero(50,True,'black','white')
time.sleep(10)