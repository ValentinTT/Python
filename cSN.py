
def bin_dec(bin):
	bin = str(bin)
	res = 0
	for aux in range(len(bin)):
		if bin[len(bin)-1-aux] == '1':
			res = res + 2**aux
	return str(res)

def bin_oct(bin):
	bin = str(bin)
	dec = bin_dec(int(bin))
	return dec_oct(int(dec))

def bin_hex(bin):
	bin = str(bin)
	dec = bin_dec(int(bin))
	return dec_hex(int(dec))

def oct_bin(oct):
	oct = str(oct)
	dec = oct_dec(int(oct))
	return dec_bin(int(dec))

def oct_dec(oct):
	oct = str(oct)
	res = 0
	leng = len(oct)
	for aux in range(leng):
		if oct[leng-1-aux] != '0':
			res = res + int(oct[leng-1-aux]) * (8**aux)
	return str(res)

def oct_hex(oct):
	oct = str(oct)
	dec = oct_dec(int(oct))
	return dec_hex(int(dec))
	
def dec_bin(dec):
	dec = str(dec)
	bin = ""
	aux = int(dec)
	while aux > 1:
		last = str(int(aux % 2))
		bin = str(last) + bin
		aux = aux // 2
	res = str(aux) + bin
	relleno = int(len(res)) % 4
	res = " " + "0" * relleno + res

	return str(res)

def dec_oct(dec):
	dec = str(dec)
	oct = ""
	aux = int(dec)
	while aux > 7:
		last = str(int(aux % 8))
		oct = str(last) + oct
		aux = aux // 8
	res = str(aux) + oct
	return str(res)

def dec_hex(dec):
	dec = str(dec)
	dec_aux = int(dec)
	res = ""
	dicc = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
	while dec_aux > 15:
		resto = dec_aux % 16
		if resto > 9:
			res = dicc[resto] + res
		else:
			res = str(resto) + res 
		dec_aux = dec_aux // 16 

	if dec_aux > 9:
		res = dicc[dec_aux] + res
	else:
		res = str(dec_aux) + res

	return str(res)

def hex_bin(hex):
	hex = str(hex)
	dec = hex_dec(hex)
	return dec_bin(int(dec))

def hex_oct(hex):
	hex = str(hex)
	dec = hex_dec(hex)
	return dec_oct(int(dec))

def hex_dec(hex):
	hex = str(hex)
	dicc = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15,
			"a" : 10, "b" : 11, "c" : 12, "d" : 13, "e" : 14, "f" : 15}
	res = 0
	for aux in range(len(hex)):
		if "ABCDEFabcdef".count(hex[len(hex)- 1 - aux]) == 0:
			res = res + int(hex[len(hex)- 1 - aux]) * 16 ** aux
		else:
			res = res + dicc[hex[len(hex)- 1 - aux]] * 16 ** aux 
	return str(res)

def bin(n):
	n = int(n)
	print("""Valor binario: {}
octal: {}
decimal: {}
hexadecimal: {}\n""".format(n, bin_oct(n), bin_dec(n), bin_hex(n)))

def oct(n):
	n = int(n)
	print("""Valor octal: {}
binario: {}
decimal: {}
hexadecimal: {}\n""".format(n, oct_bin(n), oct_dec(n), oct_hex(n)))

def dec(n):
	n = int(n)
	print("""Valor decimal: {}
binario: {}
octal: {}
hexadecimal: {}\n""".format(n, dec_bin(n),dec_oct(n), dec_hex(n)))

def hex(n):
	n = str(n)
	print("""Valor hexadecimal: {}
binario: {}
octal: {}
decimal: {}\n""".format(n.upper(), hex_bin(n), hex_oct(n), hex_dec(n)))