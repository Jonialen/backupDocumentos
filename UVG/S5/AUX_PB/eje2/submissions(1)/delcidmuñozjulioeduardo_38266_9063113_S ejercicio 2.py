print("Buen día, bienvenido a Vestitempu, donde le daremos las mejores recomendaciones sobre cómo vestir en este día de verano.\n")

print("Escoja entre Fahrenheit (F) o Celsius (C)")
Medida = input("Coloque solo la primera letra en mayúscula: ")
unidad = float(input("Coloque la temperatura en la que se encuentra: "))

if Medida == "F":
    temperatura = (unidad - 32) / 1.8          
else:
    temperatura = unidad 

if 1 <= temperatura <= 10:
    print("Frío: Chumpa, guantes, bufanda, pantalón adecuado.")
elif 11 <= temperatura <= 25:
    print("Templado: Ropa cómoda, sudadera, playera.")
elif 26 <= temperatura <= 40:
    print("Cálido: Pantaloneta, tenis, gorra, playera, bloqueador.")
elif 41 <= temperatura <= 50:
    print("Calor extremo: Ir a una piscina, traje de baño.")
else:
    print("Extremo peligroso: Hermano, salga de allí.")
