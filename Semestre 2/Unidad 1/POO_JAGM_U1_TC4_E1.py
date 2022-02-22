while True:
	print("""
		SELECCIONA UNA EL REFRESCO DE TU AGRAD0:
		1) COCA COLA $18
		2) FRESCA $14
		3) MUNDET $17
		4) FANTA $16
		5) SPRIT $15
		6) SALIR
		""")
	opcion=int(input(""))
	if opcion==1:
		print("")
		print("El producto seleccionado es coca")
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