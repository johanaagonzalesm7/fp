N = str(input('¿Cual es tu nombre(s):'));
Ap = str(input('¿Cual es tu primer apellido:'));
Am = str(input('¿Cual es tu segundo apellido:'));
D = str(input('¿Cual es tu direccion'));
P = int(input('¿Cual es tu promedo'));
AD = str(input('¿Tienes materias reprovadas Si o No?'));
Si = str(input);
No = str(input);

print (N);
print (Ap);
print (Am);
print (D);
print (P);
print (AD);
SN = str(input('Verificar si los datos son correctos, Si o NO'));
if SN == ("Si"):
	print('Tu solicitud a sido aceptada')
else:
	print("Corregir tus datos")
	N = str(input('¿Cual es tu nombre(s):'));
	Ap = str(input('¿Cual es tu primer apellido:'));
	Am = str(input('¿Cual es tu segundo apellido:'));
	D = str(input('¿Cual es tu direccion'));
	P = int(input('¿Cual es tu promedo'));
	AD = str(input('¿Tienes materias reprovadas Si o No?'));
	if  P >=8:
		print ('Ya tienes una oportunidad de ser aceptado');
	else:
		print ('solicitud cancelada');
		if D==("Pabellon de Arteaga"):
			print ('Solicitud cancelada');
		else: 
			if AD == ("Si"):
				print ('Solicitud cancelada');
			else:
				print ('Has sido aceptado para la beca');
				print ('FELICIDADES')

		
