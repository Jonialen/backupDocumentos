#--------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#CC2005 Algoritmos y Programación básica
#Sección 50
#Nombre: Sebastián Pivaral Rodríguez
#Carné: 25012
#--------------------------------------------------------------------------------

T = float(input("Ingresar temperatura: "))
unidad_medida = input("Ingrese unida de medida (F o C): ")


#Unidad de medida
if unidad_medida == "F" or unidad_medida=="f":
    T_celsius = 5/9*(T-32)
    print(T_celsius, "°C")
elif unidad_medida == "C" or unidad_medida=="c":
    print(T, "°C")
    T_celsius = T
else:
    print("Ingrese una opción correcta")
    exit()
    
    
#Clasificación de temperatura y sugerencias
if 0<=T_celsius<=10:
    print("Clima frío, llevar chumpa, guantes y bufanda")
elif 11<=T_celsius<=25:
    print("Clima templado, llevar ropa cámoda, sudadero y playera")
elif 26<=T_celsius<=40:
    print ("Clima cálido, llevar tenis, playera, pantaloneta, gorra y bloqueador")
elif T_celsius>40:
    print("Calor extremo, ir a una piscina con traje de baño")
else:
    print("Ingrese una temperatura positiva")
    