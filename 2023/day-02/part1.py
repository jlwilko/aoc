import typing

def part1(lines):
	bag = {"red":12, "green":13, "blue":14}

	tot = 0

	for game in lines:
		id, game = game.split(":")
		id = int(id.split(" ")[1])
		print(f"Id: {id}")
		possible = True
		for turn in game.split(";"):
			for colour in turn.split(","):
				colour = colour.strip().split()
				if bag[colour[1]] < int(colour[0]):
					possible = False
					break

		if possible:
			tot += id
	return tot

if __name__ == "__main__":
	with open('example.in') as f:
		lines = f.readlines()
	
	print(part1(lines))

	with open('input.in') as f:
		lines = f.readlines()
	
	print(part1(lines))

