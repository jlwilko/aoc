import numpy as np

def smartsolution():
	# sch = open("ex").read().splitlines()
	sch = open("input").read().splitlines()
	num = ""
	building = False
	valid = False
	tot = 0

	for r in range(len(sch)):
		for c in range(len(sch[r])):
			if sch[r][c].isdigit():
				building = True
				num += sch[r][c]
			else:
				if building and valid:
					tot += int(num)
				building = False
				num = ""
				valid = False

			if building and not valid:
				for rr in [-1, 0, 1]:
					for cc in [-1, 0, 1]:
						if (r+rr in [-1, len(sch)] or c+cc in [-1, len(sch[0])]):
							continue
						if (not sch[r+rr][c+cc].isdigit()) and sch[r+rr][c+cc] != '.':
							valid = True
			
			# if not sch[r][c].isdigit() or c == len(sch[r])-1:
			# 	if valid:
			# 		print(num)
			# 		tot += int(num)
			# 	building = False
			# 	num = ""
			# 	valid = False 
	return tot

def testing():
    schematic = open("input").read().splitlines()
 
    checking = False
    valid = False
    num = []
    total = 0

    for y in range(len(schematic)):
        for x in range(len(schematic[0])):

            if schematic[y][x].isdigit():
                num.append(schematic[y][x])
                checking = True
            else:
                if checking and valid:
                    total += int("".join(num))
                checking = False
                valid = False
                num = []
            
            if checking and not valid:
                for dx in [0,-1,1]:
                    for dy in [0,-1,1]:
                        if dx == dy == 0 or  x+dx in [-1,len(schematic[0])] or y+dy in [-1,len(schematic)]:
                            continue
                        
                        if not schematic[y+dy][x+dx].isdigit() and schematic[y+dy][x+dx] != ".":
                            valid = True

    print(total)
				
	 
	# # doesnt quite work becuase i implemented it wrong
	# # based on: https://github.com/Fadi88/AoC/blob/master/2023/day03/code.py
	# sch = open("ex.in").read().splitlines()
	# print(sch)

	# tot = 0
	# num = []
	# checking = False
	# valid = False

	# for i in range(len(sch)):
	# 	for j in range(len(sch[i])):
	# 		if sch[i][j].isdecimal():
	# 			num.append(int(sch[i][j]))
	# 			checking = True
			
	# 		else:
	# 			if checking and valid:
	# 				tot += int("".join(num))
	# 			checking = False
	# 			valid = False
	# 			num = []

	# 			if checking and not valid:
	# 				# check in each direction if the number has become valid
	# 				for dx  in [-1, 0, 1]:
	# 					for dy in [-1, 0, 1]:
	# 						if (dx == 0 and dy == 0) or (x+dx in [-1, len(sch[0])] or y+dy in [-1, len(sch)]):
	# 							continue
						
	# 						if not sch[i+dx][j+dy].isdigit() and sch[i+dx][j+dy] != '.':
	# 							valid = True
	# return tot

def part1(lines):
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
	valid = [not all([v in '0123456789.' for v in value]) for value in values]
	# print(valid)
	numbers = [int("".join(sch[r[0]:r[0]+1,r[1]:r[2]+1].tolist()[0])) for r in ranges]
	# print(numbers)
	total = sum(x for x, y in zip(numbers, valid) if y)
	return total

if __name__ == "__main__":

	# with open('ex.in') as f:
	# 	lines = f.readlines()
	# print(part1(lines))

	import time
	start = time.perf_counter()
	with open('input') as f:
		lines = f.readlines()
	print(part1(lines))
	print(f"MY method ={time.perf_counter() - start}")

	start = time.perf_counter()
	print(testing())
	print(f"Their method (broken for my input) = {time.perf_counter() - start}")

	start = time.perf_counter()
	print(smartsolution())
	print(f"My adaption of their method (broken for my input) = {time.perf_counter() - start}")