def ohm_law (current, resistance, potential_difference):
	if current == 0:
		return potential_difference / resistance
	elif resistance == 0:
		return potential_difference / current
	elif potential_difference == 0:
		return current * resistance
	return False

def parallel (resistances):
	result = 0
	for r in resistances:
		result += 1 / (int (r))
	return round (result ** -1, 3)
	
def series (resistances):
	result = 0
	for r in resistances:
		result += int (r) 
	return result