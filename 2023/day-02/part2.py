import functools

def part2(lines):
	possible_bags = []
	tot = 0

	for game in lines:
		id, game = game.split(":")
		id = int(id.split(" ")[1])
		print(f"Id: {id}")

		smallest_bag = {"red":0, "green":0, "blue":0}

		for turn in game.split(";"):
			for colour in turn.split(","):
				colour = colour.strip().split()
				smallest_bag[colour[1]] = max(smallest_bag[colour[1]], int(colour[0]))
		
		possible_bags.append(smallest_bag)

	game_power = [functools.reduce(lambda x,y: x*y, bag.values()) for bag in possible_bags]
	print(game_power)
	return sum(game_power)

if __name__ == "__main__":
	with open('example.in') as f:
		lines = f.readlines()
	print(part2(lines))

	with open('input.in') as f:
		lines = f.readlines()
	print(part2(lines))

