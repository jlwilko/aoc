import hashlib

def part1():
	key = "yzbqklnj"
	i = 0
	while True:

		val = key + str(i)
		if hashlib.md5(val.encode('utf-8')).hexdigest().startswith("00000"):
			return i
		i += 1

def part2():
	key = "yzbqklnj"
	i = 0
	while True:

		val = key + str(i)
		if hashlib.md5(val.encode('utf-8')).hexdigest().startswith("000000"):
			return i
		i += 1
	return

print(part1())
print(part2())
