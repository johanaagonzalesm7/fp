number = 23
running = True

while running:
    Calificacion = int(input('Intruduce tu Calificacion : '))
    Pro=float(Calificacion)

    if Pro >= 6:
        print('Felicidades has aprobado :)')
        
        running = False
    elif Pro < 6:
        print('Lo siento has reprobado :(')
else:
    print('El semestre while acabo.')
    

print('Fin')