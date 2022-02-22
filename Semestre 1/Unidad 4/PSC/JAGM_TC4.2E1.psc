Proceso sueldo
	Escribir "Cual es el nombre del empleado";
	Leer E;
	Escribir  "Cual fue el numero de horas trabajadas";
	Leer H;
	Si H>= 40  Entonces;
		H<-(H+(H*0.5))
	Fin Si
	Escribir "El valor de la hora trbajada";
	Leer  V;
	Salario<-(H*V)
	Escribir "El emplado","  ",E,"  ","Su salario es:" ,Salario;
FinProceso

