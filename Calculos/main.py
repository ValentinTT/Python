import Calculadora
from os import system

system ("cls")
print ("Bienvenido!!!")
out = 2
while out:
	option = 0
	out = 2
	
	print ("1.Calcular ley de Ohm.")
	print ("2.Calcular resistencias de un circuito en paralelo.")
	print ("3.Calcular resistencias de un circuito en serie.")
	while  option > 3 or option < 1:
		option = int (input ("Introduce una opcion: "))
	print ()

	if option == 1:
		current = int (input ("Intensidad (0 si no la conoces): "))
		resistance = int (input ("Resistencia (0 si no la conoces): "))
		potential_difference = int (input ("Tension(0 si no la conoces): "))
		print ("\n", Calculadora.ohm_law (current, resistance, potential_difference), " es el valor de la incognita")

	elif option == 2:
		resistances = input ("Introduce los valores de las resistencias separados por coma: ")
		resistances = resistances.split(",")
		print ("\nLa suma de las resistencias (Rt) es igual a: ", Calculadora.parallel (resistances))

	elif option == 3:
		resistances = input ("Introduce los valores de las resistencias separados por coma: ")
		resistances = resistances.split(",")
		print ("\nLa suma de las resistencias (Rt) es igual a: ", Calculadora.series (resistances))

	while out > 1 or out < 0:
		out =int (input("\nDeseas continuar (0=No/1=Si): "))
	print ("valentin".center (79,"-"))