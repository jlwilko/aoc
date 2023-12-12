import sys
def abs(x):
	return max(x, -x)

def part1():
	lines = open(sys.argv[1]).read().splitlines()
	grid = []
	expansion_rows = []
	for idx, line in enumerate(lines):
		grid.append([ch for ch in line])
		if all(ch == '.' for ch in line):
			expansion_rows.append(idx)


	expansion_cols = []
	for c in range(len(grid[0])-1, -1, -1):
		if all(grid[r][c] == '.' for r in range(len(grid))):
			expansion_cols.append(c)
		
	galaxies = []
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == '#':
				galaxies.append((r,c))
	
	for r in grid:
		print(r)
	factor = 999999
	
	ans = 0
	while galaxies:
		x1,y1 = galaxies.pop(0)
		for x2,y2 in galaxies:

			erows = [x for x in expansion_rows if x >= min(x1,x2) and x <= max(x1,x2)]
			ecols = [x for x in expansion_cols if x >= min(y1,y2) and x <= max(y1,y2)]
			# print(erows)
			# print(ecols)

			print( abs(y1-y2) + abs(x1-x2) + factor*len(erows) + factor*len(ecols))
			ans += abs(y1-y2) + abs(x1-x2) + factor*len(erows) + factor*len(ecols)
	return ans

def part2():
	return

if __name__ == "__main__":
	print(part1())
	print(part2())
