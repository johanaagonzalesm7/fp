while True:
	print("""
		SELECCIONA UNA OPCION:
		1) SUMA
		2) RESTA
		3) MULTIPLICACION
		4) DIVISION
		5) SALIR
		""")
	opcion=int(input(""))
	if opcion==1:
		print("")
		numeroUno=int(input("Escribe el primer valor:"))
		numeroDos=int(input("Escribe el segundo valor:"))
		Suma = (numeroUno+numeroDos)
		print ("El resultado de la suma es:",Suma)
	elif opcion==2:
		print("")
		numeroUno=int(input("Escribe el primer valor:"))
		numeroDos=int(input("Escribe el segundo valor:"))
		Resta = (numeroUno-numeroDos)
		print ("El resultado de la resta es:",Resta)
	elif opcion==3:
		print("")
		numeroUno=int(input("Escribe el primer valor:"))
		numeroDos=int(input("Escribe el segundo valor:"))
		Multiplicacion = (numeroUno*numeroDos)
		print ("El resultado de la multiplicacion es:",Multiplicacion)
	elif opcion==4:
		print("")
		numeroUno=int(input("Escribe el primer valor:"))
		numeroDos=int(input("Escribe el segundo valor:"))
		Division = (numeroUno/numeroDos)
		print ("El resultado de la division es:",Division)
	elif opcion==5:
		break
	else:
		print("Incorrecta")
