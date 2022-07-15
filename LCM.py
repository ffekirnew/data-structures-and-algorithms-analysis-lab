from EuclidsGcd import GCD

def LCM(a, b):
	return (a * b // GCD(a, b))