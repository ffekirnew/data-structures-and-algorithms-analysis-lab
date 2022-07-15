def naive_LCM(a, b):
	
	Multiples_of_A, Multiples_of_B = [], []
	AMultiple, BMultiple = 1, 1
	multiplier = 1

	while True:
		if AMultiple in Multiples_of_B:
			return AMultiple
		elif BMultiple in Multiples_of_A:
			return BMultiple

		else:
			AMultiple = a * multiplier
			BMultiple = b * multiplier
			Multiples_of_A.append(AMultiple)
			Multiples_of_B.append(BMultiple)
			multiplier += 1