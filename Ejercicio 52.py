c1 = 0
c2 = 0
c3 = 0 
c4 = 0
n = int(input('Cantidad de punrtos '))
for f in range (n):
    x = int(input('Ingresar coordenada x: '))
    y = int(input('Ingresar coordenada y: '))
    if x>0 and y>0:
        c1=c1+1
    else:
        if x<0 and y>0:
            c2=c2+1
        else:
            if x<0 and y<0:
                c3=c3+1
            else:
                if x>0 and y<0:
                    c4=c4+1
print('Cantidad de puntos ingresados en el primer cuadrante: ', c1)
print('Cantidad de puntos ingresados en el segundo cuadrante: ', c2)
print('Cantidad de puntos ingresados en el tercer cuadrante: ', c3)
print('Cantidad de puntos ingresados en el cuarto ccuadrante: ', c4)