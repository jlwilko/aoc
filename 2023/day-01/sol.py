import time

def p1(lines):
	values = []
	for line in lines:
		# find smallest index where isdecimal is true 
		first = line[min([i for i, x in enumerate(line) if x.isdecimal()])]
		# find largest index where isdecimal is true 
		last = line[max([i for i, x in enumerate(line) if x.isdecimal()])]
		val = int(first + last)
		values.append(val)

	print(sum(values))

def p2(lines):
	numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

	values = []
	for line in lines:
		# print(line)
		first = None
		last = None
		for idx, char in enumerate(line):
			if char.isdecimal():
				first = char
				break
			string_matches = [line.startswith(number, idx) for number in numbers]
			if any(string_matches):
				first = str(string_matches.index(True) + 1)
				break
		for idx, char in enumerate(line[::-1]):
			if char.isdecimal():
				last = char
				break
			string_matches = [line.startswith(number, len(line) - idx - 1) for number in numbers]
			if any(string_matches):
				# print("matched string")
				last = str(max([i for i, x in enumerate(string_matches) if x]) + 1)
				break
		# print(first,last)
		val = int(first+last)
		values.append(val)

	# print(values)
	print(sum(values))

	return


def main():
	with open('input.in') as f:
		lines = f.readlines()
		f.close()
	
	# p1(lines)
	p2(lines)



if __name__ == '__main__':
	start = time.perf_counter()
	main()
	end = time.perf_counter()
