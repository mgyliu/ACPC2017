import sys
import math

def probE():
	for line in sys.stdin:
		AN = line.split()
		N = float(AN[0])
		a = math.exp(math.log(N) / float(N))
		print(a)
		

probE()