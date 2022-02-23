Usuario="Johana Macias"
Contraseña="Johanam"
U=str(input("Ingresa tu Usuario"))
C=str(input("Ingresa tu contraseña"))
i=1
for i in range(4):
	if C==Contraseña:
		print("Bienvenido al sistema")
	else:
		print ("Contraseña o Usuario Incorrecto")
print("Espera 2 minutos para intentar de nuevo")
import time
def countdown(t):
	while t:
		mins,secs=(t,60)
		timer='{:02d}:{:02d}'.format
		print(timer,end="\r")
		time.sleep(1)
		t-=1
	print("El tiempo a termiando")
t=5
countdown(int(t))
