#IMPORTAMOS LIBRERIAS 
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import xlrd
pd.__version__

df=pd.read_excel('C:\\Users\\Usuario\\Downloads\\Futbol_Partidos.xlsx', index_col=0)

#GOLES DE VISITA Y DE LOCAL DE CADA EQUIPO
def gol_bolivia():
    goles_local_bolivia=df[df['local']=='Bolivia']
    print(goles_local_bolivia)
    total_goles=goles_local_bolivia['goles_local'].sum()
    goles_visitante_bolivia=df[df['visitante'] =='Bolivia']
    print(goles_visitante_bolivia)
    total_goles_v=goles_visitante_bolivia['goles_visita'].sum()
    return(total_goles, total_goles_v)

def gol_peru():
    goles_local_peru=df[df['local']=='Peru']
    total_goles=goles_local_peru['goles_local'].sum()
    goles_visitante_peru=df[df['visitante'] =='Peru'] 
    total_goles_v=goles_visitante_peru['goles_visita'].sum()
    return total_goles, total_goles_v

def gol_paraguay():
    goles_local_paraguay=df[df['local']=='Paraguay']
    total_goles=goles_local_paraguay['goles_local'].sum()
    goles_visitante_paraguay=df[df['visitante'] =='Paraguay']
    total_goles_v=goles_visitante_paraguay['goles_visita'].sum()
    return total_goles, total_goles_v 

def gol_japon():
    goles_local_japon=df[df['local']=='Japon']
    total_goles=goles_local_japon['goles_local'].sum()
    goles_visitante_japon=df[df['visitante'] =='Japon']
    total_goles_v=goles_visitante_japon['goles_visita'].sum()
    return total_goles, total_goles_v  

def gol_argentina():
    goles_local_argentina=df[df['local']=='Argentina']
    total_goles=goles_local_argentina['goles_local'].sum()
    goles_visitante_argentina=df[df['visitante'] =='Argentina']
    total_goles_v=goles_visitante_argentina['goles_visita'].sum()
    return total_goles, total_goles_v  

def gol_colombia():
    goles_local_colombia=df[df['local']=='Colombia']
    total_goles=goles_local_colombia['goles_local'].sum()
    goles_visitante_colombia=df[df['visitante'] =='Uruguay']
    total_goles_v=goles_visitante_colombia['goles_visita'].sum()
    return total_goles, total_goles_v  

def gol_ecuador():
    goles_local_ecuador=df[df['local']=='Ecuador']
    total_goles=goles_local_ecuador['goles_local'].sum()
    goles_visitante_ecuador=df[df['visitante'] =='Ecuador']
    total_goles_v=goles_visitante_ecuador['goles_visita'].sum()
    return total_goles, total_goles_v  

def gol_venezuela():
    goles_local_venezuela=df[df['local']=='Venezuela']
    total_goles=goles_local_venezuela['goles_local'].sum()
    goles_visitante_venezuela=df[df['visitante'] =='Venezuela']
    total_goles_v=goles_visitante_venezuela['goles_visita'].sum()
    return total_goles, total_goles_v  

def gol_chile():
    goles_local_chile=df[df['local']=='Chile']
    total_goles=goles_local_chile['goles_local'].sum()
    goles_visitante_chile=df[df['visitante'] =='Chile']
    total_goles_v=goles_visitante_chile['goles_visita'].sum()
    return total_goles, total_goles_v  


def gol_brasil():
    goles_local_brasil=df[df['local']=='Brasil']
    total_goles=goles_local_brasil['goles_local'].sum()
    goles_visitante_brasil=df[df['visitante'] =='Brasil']
    total_goles_v=goles_visitante_brasil['goles_visita'].sum()
    return total_goles, total_goles_v       

def gol_qatar():
    goles_local_qatar=df[df['local']=='Qatar']
    total_goles=goles_local_qatar['goles_local'].sum()
    goles_visitante_qatar=df[df['visitante'] =='Qatar']
    total_goles_v=goles_visitante_qatar['goles_visita'].sum()
    return total_goles, total_goles_v   

def gol_uruguay():
    goles_local_uruguay=df[df['local']=='Uruguay']
    total_goles=goles_local_uruguay['goles_local'].sum()
    goles_visitante_uruguay=df[df['visitante'] =='Uruguay']
    total_goles_v=goles_visitante_uruguay['goles_visita'].sum()
    return(total_goles, total_goles_v)  

#TOTAL DE GOLES DE TODOS LOS PARTIDOS
def total_goles():
    total_goles=df['goles_local'].sum()
    total_goles_v=df['goles_visita'].sum()
    total_t=total_goles+total_goles_v
    return total_t

#GOLES DE LOCAL Y DE VISITA EN CADA TORNEO
def gol_fifa_qua():
    gol_loc_camp=df[df['torneo'] =='FIFA World Cup qualification']
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='FIFA World Cup qualification']
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v

def gol_friendly():
    gol_loc_camp=df[df['torneo'] =='Friendly']
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='Friendly']
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v

def gol_copa_a():
    gol_loc_camp=df[df['torneo'] =='Copa América']
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='Copa América']
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v

def gol_copa_paz():
    gol_loc_camp=df[df['torneo'] =='Copa Paz del Chaco']
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='Copa Paz del Chaco']
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v  

def gol_conf_cup():
    gol_loc_camp=df[df['torneo'] =='Confederations Cup']
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='Confederations Cup']
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v       

def gol_kirin_cup():
    gol_loc_camp=df[df['torneo'] =='Kirin Cup']
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='Kirin Cup'] 
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v 

def gol_fifa_wc():
    gol_loc_camp=df[df['torneo'] =='FIFA World Cup']  
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='FIFA World Cup'] 
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v   

def gol_gold_cup():
    gol_loc_camp=df[df['torneo'] =='Gold Cup']
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='Gold Cup']
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v    

def gol_asian_cup():
    gol_loc_camp=df[df['torneo'] =='AFC Asian Cup']
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='AFC Asian Cup']
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v 

def gol_copa_pac():
    gol_loc_camp=df[df['torneo'] =='Copa del Pacífico']
    tot_gol_fifa=gol_loc_camp['goles_local'].sum()
    gol_vis_camp=df[df['torneo'] =='Copa del Pacífico']
    tot_gol_fifa_v=gol_vis_camp['goles_visita'].sum()
    return tot_gol_fifa, tot_gol_fifa_v   

#CANTIDAD TOTAL DE GOLES DE CADA CAMPEONATO 
def can_gol_1():
    tor_gol=df[df['torneo'] =='FIFA World Cup qualification']
    can_gol_l=tor_gol['goles_local'].sum()
    can_gol_v=tor_gol['goles_visita'].sum()
    goles_total=can_gol_l+can_gol_v
    return goles_total

def can_gol_2():
    tor_gol=df[df['torneo'] =='Copa América']
    can_gol_l=tor_gol['goles_local'].sum()
    can_gol_v=tor_gol['goles_visita'].sum ()
    goles_total=can_gol_l+can_gol_v  
    return goles_total

def can_gol_3():
    tor_gol=df[df['torneo'] =='Copa Paz del Chaco']
    tot_gol_l=tor_gol['goles_local'].sum()
    tot_gol_v=tor_gol['goles_visita'].sum()
    goles_total=tot_gol_l+tot_gol_v
    return(goles_total)

def can_gol_4():
    tor_gol=df[df['torneo'] =='Confederations Cup']
    tot_gol_l=tor_gol['goles_local'].sum()
    tot_gol_v=tor_gol['goles_visita'].sum()
    goles_total=tot_gol_l+tot_gol_v
    return(goles_total)

def can_gol_5():
    tor_gol=df[df['torneo'] =='Kirin Cup']
    tot_gol_l=tor_gol['goles_local'].sum()
    tot_gol_v=tor_gol['goles_visita'].sum()
    goles_total=tot_gol_l+tot_gol_v
    return(goles_total)

def can_gol_6():
    tor_gol=df[df['torneo'] =='FIFA World Cup']
    tot_gol_l=tor_gol['goles_local'].sum()
    tot_gol_v=tor_gol['goles_visita'].sum()
    goles_total=tot_gol_l+tot_gol_v
    return(goles_total)

def can_gol_7():
    tor_gol=df[df['torneo'] =='Gold Cup']
    tot_gol_l=tor_gol['goles_local'].sum()
    tot_gol_v=tor_gol['goles_visita'].sum()
    goles_total=tot_gol_l+tot_gol_v
    return(goles_total)

def can_gol_8():
    tor_gol=df[df['torneo'] =='AFC Asian Cup']
    tot_gol_l=tor_gol['goles_local'].sum()
    tot_gol_v=tor_gol['goles_visita'].sum()
    goles_total=tot_gol_l+tot_gol_v
    return(goles_total)

def can_gol_9():
    tor_gol=df[df['torneo'] =='Copa del Pacífico']
    tot_gol_l=tor_gol['goles_local'].sum()
    tot_gol_v=tor_gol['goles_visita'].sum()
    goles_total=tot_gol_l+tot_gol_v
    return(goles_total)

def can_gol_10():
    tor_gol=df[df['torneo'] =='Friendly'] 
    tot_gol_l=tor_gol['goles_local'].sum()
    tot_gol_v=tor_gol['goles_visita'].sum()
    goles_total=tot_gol_l+tot_gol_v
    return(goles_total)

#Cantidad de partidos por seleccion
def can_par():
    can_p=df['local'].value_counts()
    can_p_v=df['visitante'].value_counts()
    tot=can_p+can_p_v
    return tot

#Cantidad de partidos local y visitante 
def can_par_lc():
    print("La cantidad de partidos de cada equipo como local es:")
    can_p=df['local'].value_counts()
    print(can_p)
    print("La cantidad de partidos de cada equipo como visitante es:")
    can_p_v=df['visitante'].value_counts()
    print(can_p_v)


#Seleccion que mas goles realizo en todos los partidos  

#Nombre de equipo y los partidos en los que ha participado 
def busqueda1():
    equipo_l=input("Ingrese el nombre del equipo para ver su listado como local (Inicial en mayuscula): ")
    equipo=df[df['local'] == equipo_l]
    equipo_v=input("Ingrese el nombre del equipo para ver su listado como visitante (Inicial en mayuscula): ")
    equipo1=df[df['visitante'] == equipo_v]
    print("El listado de",equipo_l," como local es: ",equipo)
    print("El listado de",equipo_v,"como visitante es: ",equipo1)
    
#Cantidad de juegos por equipo como local y visitante 
def busqueda2():
    equipo1=input("Ingrese el nombre de la seleccion para ver cuantos partidos jugó como local (Inicial en mayuscula): ")
    equipo_l=len(df[df['local'].str.contains(equipo1)])
    equipo2=input("Ingrese el nombre de la seleccion para ver cuantos partidos jugó como visitante (Inicial en mayuscula): ")
    equipo_v=len(df[df['visitante'].str.contains(equipo2)])
    print("La cantidad de partidos jugados por",equipo1,"como local es de:",equipo_l)
    print("La cantidad de partidos jugados por",equipo2,"como visitante es de:",equipo_v)

#Ciudades en la que jugó cada equipo     
def busqueda4():
    equipo1=input("Ingrese el nombre de la seleccion para ver en que ciudad jugó como local (Inicial en mayuscula): ")
    equipo_l=df[df['local'] == equipo1]
    ciudad=equipo_l['ciudad']
    equipo2=input("Ingrese el nombre de la seleccion para ver en que ciudad jugó como visitante (Inicial en mayuscula): ")
    equipo_v=df[df['visitante'] == equipo2]
    ciudad2=equipo_v['ciudad']
    print("En las ciudades que jugó",equipo1,"como local fueron"'\n',ciudad)
    print("En las ciudades que jugó",equipo2,"como visitante fueron"'\n',ciudad2)


#LLAMADO DE LAS FUNCIONES
print("Goles local y visitante de cada equipo")
print("El total de goles de Bolivia como local y visitante es de: ",gol_bolivia())
print("El total de goles de Peru como local y visitante es de: ",gol_peru())
print("El total de goles de Paraguay como local y visitante es de: ",gol_paraguay())
print("El total de goles de Japón como local y visitante es de: ",gol_japon())
print("El total de goles de Argentina como local y visitante es de: ",gol_argentina())
print("El total de goles de Colombia como local y visitante es de: ",gol_colombia())
print("El total de goles de Ecuador como local y visitante es de: ",gol_ecuador())
print("El total de goles de Venezuela como local y visitante es de: ",gol_venezuela())
print("El total de goles de Chile como local y visitante es de: ",gol_chile())
print("El total de goles de Brasil como local y visitante es de: ",gol_brasil())
print("El total de goles de Qatar como local y visitante es de: ",gol_qatar())
print("El total de goles de Uruguay como local y visitante es de: ",gol_uruguay())
print('\n')
print("Total global de goles")
print("El total de goles global es:",total_goles())
print('\n')
print("Goles local y visitante de cada torneo")
print("El total de goles de local y visitante en la FIFA World Cup qualification es:",gol_fifa_qua())
print("El total de goles de local y visitante en amistosos es:", gol_friendly())
print("El total de goles de local y visitante en la Copa América es:", gol_copa_a())
print("El total de goles de local y visitante en la Copa Paz del Chaco es:", gol_copa_paz())
print("El total de goles de local y visitante en la Confederations Cup es:", gol_conf_cup())
print("El total de goles de local y visitante en la Kirin Cup es:", gol_kirin_cup())
print("El total de goles de local y visitante en la FIFA World Cup es:", gol_fifa_wc())
print("El total de goles de local y visitante en la Gold Cup es:", gol_gold_cup())
print("El total de goles de local y visitante en la AFC Asian Cup es:", gol_asian_cup())
print("El total de goles de local y visitante en la Copa del Pacífico es:", gol_copa_pac())
print('\n')
print("Cantidad de goles por torneo")
print("La cantidad de goles en la FIFA World Cup qualification es de:",can_gol_1())
print("La cantidad de goles en la Copa América es de:",can_gol_2())
print("La cantidad de goles en la Copa Paz del Chaco es de:",can_gol_3())
print("La cantidad de goles en la Copa Confederations Cup es de:",can_gol_4())
print("La cantidad de goles en la Kirin Cup es de:",can_gol_5())
print("La cantidad de goles en la FIFA World Cup es de:",can_gol_6())
print("La cantidad de goles en la Gold Cup es de:",can_gol_7())
print("La cantidad de goles en la AFC Asian Cup es de:",can_gol_8())
print("La cantidad de goles en la Copa del Pacífico es de:",can_gol_9())
print("La cantidad de goles en los partidos amistosos es de:",can_gol_10())
print('\n')
print("La cantidad de partidos jugados por cada seleccion es:",can_par())
print('\n')
can_par_lc()
print('\n')
busqueda1()
print('\n')
busqueda2()
print('\n')
busqueda4()