s1 = 0
s2 = 0
s3 = 0
print('Turno mañana.')
for f in range (5):
    edad=int(input('Ingrese la edad: '))
    s1=s1+edad
p1=s1/5
print('Promedio de edad del turno de la mañana: ', p1)

print('Turno tarde.')
for f in range (6):
    edad=int(input('Ingrese la edad: '))
    s2=s2+edad
p2=s2/6    
print('Promedio de edad del turno de la tarde: ', p2)

print('Turno noche.')
for f in range (11):
    edad=int(input('Ingrese la edad: '))        
    s3=s3+edad
p3=s3/11    
print('Promedio de edad del turno ded la noche:', p3)

if p1 < p2 and p1 < p3:
    print("El turno mañana tiene un promedio menor de edades.")
else:
    if p2 < p3:
        print("El turno tarde tiene un promedio menor de edades.")
    else:
        print("El turno noche tiene un promedio menor de edades.")
        