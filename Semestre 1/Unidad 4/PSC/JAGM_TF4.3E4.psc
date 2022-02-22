Proceso  sin_titulo
	Definir n1,n2 Como Entero
	Escribir "Elige 1 para obtener el area un circulo"
	Escribir "Elige 2 para obtener el area un cuadrado"
	Escribir "Elige 3 para obtener el area un rectangulo"
	Escribir "Elige 4 para obtener el area un triangulo"
	Leer Opciones
	
	Segun Opciones Hacer
		"1":
			Escribir "¿Cual es el la medida del radio?"
			Leer n1
			C<-(n1^2)*(3.1416)
			Escribir "El area del circulo es:"," ",C;
		"2":
			Escribir "¿Cual es la medida de los lados del cuadrado?"
			Leer n1
			Cu<-n1*n1
			Escribir "El area del cuadrado es:"," ",Cu;
		"3":
			Escribir "¿Cual es la base del rectangulo?"
			Leer n1
			Escribir "¿Cual es la altura del rectangulo?"
			Leer  n2
			R<-n1*n2
			Escribir "El area del rectangulo es:"," ",R;
		"4":
			Escribir "¿Cual es la base del triangulo?"
			Leer n1
			Escribir "¿Cual es la altura del triangulo"
			Leer  n2
			T<-(n1*n2)/2
			Escribir "El area del triangulo es:"," ",T;
	FinSegun
FinProceso

