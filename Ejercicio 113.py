def carga_suma():
    valor1 = int(input('Ingrese primer valor: '))
    valor2 = int(input('Ingrese segundo valor: '))
    suma=valor1+valor2
    print('La suma de los dos valores es: ', suma)
    
def separacion():
    print('__________________________________________')
    
# PROGRAMA PRINCIPAL
for f in range(5):
    carga_suma()
    separacion()