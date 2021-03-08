#!/usr/bin/env python
# coding: utf-8

# In[4]:


for x in range (101):
    print(x)


# In[10]:


for x in range (20,31):
    print(x)


# In[20]:


for x in range (1,100,2):
    print(x)


# In[22]:


suma=0
for f in range (10):
    valor=int(input('Ingrese valor: '))
    suma=suma+valor
print('')
print('La suma es:', suma)
promedio=suma/10
print('El promedio es:', promedio)


# In[28]:


aprobado=0
reprobado=0
for f in range (10):
    nota=int(input('Ingrese la nota:'))
    if nota>=7:
        aprobado=aprobado+1
    else:
        reprobado=reprobado+1
print('')
print('Cantidad de aprobados:', aprobado)
print('Cantidad de reprobados:', reprobado)


# In[ ]:




