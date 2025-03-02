n = int(input("num: ")) # Numero
n2 = 0  # Numero para comparar (auxilar)

cont = 0 # Contador de que digito voy
while n2 != n: # Cuento hasta que sean iguales
    cont += 1 # Sumo al contador (un digito mas)
    n2 = n % 10 ** cont # asigno al numero auxilar el el modulo del numero * 10^n

print("Total", cont)
