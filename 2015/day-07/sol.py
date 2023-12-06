import sys

def part1():
	d = {}

	def get(n):
		if n in d:
			return d[n]
		try:
			return int(n)
		except:
			return None

	lines = open(sys.argv[1]).read().splitlines()
	lines = sorted(lines, key=len)
	while lines:
		line = lines.pop(0)
		*cmd, arrow, dst = line.split()
		print(cmd)
		print(dst)
		if len(cmd) == 1 and get(cmd[0]) is not None:
			print("solved")
			d[dst] = get(cmd[0])
		elif len(cmd) == 2 and get(cmd[1]) is not None:
			print("solved")
			d[dst] = ~get(cmd[1]) & 0xffff
		elif get(cmd[0]) is not None and get(cmd[2]) is not None:
			print("solved")
			if cmd[1] == "AND":
				d[dst] = get(cmd[0]) & get(cmd[2]) & 0xffff
			if cmd[1] == "OR":
				d[dst] = get(cmd[0]) | get(cmd[2]) & 0xffff
			if cmd[1] == "LSHIFT":
				d[dst] = get(cmd[0]) << get(cmd[2]) & 0xffff
			if cmd[1] == "RSHIFT":
				d[dst] = get(cmd[0]) >> get(cmd[2]) & 0xffff
		else:
			lines.append(line)

		

	print(d)







print(part1())