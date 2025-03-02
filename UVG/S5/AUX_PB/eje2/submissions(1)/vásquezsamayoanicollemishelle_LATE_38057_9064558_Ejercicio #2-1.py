#Universidad Del valle de Guatemala
#CC2005 Algoritmmos y Programación Básica
#Sección 50
#Nombre: Nicolle Vásquez
#Carné: 251181

print("Siga los pasos:")
temperatura = float(input("Ingrese la temperatura:"))
unidad = input(str("ingrese unidad C celsius/ F fahrenheit:"))

if unidad == "F" or unidad =="f":
    temperatura = (temperatura - 32) * 5/9
    
if temperatura>= 0 and temperatura <= 10:
    clima = "Frio"
    ropa = "Chumpa, guantes, bufanda, pantalon adecuado"
    print(clima)
    print(ropa)

elif temperatura>= 11 and temperatura <= 25:
    clima = "Templado"
    ropa = "ropa cómoda, un sudadero, playera"
    print(clima) 
    print(ropa)
elif temperatura>= 26 and temperatura <= 40:
    clima = "calido"
    ropa = "pantaloneta, tenis, goora, playera, blooqueador"
    print(clima) 
    print(ropa)
elif temperatura<0:
    print("Ingrese una temperatura valida")
else: 
    clima = "Calor extremo"
    ropa = "piscina, con traje de baño"
    print(clima)
    print(ropa)
    
    