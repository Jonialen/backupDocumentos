#-----------------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#CC2002 Algoritmos y Programación Básica
#Sección 50
#Nombre: Ely Sofía Sandoval
#Carné: 25723
#-----------------------------------------------------------------------------------------

unidad=input("Ingrese si la temperatura es en Fahrenheir o Celsius (F, C): ")
temp=float(input("Ingrese la temperatura del lugar: "))

if unidad=="F" or unidad=="f":
    temp=(temp-32)*5/9
elif unidad=="C" or unidad =="c":
    temp=temp
else:
    print("Ingrese el valor en Celsius o Fahrenheit")
    temp="NA"
if temp =="NA":
    print("No se hizo el calculo") #me ayudó Silvia, porque de lo contrario no se imprimia correctamente
elif temp>40:
    print("La temperatura en Celsius es", round(temp,2), "grados, te recomiendo ir a la piscina, llevar traje de baño")
elif temp>26:
    print("La temperatura en Celsius es", round(temp,2), "grados, te recomiendo llevar pantaloneta, tenis, gorra, playera y bloqueador")
elif temp>10:
    print("La temperatura en Celsius es", round(temp,2), "grados, te recomiendo llevar ropa cómoda, un sudadero y playera")
elif temp>=0:
    print("La temperatura en Celsius es", round(temp,2), "grados, te recomiendo llevar chumpa, guantes, bufanda y pantalón adecuado")
else:
    print("Ingresa la temperatura correcta")