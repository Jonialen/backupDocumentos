# Universidad Del Valle de Guatemala
#CC2005 Algoritmos y Programación Básica
#Sección 50
#Nombre: Lucía Juracán Morán
#Carné: 25081

print("¡Bienvenido!, por favor siga las indicaciones:")
temperatura = input("Ingrese si su temperatura sera en C (celcius) o F (Fahrenheit): ")
grados = float(input("Ingrese la temperatura: "))
if temperatura == "F" or temperatura =="f":
    grados = (grados - 32)*5/9

elif temperatura == "C" or temperatura =="c":
    grados = grados
else:
    print("Los datos ingresados no son validos, por favor intente de nuevo")

if grados<0:
    print("Temperatura no valida")
elif 0 <= grados <=10:
    print("Te sugiero llevar chumpa, guantes, bufanda y un pantalon adecuado ;)")
elif 11 < grados <=25:
    print("Te sugiero llevar ropa cómoda, un sudadero y playeras ;)")
elif 26 < grados <=40:
    print("Te sugiero llevar pantaloneta, tenis, gorra, playera y bloqueador ;)")
else:
    print("Te sugiero ir a una piscina, con traje de baño ;)")