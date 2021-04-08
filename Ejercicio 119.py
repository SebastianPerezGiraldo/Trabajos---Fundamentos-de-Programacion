def cantidad_vocales(cadena):
    cant=0
    for x in range (len(cadena)):
        if cadena[x]=='a' or cadena[x]=='e' or cadena[x]=='i' or cadena[x]=='o' or cadena[x]=='u':
            cant=cant+1
    print('Cantidad de vocales de las palabras', cadena, 'es: ', cant)
    
# BLOQUE PRINCIPAL
