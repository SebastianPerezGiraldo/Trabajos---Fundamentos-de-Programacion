empleados = int(input('Ingrese la cantidad de empelados: '))
x = 1
conta1 = 0
conta2 = 0
gastos = 0
while x <= empleados:
    sueldo = float(input('Ingrese el sueldo de cada empleado: '))
    if sueldo <= 300:
        print('El empleado cobra entre los 100 a 300 dolares.')
        conta1 = conta1 +1
    else:
        print('El empleado cobra mas de 300 dolares.')
        conta2 = conta2 + 1
        gastos = gastos + sueldo
    x = x + 1
print('Los gastos de la empresa son: ', gastos)
        