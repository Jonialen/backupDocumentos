#Universidad del Valle de Guatemala
#C2005 - Algoritmos y programación
#Sección 50
#Nombre: Marcela Molina
#Carné: 251621

#INPUT:
Temperatura = float(input("Ingrese la temperatura:"))
sistema=str(input("Deseas ingresar la temperatura en Celsius o Fahrenheit?:"))

#OUTPUT
if sistema== "Celsius":
  print("La temperatura en Celsius es:",Temperatura)
  if Temperatura > 40:
    print(" El clima es:!CALOR EXTREMO! Te sugiero que tomes tu traje de baño y disfrutes en la piscina")
  elif Temperatura >= 26:
    print( "El clima es: Cálido, te sugiero vestirte con una playera fresca, pantalonetas y tenis. No olvides llevar una gorra y bloqueador solar!")
elif Temperatura >= 11:
  print("El clima es: Templado, te sugiero llevar ropa cómoda como una playera y un sudadero por si acaso.")
elif Temperatura >= 0:
  print("El clima es: !FRÍO! te sugiero llevar guantes, bufanda y un pantalón adecuado. No olvides una chumpa super abrigadora!")

else:
    
   if sistema== "Fahrenheit":
    Conversión=(Temperatura*9/5)+32
    print( "La temperatura en Fahrenheit es:", Conversión)
    if Conversión> 40:
      print(" El clima es:!CALOR EXTREMO! Te sugiero que tomes tu traje de baño y disfrutes en la piscina")
    elif Conversión >= 26:
      print( "El clima es: Cálido, te sugiero vestirte con una playera fresca, pantalonetas y tenis. No olvides llevar una gorra y bloqueador solar!")
    elif Conversión>= 11:
      
     print("El clima es: Templado, te sugiero llevar ropa cómoda como una playera y un sudadero por si acaso.")
    elif Conversión>= 0:
  
     print("El clima es: !FRÍO! te sugiero llevar guantes, bufansa y unn pantalón adecuado. No olvides una chumpa super abrigadora!")    


     