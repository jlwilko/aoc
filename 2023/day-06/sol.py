import sys
def part1():
	lines = open(sys.argv[1]).read().splitlines()
	times = [x for x in lines[0].split()[1:]]
	distances = [x for x in lines[1].split()[1:]]
	races = [(int(time), int(distance)) for time, distance in zip(times, distances)]
	print(races)

	ans = 1
	for t, record in races:
		winners = 0
		for i in range(t):
			# distacne covered = time held * remaining time
			dist = (t-i) * i 
			if dist > record:
				winners += 1
		ans *= winners
	print(ans)

	times = int(''.join(times))
	distances = int(''.join(distances))
	# winners = 0
	# for i in range(times):
	# 	# distacne covered = time held * remaining time
	# 	dist = (times-i) * i 
	# 	if dist > distances:
	# 		winners += 1
	# print(winners)

	import math
	ans = math.floor(math.sqrt(times**2-4*distances))
	print(ans)

	return 

if __name__ == "__main__":
	part1()
