data = open("input.txt").read().splitlines()


def parse_data(data, factor):
    points = []
    y = 0

    for l, line in enumerate(data):
        x = 0
        if "#" not in line:
            y += factor - 1
        else:
            for i, c in enumerate(line):
                if all(data[el][i] == "." for el in range(len(data))):
                    x += factor - 1
                if c == "#":
                    points.append((x, y))
                x += 1
        y += 1
    
    return points


def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


def result(points):
    res = 0
    for g in range(len(points) - 1):
        for h in range(g + 1, len(points)):
            res += manhattan_distance(points[g], points[h])
    
    return res


part1_points = parse_data(data, 2)
part2_points = parse_data(data, 1000000)

print(f"Part 1: {result(part1_points)}")
print(f"Part 2: {result(part2_points)}")