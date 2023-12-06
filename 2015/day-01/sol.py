def part1(lines):
	s = 0
	for char in lines[0]:
		if char == '(':
			s += 1
		elif char == ')':
			s -= 1
	return s


def part2(lines):
	s = 0
	for idx, char in enumerate(lines[0]):
		if char == '(':
			s += 1
		elif char == ')':
			s -= 1
		if s == -1:
			return idx + 1
	return None


	return

lines = open('input.txt').read().splitlines()
print(part1(lines))
print(part2(lines))
