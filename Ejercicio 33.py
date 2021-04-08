x = 1
suma = 0
n = int(input('Ingrese el número de personas: '))
while x <= n:
    altura = float(input('Ingrese las alturas: '))
    suma = suma + altura
    x = x +1
promedio = suma/n
print('Altura promedio.', promedio)