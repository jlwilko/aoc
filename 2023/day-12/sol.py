import sys

def get_groups(springs):
	groups = []
	counter = 0
	for ch in springs:
		if ch == "#":
			counter += 1
		else:
			if counter != 0:
				groups.append(counter)
			counter = 0 
	if counter != 0:
		groups.append(counter)
	return groups 

def generate_springs(unknowns):
	idx = [i for i,x in enumerate(unknowns) if x == '?']
	print(idx)

	# for each possible string
	for i in range(2**len(idx)):
		binary = bin(i)[2::].zfill(len(idx))
		# print(binary)

		new = list(unknowns)
		for digit, index in zip(binary,idx):
			if digit == "1":
				new[index] = '#'
			else:
				new[index] = '.'
			
		yield new 

def part1():
	lines = open(sys.argv[1]).read().splitlines()
	ans = 0
	for line in lines:
		springs, groups = line.split(" ")
		groups = [int(x) for x in groups.split(",")]

		# print(springs)
		# print(groups)

		# for each possibility for each line:
		possibles = generate_springs(springs)

		for p in possibles:
			g = get_groups(p)
			if g == groups:
				# print("incrementing")
				ans += 1
		print(ans)	


if __name__ == "__main__":
	print(part1())
