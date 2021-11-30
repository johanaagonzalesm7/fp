E = str(input("Cual es el nombre del empleado"))
H = int(input("Cual fue el numero de horas trabajadas"))
if H>= 40:
	H=(H+(H*0.5))
V = int(input("El valor de la hora trbajada"))
Salario=(H*V)
print ("El emplado","  ",E,"  ","Su salario es:" ,Salario)