data = open("input.txt").read().splitlines()
games_dict = {}

for i, line in enumerate(data):
    game_totals = {"red": 0, "green": 0, "blue": 0}
    running_totals = {"red": 0, "green": 0, "blue": 0}
    games = line.split(": ")[1].split("; ")
    game_totals = {color: (int(val.split(" ")[0]) if int(val.split(" ")[0]) > running_totals[color] else running_totals[color]) for color, val in zip(["red", "green", "blue"], games)}
    running_totals = {color: (int(val.split(" ")[0]) if int(val.split(" ")[0]) > running_totals[color] else running_totals[color]) for color, val in zip(["red", "green", "blue"], games)}
    games_dict[i] = list(game_totals.values())

# for i, line in enumerate(data):
#     games = line.split(": ")[1].split("; ")
#     game_totals = {"red": 0, "green": 0, "blue": 0}
#     running_totals = {"red": 0, "green": 0, "blue": 0}

#     for game in games:
#         colours = game.split(", ")
#         for colour in colours:
#             totals = colour.split(" ")
#             game_totals[totals[1]] = int(totals[0]) if int(totals[0]) > running_totals[totals[1]] else game_totals[totals[1]]
#             running_totals[totals[1]] = int(totals[0]) if int(totals[0]) > running_totals[totals[1]] else running_totals[totals[1]]

#     games_dict[i] = [*game_totals.values()]

ps = sum([v[0] * v[1] * v[2] for _, v in games_dict.items()])

print(f"Power set: {ps}")