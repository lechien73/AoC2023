from math import lcm

data = open("input.txt").read().splitlines()

# Build a list of instructions and a dictionary of
# nodes
insts = [c for c in data[0]]
nodes = {}
for line in data[2:]:
    n = line.split(" = ")
    nodes[n[0]] = [n[1].split(", ")[0][1:], n[1].split(", ")[1][0:-1]]

# The starting nodes for part 2
current_nodes = [node for node in nodes.keys() if node[-1] == "A"]

# Turns out I can just use one function for both parts
def traverse(node="AAA", end_node="ZZZ"):
    steps = 0
    while not node.endswith(end_node):
        for inst in insts:
            steps += 1
            node = nodes[node][0] if inst == "L" else nodes[node][1]
            if node.endswith(end_node):
                return steps

print(f"Part 1: {traverse()}")

# Handy library to find the least common multiple,
# which works quickly and efficiently for this problem
part2 = 1
for node in current_nodes:
    part2 = lcm(part2, traverse(node, "Z"))

print(f"Part 2: {part2}")

