data = open("input.txt").read().splitlines()

targets = {"red": 12, "green": 13, "blue": 14}

games_dict = {i: all(int(totals[0]) <= targets[totals[1]] for turn in line.split(": ")[1].split("; ") for colour in turn.split(", ") for totals in [colour.split(" ")]) for i, line in enumerate(data)}

possible_games = sum(games_dict.values())

print(f"Possible games: {possible_games}")