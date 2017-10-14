import math
import sys

def probJ():
	pi = math.pi
	for line in sys.stdin:
		AN = line.split()
		A = float(AN[0])
		N = float(AN[1])
		r = N / (2 * pi)
		area = pi * r * r
		if area < A:
			print("Need more materials!")
		else:
			print("Diablo is happy!")

probJ()