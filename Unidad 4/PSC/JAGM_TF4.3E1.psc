Proceso  sin_titulo
	Definir n1,n2 Como Entero
	Escribir "Elige S para suma"
	Escribir "Elige R para resta"
	Escribir "Elige M para multiplicacion"
	Escribir "Elige D para division"
	Leer Opciones

	Segun Opciones Hacer
		"S":
			Escribir "Ingresa el primer numero"
			Leer n1
			Escribir "Ingresa el segundo numero"
			Leer  n2
			S<-n1+n2
			Escribir S
		"R":
			Escribir "Ingresa el primer numero"
			Leer n1
			Escribir "Ingresa el segundo numero"
			Leer  n2
			R<-n1-n2
			Escribir R
		"M":
			Escribir "Ingresa el primer numero"
			Leer n1
			Escribir "Ingresa el segundo numero"
			Leer  n2
			M<-n1*n2
			Escribir M
		"D":
			Escribir "Ingresa el primer numero"
			Leer n1
			Escribir "Ingresa el segundo numero"
			Leer  n2
			D<-n1/n2
			Escribir D
	FinSegun
FinProceso

