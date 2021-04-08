sueldo = int(input('Ingrese el sueldo gana en la empresa: '))
antiguedad = int(input('Ingrese la antiguedad quelleva en la empresa: '))
if sueldo < 500 and antiguedad >= 10:
    aumento = sueldo * 0.20
    sueldototal = sueldo + aumento
    print('El sueldo a pagar es: ', sueldototal)
else:
    if sueldo < 500 and antiguedad < 10:
        aumento = sueldo * 0.05
        sueldototal = sueldo + aumento
        print('El sueldo a pagar es: ', sueldototal)
    else:
        print('El sueldo a pagar es: ', sueldo)