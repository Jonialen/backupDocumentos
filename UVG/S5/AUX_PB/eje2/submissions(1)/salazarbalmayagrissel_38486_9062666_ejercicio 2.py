tipo = input("¿Desea ingresar Fahrenheit o Celsius?(F/C) ")
temperatura = int(input("¿Cuál es la temperatura? "))

if tipo.lower() == "f" :
    temperatura = (temperatura - 32)*5/9
elif tipo.lower()=="c":
    temperatura = temperatura
else:
    print("Ingrese una opcion valida")
    exit()

if temperatura > 40:
     recomendacion = "Le sugiero ir a una piscina, con traje de baño."
elif temperatura > 25:
    recomendacion = "Le sugiero llevar pantaloneta, tenis, gorra, playeray bloqueador."
elif temperatura > 10:
    recomendacion = "Le sugiero llevar ropa cómoda, un sudadero y playera"
elif temperatura > 0:
    recomendacion = "Le sugiero llevar chumpa, guantes, bufanda y un pantalon adecuado"   
else:
    print("\n")
    print("Su temperatura no es valida")
    exit()

print("\n")

print("La temperatura en Celcius es: ", int(temperatura),"grados")
print (recomendacion)
