def part1(lines):
	areas = []
	for line in lines:
		l,w,h = [int(x) for x in line.split('x')]
		area = 2*l*w + 2*w*h + 2*h*l
		extra = min(l*w, w*h, h*l)
		areas.append(area + extra)
	
	return sum(areas)

def part2(lines):

	ribbons = []
	for line in lines:
		l,w,h = [int(x) for x in line.split('x')]
		ribbon = l*w*h + 2*min(l+w, l+h, w+h)
		ribbons.append(ribbon)
	
	return sum(ribbons)

lines = open('input.txt').read().splitlines()
print(part1(lines))
print(part2(lines))
