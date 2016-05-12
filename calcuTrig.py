import math

print("                       \nCALCULADORA TRIGONOMÉTRICA"+"\nESCOJAQ UNA DE LAS SIGUIENTES FIGURAS PARA CALCULAR SU AREA Y PERIMETRO\n")
opc=int(input("1.-CIRCULO\n2.-CUADRADO\n3.-TRIANGULO\n4.-PENTAGONO\n"))

while (opc!=0):
	if(opc==1): 
		r=float(input("Ingrese el radio del círculo: "))
		per=2*math.pi*r
		area=math.pi*math.pow(r,2) 
		print("El área es: "+str(area)+"\nEl perimetro es: "+str(per))
	
	elif(opc==2):
		l=float(input("Ingrese el lado del cuadrado: "))
		per=l*4
		area=l*l
		print("El área es: "+str(area)+"\nEl perimetro es: "+str(per))
	
	elif(opc==3):
		l=float(input("Ingrese el lado del triángulo(equilátero: )"))
		per=l+l+l
		area= math.pow(l,2)*(math.sqrt(3)/4)
		print("El área es: "+str(area)+"\nEl perimetro es: "+str(per))
	
	elif(opc==4):	
		l=float(input("Ingrese el lado del pentágono: "))
		r=float(input("Ingrese el radio del pentágono: "))
		per=l*5
		ap=math.sqrt(math.pow(r,2)-math.pow((l/2),2))
		area=(per*ap)/2
		print("El área es: "+str(area)+"\nEl perimetro es: "+str(per))
	
	opc=int(input("\n1.-CIRCULO\n2.-CUADRADO\n3.-TRIANGULO\n4.-PENTAGONO\n0.-SALIR\n"))