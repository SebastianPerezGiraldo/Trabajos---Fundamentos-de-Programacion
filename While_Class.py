print('SISTEMA DE NOTAS DE UN CURSO DE PROGRAMACIÓN')

# ENTRADA
num_estu=int(input('Ingrese la cantidad de estudiantes del grupo: '))

#DECLARAR LA VARIABLE QUE CONTROLA EL CICLO
contador_repeticiones = 0
cantidad_estudiantes_aprobaron = 0
cantidad_estudiantes_reprobaron = 0
suma_definitiva_estudiantes = 0
suma_definitiva_estudiantes_aprobaron = 0
suma_definitiva_estudiantes_reprobaron = 0
promedio_definitiva_estudiantes_aprobaron = 0.0
promedio_definitiva_estudiantes_reprobaron = 0.0


# PROCESO
#INICAR EL CICLO
while contador_repeticiones < num_estu:
    #LECTURA DELAS NOTAS DE CADA ESTUDIANTE
    nombre=(input('Digite nombre del estudiante: '))
    not1=float(input('Digite la nota del primer parcial del estudiante: '))
    not2=float(input('Digite la nota del segundo parcial del estudiante: '))
    not3=float(input('Digite la nota del tercer parcial del estudiante: '))
    
    #CALCULAR LA DEFINITIVA DE CADA ESTUDIANTE
    nota_defini=(not1+not2+not3)/3
    #SUMAR LAS DEFINITIVAS DE LOS ESTUDIANTES PARA CALCULAR LOS PROMEDIOS
    suma_definitiva_estudiantes=suma_definitiva_estudiantes+nota_defini
    print('')
    print('La nota definitiva es: ', nota_defini)
    
    if(nota_defini>=3.0):
        cantidad_estudiantes_aprobaron=cantidad_estudiantes_aprobaron+1
        #SUMAR LAS NOTAS DE LOS ESTUDIANTES QUE APROBARON
        suma_definitiva_estudiantes_aprobaron=suma_definitiva_estudiantes_aprobaron+nota_defini
    else:
        cantidad_estudiantes_reprobaron=cantidad_estudiantes_reprobaron+1
        #SUMAR LAS NOTAS DE LOS ESTUDIANTES QUE REPROBARON
        suma_definitiva_estudiantes_reprobaron=suma_definitiva_estudiantes_reprobaron+nota_defini
    
    #INCREMENTAR LA VARIABLE QUE CONTROLA EL CICLO
    contador_repeticiones = contador_repeticiones+1

# FIN DEL CICLO
#CALCULAR EL PROMEDIO DEL GRUPO
promedio_definitiva_estudiantes=suma_definitiva_estudiantes/num_estu
promedio_definitiva_estudiantes_aprobaron=suma_definitiva_estudiantes_aprobaron/cantidad_estudiantes_aprobaron
promedio_definitiva_estudiantes_reprobaron=suma_definitiva_estudiantes_reprobaron/cantidad_estudiantes_reprobaron

print('')
print('OTROS CALCULOS')
print('2. Cantidad de estudiantes que aprobaron: ', cantidad_estudiantes_aprobaron)
print('3. Cantidad de estudiantes que reprobaron: ', cantidad_estudiantes_reprobaron)
print('4. Promedio del grupo: ', promedio_definitiva_estudiantes)
print('5. Promedio de estudiantes que aprobaron: ', promedio_definitiva_estudiantes_aprobaron)
print('6. Promedio de estudiantes que reprobaron: ', promedio_definitiva_estudiantes_reprobaron)