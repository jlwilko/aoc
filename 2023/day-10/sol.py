import sys

def part1():
	grid = [[char for char in line] for line in open(sys.argv[1]).read().splitlines()]

			#moving down             moving up etc
	moves = {(1,0):['|', 'L','J','S'], (-1,0):['|', '7', 'F','S'], (0,-1):['-','L','F','S'], (0,1):['J', '7', '-','S']}


	# find start position
	start = None
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == "S":
				start = (r, c)
				break
		if start != None:
			break
	print(start)

	dist = [[-1 for i in row] for row in grid]
	on_pipe = [[False for i in row] for row in grid]
	# count distance from start for every point
	r = start[0]
	c = start[1]
	dist[r][c] = 0
	on_pipe[r][c] = True

	done = False
	q = [start]

	while q:
		r, c = q.pop(0)
		for rr in [0,1,-1]:
			for cc in [0,1,-1]:
				# dont search diag
				if rr != 0 and cc != 0:
					continue
				# search valid squares
				if r+rr in [-1, len(grid)] or c+cc in [-1, len(grid[0])]:
					continue
				# search only things that havent been searched
				if dist[r+rr][c+cc] != -1:
					continue

				# check that its a valid move
				if grid[r+rr][c+cc] not in moves[(rr,cc)] or grid[r][c] not in moves[(-1*rr,-1*cc)]:
					continue

				
				dist[r+rr][c+cc] = dist[r][c] + 1
				on_pipe[r+rr][c+cc] = True
				q.append((r+rr,c+cc))

	count = 0
	for r in range(1,len(grid)-1):
		inside = False
		for c in range(len(grid[0])-1):
			if on_pipe[r][c] and on_pipe[r-1][c] and grid[r][c] in moves[(1,0)]:
				inside = not inside
				continue
			if inside and not on_pipe[r][c]:
				count += 1

	return max([max(i) for i in dist]), count
	

if __name__ == "__main__":
	print(part1())
	# print(part2())
