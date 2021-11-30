Proceso  Capital
	Escribir  "¿Cual es la cantidad a invertir?"
	Leer monto
	Escribir "¿Cual seria el interes anual?"
	Leer interes
	Escribir "¿Cuantos años?"
	Leer año
	Para i Hasta año Hacer
		monto * <- (1+(interes/100))
		Escribir ("Capital obtenido" + Subcadena((i+1) + " años: " + Subcadena((trunc(monto,2)))))
	FinPara
FinProceso

