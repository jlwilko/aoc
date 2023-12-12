import sys
from typing import List

def pred_value(seq: List[int]):
	if all([x == 0 for x in seq]):
		return 0
	else:
		diffs = [e1 - e2 for e1, e2 in zip(seq[1::], seq[0::])]
		return seq[-1] + pred_value(diffs)

def pred_value_back(seq: List[int]):
	if all([x == 0 for x in seq]):
		return 0
	else:
		diffs = [e1 - e2 for e1, e2 in zip(seq[1::], seq[0::])]
		# return pred_value_back(diffs) - seq[0]
		return seq[0] - pred_value_back(diffs)

def part1():
	lines = open(sys.argv[1]).read().splitlines()
	ans = 0
	for line in lines:
		pred = pred_value([int(x) for x in line.split()])

		ans += pred
	return ans

def part2():
	lines = open(sys.argv[1]).read().splitlines()
	ans = 0
	for line in lines:
		pred = pred_value_back([int(x) for x in line.split()])

		ans += pred
		print(pred)
	return ans
	return

if __name__ == "__main__":
	print(part1())
	print(part2())
