# Declarar la estructura tipo lista vacia
listaNotas=[]

# Almacenar datos en ka lista
for posVec in range (10):
    # Leemos la nota de un estudiante
    notaEstudiante=float(input('Ingrese la nota del estudiante: '))
    # Adicionamos la nota a la lista 
    listaNotas.append(notaEstudiante)
    
# Imprimir la lista 
print()
print(listaNotas)

#-----------------------------------------------------------------------------

# Declarar una variable para almacenar la suma 
sumaNotas = 0.0

# Recorre el arreglo e ir acumulando en la variable 
for x in range (len(listaNotas)):
    sumaNotas=sumaNotas+listaNotas[x]
    
print('Suma: ', sumaNotas)
