def mostrar_mensaje(mensaje):
    print(mensaje)
    print('__________________________________________________________________')
    
def carga_suma():
    val1=int(input('Ingrese el primer valor: '))
    val2=int(input('Ingrese el segundo valor: '))
    suma=val1+val2
    print('La suma de los dos valores es: ', suma)

# PROGRAMA PRINCIPAL
mostrar_mensaje('El programa calcula la suma de dos valores ingresados por teclado.')
carga_suma()
mostrar_mensaje('Gracias por utilizar este programa.')
