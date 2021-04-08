x = int(input('Ingrese cordenada x: '))
y = int(input('Ingrese cordenada y: '))
if x > 0 and y > 0:
    print('1° cuadrante.')
else:
    if x < 0 and y > 0:
        print('2° cuadrante.')
    else:
        if x < 0 and y < 0:
            print('3° cuadrante.')
        else:
            print('4° cuadrante.')