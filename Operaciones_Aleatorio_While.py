#LIBRERIAS UTILIZADAS EN EL EJERCICIO
import random

cantidad_num=1
contador_repeticiones=0
acumulador_suma_total=0
acumulador_suma_positivos=0
acumulador_suma_negativos=0
numero=0

cantidad_num=int(input('Cantidad de números: '))

while contador_repeticiones < cantidad_num:
    numero=random.randint(-100, 100) 
    print('Número aleatorio: ', numero)
    acumulador_suma_total=acumulador_suma_total+numero
    if numero > 0:
        acumulador_suma_positivos=acumulador_suma_positivos+numero
    else:
        acumulador_suma_negativos=acumulador_suma_negativos+numero
    contador_repeticiones=contador_repeticiones+1
    
print('Suma todos: ', acumulador_suma_total)
print('Suma positivos: ', acumulador_suma_positivos)
print('Suma negativos: ', acumulador_suma_negativos)
