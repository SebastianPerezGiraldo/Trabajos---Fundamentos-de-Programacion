#Declaración y llamado a las libreras y paquetes
import math

#Declaración e inicialisción de variables
ca1 = 0.0
ca2 = 0.0
    
#Prototipo de la función
def f_titulo():
    print('CÁLCULO DE LA HIPOTENUSA DE UN TRIANGULO RECTÁNGULO')

def f_calcualarHipotenusa(p_ca1,p_ca2):
    #Variables
    hipo  = 0.0
        
    #Procesos
    hipo= math.sqrt(math.pow(p_ca1,2) + math.pow(p_ca2,2))
    
    #Retornar las respuesta
    return hipo
    
#Fin del desarrollo de la función

def f_despedida():
    print()
    print('...ADIOS...')

#Control del programa (PRINCIPAL)
f_titulo()
ca1=int(input('Digite cateto 1: '))
ca2=int(input('Digite cateto 2: '))
vps_rf_hipo=f_calcualarHipotenusa(ca1,ca2)
print()
print('La hipotenusa es: ', vps_rf_hipo)

#Realizo el llamado a la función por segunda vez

f_titulo()
ca1=int(input('Digite cateto 1: '))
ca2=int(input('Digite cateto 2: '))
vps_rf_hipo=f_calcualarHipotenusa(ca1,ca2)
print()
print('La hipotenusa es: ', vps_rf_hipo)
f_despedida()
