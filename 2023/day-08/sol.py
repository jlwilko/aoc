import sys
from dataclasses import dataclass

@dataclass
class Node:
	name: str
	left: str
	right: str

def find(el, arr):
	return next((x for x in arr if el == x.name))

def findEndsWith(el, arr):
	return [x for x in arr if x.name.endswith(el)]

def gcd(a,b):
	larger = max(a,b)
	smol = min(a,b)
	a = larger
	b = smol
	while b != 0:
		a, b = b, a % b
	return a



def part1():
	lines = open(sys.argv[1]).read()
	moves, instructions = lines.split('\n\n')

	m = []
	for ins in instructions.splitlines():
		ins = ins.replace("(","")
		ins = ins.replace(")","")
		ins = ins.replace(",","")
		ins = ins.replace("=","")
		ins = ins.split()
		print(ins)
		m.append(Node(*ins))
	
	print(m)

	el = find("AAA", m)
	print(el)
	steps = 0
	while el.name != "ZZZ":
		if moves[steps % len(moves)] == "L":
			el = find(el.left, m)
			print(el)
		else:
			assert(moves[steps % len(moves) == "R"])
			el = find(el.right, m)
			print(el)
		steps += 1

	return steps
	

def part2():
	lines = open(sys.argv[1]).read()
	moves, instructions = lines.split('\n\n')

	m = []
	for ins in instructions.splitlines():
		ins = ins.replace("(","")
		ins = ins.replace(")","")
		ins = ins.replace(",","")
		ins = ins.replace("=","")
		ins = ins.split()
		m.append(Node(*ins))
	
	print(m)

	nodes = [x for x in m if x.name.endswith("A")]
	print(nodes)

	cycles = []
	finalnodes = []
	for el in nodes: 
		steps = 0
		while not el.name.endswith("Z"):
			if moves[steps % len(moves)] == "L":
				el = find(el.left, m)
				# print(el)
			else:
				assert(moves[steps % len(moves) == "R"])
				el = find(el.right, m)
				# print(el)
			steps += 1
		cycles.append(steps)
		finalnodes.append(el)
	
	# find LCM of cycles
	ans = cycles.pop()
	while cycles:
		n = cycles.pop()
		ans = ans * n / gcd(ans, n)

	return ans

if __name__ == "__main__":
	print(part1())
	print(part2())
