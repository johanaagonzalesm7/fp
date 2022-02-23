Usuario="Johana Macias"
Contraseña="Johanam"
U=str(input("Ingresa tu Usuario"))
C=str(input("Ingresa tu contraseña"))
i=0
while i==4:
	if C==Contraseña:
		print("Bienvenido al sistema")
	else:
		print("Contraseña o Usuario Incorrecto, Intenta de nuevo")
for i in range(1,4):
	print("Intentos fallidos")