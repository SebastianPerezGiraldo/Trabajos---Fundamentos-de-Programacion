# MATRICES
# 1. Declarar la matriz. 
matrizNum=[[12,32,56,48],[8,48,18,58],[2,4,6,8]]

# 2. Imprimir la matriz.
print('La matriz completa es: ',matrizNum)

# 3. Imprimir una posición fija.
print('Posición especifica: ',matrizNum[0][2])

# 4. Solicitar la posición del usuario.
fil=int(input('Fila: '))
col=int(input('Columna: '))
print('Posición leida por teclado: ',matrizNum[fil-1][col-1]) # Se coloca -1 para que no empiece en 0 sino en 1.

# 5. Imprimir una fila determinada.
print('Fila 1: ',matrizNum[0])
print('Fila 2: ',matrizNum[1])
print('Fila 3: ',matrizNum[2])

# 6. Imprimir una columna determinada.
for f in range(3):
    print('Columna 2: ',matrizNum[f][1])
    
# 7. Imprimir la columna que el usuario quiera.
col=int(input('Columna: '))
for f in range(3):
    print('Columna 2: ',matrizNum[f][col])
    
# 8. Sumar todos los elemnto de la matriz.
sumaEleMat=0
for f in range(3):
    for c in range(4):
        sumaEleMat=sumaEleMat+matrizNum[f][c]
print('La suma de todos los elementos es: ',sumaEleMat)

# 9. Sumar e imprimir los elementos de cada fila.
sumaEleMat=0
for f in range(3):
    for c in range(4):
        sumaEleMat=sumaEleMat+matrizNum[f][c]
    print('La suma de cada elementos es: ',sumaEleMat)
    sumaEleMat=0