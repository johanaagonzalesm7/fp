Proceso  Capital
	Escribir  "�Cual es la cantidad a invertir?"
	Leer monto
	Escribir "�Cual seria el interes anual?"
	Leer interes
	Escribir "�Cuantos a�os?"
	Leer a�o
	Para i Hasta a�o Hacer
		monto * <- (1+(interes/100))
		Escribir ("Capital obtenido" + Subcadena((i+1) + " a�os: " + Subcadena((trunc(monto,2)))))
	FinPara
FinProceso

