N1 = str(input('Ingresa el primer nombre:'))
N2 = str(input('Ingresa el segundo nombre:'))
N3 = str(input('Ingresa el tercer nombre:'))
E1 = int(input('Ingresa la primera edad:'))
E2 = int(input('Ingresa la segunda edad:'))
E3 = int(input('Ingresa la tercera edad:'))
if E1>E2:
	if E1>E3:
		print ('La persona mayor es', N1)
else:
	if E2>E3: 
		print ('La persona mayor es', N2)
	else:
		print ('La persona mayor es:', N3)

