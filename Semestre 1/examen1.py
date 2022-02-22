class alumno():
	def __init__(self,residencia,edad,distancia,promedioetica,promedioprogramacion,promedioinvestigacion,promediotics,promediomatematicas,promediocalculo,preparatoria):
		super(alumno, self).__init__()
		self.residencia = residencia
		self.edad = edad
		self.distancia = distancia
		self.promedioetica = promedioetica
		self.promedioprogramacion = promedioprogramacion
		self.promedioinvestigacion = promedioinvestigacion
		self.promediotics = promediotics
		self.promediomatematicas = promediomatematicas
		self.promediocalculo = promediocalculo
		self.preparatoria = preparatoria
		

Reina = alumno("Emiliano Zapata", 17, "2.5km", 10, 8, 8, 7, 9, 8, 10) 
Britzy = alumno("Rindon de Romos", 18, "13m", 7, 6, 9, 5, 9, 7, 9) 
Mirozlava = alumno("Cosio", 19, "26km", 9, 7, 10, 6, 9, 10, 10) 
Fernando = alumno("Pabellon de Arteaga", 17, "2.8km", 10, 10, 8, 7, 9, 8, 6) 
Johana = alumno("Jesus Maria", 18, "29km", 9, 8, 6, 7, 7, 10, 9) 
Melany = alumno("Pabellon de Arteaga", 18, "2.8km", 5, 8, 6, 9, 10, 7, 8) 
Alejandro = alumno("Rindon de Romos", 19, "13m", 10, 9, 9, 6, 5, 7, 9) 
Diego = alumno("Rindon de Romos", 19, "13m", 7, 8, 9, 5, 10, 8, 10) 
Arely = alumno("Rindon de Romos", 18, "13m", 6, 6, 9, 10, 9, 6, 9) 
Alexis = alumno("Rindon de Romos", 18, "13m", 7, 6, 9, 5, 9, 5, 7) 
Isaac = alumno("Rindon de Romos", 19, "13m", 10, 6, 7, 9, 6, 7, 6) 
Austin = alumno("Pabellon de Arteaga", 18, "2.8km", 7, 8, 7, 9, 9, 7, 8) 
Donaldo = alumno("Pabellon de Arteaga", 17, "2.8km", 9, 6, 5, 10, 7, 7, 8) 
Elias = alumno("Rindon de Romos", 18, "13m", 10, 9, 8, 6, 9, 10, 10) 
Paola = alumno("Pabellon de Arteaga", 19, "2.8km", 10, 8, 6, 9, 10, 7, 7) 
print ("INGENIEROS EN TECNOLOGIAS DE LA INFORMACION Y COMUNICACION")
opcion = 0
while True:
	print("""
		SELECCIONA UNA OPCION:
		1) SALIR
		2) LOS 5 ESTUDIANTES CON MEJOR CALIFICACION
		3) PROMEDIO DE TODOS LOS ESTUDIANTES EN LA PREPARATORIA
		4) ALUMNOS QUE VIVEN CERCA Y LEJOS
		5) MATERIA CON MEJOR RENDIMIENTO
		6) LOS ALUMNOS QUE SON MAYORES DE EDAD
		""")
	opcion = int(input("SELECCIONA UNA OPCION:"))
	if opcion == 2:
		print ("")
		print("Elias con un promedio de 8.8 de", Elias.residencia)
		print("Mirozlava con un promedio de 8.5 de", Mirozlava.residencia)
		print("Reina con un promedio de 8.5 de", Reina.residencia)
		print("Fernando con un promedio de 8.2 de", Fernando.residencia)
		print("Johana con un promedio de 8 de", Johana.residencia)
	elif opcion == 3:
		print ("")
		print ("Promedio general del grupo en preparatoria es de: 7.7")
		print ("El promedio de cada uno de los integrantes del grupo son:")
		print (Reina.preparatoria, Britzy.preparatoria, Mirozlava.preparatoria, Fernando.preparatoria, Johana.preparatoria)
		print (Melany.preparatoria, Alejandro.preparatoria, Diego.preparatoria, Arely.preparatoria, Alexis.preparatoria)
		print (Isaac.preparatoria, Austin.preparatoria, Donaldo.preparatoria, Elias.preparatoria, Paola.preparatoria)
	elif opcion == 4:
		print("")
		print("La estudiante Johana vive mas lejos del ITPA con una distancia de:",Johana.distancia)
		print("Los etudiantes Fernando, Melany, Austin, Donaldo y Paola son los viven mas cerca del ITPA con una distancia de:",Paola.distancia)
	elif opcion == 5:
		print ("")
		print ("La materia con mejor rendimierto es Taller de Etica con un promedio de 8.4 ")
	elif opcion == 6:
		print("")
		print("Mirozlava con una edad de:", Mirozlava.edad)
		print("Alejandro con una edad de:", Alejandro.edad)
		print("Isaac con una edad de:", Isaac.edad)
		print("Diego con una edad de:", Diego.edad)
		print("Paola con una edad de:", Paola.edad)
		
	elif opcion == 1:
		break
	else:
		print("Incorrecta")