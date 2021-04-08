x=1
suma1=0
suma2=0
print("Primer lista")
while x<=15:
    valor=int(input("Ingrese valor:"))
    suma1=suma1+valor
    x=x+1
print("Segunda lista")
xs = 1
while xs<=15:
    valor=int(input("Ingrese valor:"))
    suma2=suma2+valor
    xs=xs+1
if suma1>suma2:
    print("Lista 1 mayor.")
else:
    if suma2>suma1:
        print("Lista2 mayor.")
    else:
        print("Listas iguales.")