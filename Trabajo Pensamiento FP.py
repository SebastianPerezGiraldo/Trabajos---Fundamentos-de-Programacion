#!/usr/bin/env python
# coding: utf-8

# # VALOR NETO

# In[14]:


valor_neto = float(input("Ingrese valor neto de la compra: "))
iva = float(0.19)
descuento = float(0.5)
total_iva = valor_neto * iva
total_pago = total_iva + valor_neto
total_descuento = total_pago - descuento
print("Su total a pagar con iva es: ", total_pago)
print("Su total a pagar con descuento es: ", total_descuento)


# # CÍRCULO Y CIRCUNFERENCIA 

# In[13]:


radio = int(input("Ingrese el radio del círculo: "))
pi = float(3.14)
area_cir = pi * radio**2
long_cir = 2 * pi * radio
print("El área del cuadrado es", area_cir)
print("La longitud de su circunferencia es", long_cir)


# # CARACTERÍSTICAS IMC

# In[27]:


estatura = float(input("Ingrese su estatura: "))
peso = float(input("Ingrese su peso en kilogramos: "))
masa_corporal = peso / estatura**2
print("Su masa corporal es")
print(masa_corporal)


# # EXAMEN SUPLETORIO

# In[14]:


nom = input("Ingrese su nombre completo: ")
exam1 = int(input("Ingrese la calificación del primer bimestre: "))
exam2 = int(input("Ingrese la calificación del segundo bimestre: "))
dos_bim = exam1 + exam2 / 2
if dos_bim > 5:
    print("Ha ganado el examen")
    print(dos_bim)
else:
    print("Ha perdido el examen")
    print(dos_bim)


# # VELOCIDAD VEHÍCULO

# In[1]:


distancia = float(input("Ingrese la ditancia recorrida: "))
tiempo = float(input("Ingrese el tiempo transcurrido: "))
kil_hor = distancia / tiempo
print("La velocidad del vehículo es", kil_hor)


# # ACTIVIDAD EMPLEADOS

# In[2]:


print("Actividad número uno:")
emple = int(input("Ingrese la cantidad de empeados: "))
horas = float(input("Ingrese las horas transcurridas: ")) 
print("")
print("Actividad número uno, segunda parte:")
emple2 = int(input("Ingrese la cantidad de empleados: "))
horas2 = float(input("Ingrese las horas transcurridas: "))


# # TEMPERATURA 

# In[5]:


c = float(input("Ingrese la temperatura en C°: "))
k = c + 273.15
f = (9 * c)/5 + 32
print("La temperatura de C° a Kelvin es", k)
print("La temperatura de C° a Fahrenheit es", f)


# # ÁREA Y PERÍMETRO RECTÁNGULO

# In[12]:


a = int(input("Ingrese el ancho del rectangulo: "))
b = int(input("Ingrese el largo del rectangulo: "))
perimetro = a + a + b + b
area = a * b
print("El perímetro del rectangulo es", perimetro)
print("El área del rectagulo es", area)


# # SUELDO EMPLEADO

# In[6]:


nom = input("Ingresar nombre del trabajo: ")
num_hor = int(input("Ingresar número de horas trabajadas: "))
val_hor = float(input("Ingresar el valor por cada hora: "))
seg_soc = 0.16
bonifi = 0.02
pago = num_hor * val_hor
val_total = (num_hor * val_hor) - seg_soc
val_bonif = val_total + bonifi
print("El sueldo neto es", pago)
if val_total > 300:
    print("El sueldo total es", val_total)
else:
    print("El sueldo total con bonificación es", val_bonif)


# # MESA HORIZONTAL

# In[ ]:


masa = int(input('Ingrese la masa del cuerpo en kilogramos (kg): '))
acel = int(input('Ingrese la aceleración del cuerpo (mtr/seg^2): '))
fuer = masa * acel
print('La fuerza que se aplica a un cuerpo en una mesa horizontal es', )
print(fuer)


# # CALCULADORA

# In[ ]:


num1 = float(input('Ingrese un número: '))
sing = input('Ingrese un signo de operaciones matemáticas: ')
num2 = float(input('Ingrese un número: '))
suma = num1+num2
rest = num1-num2
mult = num1*num2
divi = num1/num2
pote = num1**num2
(num1==1) or (num1==2) or (num1==3) or (num1==4) or (num1==5) or (num1==6) or (num1==7) or (num1==8) or (num1==9) or (num1==0)
(num2==1) or (num2==2) or (num2==3) or (num2==4) or (num2==5) or (num2==6) or (num2==7) or (num2==8) or (num2==9) or (num2==0)
print('')
if(sing=='+'):
    print('Suma=', suma)
elif(sing=='-'):
    print('Resta=', rest)
elif(sing=='*'):
    print('Multiplicación=', mult)
elif(sing=='/'):
    print('División=', divi)
elif(sing=='**'):
    print('Potensiación=', pote)


# # RAÍCES

# In[ ]:




