import numpy as np
def day():
	lines = open('input').read().splitlines()
	tot = 0
	copies = np.ones(len(lines))
	for idx, line in enumerate(lines):
		line = line.split(":")[1]
		winners = line.split("|")[0].strip().split()
		numbers = line.split("|")[1].strip().split()

		count = sum([1 for number in numbers if number in winners])
		if count != 0:
			tot += 1 << count-1
			copies[idx+1:idx+1+count] += copies[idx]

	print(tot)
	print(sum(copies))
	return 


if __name__ == "__main__":
	day()