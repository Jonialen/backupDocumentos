#---------------------------------------------------------------
#Universidad Del Valle de Guatemala
#Algoritmos y Programación Básica
#Sección 50
#Nombre: Jose Batista
#Carné 25269
#--------------------------------------------------------------
tipo_de_temp = input(str("Ingrese el tipo de temperatura que desea utilizar (F para Fahrenheit y C para Celsius): "))
temperatura = float(input("Ingrese la temperatura: "))
if tipo_de_temp == "F":
    temperatura = (temperatura - 32) * 5/9
    print("La temperatura en Celsius es de: ", temperatura)
if 0<=temperatura<=10:
    print("Está frio, te sugiero llevar chumpa, guantes, bufanda y pantalón adecuado.")
elif 11<=temperatura<=25:
    print("Está templado, te sugiero llevar ropa cómoda, un sudadero, playera.")
elif 26<=temperatura<=40:
    print("Está cálido, te sugiero llevar pantaloneta, tenis, gorra, playera, bloqueador.")
elif temperatura>=41:
    print("Hay un calor extremo, te sugiero ir a una piscina y use un traje de baño.")
else:
    print("Hace muchisimo frio para ir, mejor reconsidera tu viaje.")
