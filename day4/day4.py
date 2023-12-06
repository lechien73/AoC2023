data = open("input.txt").read().splitlines()
part1 = 0
part2 = 0

cards_list = []
cards = {}

for i, line in enumerate(data):
    # Populate our cards dictionary for part 2
    cards[i + 1] = 1

    line = line.split(": ")[1].split(" | ")

    # Create two sets - one for winning numbers and the other for
    # the numbers we have
    winning_nums = {int(i.strip()) for i in line[0].split(" ") if i}
    my_nums = {int(i.strip()) for i in line[1].split(" ") if i}

    # Creates a set based on the intersection of the two sets
    # The intersection is where numbers are in both sets.
    intersections = winning_nums & my_nums 
    
    # The points are powers of 2 - we love those in programming
    part1 += int(2 ** (len(intersections) - 1))

    cards_list.append(len(intersections))

# Lots of ugly for loops in here corresponding to lots
# of scribbled notes to figure out the logic
for i, card in enumerate(cards_list):
    for _ in range(cards[i + 1]):
        for copy in range(i + 2, i + 2 + card):
            cards[copy] += 1
    part2 += cards[i + 1]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")


