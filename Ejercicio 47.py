cantidad=0
n=int(input('Cuantos triangulos va procesar: '))
for f in range(n):
    base=int(input('Ingrese la base del triangulo: '))
    altura=int(input('Ingrese la altura del triangulo: '))
    superf=base*altura/2
    print('La superficie es: ', superf)
    if superf > 12:
        cantidad=cantidad+1
print('La canridad de triangulos con superficie mayor a 12 son: ', cantidad)
