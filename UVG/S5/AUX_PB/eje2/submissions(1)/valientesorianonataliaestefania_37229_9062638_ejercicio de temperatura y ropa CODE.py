#EJERCICIO 2

#Universidad del Valle de Guatemala
#C2005 - Algoritmos y programación básica
#SECCIÓN: 50
#Nombre: Natalia Estefanía Valiente Soriano
#Carné: 25767

#VARIABLES
escala= input("Por favor ingrese su escala de preferencia, F o C:")
Temperatura= float(input("por favor ingrese la temperatura actual:"))

#DEFINICIÓN DE TEMPERATURA
if escala == "F" or escala =="f":
    Temperatura= (Temperatura -32)*5/9
elif escala == "C" or escala =="c":
    Temperatura = Temperatura
else:
    print("Ingrese escala valida")
    

#TEMPERATURA Y ROPA
print(Temperatura)
if Temperatura <=10:
    print("Hace mucho frío")
    print("Se recomienda llevar ropa abrigada como: guantes, abrigo, bufanda, etc")
elif Temperatura <= 25:
    print("Clima templado")
    print("Se recomienda llevar ropa cómoda, medianamente abrigada")
elif Temperatura <=40:
    print("Clima cálido")
    print("Se sugiere llevar pantaloneta, tenis, gorra y protector solar")
elif Temperatura >40:
    print("Hace mucho calor")
    print("Se recomienda ir a la piscina, utilice traje de baño.")
else:
    print("Ingrese algo valido")

