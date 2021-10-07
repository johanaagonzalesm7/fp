Proceso Nombres_y_Edad
	Definir N1,N2,N3 Como Caracter;
	Definir E1,E2,E3 Como Entero;
	Escribir ("Ingresa el primer nombre:");
	Leer N1;
	Escribir ("Ingresa el segundo nombre:");
	Leer N2;
	Escribir ("Ingresa el tercer nombre:");
	Leer N3;
	Escribir ("Ingresa la primera edad:");
	Leer E1;
	Escribir ("Ingresa la segunda edad:");
	Leer E2;
	Escribir ("Ingresa la tercera edad:");
	Leer E3;
	Si E1>E2 Entonces
		Si E1>E3 Entonces
			Escribir 'La persona mayor es', N1
		FinSi
	Sino
		Si E2>E3 Entonces
			Escribir 'La persona mayor es', N2
		Sino
			Escribir "La persona mayor es:" , N3
		FinSi
	FinSi
FinProceso
