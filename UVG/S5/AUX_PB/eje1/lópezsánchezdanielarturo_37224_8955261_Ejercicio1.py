#---------------------------------------------------------------
#Universidad Del Valle de Guatemala
#Algoritmos y Programación Básica
#Sección 50
#Nombre: Daniel López
#Carné 25670
#---------------------------------------------------------------

# Paso 1 ----- Pedir los datos y guardarlos en variables
print('Hola! Este programa le ayudara a calcular cuanta cerca de madera\ntiene que utilizar para su terreno\n\n')
ancho = float(input('Ingrese el ancho del terreno en metros (sin dimensional): '))
largo = float(input('Ingrese el largo del terreno en metros (sin dimensional): '))
dist_postes = float(input('¿Cual es la distancia maxima que puede haber entre los postes?: '))
print('\n\n Muy bien! \n\n')
costo_pm = float(input('Ahora ingrese el dato exacto del costo (Q.) unitario del metro lineal de madera: '))

#Paso 2 ------ Crear nuevas variables con los calculos
perimetro = 2*(ancho+largo)
costo_total = perimetro*costo_pm
num_postes = perimetro//dist_postes

#Paso 3 ------ Ajustes al numero total de postes
if (perimetro%dist_postes > 0):
    num_postes = num_postes + 1

if (num_postes <= 4):
    num_postes = 4 # Debe haber un poste en cada esquina

# Paso 4 ------ Display de resultados en consola
print('\n-------- RESULTADOS --------------\n')
print('o METROS DE MADERA NECESARIOS: ', perimetro)
print('o COSTO TOTAL DEL CERCADO: ', costo_total)
print('o NUMERO DE POSTES: ', num_postes)






