import sys



def probA():
	grid1 = []
	grid2 = []

	run = True
	while run:
		dim1 = sys.stdin.readline().rstrip('\n').split()
		dim1_w = dim1[0]
		dim1_h = dim1[1]
		print("Width of g1 is: "+ dim1_w)
		print("height of g1 is: " + dim1_h)

		i = 0

		nestedRun = True
		while(nestedRun==True):
			print("Reading the rows now")
			row = sys.stdin.readline().rstrip('\n').split()
			grid1.append(row)
			i +=1
			if i == int(dim1_h):
				nestedRun = False

		dim2 = sys.stdin.readline().rstrip('\n').split()
		dim2_w = dim2[0]
		dim2_h = dim2[1]
		print("Width of g2 is: "+ dim2_w)
		print("height of g2 is: " + dim2_h)

		j = 0

		nestedRun2 = True
		while(nestedRun2==True):
			print("Reading the rows now for second grid now")
			row = sys.stdin.readline().rstrip('\n').split()
			grid2.append(row)
			j +=1
			if j == int(dim2_h):
				nestedRun2 = False

		print("we now have both grids")
		run = False
	# 	i = 0
	# 	while(True):
	# 		print("dim1_h = " + str(dim1_h))
	# 		print("i = " + str(i))
	# 		line = sys.stdin.readline().rstrip('\n').split()
	# 		grid1.append(line)
	# 		i += 1
	# 		if (i == dim1_h):
	# 			break
	# 	dim2 = sys.stdin.readline().rstrip('\n').split()
	# 	dim2_w = dim1[0]
	# 	dim2_h = dim1[1]
	# 	i = 0
	# 	while i < dim2_h:
	# 		line = sys.stdin.readline().rstrip('\n').split()
	# 		grid2.append(line)
	# 		i += 1
	# 	run = False
	# print(len(grid1))
	# print(len(grid2))

	    

probA()