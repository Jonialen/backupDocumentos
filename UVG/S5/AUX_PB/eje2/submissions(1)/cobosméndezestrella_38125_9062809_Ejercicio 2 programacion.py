#Universidad del Valle de Guatemala
#CC2005 Algoritmos y programación
#Sección 50
#Nombre:Estrella Cobos Mendez
#Carné:251295

temperatura = input("Ingrese si su temperatura será en C o F: ")
grados = float(input("Ingrese la tmperatura: "))
if temperatura == "F" or temperatura == "f":
    grados = (grados - 32)*5/9
    
elif temperatura == "C" or temperatura == "c":
    grados = grados
    
else:
    print("Los datos no son validos")
    

if grados<0:
    print("No valido")
elif 0 <= grados <=10:
    print("Frío, debes llevar chumpa, guantes, bufanda, pantalon adecuado")
elif 11 < grados <= 25:
    print("Templado, debes llevar ropa cómoda, un sudadero, playera")
elif 26 < grados <= 40:
    print("Cálido, debes llevar pantaloneta, tenis, gorra, playera, bloqueador")
else:
    print("Calor extremo, debes ir a una piscina, con traje de baño")
               