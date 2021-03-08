#!/usr/bin/env python
# coding: utf-8

# In[8]:


x=1
while x <= 100:
    print(x)
    x=x+1


# In[9]:


x=1
while x <= 500:
    print(x)
    x=x+1


# In[16]:


x=50
while x <= 100:
    print(x)
    x=x+1


# In[17]:


x=-50
while x <= 0:
    print(x)
    x=x+1


# In[18]:


x=2
while x <= 100:
    print(x)
    x=x+2


# In[19]:


n=int(input('Ingrese el valor total: '))
x=1
while x <= n:
    print(x)
    x=x+1


# In[1]:


x=1
suma=0
while x <= 10:
    valor=int(input('Digite un valor: '))
    suma=suma+valor
    x=x+1
promedio=suma//10
print('')
print('La suma de estos números es', suma)
print('El promedio de estos número es', promedio)


# In[5]:


cantidad=0
x=1
c=int(input('Cantidad de piezas a procesar: '))
while x<=c:
    largo=float(input('Ingrese la longitud de cada perfil: '))
    if largo>=1.20 and largo<=1.30:
        cantidad=cantidad+1
    x=x+1
print('')
print('La cantidad de piezas aptas son', cantidad)


# In[2]:


print('NOTAS ALUMNOS')
x=1
conta1=0
conta2=0
while x<=10:
    nota=float(input('Ingrese la nota: '))
    if nota>=7:
        conta1=conta1+1
    else:
        conta2=conta2+1
    x=x+1
print('Cantidad de alumnos con notas mayores o iguales a 7:', conta1)
print('Cantidad de alumnos con notas menores a 7:', conta2)


# In[9]:


x=1
suma=0
n=int(input('Digite el conjunto de alturas que necesita: '))
while x<=n:
    a=float(input('Ingrese la altura de la persona: '))
    suma=suma+a
    x=x+1
promedio=suma/n
print('La estatura promedio es', promedio)


# In[14]:


empleados=int(input('Ingrese el número de empleados que hay en la empresa: '))
x=1
smenor=0
smayor=0
gastos=0
while x<=empleados:
    sueldo=float(input('Ingrese el sueldo de los empleados: '))
    if sueldo<=300:
        smenor=smenor+1
    else:
        smayor=smayor+1
    gastos=gastos+sueldo
    x=x+1
print('')
print('Cantidad de empleados con sueldo entre 100 y 300', smenor)
print('Cantidad de sueldo mayor a 300', smayor)
print('Gastos total de la empresa en sueldo', gastos)


# In[16]:


x=11
while x<=275:
    print(x)
    x=x+11


# In[17]:


x=8
while x<=500:
    print(x)
    x=x+8


# In[19]:


x=1
suma1=0
suma2=0
print('Primer lista')
while x<=15:
    valor=int(input('Ingrese el valor: '))
    sum1=suma1+valor
    x=x+1
print('')
print('Segunda lista')
x = 1
while x<=15:
    valor=int(input('Ingrse el valor: '))
    suma2=suma2+valor
    x=x+1
print('')
if suma1>suma2:
    print('Lista 1 mayor.')
else:
    if suma1<suma2:
        print('Lista 2 mayor.')
    else:
        print('Listas iguales.')
        


# In[21]:


x=1
pares=0
impares=0
n=int(input('Número que ingrsará: '))
print('')
while x<=n:
    valor=int(input('Ingrese el valor: '))
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
    x=x+1
print('')
print('Cantidad de pares', pares)
print('Cantidad de impares', impares)
        

