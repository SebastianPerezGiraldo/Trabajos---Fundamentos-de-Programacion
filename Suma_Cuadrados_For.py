# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# SUMA CUADRADO PRIMEROS 100 NÚMERO ENTEROS (FOR)

acumulador_suma=0
cuadrado_num=0
num=1

cantidad_num = int(input('Cantidad de números: '))

for num in range(cantidad_num+1):
    cuadrado_num = num*num
    acumulador_suma = acumulador_suma + cuadrado_num
    print('El cuadrado de: ', num, 'es: ', cuadrado_num)
    print('La suma acumulada es: ', acumulador_suma)
    
print('La suma de los cuadrados es: ', acumulador_suma)
