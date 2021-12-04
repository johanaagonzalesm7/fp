while True:
	print("""
		SELECCIONA UNA OPCION:
		1) SUMA
		2) RESTA
		3) MULTIPLICACION
		4) DIVISION
		5) SALIR
		""")
	opcion=int(input("Selecciona Una Opcion:"))
	if opcion==1:
		print("")
		n1=int(input("Escribe el primer valor:"))
		n2=int(input("Escribe el segundo valor:"))
		S = (n1+n2)
		print ("El resultado de la suma es:",S)
	elif opcion==2:
		print("")
		n1=int(input("Escribe el primer valor:"))
		n2=int(input("Escribe el segundo valor:"))
		R = (n1-n2)
		print ("El resultado de la resta es:",R)
	elif opcion==3:
		print("")
		n1=int(input("Escribe el primer valor:"))
		n2=int(input("Escribe el segundo valor:"))
		M = (n1*n2)
		print ("El resultado de la multiplicacion es:",M)
	elif opcion==4:
		print("")
		n1=int(input("Escribe el primer valor:"))
		n2=int(input("Escribe el segundo valor:"))
		D = (n1/n2)
		print ("El resultado de la division es:",D)
	elif opcion==5:
		break
	else:
		print("Incorrecta")
