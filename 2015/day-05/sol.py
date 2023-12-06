def part1(lines):
	three_vowels = [sum([1 for c in line if c in 'aeiou']) >= 3 for line in lines]
	double = [any([line[i] == line[i+1] for i in range(len(line)-1)]) for line in lines]
	good_strings = [not any([bad in line for bad in ['ab','cd','pq','xy']]) for line in lines]

	return sum([all([three_vowels[i], double[i], good_strings[i]]) for i in range(len(lines))])

def part2(lines):
	double = [any([line[i] == line[i+2] for i in range(len(line)-2)]) for line in lines]
	pair = [any([line.count(line[i:i+2]) > 1 for i in range(len(line)-1)]) for line in lines]

	return sum([all([double[i], pair[i]]) for i in range(len(lines))])

lines = open('input').read().splitlines()
print(part1(lines))
print(part2(lines))
