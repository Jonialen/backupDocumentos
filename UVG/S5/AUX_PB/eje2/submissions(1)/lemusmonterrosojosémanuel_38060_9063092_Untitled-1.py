#
#Universida del Valle de Guatemala
#CC2005 Algoritmos y programación Básica
#Sección 50
#Nombre: José Lemus
#Carné: 251197
#
temperatura = str(input("Su temperatura va a ser ingresada en F o en C, (F/C) "))
grado = float(input("Ingrese el grado de temperatuta en el que se encuentra o se va a encontrar "))
if temperatura == "F":
    grado = (grado - 32) *5/9
    print("Su temperatura es ", grado," C")
else:
    grado=grado
    print("Su temperatura es ", grado," C")

if 0<= grado <=10:
    print("Frío, debe usar chumpa, guantes y bufanda")
elif 11<= grado >=25:
    print("Templado, usar ropa cómoda, sudadero y playera")
elif 26<= grado <= 40:
    print("Cálido, use gorra, pantaloneta y bloqueador")
else:
    print("Calor extremo, vaya a una piscina y utilice traje de baño")