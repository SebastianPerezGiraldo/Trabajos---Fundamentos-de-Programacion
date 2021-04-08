def mostrar_mayor(v1,v2,v3):
    print('El valor mayor de los tres números es: ')
    if v1 > v2 and v1 > v3:
        print(v1)
    else:
        if v2 > v3:
            print('v2')
        else:
            print('v3')

def cargar():
    val1=int(input('Ingrese un valor: '))
    val2=int(input('Ingrese un valor: '))
    val3=int(input('Ingrese un valor: '))
    mostrar_mayor(val1,val2,val3)

# PROGRAMA PRINCIPAL
cargar()