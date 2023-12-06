from math import prod

data = open("input.txt").read().splitlines()

# zip is wonderful - it combines each element from a list into tuples
part1 = zip((int(i) for i in data[0].split()[1:]), (int(i) for i in data[1].split()[1:]))
part2 = zip([int("".join(data[0].split()[1:]))], [int("".join(data[1].split()[1:]))])


def process(time_distance):
    ways_to_win = {}

    # Suspiciously simple loop and list comprehension
    # basically using the old velocity formula of distance / time

    for i, t in enumerate(time_distance):
        ways_to_win[i] = [v for v in range(1,t[0]) if t[1]/(v) < t[0] - v]
    
    return ways_to_win

result1 = process(part1)
print(f"Part 1: {prod((len(result1[i]) for i in result1.keys()))}")

result2 = process(part2)
print(f"Part 2: {prod((len(result2[i]) for i in result2.keys()))}")