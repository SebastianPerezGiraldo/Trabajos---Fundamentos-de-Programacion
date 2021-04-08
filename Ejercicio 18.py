totalpreguntas = int(input('Cantidad de preguntas realizadas: '))
totalcorrectas = int(input('Cantidad de preguntas contestadas correctamente: '))
porcentaje = totalcorrectas * 100 / totalpreguntas
if porcentaje >= 90:
    print('Nivel maximo.')
else:
    if porcentaje >= 75:
        print('Nivel medio.')
    else:
        if porcentaje >= 50:
            print('Nivel regular.')
        else:
            print('Fuera de nivel.')