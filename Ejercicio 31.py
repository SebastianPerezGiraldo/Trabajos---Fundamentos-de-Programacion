x = 1
cantidad = 0
n = int(input('Ingresar la cantidad e piezas: '))
while x <= n:
    largo = float(input('Ingresar el largo de cada perfil: '))
    if largo >= 1.2 and largo<= 1.3:
        cantidad = cantidad + 1
    x = x + 1
print('La cantidad de piezas aptas son: ', cantidad)
             