import numpy as np
def part2(lines):
	sch = np.array([list(line.strip()) for line in lines])
	# print(sch)

	ranges = []

	# loop over each character and build a list of ranges that are occupied by numbers
	for i, row in enumerate(sch):
		start = None
		for j,char in enumerate(sch):
			if sch[i,j].isdecimal() and (j==0 or not sch[i,j-1].isdecimal()):
				start = j
			if sch[i,j].isdecimal() and (j==len(sch[i])-1 or not sch[i,j+1].isdecimal()):
				ranges.append((i, start, j))

	expanded_ranges = [(max(r[0]-1,0), min(r[0]+2,len(sch)), max(r[1]-1,0), min(r[2]+2,len(sch[0]))) for r in ranges]
	# print(expanded_ranges)
	values = [list(sch[i[0]:i[1], i[2]:i[3]].flatten()) for i in expanded_ranges]
	# print(values)
	valid = [any([v in '*' for v in value]) for value in values]
	numbers = [int("".join(sch[r[0]:r[0]+1,r[1]:r[2]+1].tolist()[0])) for r in ranges]
	numbers = [x for x,y in zip(numbers, valid) if y]
	numbers_ranges = [r for r,y in zip(ranges, valid) if y]
	# print(f"{numbers=}")
	# print(f"{numbers_ranges=}")

	tot = 0

	for i, row in enumerate(sch):
		for j,char in enumerate(sch):
			if sch[i,j] == '*':
				adjacent_ranges = [i >= r[0]-1 and i <= r[0]+1 and j >= r[1]-1 and j<=r[2]+1 for r in numbers_ranges]
				if (sum(adjacent_ranges) == 2):
					gear_elements = [x for x,y in zip(numbers, adjacent_ranges) if y]
					tot += gear_elements[0] * gear_elements[1]

	return tot

if __name__ == "__main__":
	with open('ex.in') as f:
		lines = f.readlines()
	print(part2(lines))

	with open('input.in') as f:
		lines = f.readlines()
	print(part2(lines))