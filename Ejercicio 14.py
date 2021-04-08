not1 = int(input('Ingrese la primera nota: '))
not2 = int(input('Ingrese la segunda nota: '))
not3 = int(input('Ingrese la tercera nota: '))
promedio = (not1+not2+not3)/3
if promedio >= 7:
    print('Promocionado.')
else:
    if promedio >= 4:
        print('Regular')
    else:
        print('Reprobado.')
