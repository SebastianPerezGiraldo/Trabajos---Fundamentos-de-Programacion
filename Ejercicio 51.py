cant1=0
cant2=0
cant3=0
n = int(input('Ingrese número de triangulos que va ingresar: '))
for f in range (n):
    l1 = int(input('Ingresar primer lado del triangulo: '))
    l2 = int(input('Ingresar segundo lado del triangulo: '))
    l3 = int(input('Ingresar tercer lado del triangulo: '))
    if l1 == l2 and l1 == l3:
        print('Equilátero, tres lados iguales.')
        cant1=cant1+2
    else:
        if l1 == l2 or l1 == l3 or l2 == l3:
            print('Isóceles, dos lados iguales.')
            cant2=cant2+1
        else:
            print('Escaleno, ningún lado igual')
            cant3=cant3+1
print('Cantidad de triangulos eqiláteros: ', cant1)
print('Cantidad de triangulos isóceles: ', cant2)
print('Cantidad de triangulos escalenos: ', cant3)
