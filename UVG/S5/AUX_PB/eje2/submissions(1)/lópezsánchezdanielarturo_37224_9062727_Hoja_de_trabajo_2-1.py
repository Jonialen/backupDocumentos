#---------------------------------------------------------------
#Universidad Del Valle de Guatemala
#Algoritmos y Programación Básica
#Sección 50
#Nombre: Daniel López
#Carné 25670
#---------------------------------------------------------------

# -------- INGRESO DE DATOS ------------
print('-------- Bienvenido a Whether-Weather ------------\nEn este programa le ayudaremos a definir la ropa que debe llevar a su destino.')
temp =  float(input('Ingrese la temperatura promedio de su destino en la época que lo visitará:\n'))
degree= str(input('¿Este valor está dado en escala Celsius (C) o Fahrenheit (F)?\nIngrese la letra "C" o "F" según corresponda: '))


# ----------- Conversion de datos -------
if degree == 'F' or degree=='f':
    temp = (temp - 32)*5/9
    print('La temperatura fue convertida a grados Celsius')
elif degree =="C" or degree=="c":
    temp = temp 
    print('La escala es Celsius')
else:
    print("Ingrese una escala real")
    exit()

# --------- Errores de rangos de temperatura ---------
if temp < 0 or temp > 60: # rangos establecidos como temperaturas reales para C
    print('Ingrese datos reales de temperatura Celsius')
    exit() 
else: print('Escala correcta de temperatura')

# ------------- Desplegar recomendacion -------
print('Temperatura promedio: ', round(temp,None), '°C')
if temp > 40:
    print('Hará calor extremo. Se recomienda ir a una piscina, con traje de baño.')
elif temp >= 26:
    print("Estará cálido. Lleva pantaloneta, tenis, gorra, playera y bloqueador.")
elif temp >= 11:
    print('Estará templado. Lleva ropa cómoda, un sudadero y playera.')
else:
    print('Hará mucho frío. Lleva chumpa, guantes, bufanda y pantalón adecuado.')




