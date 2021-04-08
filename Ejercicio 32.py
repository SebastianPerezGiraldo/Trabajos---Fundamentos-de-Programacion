x = 1
conta1 = 0
conta2 = 0
while x <= 10:
    notas = int(input('Ingrese la nota del alumno: '))
    if notas >= 7:
        conta1 = conta1 + 1
    else:
        conta2 = conta2 + 1
    x = x + 1
print('Alumnos que tienen nota mayor o igual a 7: ', conta1)
print('Alumnos que tienen nota menor a 7: ', conta2)