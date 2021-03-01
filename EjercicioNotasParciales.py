nomestud=input("Ingrese su nombre:")
pp=float(input("Ingresar nota primer parcial:"))
sp=float(input("Ingresar nota segundo parcial:"))
tp=float(input("Ingresar nota tercer parcial:"))
ina=float(input("Ingrese el número de inasistencias:"))
porcen1=pp*0.35
porcen2=sp*0.35
porcen3=tp*0.30
notafinal=porcen1+porcen2+porcen3/3
print("Su nota final es")
print(notafinal)

if (ina < 12) and (notafinal >= 3):
    print("Ganó académicamente")

if (ina < 12) and (notafinal < 3):
    print("Perdió académicamente")

if (ina > 12) and (notafinal/2):
    print("Perdió por inasistencias")

if (ina > 12) and (notafinal < 3):
    print("Perdió académicamente y por inasistencias")

