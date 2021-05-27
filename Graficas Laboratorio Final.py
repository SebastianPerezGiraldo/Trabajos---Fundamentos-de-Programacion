import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Importante, para graficar tenemos que quitar los dos numerales de cada codigo de grafica.

## Goles de paises en local
x = ["Argentina","Bolivia","Brasil","chile","colombia","Ecuador","Japon","Paraguay","Peru","Qatar","uruguay","Venezuela"]
y = [195,113,222,157,139,121,47,123,135,4,141,96]

##plt.barh(x, y, color="green")


## Goles de paises en visitante
x2 = ["Argentina","Bolivia","Brasil","chile","colombia","Ecuador","Japon","Paraguay","Peru","Qatar","uruguay","Venezuela"]
y2 = [114,66,108,87,96,79,9,95,79,5,96,64]

##plt.barh(x2, y2, color="green")


## Cantidad de goles en total
x3 = ["Goles"]
y3 = [2391]

##plt.barh(x3, y3, color="green")


## Goles por copa local
x4 = ["FIFA Q","amistosos","Copa america","Copa paz","Confederate cup","Kirin cup","FIFA","Gold cup","AFC","Pasifico cup"]
y4 = [877,305,258,1,12,13,15,2,4,6]

##plt.barh(x4, y4, color="green")

## Goles por copa visitante
x5 = ["FIFA Q","amistosos","Copa america","Copa paz","Confederate cup","Kirin cup","FIFA","Gold cup","AFC","Pasifico cup"]
y5 = [488,225,143,3,10,6,11,3,5,7]

##plt.barh(x5, y5, color="green")

## Goles por copa total
x6 = ["FIFA Q","amistosos","Copa america","Copa paz","Confederate cup","Kirin cup","FIFA","Gold cup","AFC","Pasifico cup"]
y6 = [1754,530,401,4,22,19,26,5,9,13]

##plt.barh(x6, y6, color="green")


## Partidos jugados en local por selecciones
x7 = ["Argentina","Bolivia","Brasil","chile","colombia","Ecuador","Japon","Paraguay","Peru","Qatar","uruguay","Venezuela"]
y7 = [105,81,94,88,91,72,44,81,92,6,80,80]

##plt.barh(x7, y7, color="green")


## Partidos jugados en visitantes por selecciones
x8 = ["Argentina","Bolivia","Brasil","chile","colombia","Ecuador","Japon","Paraguay","Peru","Qatar","uruguay","Venezuela"]
y8 = [75,92,60,89,96,97,9,101,103,4,89,99]

##plt.barh(x8, y8, color="green")

## Seleccion que jugo mas partidos 
x9 = ["Argentina","Bolivia","Brasil","chile","colombia","Ecuador","Japon","Paraguay","Peru","Qatar","uruguay","Venezuela"]
y9 = [180,173,154,177,187,169,53,182,195,10,169,179]

##plt.barh(x9, y9, color="green")

## Goles totales de cada seleccion
x10 = ["Argentina","Bolivia","Brasil","chile","colombia","Ecuador","Japon","Paraguay","Peru","Qatar","uruguay","Venezuela"]
y10 = [309,179,330,224,235,200,56,218,214,9,237,160]

##plt.barh(x10, y10, color="green")