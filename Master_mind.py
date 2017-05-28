import random
import string
from os import system as clear

def master_mind (option):
	"""Crea un número alazar y ejecuta un bucle hasta que el usuario consigue adivinar
	el número, contavilizando el número de intentos"""
	codigo = 0	
	copia_codigo = []
	intentos = 0	

	print ("\nTienes que adivinar un número de ", option, "dígitos:\n ")

	while len (str (codigo)) != option:	#Se repite el bucle hasta que el largo del codigo sea igual a la dificultad (ej codigo 102 dificultad facil)
		codigo =  int (random.random () * (10 ** option))	#Crea un numero alazar entre 0 y 1 y lo multiplica para darle la longitud de la dificultad.
	codigo = list (str(codigo))	#Convierte el número a un string y luego a una lista

	while True:	#Bucle infinito
		jugador = []	
		copia_codigo [:] = codigo [:]	#Se crea una copia del codigo.
		intentos += 1	#Aumenta en uno los intentos.

		while len (jugador) != option:	#Se repite mientras el numero introducido no tenga la misma longitud que el codigo.
			jugador = list (input ("Introduce tu propuesta: "))

		for i in range (option):	#Bucle que recorre todas las posiciones de la variable copia_codigo.
			if copia_codigo[i] == jugador[i]:	#Si lo que se halla en la posicion i en jugador y copia codigo ejecuta el cuerpo if.
				jugador [i] = "acierto"		#Cambia el valor por la cadena "acierto".
				copia_codigo [i] = "ya_comparado"	#Cambia el valor por la cadena "ya comparado" para evitar errores con las coincidencias.

		if jugador.count ("acierto") == option:	#Si todos los valores de jugador son aciertos finaliza el bucle.
			break

		for i in copia_codigo:	#Recorre todo el bucle copia_codigo.
			if i in jugador:	#Si encuentra que i esta en jugador cambia ambas variables para no compararlas más.
				jugador [jugador.index(i)] = "coincidencia"
				copia_codigo [copia_codigo.index(i)] = "ya_comparado"

		print ("\nAciertos: ", jugador.count ("acierto"))	#Cuenta el número de aciertos.
		print ("Coincidencias: ", jugador.count ("coincidencia"))	#Cuenta el número de coincidencias.

	print ("\nFelicidades!!!!!".center (79, " "))
	print ("Lo lograste en", intentos, " intentos")

while True:
	clear ("cls")
	print ("Bienvenido a Master Mind!!".center  (79, "-"))
	print ("1.Facil (3 dígitos)")
	print ("2.Dificil (4 dígitos)")
	print ("3.Pesadilla (5 dígitos)")

	option = 0
	while option not in range (1,4):
		option = int (input ("Ingresa una opcion: "))

	master_mind (option + 2)
	print ("\n")

	option = 0
	while option not in [1,2]:
		option = int (input ("Ingresa 1 para salir o 2 para continuar: "))
	if option == 1:
		break
	print ("".center (79,"."))
