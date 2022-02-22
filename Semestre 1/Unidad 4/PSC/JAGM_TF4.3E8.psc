Proceso  sin_titulo
	Definir clas,atri Como Cadena
	Escribir "¿Cual es el nombre de la clase?"
	Leer clas
	Definir i Como Real
	Dimension atri(5)
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir "Escribe el atributo"," ",i+0
		Leer atri(i);
	FinPara
	Escribir " "
	Escribir "La clase se llama:"," ",clas
	Escribir " "
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir "El atributo es:"," ", atri(i);
	FinPara
	
	
FinProceso

