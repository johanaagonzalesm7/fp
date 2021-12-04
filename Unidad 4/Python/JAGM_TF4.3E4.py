while True:
	print("""
		Elige una opcion:
		1) Obtener el area de un CIRCULO
		2) Obtener el area de un CUADRADO
		3) Obtener el area de un RECTANGULO
		4) Obtener el area de un TRIANGULO
		5) Salir
		""")
	Opcion=int(input("Elige una opcion:"))
	if Opcion==1:
		n1=int(input("¿Cual es el la medida del radio?"))
		C=(n1*n1)*(3.1416)
		print("El area del circulo es:",C)
	elif Opcion==2:
		n1=int(input("¿Cual es la medida de los lados del cuadrado?"))
		Cu=n1*n1
		print("El area del cuadrado es:",Cu)
	elif Opcion==3:
		n1=int(input("¿Cual es la base del rectangulo?"))
		n2=int(input("¿Cual es la altura del rectangulo?"))
		R=n1*n2
		print("El area del rectangulo es:",R)
	elif Opcion==4:
		n1=int(input("¿Cual es la base del triangulo?"))
		n2=int(input("¿Cual es la altura del triangulo"))
		T=(n1*n2)/2
		print("El area del triangulo es:",T)
	elif Opcion==5:
		break
	else:
		print("Opcion Incorrecta")
	


	pass