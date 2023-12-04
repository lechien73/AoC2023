from collections import defaultdict
from re import finditer

data = open("input.txt").read().splitlines()

# Create a set containing the coordinates of all the symbols
symbols = {(r, c) for r in range(len(data[0])) for c in range(len(data[0])) if data[r][c] not in ".01234566789"}

parts = defaultdict(list)

# Create a set containing all of the numbers and their coordinates

for i, line in enumerate(data):
    for occ in finditer(r"\d+", line):
        neighbours = {(i+s, c+d) for s in (-1, 0, 1) for d in (-1, 0, 1) for c in range(*occ.span())}

        # Iterate through the intersected sets and create the parts
        # dictionary
        for s in neighbours & symbols:
            parts[s] = int(occ[0])

# Now, it's a simple case of summing each neighbouring part for part 1
part1 = sum(sum(part) for part in parts.values())

# Or getting the sum of the product of the gear ratios for part 2
part2 = sum(part[0] * part[1] for part in parts.values() if len(part)==2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")