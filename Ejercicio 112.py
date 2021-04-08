def presentacion():
    print('Programa que permite cargar dos valores por teclado.')
    print('Efectua la suma de dos valores.')
    print('Muestre el resultado de la suma.')
    print('_______________________________')

def carga_suma():
    valor1 = int(input('Ingrese el primer valor: '))
    valor2 = int(input('Ingrese el segundo valor: '))
    suma=valor1+valor2
    print('La suma de los dos valores es: ', suma)
    
def finalizacion():
    print('_______________________________')
    print('Gracias por utilizar este programa.')
    
# PROGRAMA PRINCIPAL
presentacion()
carga_suma()
finalizacion()