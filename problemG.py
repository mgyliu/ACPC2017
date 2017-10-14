import sys

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
tones = [2,2,1,2,2,2]



def probG():
	run = True
	out = ""
	unique = []
	while run:
	    num = sys.stdin.readline().rstrip('\n')
	    series = sys.stdin.readline().rstrip('\n').split()
	    

	    # for i in series:
	    # 	print(i)

	    for item in series:
	    	if (notes.index(item) + 1) not in unique:
	    		unique.append(notes.index(item) + 1)

	    if num == '':
	        run = False

	unique.sort()

	for note in notes:
		n = notes.index(note) + 1
		scale = []

		for t in tones:
			scale.append(n)
			if ((n + t) % 12 != 0):
				n = (n + t) % 12
			else:
				n = n + t
		scale.append(n)

		check = False

		for i in unique:
			if i in scale:
				check = True
			else:
				check = False
				break
		if (check):
			out = out + note + " "


	out = out.strip()
	if (out == ""):
		print("none")
	else:
		print(out)

probG()
