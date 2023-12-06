import numpy as np

def part1(lines):
	grid = np.zeros((1000,1000))
	for line in lines:
		words = line.split(" ")
		print(words)
		if words[0] == "toggle":
			start = [int(x) for x in words[1].split(",")]
			end = [int(x) for x in words[3].split(",")]
			np.logical_xor(grid[start[0]:end[0]+1,start[1]:end[1]+1], np.ones((end[0]-start[0]+1,end[1]-start[1]+1)), out=grid[start[0]:end[0]+1,start[1]:end[1]+1])

		elif words[1] == "on":
			start = [int(x) for x in words[2].split(",")]
			end = [int(x) for x in words[4].split(",")]
			grid[start[0]:end[0]+1,start[1]:end[1]+1] = np.ones((end[0]-start[0]+1,end[1]-start[1]+1))
		
		elif words[1] == "off":
			start = [int(x) for x in words[2].split(",")]
			end = [int(x) for x in words[4].split(",")]
			grid[start[0]:end[0]+1,start[1]:end[1]+1] = np.zeros((end[0]-start[0]+1,end[1]-start[1]+1))

	return sum(sum(grid))

def part2(lines):
	grid = np.zeros((1000,1000))
	for line in lines:
		words = line.split(" ")
		print(words)
		if words[0] == "toggle":
			start = [int(x) for x in words[1].split(",")]
			end = [int(x) for x in words[3].split(",")]
			grid[start[0]:end[0]+1,start[1]:end[1]+1] += 2

		elif words[1] == "on":
			start = [int(x) for x in words[2].split(",")]
			end = [int(x) for x in words[4].split(",")]
			grid[start[0]:end[0]+1,start[1]:end[1]+1] += 1
		
		elif words[1] == "off":
			start = [int(x) for x in words[2].split(",")]
			end = [int(x) for x in words[4].split(",")]
			grid[start[0]:end[0]+1,start[1]:end[1]+1] -= 1
			grid[grid < 0] = 0
	return sum(sum(grid))

lines = open('input').read().splitlines()
print(part1(lines))
print(part2(lines))
