c1 = 0
c2 = 0
c3 = 0
c4 = 0
for f in range (10):
    valor = int(input('Ingrese un valor: '))
    if valor < 0:
       c1=c1+1
    else:
        if valor > 0:
            c2=c2+1
    if valor%15 == 0:
        c3=c3+1
    if valor%2 == 0:
        c4=c4+1
print('Cantidad de valores negativos: ', c1)
print('Cantidad de valores positivos: ', c2)
print('Cantidad de multiplos de 15: ', c3)
print('Suma de los valores pares: ', c4)