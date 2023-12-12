import sys
from collections import Counter

def part1():
	lines = open(sys.argv[1]).read().splitlines()
	hands = [el.split(" ")[0] for el in lines]
	bets = [el.split(" ")[1] for el in lines]

	typ = [[1,1,1,1,1], [1,1,1,2], [1,2,2], [1,1,3], [2,3], [1,4], [5]]
	chars = "23456789TJQKA"

	scores = []
	for bet, hand in zip(bets,hands):
		c = sorted(Counter(hand).values())
		score = (typ.index(c), *[chars.index(h) for h in hand])
		scores.append((score,hand,bet))

	sorted_scores = sorted(scores, key=lambda x:x[0])
	# print(sorted_scores)
	total = 0
	for idx, el in enumerate(sorted_scores):
		total += int(el[2])*(idx+1)
	print(total)
part1()

def part2():
	lines = open(sys.argv[1]).read().splitlines()
	hands = [el.split(" ")[0] for el in lines]
	bets = [el.split(" ")[1] for el in lines]

	typ = [[1,1,1,1,1], [1,1,1,2], [1,2,2], [1,1,3], [2,3], [1,4], [5]]
	chars = "J23456789TQKA"

	scores = []
	for bet, hand in zip(bets,hands):
		possible_hands = [hand.replace("J", c) for c in chars] if "J" in hand else [hand]
		c = sorted([typ.index(sorted(Counter(hand).values())) for hand in possible_hands])
		score = (max(c), *[chars.index(h) for h in hand])
		scores.append((score,hand,bet))

	sorted_scores = sorted(scores, key=lambda x:x[0])
	# print(sorted_scores)
	total = 0
	# print(sum([(idx+1)*int(bid) for idx, (_, _, bid) in enumerate(sorted_scores)]))
	for idx, el in enumerate(sorted_scores):
		total += int(el[2])*(idx+1)
	print(total)

part2()