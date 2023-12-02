data = open("input.txt").read().splitlines()

games_dict = {}
targets = {"red": 12, "green": 13, "blue": 14}

target_reds = 12
target_blues = 14
target_greens = 13

for i, line in enumerate(data):
    turns = line.split(": ")[1].split("; ")
    possible = True
    for turn in turns:
        colours = turn.split(", ")
        for colour in colours:
            totals = colour.split(" ")
            possible = False if int(totals[0]) > targets[totals[1]] else possible
            # possible = False if totals[1] == "green" and int(totals[0]) > target_greens else possible
            # possible = False if totals[1] == "blue" and int(totals[0]) > target_blues else possible
    
    games_dict[i] = possible

possible_games = sum([k for k, v in games_dict.items() if v])

print(f"Possible games: {possible_games}")


