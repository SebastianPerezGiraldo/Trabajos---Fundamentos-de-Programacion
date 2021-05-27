# Librerias 
import matplotlib
import matplotlib.pyplot as plt 

# Generar Datos
# Interactuar con listas
nombreProductos=['Arroz','Azucar','Vino','Leche']
ventaProductos=[100,50,30,20]

# Funciones que resuelven las preguntas 
def totalVentas():
    sumTotVen=0
    for pos in range(4):
        sumTotVen=sumTotVen+ventaProductos[pos]
    return (sumTotVen)
    
def promVenTot():
    promVen=0.0
    promVen=totalVentas()/len(ventaProductos)
    return(promVen)

# Llamar la función
print('Total de ventas: ', totalVentas())
print('Promedio de ventas: ', promVenTot())
    
# Generar el gráfico
fig, ax = plt.subplots()
ax.set_title('VENTAS DE LA EMPRESA')
ax.set_ylabel('VALOR')
ax.set_xlabel('PRODUCTO')

# Crear el gráfico
plt.bar(nombreProductos,ventaProductos)
plt.show()
