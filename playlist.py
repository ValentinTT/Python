#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir, rename
from os.path import isfile, join, getmtime, dirname, abspath, basename

dictionary = {}
lista = []
mypath = dirname(abspath(__file__))
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in onlyfiles:
	m_time = getmtime(mypath + "/" + i)
	while(True):
		try:
			lista.index(m_time)
			m_time += 1
		except ValueError:
			break
	lista.append(m_time)	
	dictionary[m_time] = i
	print(i, ": ", m_time)
lista.sort(reverse=False)

for i in range(len(lista)):
	print(dictionary[lista[i]][3:5])
	if(dictionary[lista[i]][3:5] == "--"):
		rename(dictionary[lista[i]], dictionary[lista[i]][5:])
		dictionary[lista[i]] = dictionary[lista[i]][5:]
		print("Corregido")

for i in range(len(lista)):
	if(dictionary[lista[i]] == basename(__file__)):
		continue
	if(i < 10):
		try:
			print(dictionary[lista[i]])		
			rename(dictionary[lista[i]], "00"+str(i) + "--" + dictionary[lista[i]])
		except:
			print("\t\t", i, "-*-Unexcpected error")
	elif(i < 100):
		try:
			print(dictionary[lista[i]])		
			rename(dictionary[lista[i]], "0"+str(i) + "--" + dictionary[lista[i]])
		except:
			print("\t\t", i, "-*-Unexpected error")
	else:
		try:
			print(dictionary[lista[i]])		
			rename(dictionary[lista[i]], str(i) + "--" + dictionary[lista[i]])
		except:
			print("\t\t", i, "-*-Unexpected error")
print ("\n\n\n", dictionary)

"""/media/vtt/VTT-Datos/Musica/Electrónica/marzo2017"""
