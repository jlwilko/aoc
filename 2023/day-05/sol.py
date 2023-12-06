import sys
def get_nested_maps(maps, num):
	for i in maps:
		# print(num)
		for key in i:
			if num in key:
				# print(f"found {num} in {key}")
				num = num + i[key]
				break
	return num

def interval_map(ranges, m):
	# m is a dict of ranges to values
	# ranges is a list of ranges
	# return a list of ranges mapped using m

	mapped = []
	for key in m:
		not_mapped = []
		while ranges:
			r = ranges.pop(0)
			# generate regions of overlap
			before = (r[0], min(key[0], r[1]))
			inter = (max(r[0], key[0]), min(r[1], key[-1]))
			after = (max(r[0], key[-1]), r[1])

			if before[1] > before[0]:
				not_mapped.append(before)
			if after[1] > after[0]:
				not_mapped.append(after)
			if inter[1] > inter[0]:
				mapped.append((inter[0]+m[key], inter[1]+m[key]))
			
		ranges = not_mapped
	return mapped+ranges


def read_map(gen):
	# get rid of 'map' string
	next(gen)
	m = {}
	while True:
		line = [int(n) for n in next(gen, "").strip().split()]
		if line == []:
			break
		m[range(line[1], line[1]+line[2])] = line[0] - line[1]
	return m

def part1(lines):
	gen = (x for x in lines)
	seeds = [int(n) for n in next(gen).split()[1:]]
	next(gen)
	soil = read_map(gen)
	fert = read_map(gen)
	water = read_map(gen)
	light = read_map(gen)
	temp = read_map(gen)
	hum = read_map(gen)
	location = read_map(gen)
	maps = [soil, fert, water, light, temp, hum, location]

	locations = [get_nested_maps(maps, seed) for seed in seeds]
	return min(locations)

def part2(lines):
	gen = (x for x in lines)
	ranges = [int(n) for n in next(gen).split()[1:]]
	seeds = [(r0, r0+r1) for r0,r1 in zip(ranges[::2], ranges[1::2])]
	next(gen)
	soil = read_map(gen)
	fert = read_map(gen)
	water = read_map(gen)
	light = read_map(gen)
	temp = read_map(gen)
	hum = read_map(gen)
	location = read_map(gen)
	maps = [soil, fert, water, light, temp, hum, location]
	for i in maps:
		seeds = interval_map(seeds, i)
	smallest = min(seeds, key=lambda x:x[0])
	return smallest[0]

if __name__ == "__main__":
	import time
	start = time.perf_counter()
	with open(sys.argv[1]) as f:
		lines = f.readlines()
	
	print(part1(lines))
	print(part2(lines))
	print(f"Time: {1e3*(time.perf_counter()-start)} ms")
