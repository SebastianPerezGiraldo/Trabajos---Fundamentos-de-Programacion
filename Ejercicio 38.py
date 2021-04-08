x = 1
pares = 0
impares = 0
n = int(input('Cantidad de números enteros que va ingresar: '))
while x <= n:
    valor = int(input('Digite el número: '))
    if valor % 2 == 0:
        pares=pares+1
    else:
        impares=impares+1
    x=x+1
print("Cantadad de pares.", pares)
print("Cantidad de impares.", impares)