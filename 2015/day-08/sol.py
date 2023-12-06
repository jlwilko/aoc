import sys

def part1():
	tot = 0
	lines = open(sys.argv[1]).read().splitlines()
	for line in lines:
		l = len(line)
		line = line.replace('\\\\', 'a')
		line = line.replace('\\"', 'a')
		hex_chars = line.count('\\x')
		mem_len = len(line) - 3*hex_chars - 2
		tot += l - mem_len
	
	print(tot)

def part2():
	tot = 0
	lines = open(sys.argv[1]).read().splitlines()
	for line in lines:
		print(line)
		diff = 2
		diff += line.count(r'"')
		diff += line.count("\\")
		tot += diff


	print(tot)

part1()
part2()