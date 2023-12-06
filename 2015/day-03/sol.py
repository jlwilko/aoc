def part1(lines):
	coords = set()
	x = y = 0
	coords.add((x,y))
	for c in lines[0]:
		if c == '^':
			y += 1
		elif c == 'v':
			y -= 1
		elif c == '<':
			x -= 1
		elif c == '>':
			x += 1
		coords.add((x,y))
	return len(coords)

def part2(lines):
	santa_coords = set()
	robo_coords = set()
	sx = sy = rx = ry = 0
	santa_coords.add((sx,sy))
	robo_coords.add((rx,ry))
	for i,c in enumerate(lines[0]):
		if i % 2 == 0:
			if c == '^':
				sy += 1
			elif c == 'v':
				sy -= 1
			elif c == '<':
				sx -= 1
			elif c == '>':
				sx += 1
			santa_coords.add((sx,sy))
		else:
			if c == '^':
				ry += 1
			elif c == 'v':
				ry -= 1
			elif c == '<':
				rx -= 1
			elif c == '>':
				rx += 1
			robo_coords.add((rx,ry))
	return len(santa_coords | robo_coords)

lines = open('input.txt').read().splitlines()
print(part1(lines))
print(part2(lines))
