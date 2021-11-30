monto = float(input("¿Cual es la cantidad a invetir?"))
interes = float(input("¿Cual seria el interes anual?"))
años = int(input("¿Cuantos años?"))
for i in range(años):
	monto *= 1 + interes / 100
	print("Capital obtenido" + str(i+1) + " años: " + str(round(monto,2)))