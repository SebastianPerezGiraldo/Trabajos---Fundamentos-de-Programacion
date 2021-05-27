#  Lectura de archivos tipo excel
#  Importar librerías
import pandas as pd

#  Leer archivo excel
df_archivoExcel = pd.read_excel('Ventas Productos.xlsx',index_col="Producto")
df_archivoExcel = df_archivoExcel[:10].copy()
print(df_archivoExcel)


# Grafica Vertical
df_archivoExcel.plot(kind = 'bar')

# Grafica Horizontal
df_archivoExcel.plot(kind = 'barh')

#  Ocupar todo el espacio
df_archivoExcel.plot(kind = 'barh', width=1) # Cada grupo de barras ocupa todo el espacio que tiene asignado

#  Grozor de las barras
df_archivoExcel.plot(kind = 'barh', width=3)

# Gráfica Apilada
df_archivoExcel.plot(kind = 'bar', 
                     stacked = 'True',          # Muestra las barras apiladas
                     alpha = 0.4,               # nivel de transparencia
                     width = 0.9,               # Grosor de las barras para dejar espacio entre ellas
                     figsize=(9,4));   

# Gráfico por una medalla

df_archivoExcel.plot(kind = 'bar',
                     width=0.8,
                     subplots=True,
                     figsize=(10,20));

# Cambiar colores
colores = ['YELLOW','BLUE','RED']

df_archivoExcel.plot(kind = 'bar',
             width=0.8,
             figsize=(10,4),
             color = colores);



# Funciones propias del desarrollador
Total2018 = df_archivoExcel[2018].sum()
print("Ventas año 2018 : ", Total2018)


maxs = df_archivoExcel.max()
print("Máximos de cada Columna:")
print(maxs)

mins = df_archivoExcel.min()
print("Máximos de cada Columna:")
print(mins)

medias = df_archivoExcel.mean()
print("Medias de cada Columna:")
print(medias)
