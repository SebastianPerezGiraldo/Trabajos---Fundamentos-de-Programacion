aprobados = 0
reprobados = 0
for x in range (10):
    nota = float(input('Ingrse las notas de los alumnos: '))
    if nota >= 7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1
print('Aprobados', aprobados)
print('Reprobados', reprobados)