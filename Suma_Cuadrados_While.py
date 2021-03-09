# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:42:58 2021

@author: sebas
"""

contador_repeticiones=1
cuadrado_num=0
acumulador_suma=0
cantidad_num=0

cantidad_num=int(input('Ingrese la cantidad de números: '))

while contador_repeticiones <= cantidad_num:
    cuadrado_num = pow(contador_repeticiones,2)
    acumulador_suma+=cuadrado_num
    print('El cuadrado de: ', contador_repeticiones, 'es:', cuadrado_num)
    print('La suma acumulada es:', acumulador_suma)
    contador_repeticiones=contador_repeticiones+1
    
print('La suma de los cuadrados es: ', acumulador_suma)
