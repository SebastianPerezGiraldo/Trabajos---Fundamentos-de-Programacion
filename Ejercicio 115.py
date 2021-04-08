def tres_valores():
    val1=int(input('Ingrese un valor: '))
    val2=int(input('Ingrese un valor: '))
    val3=int(input('Ingrese un valor: '))
    print('Menor de los tres: ')
    if val1 < val2 and val1 < val3:
        print(val1)
    else:
        if val2 > val3:
            print(val2)
        else:
            print(val3)
            
# PROGRAMA PRINCIPAL
tres_valores()
tres_valores()