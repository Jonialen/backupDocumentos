#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#CC2005 Algoritmos y Programación Básica 
#Sección 50
#Nombre: Christian Hastedt
#Carné: 25705
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tipo = input("Ingrese la unidad de temperatura (F para Fahrenheit, C para Celsius): ")
temp = float(input("Ingrese la temperatura: "))


if tipo == "F" or tipo =="f":
    temp = (temp - 32) * 5 / 9
    print("Temperatura convertida a Celsius:",temp,"°C")
elif tipo == "C" or tipo =="c":
    temp=temp
    temp ="NA"
    
else:
    temp = "NA"
    print("Ingrese una opcion valida")
    
if temp == "NA":
    print("No se hizo el cálculo")

elif temp > 40:
    print("Categoría: Calor extremo")
    print("Recomendación: Es recomendable ir a la piscina y usar traje de baño.")
elif temp >= 26:
    print("Categoría: Cálido")
    print("Recomendación: Usa pantaloneta, tenis, gorra, playera y bloqueador.")
elif temp >= 11:
    print("Categoría: Templado")
    print("Recomendación: Usa ropa cómoda, sudadero y playera.")
else:
    print("Categoría: Frío")
    print("Recomendación: Usa chumpa, guantes, bufanda y pantalón adecuado.")
