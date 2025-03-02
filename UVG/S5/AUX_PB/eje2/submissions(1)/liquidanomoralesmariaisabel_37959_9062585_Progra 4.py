#------------------------------------------------------------------------------------------------------------------------
#Universidad del Valle de Guatemala
#Algoritmos y Programación Básica CC2005
#Sección 50
#María Isabel Liquidano
#251158
#------------------------------------------------------------------------------------------------------------------------

#El usuario debe ingresar los datos

temperatura = float(input("Ingrese la temperatura: "))

unidad = str(input("Ingrese la unidad de la temperatura (C o F): "))

# verificar que la unidad esté en °C, si no, convertirla

if unidad == "F" or unidad == "f":
    
    temperatura = (temperatura -32)*5/9
    
    print("La temperatura en celsius es ",temperatura)
    
elif unidad == "C" or unidad == "c":
    
    temperatura = temperatura
    
else:
    
    temperatura = "No aplica"
    
    print("Ingrese una escala valida")
    
# Clasificar el clima para sugerir la vestimenta adecuada

if temperatura == "No aplica":
    
    print("No se pudo sugerir vestimenta")

elif temperatura > 40:
    
    print("Hay calor extremo")
    
    print("Llevar traje de baño, ir a una piscina")
    
elif temperatura >= 26:
    
    print("Está cálido")
    
    print("Llevar pantaloneta, tenis, gorra, playera y bloqueador")
    
elif temperatura >= 11:
    
    print("Está templado")
    
    print("Llevar ropa cómoda como sudaderos y playeras")
    
else:
    
    print("Hay frío")
    
    print("Llevar chumpa, guantes, bufanda y pantalón adecuado")