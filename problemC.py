import sys


def probC():
	for line in sys.stdin:
		nm = line.split()
		n = int(nm[0])
		m = int(nm[1])
		result = n/float(m)
		print(result)

probC()