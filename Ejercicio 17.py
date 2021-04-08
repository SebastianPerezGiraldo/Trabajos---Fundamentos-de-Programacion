num = int(input('Ingrese un número entero positivo: '))
if num < 10:
    print('El número tiene una cifra.')
else:
    if num < 100:
        print('El número tiene dos cifras.')
    else:
        if num < 1000:
            print('El número tiene tres cifras.')
        else:
            print('Error tiene mas de tres cifras.')
