def fact(x):
		# assert isinstance(x, int)
		# assert x >= 0
		print("Debug: x=", x)
		if x == 0:
				return 1
		else:
				return x * fact(x - 1)

def half_fact(x):
		return fact(x / 2)

def invert(x):
	y = 1/x
	print('Never printed if x is 0.')
	return y

def invert_safe(x):
	try:
		return invert(x)
	except ZeroDivisionError as e:
		print('handled', e)
		return 0